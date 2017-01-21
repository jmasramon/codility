(ns clojproj.theJoy)


(defn sum-down-from [sum x]
  (if (> x 0)
    (recur (+ sum x) (dec x))
    sum))

(defn sum-down-from-loop [x]
  (loop [sum 0 x x]
    (if (> x 0)
      (recur (+ sum x) (dec x))
      sum)))

(defn sum-down-from-idiomatic [x]
  (reduce +
          (take-while pos?
                      (iterate dec x))))
