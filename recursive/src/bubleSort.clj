(ns bubleSort
  (:gen-class))

  (defn currentIsBiggerThanNextOne [B i]
  ;;   (println "checking" i "in" B)
    (> (get B i) (get B (inc i))))


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

  (defn bubleSortOnce [A]
      (let [n (count A) res (loop [B A i 0]
                  (if (< i (dec n))
                    (if (currentIsBiggerThanNextOne B i)
                      (recur (swapCurrentAndNext B i)
                             (inc i))
                      (recur B (inc i)))
                    B))]
        res))



(defn -main [& args]
  (prn "trying bigger than the next")
  (prn (currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 0))
  (prn (currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 1))
  (prn (currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 2))
  (prn (currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 3))
  (prn (currentIsBiggerThanNextOne [1 8 4 2 5 7 ] 4))
  
  (prn "trying swapCurrentAndNext")
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 0))
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 1))
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 2))
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 3))
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 4))
  (prn (swapCurrentAndNext [1 8 4 2 5 7 ] 5))
  
  (prn "trying bubleSort")
  (prn (bubleSortOnce [1 8 4 2 5 7 ]))

)

