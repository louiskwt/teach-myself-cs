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


