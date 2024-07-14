# SICP

## Ch 1.  Building Abstractions wiht Functions

The purpose of a programming language is to provide the means to combine simple ideas to form more complex ideas so that we can perform tasks with computer.

Each powerful (and useful) language has 3 mechanisms for accomplishing this:

    1. Primitive expression
    2. Means of combination
    3. Means of abstraction

In programming, we deal with 2 kinds of elements: functions and data. Though they are not so distinct.

To have variables and functions, the program needs to keep track of it in memory and that memory in the programming language context is environment.

The concepts of environment is implemented through the language's interpreter*, which runs in a read-evaluate-print loop.

Q: how about complied language?

> JavaScript programmers know the value of everything but the cost of nothing. --Alan Perils -- Oscar Wilde

Modes of evaluation

    1. applicative order: evaluates everything and then apply
    2. normal order: fully expand and then reduce when needed

In JS (and python), the && and || are syntactic forms, not operators, their right-hand expression is not always evaluated.

* Something to explore: Newton's Method for square root.
