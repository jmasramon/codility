(defn fibonacci [n]
  (case n
    0 0
    1 1
    2 1
    (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(fibonacci 0)
(fibonacci 1)
(fibonacci 2)
(fibonacci 3)
(fibonacci 4)
(fibonacci 5)
(fibonacci 6)


(defn fibonnaciIter [n]
  (loop [n0 n, n1 0, n2 1]
    (case n0
      0 n1
      1 n2
      (recur (dec n0) n2  (+ n2 n1)))))

(fibonnaciIter 0)
(fibonnaciIter 1)
(fibonnaciIter 2)
(fibonnaciIter 3)
(fibonnaciIter 4)
(fibonnaciIter 5)
(fibonnaciIter 6)
