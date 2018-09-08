{-# OPTIONS_GHC -fno-warn-warnings-deprecations #-}
{-# LANGUAGE FlexibleInstances #-}

module Libraries where

import Control.Monad.Trans.Class
import Control.Monad.Trans.State
import qualified Data.Map as M

import CodeGen
import Utils


libBase :: Run ()
libBase = do
    write $ [ "",
        "@s = internal constant [5 x i8] c\"%.*s\\00\"",
        "" ]
    lift $ modify (M.insert "$number" (Number 0))
    declare (tFunc [tInt] (tPtr tChar)) "@malloc"
    declare (tFunc [tPtr tChar, tPtr tChar, tInt] (tPtr tChar)) "@memcpy"
    declare (tFunc [tChar] (tInt)) "@putchar"
    declare (tFunc [tPtr tChar, tInt, tPtr tChar] (tInt)) "@printf"

    -- Char <-> Int (ASCII)
    define (tFunc [tChar] tInt) "ord" $ do
        v <- zext tChar tInt "%0"
        ret tInt v
    define (tFunc [tInt] tChar) "chr" $ do
        v <- trunc tInt tChar "%0"
        ret tChar v

    -- [Char] to String
    define (tFunc [tArray tChar] tString) "str" $ do
        p1 <- gep tString "%0" ["0"] [0] >>= load (tPtr tChar)
        v <- gep tString "%0" ["0"] [1] >>= load tInt
        (_, p2) <- initArray tChar [] [v]
        p3 <- gep tString p2 ["0"] [0] >>= load (tPtr tChar)
        call (tPtr tChar) "@memcpy" [(tPtr tChar, p3), (tPtr tChar, p1), (tInt, v)]
        ret tString p2

    -- Standard output
    define (tFunc [tString] tVoid) "write" $ do
        p <- gep tString "%0" ["0"] [0] >>= load (tPtr tChar)
        v <- gep tString "%0" ["0"] [1] >>= load tInt
        write $ indent [ "%s = getelementptr [5 x i8], [5 x i8]* @s, i32 0, i32 0" ]
        call tInt "@printf" [(tPtr tChar, "%s"), (tInt, v), (tPtr tChar, p)]
        ret tVoid ""
