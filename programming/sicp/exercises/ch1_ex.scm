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