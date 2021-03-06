
# Specification


## Operators

This table presents all operators available in Pyxell, sorted by precedence, from highest to lowest.
Operators in the same row have equal precedence.

| Operators                        | Description                                              | Arity     | Associativity |
| -------------------------------- | -------------------------------------------------------- | --------- | ------------- |
| `.`, `?.`                        | attribute access                                         | binary    | left          |
| `[]`, `?[]`                      | element access                                           | binary    | left          |
| `()`                             | function call                                            | multiary  | left          |
| `!`                              | non-null assertion                                       | unary     | left          |
| `^`, `^^`                        | exponentiation, integer exponentiation                   | binary    | right         |
| `+`, `-`                         | unary plus and minus                                     | unary     | right         |
| `/`                              | division                                                 | binary    | left          |
| `//`, `%`, `*`, `&`              | floor division, modulo, multiplication, set intersection | binary    | left          |
| `+`, `-`                         | addition, subtraction                                    | binary    | left          |
| `%%`                             | divisibility                                             | binary    | left          |
| `??`                             | null coalescing                                          | binary    | left          |
| `..`, `...`                      | inclusive and exclusive range                            | binary    | left          |
| `...`                            | infinite range                                           | unary     | left          |
| `by`                             | iteration step                                           | binary    | left          |
| `...`                            | spread                                                   | unary     | right         |
| `==`, `!=`, `<`, `<=`, `>`, `>=` | comparisons (chainable)                                  | binary    | right         |
| `in`, `not in`                   | membership                                               | binary    | left          |
| `is null`, `is not null`         | null check                                               | binary    | left          |
| `not`                            | logical negation                                         | binary    | right         |
| `and`                            | logical conjunction (short-circuiting)                   | binary    | right         |
| `or`                             | logical disjunction (short-circuiting)                   | binary    | right         |
| `? :`                            | conditional operator                                     | ternary   | right         |

Associativity of unary operators determines on which side the expression should be, e.g.: `a!` (left), `-a` (right).


## Types

This section describes all data types available in Pyxell, together with their properties and methods.

### Fundamental types

| Type name  | Description                                 | Example value | Default value |
| ---------- | ------------------------------------------- | ------------- | ------------- |
| `Void`     | no value (for functions returning nothing)  |               |               |
| `Int`      | 64-bit signed integer number                | `42`          | `0`           |
| `Rat`      | arbitrary-precision rational number         | `1.5`         | `0r`          |
| `Float`    | double-precision floating-point number      | `3.14f`       | `0f`          |
| `Bool`     | boolean value                               | `true`        | `false`       |
| `Char`     | single-byte character                       | `'A'`         | `'\x0'`       |
| `String`   | arbitrary-length string of characters       | `"example"`   | `""`          |

### Compound types

| Type name pattern     | Description      | Example value   | Default value                            |
| --------------------- | ---------------- | --------------- | ---------------------------------------- |
| `[Type]`              | array            | `[1, 2]`        | `[]`                                     |
| `{Type}`              | set              | `{"abc", ""}`   | `{}`                                     |
| `{Key:Value}`         | dictionary       | `{'x': false}`  | `{:}`                                    |
| `Type?`               | nullable value   | `null`          | `null`                                   |
| `Type1*Type2`         | tuple            | `true, 4.6`     | tuple of default values                  |
| `Arg1->Arg2->Result`  | function         | `_+_`           | function returning the default value     |
| custom class name     | class object     |                 | none (uninitialized object is invalid)   |

### `Int` properties

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `char`           | `Char`       | character corresponding to the integer code (in ASCII)           |

### `Rat` properties and methods

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `fraction`       | `Rat*Rat`    | numerator and denominator of the number, in the reduced form     |

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `toInt() Int`                                     | returns the number converted to `Int` (conversion may be lossy)                                                 |

### `Float` methods

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `toInt() Int`                                     | returns the number converted to `Int` (conversion may be lossy)                                                 |

### `Char` properties

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `code`           | `Int`        | integer code of the character (in ASCII)                         |

### `String` properties and methods

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `empty`          | `Bool`       | whether the string is empty                                      |
| `length`         | `Int`        | number of characters in the string                               |

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `all(Char->Bool f) Bool`                          | determines whether all characters in the string satisfy a condition                                             |
| `any(Char->Bool f) Bool`                          | determines whether any character in the string satisfies a condition                                            |
| `count(Char c) Int`                               | returns the number of occurrences of a character within the string                                              |
| `endsWith(String s) Bool`                         | determines whether the string ends with a given string                                                          |
| `filter(Char->Bool f) String`                     | returns a string with only those characters from the original string that satisfy a condition                   |
| `find(String s, Int start: 0) Int?`               | returns the index of the first occurrence of a string within the string, or `null` if it is not found           |
| `fold<B>(Char->B->B f, B r) B`                    | applies an accumulator function over the string, with a given initial accumulator value                         |
| `get(Int p) Char?`                                | returns the character under a given index in the string, or `null` if the index is out of bounds                |
| `map(Char->Char f) String`                        | returns a string with characters from the original string transformed by a mapping function                     |
| `reduce(Char->Char->Char f) Char`                 | applies an accumulator function over the string, with the first character as the initial value                  |
| `split(String sep) [String]`                      | splits the string into substrings delimited by a given separator                                                |
| `startsWith(String s) Bool`                       | determines whether the string starts with a given string                                                        |
| `toInt() Int`                                     | returns the string's content converted to `Int` (conversion may fail)                                           |
| `toFloat() Float`                                 | returns the string's content converted to `Float` (conversion may fail)                                         |
| `toRat() Rat`                                     | returns the string's content converted to `Rat` (conversion may fail)                                           |

