.. CIRpy documentation master file, created by sphinx-quickstart on Tue Mar 24 16:12:38 2015.

CIRpy
=====

.. sectionauthor:: Matt Swain <m.swain@me.com>

**CIRpy** is a Python interface for the `Chemical Identifier Resolver (CIR)`_ by the CADD Group at the NCI/NIH.

CIR is a web service that will resolve any chemical identifier to another chemical representation. For example, you can
pass it a chemical name and and request the corresponding SMILES string::

    >>> import cirpy
    >>> cirpy.resolve('Aspirin', 'smiles')
    'C1=CC=CC(=C1C(O)=O)OC(C)=O'

CIRpy makes interacting with CIR through Python easy. There's no need to construct url requests and parse XML responses
— CIRpy does all this for you.

Features
--------

- Resolve chemical identifiers such as names, CAS registry numbers, SMILES strings and SDF files to any other chemical
  representation.
- Get calculated properties such as molecular weight and hydrogen bond donor and acceptor counts.
- Download chemical file formats such as SDF, XYZ, CIF and CDXML.
- Get 2D compound depictions as a GIF or PNG images.
- Supports Python versions 2.7 – 3.4.
- Released under the `MIT license`_.

User guide
----------

A step-by-step guide to getting started with CIRpy.

.. toctree::
   :maxdepth: 2

   guide/install
   guide/gettingstarted
   guide/resolvers
   guide/query
   guide/misc
   guide/contributing

API documentation
-----------------

Comprehensive API documentation with information on every function, class and method.

.. toctree::
   :maxdepth: 2

   api

.. _`Chemical Identifier Resolver (CIR)`: http://cactus.nci.nih.gov/chemical/structure
.. _`MIT license`: https://github.com/mcs07/CIRpy/blob/master/LICENSE
