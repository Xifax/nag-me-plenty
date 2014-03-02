Nag Me Plenty
=============

Small little tool to nag you relentlessly.

Implemented in Python 2.7 and Enaml.

Running application
-------------------

Works from virtualenv (system-wide Enaml is prone to blow ups):

    bin/nagme


Nota Bene
---------

PyQt4 & SIP are a pain to install. Use either virtualenvwrapper script or
simply run `make link-qt` to copy PyQt lib to site virtualenv packages.
