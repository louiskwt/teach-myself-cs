; ex 1.1.1
10
12
8
3
6

; ex 1.1.2
19
false

; ex 1.2
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))

; ex 1.3 Sum of Square
(define (square x) (* x x))

(define (getlarger x y)
    (cond ((>= x y) x)
          ((>= y x) y)
    )
)

(define (getlargest x y z)
    (cond ((and (>= x y) (>= x z)) x)
          ((and (>= y x) (>= y z)) y)
          ((and (>= z x) (>= z y)) z)
    )
)

(define (getsecondlargest x y z)
    (cond ((and (>= x y) (>= x z)) (getlarger y z))
          ((and (>= y x) (>= y z)) (getlarger x z))
          ((and (>= z x) (>= z y)) (getlarger x y))
    )
)

(define (solution x y z) (+ (square (getlargest x y z)) (square (getsecondlargest x y z))))

; ex 1.4
(define (mystery a b)
  ((if (> b 0) + -) a b))

;Describe the behavior of the procedure by selecting which descriptions are equivalent. If you think that the procedure definition is invalid, choose the reasons why.

; no errors
; equivalent: (+ a (abs b)) | (if (> b 0) (+ a b) (- a b)) | (+ a (if (> b 0) b (- b)))


; ex 1.5
(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))

; test 0 (p))
; In applicative-order evaluation, (p) will be evaluated, resulting in an infinite loop
; In normal-order evaluation, (p) is not evaluated because predicate of if evaluates to true

; ex 1.6
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
; the problem of not using the special form if is that it will lead to an infinite loop where sqrt-iter always evaluates itself

;ex 1.7
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) (* guess 0.001))) ; the 0.001 is already a faction_threshold

; solution
(define (square-root x)
  (sqrt-iter 1.0 x)
)

; ex 1.1.8 cube-root
  ; (display "guess: ")
  ;(display guess)
  ; (newline)
      ;(begin
      ;  (display "improved guess: ")
      ;  (display (improve-cube-root guess x))
      ;  (newline))

(define (cube x) (* x x x))

(define (good-enough? guess x)
  (< (abs (- (cube guess) x)) (* guess 0.001))) 

(define (cube-root-iter guess x)
  (if (good-enough? guess x)
      guess
      (cube-root-iter (improve-cube-root guess x) x)))

(define (improve-cube-root guess x)
  (/ (+ (/ x (square guess)) (* guess 2)) 3))

(define (cube-root x)
  (cube-root-iter 1.0 x))

; ex 1.1.9
(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))  ; it's recursive

(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b)))) ; it's iterative
  
; ex 1.1.10
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))

(A 1 10) ;1024
(A 2 4) ;65536
(A 3 3) ;65536

(define (f n) (A 0 n))

(define (g n) (A 1 n))

(define (h n) (A 2 n))

(define (k n) (* 5 n n))

;f(n) = 2n
; g(n) = 2
; h(n) = A(n-1, A(n-1, A(n-1, ... A(n-1, 2)...)))
; k(n) = 5n^2

; Tree recursion
(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))

; Tail Recursion
(define (fib n)
  (fib-iter 1 0 n))

(define (fib-iter a b count)
  (if (= count 0)
      b
      (fib-iter (+ a b) a (- count 1))))

; ex 1.1.11
(define (f n)
  (cond ((< n 3) n)
        (else (+ (f (- n 1)) (* 2 (f (- n 2))) (* 3 (f (- n 3)))))))


(define (f-iter n)
  (define (iter-helper a b c count)
    (if (= count 0)
        c
        (iter-helper (+ a (* 2 b) (* 3 c)) a b (- count 1))))
  (iter-helper 2 1 0 n))    

;ex 1.1.12
(define (solution row col)
  (cond ((= row 0) 0)
        ((= col 1) 1)
        ((= col row) 1)
        ((> col row) 0)
        ((< col 1) 0)
        (else (+ (solution (- row 1) col) (solution (- row 1) (- col 1))))
  )
) 

; ex 1.1.13
; Step 1: Base cases
; We start with the base cases of the Fibonacci sequence:
; Fib(0) = 0
; Fib(1) = 1

