{-# OPTIONS_GHC -fno-warn-warnings-deprecations #-}
{-# LANGUAGE FlexibleInstances #-}

module Utils where

import Data.List

import AbsPyxell hiding (Type)
import qualified AbsPyxell as Abs (Type)


-- | Representation of a position in the program's source code.
type Pos = Maybe (Int, Int)

-- | Alias for Type without passing Pos.
type Type = Abs.Type Pos

-- | Show instance for displaying types.
instance {-# OVERLAPS #-} Show Type where
    show typ = case typ of
        TInt _ -> "Int"
        TBool _ -> "Bool"
        TChar _ -> "Char"
        TObject _ -> "Object"
        TString _ -> "String"
        TArray _ t -> "[" ++ show t ++ "]"
        --TPower _ typ exp -> show typ ++ show exp
        TTuple _ types -> intercalate "*" $ map show types
        --TFunc _ typ1 typ2 -> show typ1 ++ "->" ++ show typ2

-- | Unification function. Returns a common supertype of given types.
unifyTypes t1 t2 = do
    case (t1, t2) of
        (TInt _, TInt _) -> Just tInt
        (TBool _, TBool _) -> Just tBool
        (TChar _, TChar _) -> Just tChar
        --(TObject _, _) -> tObject
        --(_, TObject _) -> tObject
        (TString _, TString _) -> Just tString
        (TArray _ t1', TArray _ t2') -> fmap tArray (unifyTypes t1' t2')
        (TTuple _ ts1, TTuple _ ts2) ->
            if length ts1 == length ts2 then fmap tTuple (sequence (map (uncurry unifyTypes) (zip ts1 ts2)))
            else Nothing
        otherwise -> Nothing

-- | Helper functions for initializing types without a position.
tPtr = TPtr Nothing
tDeref = TDeref Nothing
tLabel = TLabel Nothing
tVoid = TVoid Nothing
tInt = TInt Nothing
tBool = TBool Nothing
tChar = TChar Nothing
tObject = TObject Nothing
tString = TString Nothing
tArray = TArray Nothing
tTuple = TTuple Nothing

-- | Shorter name for none position.
_pos = Nothing
