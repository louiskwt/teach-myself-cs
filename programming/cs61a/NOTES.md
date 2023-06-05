# Course Notes

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

- Closure referes to the locally defined functions that enclose information in the function scope

- Currying - Transforming a multi-argument function into a single-argument, higher-order function

> E.g  make_adder(2)(3)
  

- lambda exoressions - anonymous function that has a single expression as its body. assignment and control statements are not allowed.

- functional abstractions

    1. def: binding computational process to a name
    2. you don't have to worry about the implementation, but you should know the expected behaviour
    3. naming doesn't matter in terms of correctness, but it matters for composition
