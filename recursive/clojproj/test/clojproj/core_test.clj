(ns clojproj.core-test
  (:require [expectations :refer :all]
            [clojproj.core :refer :all]))


(expect 0 (sum-a-string ""))
(expect 0 (sum-a-string "0"))
(expect 1 (sum-a-string "1"))
(expect 123456 (sum-a-string "123456"))

(expect '(\1 \2 \+ \3) (parse-string "12+3"))

(expect ["12" "3"] (split-string "12+3"))

(expect 15 (add-splitted-string  ["12" "3"] ))

;; (expect 15 (sum-a-string "12+3"))


