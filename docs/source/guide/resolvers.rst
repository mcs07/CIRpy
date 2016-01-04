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
    name_by_opsin
    name_by_cir

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

By default, CIR resolves names first by using OPSIN, and if that fails, using a lookup in its own name index. With
CIRpy you can customize which of these resolvers are used, and also specify the order of precedence.

Just use the ``resolve`` function with a third parameter - a list containing any of the strings ``name_by_opsin``,
``name_by_cir`` in the order in which they should be tried::

    >>> cirpy.resolve('Morphine', 'smiles', ['name_by_opsin'])
    'CN1CC[C@]23[C@H]4Oc5c(O)ccc(C[C@@H]1[C@@H]2C=C[C@@H]4O)c35'
    >>> cirpy.resolve('Morphine', 'smiles', ['name_by_cir','name_by_opsin'])
    'CN1CC[C@]23[C@H]4Oc5c(O)ccc(C[C@@H]1[C@@H]2C=CC4O)c35'

`Read more about resolving names on the CIR blog`_.

.. note::

   The ``chemspider_id`` and ``name_by_chemspider`` resolvers no longer exist.

.. _`Read more about resolving names on the CIR blog`: http://cactus.nci.nih.gov/blog/?p=1386
