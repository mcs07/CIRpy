.. _misc:

Miscellaneous
=============

Tautomers
---------

To get all possible resolved tautomers, use the ``tautomers`` parameter::

    tautomers = query('warfarin', 'smiles', tautomers=True)

The Molecule object
-------------------

The Molecule class provides an easy way to collect and store various structure representations and properties for a
given input::

    from cirpy import Molecule

    mol = Molecule('N[C@@H](C)C(=O)O')

``mol`` then has the following properties::

    mol.stdinchi
    mol.stdinchikey
    mol.smiles
    mol.ficts
    mol.ficus
    mol.uuuuu
    mol.hashisy
    mol.sdf
    mol.names
    mol.iupac_name
    mol.cas
    mol.image_url               # The url of a GIF image
    mol.twirl_url               # The url of a TwirlyMol 3D viewer
    mol.mw                      # Molecular weight
    mol.formula
    mol.h_bond_donor_count
    mol.h_bond_acceptor_count
    mol.h_bond_center_count
    mol.rule_of_5_violation_count
    mol.rotor_count
    mol.effective_rotor_count
    mol.ring_count
    mol.ringsys_count

The first time you access each one of these properties, a request is made to the CIR servers. The result is cached,
however, so subsequent access is much faster.

Downloading files
-----------------

A convenience function is provided to facilitate downloading the CIR output to a file::

    cirpy.download('Aspirin', 'test.sdf', 'sdf')
    cirpy.download('Aspirin', 'test.sdf', 'sdf', overwrite=True)

This works in the same way as the ``resolve`` function, but also accepts a filename. There is an optional ``overwrite``
parameter to specify whether any existing file should be overwritten.

Constructing API URLs
---------------------

Construct API URLs::

    >>> cirpy.construct_api_url('Porphyrin', 'smiles')
    'http://cactus.nci.nih.gov/chemical/structure/Porphyrin/smiles/xml'


Logging
-------

CIRpy can generate logging statements if required. Just set the desired logging level::

    import logging
    logging.basicConfig(level=logging.DEBUG)

The logger is named 'cirpy'. There is more information on logging in the `Python logging documentation`_.


Pattern matching
----------------

.. note::

   It looks like the ``name_pattern`` resolver no longer works.


There is an additional ``name_pattern`` resolver that allows for Google-like searches. For example::

    results = query('Morphine','smiles', ['name_pattern'])

The ``notation`` attribute of each ``Result`` will show you the name of the match (e.g. "Morphine N-oxide", "Morphine
Sulfate") and the ``value`` attribute will be the representation specified in the query (SMILES in the above example).

`Read more about pattern matching on the CIR blog`_.

.. _`Python logging documentation`: http://docs.python.org/2/howto/logging.html
.. _`Read more about pattern matching on the CIR blog`: http://cactus.nci.nih.gov/blog/?p=1456
