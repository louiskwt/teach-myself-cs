--1.1.1
10
12
8
3
6

--1.1.2
19
false

--1.2
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))

-- Sum of Square
(define (square x) (* x x))
(define (solution x, y, z) (+ (square x) (square y)))