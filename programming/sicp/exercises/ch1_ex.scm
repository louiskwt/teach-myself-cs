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

; Sum of Square
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

(define (solution x y z) (+ (square (getlargest(x y z))) (square (getsecondlargest x y z))))