### Array properties and methods

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `empty`          | `Bool`       | whether the array is empty                                       |
| `length`         | `Int`        | number of elements in the array                                  |

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `all<A>(A->Bool f: _) Bool`                       | determines whether all elements in the array satisfy a condition                                                |
| `any<A>(A->Bool f: _) Bool`                       | determines whether any element in the array satisfies a condition                                               |
| `clear<A>() Void`                                 | removes all elements from the array                                                                             |
| `copy<A>() [A]`                                   | return a shallow copy of the array                                                                              |
| `count<A>(A x) A?`                                | returns the number of occurrences of an element within the array                                                |
| `erase<A>(Int p, Int count: 1) Void`              | removes elements from the array at a given position                                                             |
| `extend<A>([A] a) Void`                           | appends all elements in a given array to the array                                                              |
| `filter<A>(A->Bool f) [A]`                        | returns an array with only those elements from the original array that satisfy a condition                      |
| `find<A>(A x, Int start: 0) Int?`                 | returns the index of the first occurrence of an element within the array, or `null` if it is not found          |
| `fold<A,B>(A->B->B f, B r) B`                     | applies an accumulator function over the array, with a given initial accumulator value                          |
| `get<A>(Int p) A?`                                | returns the element under a given index in the array, or `null` if the index is out of bounds                   |
| `insert<A>(Int p, A x) Void`                      | inserts a new element at a given position of the array                                                          |
| `join(String sep: "") String`                     | returns a string consisting of elements from the array (characters or strings) delimited by a given separator   |
| `map<A,B>(A->B f) [B]`                            | returns an array with elements from the original array transformed by a mapping function                        |
| `pop<A>() A`                                      | removes the last element from the array and returns it (will fail if the array is empty)                        |
| `push<A>(A x) Void`                               | appends a given element to the end of the array                                                                 |
| `reduce<A>(A->A->A f) A`                          | applies an accumulator function over the array, with the first element as the initial value                     |
| `reverse<A>() Void`                               | reverses the order of elements in the array                                                                     |
| `sort<A,K>(Bool reverse: false, A->K key: _) [A]` | sorts the array in place, stably, using a function to extract comparison keys; returns the sorted array         |

### Set properties and methods

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `empty`          | `Bool`       | whether the set is empty                                         |
| `length`         | `Int`        | number of elements in the set                                    |

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `add<A>(A x) Void`                                | adds a given element to the set                                                                                 |
| `all<A>(A->Bool f: _) Bool`                       | determines whether all elements in the set satisfy a condition                                                  |
| `any<A>(A->Bool f: _) Bool`                       | determines whether any element in the set satisfies a condition                                                 |
| `clear<A>() Void`                                 | removes all elements from the set                                                                               |
| `copy<A>() {A}`                                   | return a shallow copy of the set                                                                                |
| `filter<A>(A->Bool f) {A}`                        | returns a set with only those elements from the original set that satisfy a condition                           |
| `fold<A,B>(A->B->B f, B r) B`                     | applies an accumulator function over the set, with a given initial accumulator value                            |
| `intersect<A>({A} s) Void`                        | removes all elements not present in a given set from the set                                                    |
| `map<A,B>(A->B f) {B}`                            | returns a set with elements from the original set transformed by a mapping function                             |
| `pop<A>() A`                                      | removes some element from the set and returns it (will fail if the set is empty)                                |
| `reduce<A>(A->A->A f) A`                          | applies an accumulator function over the set, with one of the elements as the initial value                     |
| `remove<A>(A x) Void`                             | removes a given element from the set                                                                            |
| `subtract<A>({A} s) Void`                         | removes all elements in a given set from the set                                                                |
| `union<A>({A} s) Void`                            | adds all elements in a given set to the set                                                                     |

