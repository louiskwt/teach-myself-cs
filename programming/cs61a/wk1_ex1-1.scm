; intro to prefix form

(+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) ;74/5

; intro to prefix form
(/  (+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) (* 3 (- 6 2) (- 2 7)))

; three square sum ans
(define (square x)
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

(define (three-square-sum a b c)
        (square-sum (>= a b) (>= b c)))


