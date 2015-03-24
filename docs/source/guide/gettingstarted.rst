.. _gettingstarted:

Getting started
===============

This page gives a introduction on how to get started with CIRpy. Before we start, make sure you have
:ref:`installed CIRpy <install>`.

Basic usage
-----------

The simplest way to use CIRpy is with the ``resolve`` function::

    >>> import cirpy
    >>> cirpy.resolve('Aspirin', 'smiles')
    'C1=CC=CC(=C1C(O)=O)OC(C)=O'

The first parameter is the input string and the second parameter is the desired output representation. The main
output representations for the second parameter are::

    stdinchi
    stdinchikey
    inchi
    smiles
    ficts
    ficus
    uuuuu
    hashisy
    sdf
    names
    iupac_name
    cas
    chemspider_id
    formula

All return a string, apart from ``names`` and ``cas``, which return a list of strings.

File formats
------------

Output can additionally be returned in a variety of file formats that are specified using the second parameter in the
same way::

    >>> cirpy.resolve('c1ccccc1', 'cif')
    "data_C6H6\n#\n_chem_comp.id\t'C6H6'\n#\nloop_\n_chem_comp_atom.comp_id\n..."

The full list of file formats::

    alc
    cdxml
    cerius
    charmm
    cif
    cml
    ctx
    gjf
    gromacs
    hyperchem
    jme
    maestro
    mol
    mol2
    mrv
    pdb
    sdf3000
    sln
    xyz

Properties
----------

A number of calculated structure-based properties can be returned, also specified using the second parameter::

    >>> cirpy.resolve('coumarin 343', 'h_bond_acceptor_count')
    '5'


The full list of properties::

    mw                           # (Molecular weight)
    h_bond_donor_count
    h_bond_acceptor_count
    h_bond_center_count
    rule_of_5_violation_count
    rotor_count
    effective_rotor_count
    ring_count
    ringsys_count

