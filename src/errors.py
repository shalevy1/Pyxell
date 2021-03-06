
from antlr4.error.ErrorListener import ErrorListener


class PyxellErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise PyxellError(PyxellError.InvalidSyntax(), line, column+1)


class PyxellError(Exception):

    InvalidSyntax = lambda: f"Syntax error"

    AbstractClass = lambda t: f"Cannot instantiate an abstract class `{t.show()}`"
    CannotUnpack = lambda t, n: f"Cannot unpack value of type `{t.show()}` into {n} values"
    ExpectedNamedArgument = lambda: f"Positional argument cannot follow named arguments"
    IntegerTooLarge = lambda: f"Integer constant is too large"
    InvalidArgumentTypes = lambda t: f"Cannot unify argument types for type variable `{t.show()}`"
    InvalidDeclaration = lambda t: f"Cannot declare variable of type `{t.show()}`"
    InvalidFunctionCall = lambda id, types, msg: f"Error in function `{id}` called here{(' (with types ' + ', '.join(f'{name}={type.show()}' for name, type in types.items()) + ')') if types else ''}.\n{msg}"
    InvalidMember = lambda id: f"Invalid type signature of member `{id}`"
    InvalidReturnType = lambda t: f"`{t.show()}` is not a valid return type"
    InvalidUsage = lambda s: f"`{s}` cannot be used here"
    MissingArgument = lambda id: f"Missing required argument `{id}`"
    NoAttribute = lambda t, id: f"Type `{t.show()}` has no attribute `{id}`"
    NoBinaryOperator = lambda op, t1, t2: f"No binary operator `{op}` defined for `{t1.show()}` and `{t2.show()}`"
    NoConversion = lambda t1, t2: f"No implicit conversion from `{t1.show()}` to `{t2.show()}`"
    NoUnaryOperator = lambda op, t: f"No unary operator `{op}` defined for `{t.show()}`"
    NotComparable = lambda t1, t2: f"Cannot compare `{t1.show()}` with `{t2.show()}`"
    NotDefaultable = lambda t: f"Type `{t.show()}` does not have a default value"
    NotDictionary = lambda t: f"Type `{t.show()}` is not a dictionary"
    NotHashable = lambda t: f"Type `{t.show()}` is not hashable"
    NotIndexable = lambda t: f"Type `{t.show()}` is not indexable"
    NotIterable = lambda t: f"Type `{t.show()}` is not iterable"
    NotLvalue = lambda: f"Expression cannot be assigned to"
    NotFunction = lambda t: f"Type `{t.show()}` is not a function"
    NotNullable = lambda t: f"Type `{t.show()}` is not nullable"
    NotPrintable = lambda t: f"Variable of type `{t.show()}` cannot be printed"
    NotClass = lambda t: f"Type `{t.show()}` is not a class"
    NotType = lambda id: f"Identifier `{id}` does not represent a type"
    NotVariable = lambda id: f"Identifier `{id}` does not represent a variable"
    RedefinedIdentifier = lambda id: f"Identifier `{id}` cannot be redefined"
    RepeatedArgument = lambda id: f"Repeated argument `{id}`"
    RepeatedMember = lambda id: f"Repeated member `{id}`"
    RepeatedVariadic = lambda: f"Function may have only one variadic argument"
    TooFewArguments = lambda: f"Too few arguments"
    TooManyArguments = lambda: f"Too many arguments"
    UndeclaredIdentifier = lambda id: f"Undeclared identifier `{id}`"
    UnexpectedArgument = lambda id: f"Unexpected argument `{id}`"
    UnexpectedVoid = lambda: f"Function without return value cannot be called here"
    UnknownLabel = lambda id: f"Unknown label `{id}`"
    UnknownModule = lambda id: f"Unknown module `{id}`"
    UnknownType = lambda: f"Cannot settle type of the expression"

    def __init__(self, msg, line, column=None):
        self.line = line
        self.column = column
        text = f"Line {line}"
        if column:
            text += f", column {column}"
        text += f": {msg}."
        super().__init__(text)


class NotSupportedError(Exception):
    pass