### Dictionary properties and methods

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| `empty`          | `Bool`       | whether the dictionary is empty                                  |
| `length`         | `Int`        | number of elements in the dictionary                             |

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `all<A,B>(A*B->Bool f) Bool`                      | determines whether all key-value pairs in the dictionary satisfy a condition                                    |
| `any<A,B>(A*B->Bool f) Bool`                      | determines whether any key-value pair in the dictionary satisfies a condition                                   |
| `clear<A,B>() Void`                               | removes all elements from the dictionary                                                                        |
| `copy<A,B>() {A:B}`                               | return a shallow copy of the dictionary                                                                         |
| `filter<A,B>(A*B->Bool f) {A:B}`                  | returns a dictionary with only those key-value pairs from the original dictionary that satisfy a condition      |
| `fold<A,B,C>(A*B->C->C f, C r) C`                 | applies an accumulator function over the dictionary, with a given initial accumulator value                     |
| `get<A,B>(A x) B?`                                | returns the value under a given key in the dictionary, or `null` if the key is not present                      |
| `map<A,B,C,D>(A*B->C*D f) {C:D}`                  | returns a dictionary with key-value pairs from the original dictionary transformed by a mapping function        |
| `reduce<A,B>(A*B->A*B->A*B f) A*B`                | applies an accumulator function over the dictionary, with one of the key-value pairs as the initial value       |
| `remove<A,B>(A x) Void`                           | removes a given key from the dictionary                                                                         |
| `update<A,B>({A:B} d) Void`                       | updates the dictionary with keys and values from a given dictionary                                             |

### Tuple properties

| Property name    | Type         | Description                                                      |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| letter `a`–`z`   | any          | corresponding element of the tuple                               |

### Common methods (all types)

| Method header                                     | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `toString() String`                               | returns the string representation of the value                                                                  |


## Standard library

This section describes the built-in functions in Pyxell, as well as constants and functions within corresponding modules.

### I/O functions

| Function header                                   | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `read() String`                                   | reads a string from the standard input, to the first whitespace character                                       |
| `readChar() Char`                                 | reads a single character from the standard input                                                                |
| `readFloat() Float`                               | reads a floating-point number from the standard input                                                           |
| `readInt() Int`                                   | reads an integer number from the standard input                                                                 |
| `readLine() String`                               | reads a string from the standard input, to the first newline character                                          |
| `readRat() Rat`                                   | reads a rational number from the standard input                                                                 |
| `write(String s) Void`                            | writes a string to the standard output                                                                          |

### Bitwise functions

| Function header                                   | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `bitAnd(Int x, Int y) Int`                        | returns the bitwise AND of `x` and `y`                                                                          |
| `bitNot(Int x) Int`                               | returns the bitwise NOT of `x`                                                                                  |
| `bitOr(Int x, Int y) Int`                         | returns the bitwise OR of `x` and `y`                                                                           |
| `bitShift(Int x, Int y) Int`                      | returns the bitwise shift of `x`: left for positive `y`, right for negative `y`                                 |
| `bitXor(Int x, Int y) Int`                        | returns the bitwise XOR of `x` and `y`                                                                          |

### Arithmetic functions

| Function header                                   | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `abs<T>(T x) T`                                   | returns the absolute value of `x`                                                                               |
| `clamp<T>(T x, T a, T b) T`                       | returns `x` clamped to the interval `[a, b]`                                                                    |
| `max<T>(T x, T y) T`                              | returns the maximum of `x` and `y`                                                                              |
| `min<T>(T x, T y) T`                              | returns the minimum of `x` and `y`                                                                              |
| `sign<T>(T x) T`                                  | returns the sign of `x` (`-1`, `0`, or `1`)                                                                     |

### `math` module

| Constant name    | Type         | Value                                                            |
| ---------------- | ------------ | ---------------------------------------------------------------- |
| E                | Float        | approximation of the number _e_: `2.718281828459045f`            |
| INF              | Float        | floating-point positive infinity                                 |
| PI               | Float        | approximation of the number _π_: `3.141592653589793f`            |

| Function header                                   | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `acos(Float x) Float`                             | returns the angle (in radians) whose cosine is `x`                                                              |
| `asin(Float x) Float`                             | returns the angle (in radians) whose sine is `x`                                                                |
| `atan(Float x) Float`                             | returns the angle (in radians) whose tangent is `x`                                                             |
| `ceil(Float x) Float`                             | returns the smallest integral value greater than or equal to `x`                                                |
| `cos(Float x) Float`                              | returns the cosine of `x` (in radians)                                                                          |
| `exp(Float x) Float`                              | returns _e_ raised to the power of `x`                                                                          |
| `floor(Float x) Float`                            | returns the largest integral value less than or equal to `x`                                                    |
| `log(Float x) Float`                              | returns the natural logarithm of `x`                                                                            |
| `log10(Float x) Float`                            | returns the base 10 logarithm of `x`                                                                            |
| `round(Float x, Int p: 0) Float`                  | returns `x` rounded to `p` fractional digits                                                                    |
| `sin(Float x) Float`                              | returns the sine of `x` (in radians)                                                                            |
| `sqrt(Float x) Float`                             | returns the square root of `x`                                                                                  |
| `tan(Float x) Float`                              | returns the tangent of `x` (in radians)                                                                         |
| `trunc(Float x) Float`                            | returns the integral part of `x` (`x` rounded towards 0)                                                        |

### `random` module

| Function header                                   | Description                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `randFloat(Float r: 1) Float`                     | returns a random floating-point number from the interval `[0, r)`                                               |
| `randInt(Int r: 2) Float`                         | returns a random integer number from the interval `[0, r)`                                                      |
| `seed(Int x) Float`                               | initializes the pseudo-random number generator with a given seed                                                |
