# Lecture 1 

Topics Cover

1. Solving problems using computation
2. python programming language
3. organising modular program
4. Algorithms
5. Algorithmic complexity

_CS focsues on the imperative knowledge (how to / recipe) not the declarative knowledge (statements of facts)_

## Imparative Knowledge Example (Finding Square Root with Newton's Method)

1. Start with a guess g
2. if g * g is close enough to x, stop and say g is the square root
3. else make a new guess by averaging g and x / g
4. using the new guess, repeat the process until it's close enough


We have an algorithm

1. Sequence of simple steps
2. flow of control
3. a mean to determine when to stop

## Big Idea:

Although computer is powerful for processing data, it can only do what you tell it to do.

## Basic Primitives

Turing showed that you can compute anything with only 6 primitives: left, right, print, scan, erase, no op

Church-Turing Thesis: if a functoin is computable, a Turing Machine can be programmed to compute it

The if in Church-Turin thesis is important because not all function is computable.

E.g. 

- halting problem

it is impossible to write a program that given an arbitrary program, call it P, prints true if and only if it runs forever

Turing Completeness: A programming language is Turing complete if it can be used to simulatre a universal Turing machine. (Most modern programming langauges are)

Real programming languages have more convenient set of primitives and ways to combine primitives to create new primitives

_Anything computable in one language is computable in any other programming language_

## Aspects of language

Program only has one meaning, but the meaning may not be what you intend

Things can go wrong

1. syntax error
2. static semantic error (valid syntax but invalid meaning or not meaningful)
3. the output is not what you intended! (semantic error)


## what is programming about

It's about creating data objects and manipulating them

Objects have a type that defines the kinds of things programs can do them

- Scalar object (no internal structure)

    1. int 
    2. float
    3. bool
    4. NoneType

- Non-scalar (has an internal structure / can be subdivided into smaller elements)
    1. list
    2. dictionary

## Type Casting

Can convert one object to another type
float(3)

But the original object is still in memory not modified

Python follows these principles for type casting:

- Immutable types (e.g., int, float, str) cannot be modified in place.
- Operations that "change" a value actually return a new object.

This prevents unintended side effects and makes Python safer for concurrent execution.

## Expressions

In programming, expression is any code that evaluates to a value, it can be

1. literals (e.g., "hello", 42)
2. variables (e.g., x)
3. function calls (e.g. type(x))
4. operator (e.g. <Object> < Operator> < Object>)

Python evaluates the expression and then store the value, but not the expression itself

BIG IDEA: Python replace complex expressions by ONE value

- it means that expressions are evaluated at runtime and doesn't keep track of how the value is computed

- functions and objects can store behaviour, but not expression

* you can store expressions using eval() and ast.parse() to allow python to analyze the expression structually 

    - eval() is used to execute a string as a Python expression but it can be dangerous
    - ast is used for parsing and analyzing code without executing it (used in pylint, mypy) or for building custom interpreters

** functions are stored as function object, and its logic is stored as complied bytecode, not as the expression from the code!

## Operators on int and float

For sum, difference, and product, if both are ints, result is int; if either or both are floats, result is float

For division, the result is always float

opearator precedence without paraenthesis

**

* / % executed left to right, as appear in expression

+ = executed left to right, as appear in expression

## Variables

Math variable
- Abstract
- Can represent many values

CS variables
- bound to one single value
- can be bound to an expression

= sign in programming is an assignment statement, not equality

variables can enhance reusability

can re-bind variable names using new assignment statement

BIG IDEA: Lines are evaluated one after another

## Computational Thinkinng

- Thinking imperatively and designing algorithms to solve problems

Definition of an algorithm: a finite list of instructions that describe a computation that when executed on a set of inputs will proceed through as set of well-defined states and eventually produce an output.

