; intro to prefix form

(+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) ;74/5

; intro to prefix form
(/  (+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) (* 3 (- 6 2) (- 2 7)))

; three square sum ans
define (square x)
        (* x x)
    )

(define (square-sum x y)
        (+ (square x) (square y))
    )

(define (>= x y)
  (if (or (> x y) (= x y))
    x
    y
    ))

(define (next-large-num curr x y z)
        ; one arm if will not work in auto grader because it can be buggy
        (when (and (= x curr) (or (> y z) (= y z))) y)
        (when (and (= y curr) (or (> x z) (= x z))) x)
        z
    )

(define (three-square-sum a b c)
        (define curr (>= a b))
        (square-sum curr (next-large-num curr a b c))
         )

; composite expression
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

; ^ inside the body of the function a-plus-abs-b, the operator is first determined by the conditional check if b is bigger than 0. If b is bigger than 0, it will return the + operator, or else it will return - to ensure that a will always add the absolute value of b

; Order of calculation

;What behavior will Ben observe with an interpreter that uses applicative-order evaluation? What behavior will he observe with an interpreter that uses normal-order evaluation? Explain your answer.(Assume that the evaluation rule for the special form if is the same whether the interpreter is using normal or applicative order: The predicate expression is evaluated first, and the result determines whether to evaluate the consequent or the alternative expression.)

; In case of normal order, the functoin will return 0 and everything should be fine because the y part will never be evaluated since x = 0 and the problematic part (p) will never be run

; but in an interpreter that uses applicative-order-evaluation, the problematic (p) will first be evaluated in the before its body runs, and the entire program will hang 

; special form
; when wrapping the cond inside a function, it returns an actuatl value and will be first evaluated if used in the body of a functoin; in that case the new-if cannot be used to check / determine whether the guess and x are good enough


;Ex 1,7 
(define (average x y) (/ (+ x y) 2))
(define (improve guess x) (average guess (/ x guess)))
(define (good-enough? guess x)
 (< (abs (- (square guess) x)) 0.01)) ; change from 0.001 to 0.01

(define (sqrt-iter guess x) (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

# the problem with the good-enough? test is that it loses its precision when it comes to a very large or small number
  an example would be:
                      (square (sqrt 1000)) would not give you back 1000
                      (sqrt (+ (sqrt 2) (sqrt 3))) is a bit off
 to improve it, I changed the checking value 0.001 to 0.01, and the results have been improved to be a bit more precise, compared to my scientific calculator


