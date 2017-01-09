(defn fibonacci [n]
  (case n
    0 0
    1 1
    2 1
    (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(fibonacci 1)
(fibonacci 2)
(fibonacci 3)
(fibonacci 4)
(fibonacci 5)
(fibonacci 6)


(defn fibonnaciIter [n]
  (defn loop [n, n1, n2]
    n)
  (loop n 0 1))

(fibonnaciIter 1)
(fibonnaciIter 2)
(fibonnaciIter 3)
(fibonnaciIter 4)
(fibonnaciIter 5)
(fibonnaciIter 6)
