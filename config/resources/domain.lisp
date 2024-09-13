(in-package :mu-cl-resources)

(setf *include-count-in-paginated-responses* t)
(setf *supply-cache-headers-p* t)
(setf sparql:*experimental-no-application-graph-for-sudo-select-queries* t)
(setf *cache-model-properties-p* t)
(setf mu-support::*use-custom-boolean-type-p* nil)
(setq *cache-count-queries-p* t)
(setf sparql:*query-log-types* nil) ;; hint: use app-http-logger for logging queries instead, all is '(:default :update-group :update :query :ask)


;; example
;; (define-resource dataset ()
;;   :class (s-prefix "dcat:Dataset")
;;   :properties `((:title :string ,(s-prefix "dct:title"))
;;                 (:description :string ,(s-prefix "dct:description")))
;;   :has-one `((catalog :via ,(s-prefix "dcat:dataset")
;;                       :inverse t
;;                       :as "catalog"))
;;   :has-many `((theme :via ,(s-prefix "dcat:theme")
;;                      :as "themes"))
;;   :resource-base (s-url "http://webcat.tmp.semte.ch/datasets/")
;;   :on-path "datasets")

(define-resource concept-scheme ()
  :class (s-prefix "skos:ConceptScheme")
  :properties `((:label :string ,(s-prefix "skos:prefLabel")))
  :has-many `((concept :via ,(s-prefix "skos:topConceptOf")
                       :inverse t
                       :as "children"))
  :resource-base (s-url "http://app.hackathon-4.s.redhost.be/schemes/")
  :on-path "concept-schemes")

(define-resource concept ()
  :class (s-prefix "skos:Concept")
  :properties `((:label :string ,(s-prefix "skos:prefLabel"))
                (:order :number ,(s-prefix "ext:number")))
  :has-many `((concept :via ,(s-prefix "skos:broader")
                       :inverse t
                       :as "children"))
  :has-one `((concept :via ,(s-prefix "skos:broader")
                      :as "parent"))
  :resource-base (s-url "http://app.hackathon-4.s.redhost.be/concepts/")
  :on-path "concepts")

;; reading in the domain.json
(read-domain-file "domain.json")
