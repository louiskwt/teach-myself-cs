# SICP notes

## Key ideas

All computing begins with representing information, specifying logic to process it, and designing abstractions that manage the complexity of that logic.

Every powerful language has three such mechanisms:

primitive expressions and statements, which represent the simplest building blocks that the language provides,
means of combination, by which compound elements are built from simpler ones, and
means of abstraction, by which compound elements can be named and manipulated as units.

In programming, we deal with two kinds of elements: functions and data. (Soon we will discover that they are really not so distinct.) Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. Thus, any powerful programming language should be able to describe primitive data and primitive functions, as well as have some methods for combining and abstracting both functions and data.

## Guide to designing function

- give each function exactly one job
- don't repeat yourself (DRY). Impelment a process just once, but execute it many times
- define functions generally

Higher Order Functions

- Functions that manipulate functions are called higher-order functions. This section shows how higher-order functions can serve as powerful abstraction mechanisms, vastly increasing the expressive power of our language.

- decorators are hofs
