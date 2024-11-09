# SICP notes

## Key ideas

All computing begins with representing information, specifying logic to process it, and designing abstractions that manage the complexity of that logic.

Every powerful language has three such mechanisms:

primitive expressions and statements, which represent the simplest building blocks that the language provides,
means of combination, by which compound elements are built from simpler ones, and
means of abstraction, by which compound elements can be named and manipulated as units.

In programming, we deal with two kinds of elements: functions and data. (Soon we will discover that they are really not so distinct.) Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. Thus, any powerful programming language should be able to describe primitive data and primitive functions, as well as have some methods for combining and abstracting both functions and data.

### Abstraction

What's abstraction? Abstraction is a mean to hide implementation details so that as long as the input and expected output don't change, how the abstraction is implemented is not relevant and other developers or programmaers can simply utilise the abstacted piece of code without worrying about the underlying details. Overall, abstraction helps modularise code to improve maintainability for programmers who develop the code and usability for other developers who rely on it in their programs.

- Types of abstraction:
  - Functional Abstraction: grouping combined computational elements and process as a single function
  - Class Abstractoin: grrouping combined computational elements and process as a single class

## Guide to designing function

- give each function exactly one job
- don't repeat yourself (DRY). Impelment a process just once, but execute it many times
- define functions generally

## Higher Order Functions

- Functions that manipulate functions are called higher-order functions. This section shows how higher-order functions can serve as powerful abstraction mechanisms, vastly increasing the expressive power of our language.

- decorators are hofs

## Lambda

When the function returned by the lambda expression is called, the return expression of a lambda expression executed.

- Lambdas can return other lambdas!
