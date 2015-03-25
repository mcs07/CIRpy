CIRpy
=====

.. image:: http://img.shields.io/pypi/v/CIRpy.svg?style=flat
    :target: https://pypi.python.org/pypi/CIRpy

.. image:: http://img.shields.io/pypi/l/CIRpy.svg?style=flat
    :target: https://github.com/mcs07/CIRpy/blob/master/LICENSE

.. image:: http://img.shields.io/travis/mcs07/CIRpy/master.svg?style=flat
    :target: https://travis-ci.org/mcs07/CIRpy

.. image:: http://img.shields.io/coveralls/mcs07/CIRpy/master.svg?style=flat
    :target: https://coveralls.io/r/mcs07/CIRpy?branch=master

Introduction
------------

**CIRpy** is a Python interface for the `Chemical Identifier Resolver (CIR)`_ by the CADD Group at the NCI/NIH.

CIR is a web service that will resolve any chemical identifier to another chemical representation. For example, you can
pass it a chemical name and and request the corresponding SMILES string::

    >>> import cirpy
    >>> cirpy.resolve('Aspirin', 'smiles')
    'C1=CC=CC(=C1C(O)=O)OC(C)=O'

CIRpy makes interacting with CIR through Python easy. There's no need to construct url requests and parse XML responses
— CIRpy does all this for you.

Installation
------------

Install CIRpy using::

    pip install cirpy

Alternatively, try one of the other `installation options`_.

Documentation
-------------

Full documentation is available at http://cirpy.readthedocs.org.

Contribute
----------

- Feature ideas and bug reports are welcome on the `Issue Tracker`_.
- Fork the `source code`_ on GitHub, make changes and file a pull request.

Acknowledgements
----------------

All of CIRpy's functionality relies on the fantastic `CIR web service`_ created by the CADD Group at the NCI/NIH.

License
-------

CIRpy is licensed under the `MIT license`_.

.. _`Chemical Identifier Resolver (CIR)`: http://cactus.nci.nih.gov/chemical/structure
.. _`installation options`: http://cirpy.readthedocs.org/en/latest/guide/install.html
.. _`CIR web service`: http://cactus.nci.nih.gov/chemical/structure
.. _`source code`: https://github.com/mcs07/CIRpy
.. _`Issue Tracker`: https://github.com/mcs07/CIRpy/issues
.. _`MIT license`: https://github.com/mcs07/CIRpy/blob/master/LICENSE
