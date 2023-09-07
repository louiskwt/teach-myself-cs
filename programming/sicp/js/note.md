## Applicative vs Normal Order Evaluation

Applicative order and normal order are evaluation strategies used in programming languages, particularly when it
comes to evaluating function arguments. Let's take a closer look at each strategy:

### Applicative Order Evaluation:

- Applicative order evaluation, also known as eager evaluation or strict evaluation, is an evaluation strategy where function arguments are evaluated before applying the function. In this strategy, the arguments are fully evaluated, and the resulting values are then passed to the function for computation.

In applicative order evaluation, the arguments are evaluated from left to right, regardless of whether the function needs all the arguments or not. This means that all arguments are evaluated before the function call is made.

### Normal Order Evaluation:

- Normal order evaluation, also known as lazy evaluation, is an evaluation strategy where function arguments are not evaluated until they are actually needed. In this strategy, the arguments are passed as unevaluated expressions, and they are evaluated only when their values are required for computation.

In normal order evaluation, the arguments are not evaluated if they are not used in the function body. The evaluation is delayed until the value is explicitly needed.
