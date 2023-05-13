; intro to prefix form

(+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) ;74/5

(* 3 (- 6 2) (- 2 7)) 

; ans
(/  (+ 5 4 (- 2 (- 3 (+ 6 ( / 4 5) ) ) ) ) (* 3 (- 6 2) (- 2 7)))


(define (largest a b c)
    (define l 0)
    (if (and (> a b) (> a c))
      (= l a))
    (if (and (> b c) (> b a))
      (= l b))
    (if (and (> c a) (> c b))
      (= l c))
    l 
  )

(define (smallest a b c)
        (define s 0)
        (if (and (< a b) (< a c))
          (= s a))
        (if (and (< b a) (< b c))
          (= s b))
        (if (and (< c a) (< c b))
          (= s c))
        s
)

(define (second-largest a b c)
        (define sl 0)
        (if (and (not (largest(a b c) a)) (not (smallest(a b c) a)))
          (= sl a))
        (if (and (not (largest(a b c) b)) (not (smallest(a b c) b)))
          (= sl b))
        (if (and (not (largest(a b c) c)) (not (smallest(a b c) c)))
          (= sl c))
        c
)

(define (square x)
        (* x x)
    )

(define (square-sum x y)
        (+ (square x) (square y))
    )



