(defn- bubble [ys x] ; make one value (the first in the vector) buble up
  (print "bubble function: ")
  (print " ys:")
  (print ys)
  (print " x:")
  (println x)

  (if-let [y (peek ys)] ; get the first element
    (if (> y x)
      (conj (pop ys) x y)
      (conj ys x))
    [x])) ; if empty, pupulate it with this first element

(defn bubble-sort [xs]
  (print "bubble-sort function: ")
  (print " xs:")
  (println xs)
  (let [ys (reduce bubble [] xs)]
    (print "ys:")
    (println ys)
    (if (= xs ys) ; no change in this iteration -> we have finished
      xs
      (recur ys)))) ; make the next vaule bubble-up

(bubble-sort [5 4 3 2 1]) ;
