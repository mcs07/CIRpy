.. _resolvers:

Resolvers
=========

CIR interprets input strings using a series of "resolvers" in a specific order. Each one is tried in turn until one
successfully interprets the input.

The available resolvers are not well documented, but the ones that I can identify, roughly in the order that they are
tried by default, are::

    smiles
    stdinchikey
    stdinchi
    ncicadd_identifier      # (for FICTS, FICuS, uuuuu)
    hashisy
    cas_number
    chemspider_id           # input must be chemspider_id=1234567
    name_by_opsin
    name_by_cir
    name_by_chemspider

Customizing resolvers
---------------------

You can customize which resolvers are used (and the order they are used in), by supplying a list of resolvers as a
third parameter to the ``resolve`` function:

    >>> cirpy.resolve('Aspirin', 'sdf', ['cas_number', 'name_by_cir', 'name_by_opsin'])
    'C9H8O4\nAPtclcactv03241513052D 0   0.00000     0.00000\n \n 21 21...'
    >>> cirpy.resolve('C1=CC=CC(=C1C(O)=O)OC(C)=O', 'names', ['smiles', 'stdinchi'])
    ['2-acetyloxybenzoic acid', '2-Acetoxybenzoic acid', '50-78-2', ...]

Manually specifying the resolvers can be useful when an ambiguous input identifier could be interpreted as multiple
different formats, but you know which format it is.

Resolving names
---------------

By default, CIR resolves names first by using OPSIN, and if that fails, using a lookup in its own name index. A
ChemSpider lookup is also available, but not used by default. With CIRpy you can tell CIR to use any combination of
these three services, and also specify the order of precedence.

Just use the ``resolve`` function with a third parameter - a list containing any of the strings ``name_by_opsin``,
``name_by_cir`` and ``name_by_chemspider``, in the order in which they should be tried::

    >>> cirpy.resolve('Aspirin', 'smiles', ['name_by_opsin', 'name_by_cir', 'name_by_chemspider'])
    'C1=CC=CC(=C1C(O)=O)OC(C)=O'
    >>> cirpy.resolve('Aspirin', 'smiles', ['name_by_chemspider','name_by_cir'])
    'CC(=O)OC1=C(C=CC=C1)C(O)=O'

`Read more about resolving names on the CIR blog`_.

.. note::

   The ``name_by_chemspider`` resolver is not used unless explicitly specified in the resolvers list.

.. _`Read more about resolving names on the CIR blog`: http://cactus.nci.nih.gov/blog/?p=1386
