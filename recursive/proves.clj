;; Prcticing with finding maximums recursively without assignment

(defn prova []
  (let [max_h 0, ind_max 0, data [1 2 3 4 9 5 6 7 8]]
    (let [res (loop [i 8 max_hh max_h i_max ind_max]
                (if (> i 0)
                  (let [mountainH (data i)]
                    ; mountainH: represents the height of one mountain.
                    (if (> mountainH max_hh)
                      (recur (dec i) mountainH i)
                      (recur (dec i) max_hh i_max)))
                  i_max))]
        (println res))))


(defn prova2 []
  (let [imax (first (apply max-key second (map-indexed vector [1 2 3 4 9 5 6 7 8])))]
    (println imax)))

(prova2)
(prova)
