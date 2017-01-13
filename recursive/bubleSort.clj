(defn currentIsBiggerThanNextOne [B i]
;;   (println "checking" i "in" B)
  (> (get B i) (get B (inc i))))

(currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 0)
(currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 1)
(currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 2)
(currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 3)
(currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 4)


(defn swapCurrentAndNext [B i]
;;   (println "swapping" i "in" B)
  (let [n (count B)]
    (if (< i (dec n))
      (vec (concat (conj (conj (subvec B 0 i)
                        (get B (inc i)))
                    (get B i))
              (if (< i (dec n))
                (subvec B (+ i 2))
                [])))
      B)))

(swapCurrentAndNext [1 8 4 2 5 7 ] 0)
(swapCurrentAndNext [1 8 4 2 5 7 ] 1)
(swapCurrentAndNext [1 8 4 2 5 7 ] 2)
(swapCurrentAndNext [1 8 4 2 5 7 ] 3)
(swapCurrentAndNext [1 8 4 2 5 7 ] 4)
(swapCurrentAndNext [1 8 4 2 5 7 ] 5)

(defn bubleSortOnce [A]
    (let [n (count A) res (loop [B A i 0]
                (if (< i (dec n))
                  (if (currentIsBiggerThanNextOne B i)
                    (recur (swapCurrentAndNext B i)
                           (inc i))
                    (recur B (inc i)))
                  B))]
      res))


(bubleSortOnce [1 8 4 2 5 7 ])


