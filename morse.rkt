#!/usr/bin/env racket
#lang racket

(require (only-in racket/cmdline command-line)
         racket/dict
         racket/set)

(define legend
  (make-hash
   '((#\a . ".-")
     (#\b . "-...")
     (#\c . "-.-.")
     (#\d . "-..")
     (#\e . ".")
     (#\f . "..-.")
     (#\g . "--.")
     (#\h . "....")
     (#\i . "..")
     (#\j . ".---")
     (#\k . "-.-")
     (#\l . ".-..")
     (#\m . "--")
     (#\n . "-.")
     (#\o . "---")
     (#\p . ".--.")
     (#\q . "--.-")
     (#\r . ".-.")
     (#\s . "...")
     (#\t . "-")
     (#\u . "..-")
     (#\v . "...-")
     (#\w . ".--")
     (#\x . "-..-")
     (#\y . "-.--")
     (#\z . "--..")
     (#\space . "/")
     (#\0 . "-----")
     (#\1 . ".----")
     (#\2 . "..---")
     (#\3 . "...--")
     (#\4 . "....-")
     (#\5 . ".....")
     (#\6 . "-....")
     (#\7 . "--...")
     (#\8 . "---..")
     (#\9 . "----.")
     (#\9 . ",")
     (#\. . ".")
     (#\! . "!")
     (#\? . "?"))))


(define reverse-legend
  (let ((h (make-hash)))
    (hash-for-each legend
                   (lambda (k v)
                     (hash-set! h v k)))
    h))

(define (morse? s)
  (let [(st (set #\. #\- #\/))]
    (set-member? st (string-ref s 0))))

(define (morse->eng s)
  (dict-ref reverse-legend s))

(define (eng->morse s)
  (map (lambda (k) (dict-ref legend k))
       (string->list s)))

(define (decode s)
  (let [(s* (string-downcase s))]
    (cond
      ((morse? s*)
       (list->string (map morse->eng (string-split s* " "))))
      (else
       (string-join (eng->morse s*) " ")))))

(define main
  (command-line
   #:usage-help
   "Translate English to Morse code, and vice versa. <msg> is the message to be"
   "decoded. Input type will be automatically detected and converted. Must be"
   "wrapped in quotes."
   #:args (msg)
   (println (decode msg))))