; Step 2: Inductive hypothesis
; Assume that for some k ≥ 1, Fib(k) = (φ^k - ψ^k)/√5, where ψ = (1 - √5)/2.

; Step 3: Inductive step
; We need to show that Fib(k+1) = (φ^(k+1) - ψ^(k+1))/√5.

; Using the definition of the Fibonacci sequence, Fib(k+1) = Fib(k) + Fib(k-1).

; Substituting the inductive hypothesis:
; Fib(k+1) = (φ^k - ψ^k)/√5 + (φ^(k-1) - ψ^(k-1))/√5

; Simplifying, we get:
; Fib(k+1) = (φ^k + φ^(k-1) - ψ^k - ψ^(k-1))/√5

; Next, we'll manipulate the expression to simplify it further.

; Step 4: Manipulation
; We know that φ and ψ are solutions to the quadratic equation x^2 = x + 1.

; For φ, we have:
; φ^2 = φ + 1

; Rearranging, we get:
; φ^2 - φ - 1 = 0

; Similarly, for ψ, we have:
; ψ^2 = ψ + 1

; Rearranging, we get:
; ψ^2 - ψ - 1 = 0

; Now, let's express φ^k and ψ^k in terms of φ and ψ:
; φ^k = φ^(k-1) * φ
; ψ^k = ψ^(k-1) * ψ

; Substituting these expressions into our previous equation, we get:
; Fib(k+1) = (φ^k + φ^(k-1) - ψ^k - ψ^(k-1))/√5
; = φ^(k-1) * (φ + 1) - ψ^(k-1) * (ψ + 1))/√5
; = φ^(k-1) * φ^2 - ψ^(k-1) * ψ^2)/√5

; Using the quadratic equations for φ and ψ, we can simplify further:
; Fib(k+1) = φ^(k+1) - ψ^(k+1))/√5

; Therefore, we have shown that Fib(k+1) = (φ^(k+1) - ψ^(k+1))/√5, assuming that Fib(k) = (φ^k - ψ^k)/√5.

; Step 5: Conclusion
; By induction, we have proven that for all n ≥ 0, Fib(n) = (φ^n - ψ^n)/√5.

; Now, let's examine the expression (φ^n - ψ^n)/√5. We know that ψ < 1, and as n gets larger, ψ^n approaches 0. Therefore, the term ψ^n becomes negligible.

; ex 1.1.14
; space complexity: n --> 3
; time complexity: 2^n --> 2^3 = 8

; ex 1.1.15
; How many times is the procedure p applied when (sine 12.15) is evaluated? --> 5
; What is the order of growth in space and number of steps (as a function of a) used by the process generated by the sine procedure when (sine a) is evaluated? --> Θ(log(n))

; ex 1.1.16
(define (even? n)
  (= (remainder n 2) 0))

(define (square n)
  (* n n))

(define (fast-expt-iter b counter product)
  (cond ((= counter 0) product)
        ((even? counter) (fast-expt-iter (square b) (/ counter 2) product))
        (else (fast-expt-iter b (- counter 1) (* product b)))
  ))

(define (fast-expt b n)
  (fast-expt-iter b n 1)
)

; ex 1.1.17
(define (even? n)
  (= (remainder n 2) 0))

(define (double x) 
  (+ x x))

(define (halve x)
  (/ x 2))

(define (fast-mul a b)
  (define (multiply-iter a b acc)
    (cond ((= b 0) acc)
          ((even? b) (multiply-iter (double a) (halve b) acc))
          (else (multiply-iter a (- b 1) (+ acc a)))))
  (multiply-iter a b 0))

; ex 1.1.18
(define (mul-iter a b) 
  (define (multiply-iter a b acc)
    (cond ((= b 0) acc)
          ((even? b) (multiply-iter (double a) (halve b) acc))
          (else (multiply-iter a (- b 1) (+ acc a)))))
  (multiply-iter a b 0))

; ex 1.1.19
(define (fib n)
  (fib-iter 1 0 0 1 n))

(define (even? n)
  (= (remainder n 2) 0))

(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   <??>      ; compute p'
                   <??>      ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))


