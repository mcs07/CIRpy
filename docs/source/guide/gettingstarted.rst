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
    formula

All return a string, apart from ``names`` and ``cas``, which return a list of strings.

File formats
------------

Output can additionally be returned in a variety of file formats that are specified using the second parameter in the
same way::

    >>> cirpy.resolve('c1ccccc1', 'cif')
    "data_C6H6\n#\n_chem_comp.id\t'C6H6'\n#\nloop_\n_chem_comp_atom.comp_id\n..."

The full list of file formats::

    alc         # Alchemy format
    cdxml       # CambridgeSoft ChemDraw XML format
    cerius      # MSI Cerius II format
    charmm      # Chemistry at HARvard Macromolecular Mechanics file format
    cif         # Crystallographic Information File
    cml         # Chemical Markup Language
    ctx         # Gasteiger Clear Text format
    gjf         # Gaussian input data file
    gromacs     # GROMACS file format
    hyperchem   # HyperChem file format
    jme         # Java Molecule Editor format
    maestro     # Schroedinger MacroModel structure file format
    mol         # Symyx molecule file
    mol2        # Tripos Sybyl MOL2 format
    mrv         # ChemAxon MRV format
    pdb         # Protein Data Bank
    sdf3000     # Symyx Structure Data Format 3000
    sln         # SYBYL Line Notation
    xyz         # xyz file format

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

