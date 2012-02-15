.. simpleversions documentation master file, created by
   sphinx-quickstart on Fri Jul 22 10:07:34 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to simpleversions's documentation!
===========================================

Reference Material
==================

.. toctree::
   :maxdepth: 1
   :glob:

   api/*

Building Documentation
======================
You can always `view the source code on github
<http://github.com/wgen/simpleversions>`_.  This documentation
lives in :file:`src/docs`.

To **run unittests**::

    $ python setup.py nosetests

To **build this documentation**::

    $ python setup.py build_sphinx

The built documentation is available (by default) in :file:`build/sphinx/html`,
and can be viewed locally on your web browser without the need for a separate
web server.

Logging_utils is only compatible with Python version 2.5 and greater, as it uses
absolute_import from __future__

Index and Glossary
==================

* :ref:`genindex`
* :ref:`search`

