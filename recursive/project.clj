(defproject codility "0.1.0"
  :description "Practicing algorithmicw"
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [expectations "2.1.9"]]
  :plugins [[lein-autoexpect "1.0"]
            [lein-ancient "0.6.10"]]

  :main bubleSort
  :aot [bubleSort])
