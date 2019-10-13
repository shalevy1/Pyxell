
import llvmlite.ir as ll


class CustomStructType(ll.LiteralStructType):

    def __init__(self, elements, kind):
        super().__init__(elements)
        self.kind = kind

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        return self.kind == other.kind


tVoid = ll.VoidType()
tInt = ll.IntType(64)
tBool = ll.IntType(1)
tChar = ll.IntType(8)


def tPtr(type=tChar):
    return type.as_pointer()


tString = CustomStructType([tPtr(), tInt], 'string')

def isString(type):
    return getattr(type, 'kind', None) == 'string'

ll.Type.isString = isString


def tArray(subtype):
    type = CustomStructType([tPtr(subtype), tInt], 'array')
    type.subtype = subtype
    return type

def isArray(type):
    return getattr(type, 'kind', None) == 'array'

ll.Type.isArray = isArray


def tTuple(elements):
    if len(elements) == 1:
        return elements[0]
    return CustomStructType(elements, 'tuple')

def isTuple(type):
    return getattr(type, 'kind', None) == 'tuple'

ll.Type.isTuple = isTuple


def tFunc(args, ret=tVoid):
    return ll.FunctionType(ret, args)


def showType(type):
    if type == tVoid:
        return 'Void'
    if type == tInt:
        return 'Int'
    if type == tBool:
        return 'Bool'
    if type == tChar:
        return 'Char'
    if type.isString():
        return 'String'
    if type.isArray():
        return f'[{type.subtype.show()}]'
    if type.isTuple():
        return '*'.join(t.show() for t in type.elements)
    return str(type)

ll.Type.show = showType


def vInt(n):
    return ll.Constant(tInt, n)

def vBool(b):
    return ll.Constant(tBool, int(b))

vFalse = vBool(False)
vTrue = vBool(True)

def vChar(c):
    return ll.Constant(tChar, ord(c))

def vNull(type=tChar):
    return ll.Constant(tPtr(type), 'null')

def vIndex(i):
    return ll.Constant(ll.IntType(32), i)
