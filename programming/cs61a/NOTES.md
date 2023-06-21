# Course Notes

## Functions and Abstractions Ch 1.1 - 1.6 

> A language isn't something you learn so much as something you join. -- Arkia Okrent

- A powerful programming language has three mechanisms:
    
    1. primitive expressions and statements
    2. means of combination, by which elements are built from primitve ones
    3. means of abstraction, by which compund elements can be named and manipluated as units

- Variable assignment and funtions are the simplest form of abstraction

- Naming and environment

    - In order to make abstraction possible, environment and name are needed
    - if a value has been given a name, we say that the name binds to the value.

- Evaluating Nested Expressions (an inside-out tree structure)

- Non-pure function is a function that has a side effect other than its return value

- every variable and function exists in the global frame of the program, but each function created   can generate a local frame for the function. Be careful of scoping issue

- Higher order functions: a means to generalise the pattern of computational process

    1. HOF means passing a funciton as an argument to another function
    2. a function can also return a function for further computation / generalizing computational process

> All in all, a higher order functoin is a function that manipulates other functions by taking in functions as  arguments, returning a function, or both. Its aim is to delay further computation / generalize computational  process

- Closure referes to the locally defined functions that enclose information in the function scope

- Currying - Transforming a multi-argument function into a single-argument, higher-order function

> E.g  make_adder(2)(3)
  

- lambda exoressions - anonymous function that has a single expression as its body. assignment and control statements are not allowed.

- functional abstractions

    1. def: binding computational process to a name
    2. you don't have to worry about the implementation, but you should know the expected behaviour
    3. naming doesn't matter in terms of correctness, but it matters for composition

- Self reference refers to a particular design of HOF, where a function eventually return itself. In particular, a self-referencing function will not return a function call, but rather the (evaluated) funtion object itself. This feature is very interesting an useful for dynamic language like Python and JS, and one can take advantage of that.


## Recursion

A function is called recursive if the body of the function calls the funciton itself, either directly or indirectly

- Anatomy of Recursive Functions

    1. A base case
    2. The recursive call

Main point

> Recursive functions express computation by simplifying problems incrementally.

Verifying the correctness of a recursive function is a form of proof by induction

    1. start by verifying the base case
    2. substitute it with k + 1 to verify that it can work for k + 1 temrs

Iterative Approach vs Recursive Approach

    - In general, iterative functions must maintain some local state that changes throughout the course of implemntation
    - Recursive functions, on the other hand, bind the values in different frames (recurive calls) without tracking the state. It avoids the nuisance of corretly assigning local names during iteration.

Recursive fucntions can be easier to define correctly, but it's hard to recognize the process evolved by recursive functions.

When a recursive procedure is divided among two funcitons that call each other, the functions are said to be mutually recurisve. (flipping back-and-forth between two functions in recursive calls)


Mutually recursive functions can be turned into a single recursive function by breaking the abstraction boundary between the two functions
