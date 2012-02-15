Simpleversions
==============

This is a library intended to handle a relatively simple versioning scheme.

A version is composed of any number of subversions, separated by '_', '-', or '~'.
Each subversion is composed of any number of numbers, separated by '.' or ','.

A missing subversion is considered greater than a corresponding existing subversion
(so 1.0~10 < 1.0). This allows for subversions to be used as markings for pre-builds of a main product.
A missing number is considered to be 0 (so 1.0 == 1.0.0).
All other characters are ignored

Examples
========

::
    1 == 1.0 == 1.0.0 == 1.0.0a == 1.0.0test
    1 < 2 < 2.1~1 < 2.1 < 2.2
    1 > 1~100 > 1~1
