(ns clojproj.4clojure)

(defn duplicate-list [x]
  (mapcat #(conj '() % %) x))

(let [[first-name last-name & aliases]
           (list "Rich" "Hickey" "The Clojurer" "Go Time" "Lambda Guru")]
       (str
            aliases))
