(ns clojproj.core
  )

(require '[clojure.string :as str])
(require '[clojure.core.reducers :as r])

(defn parse-string [s]
  (seq (char-array s)))

(defn split-string [s]
  (str/split s #"\+"))

(defn add-splitted-string [ss]
  (r/fold + (map read-string ss)))

(defn sum-a-string [s]
  (if (empty? s)
    0
    (add-splitted-string (split-string s))))


