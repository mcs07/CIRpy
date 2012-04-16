# CIRpy

## Introduction

CIRpy is a Python interface for the [Chemical Identifier Resolver (CIR)](http://cactus.nci.nih.gov/chemical/structure) by the CADD Group at the NCI/NIH.

CIR is a web service that performs various chemical name to structure conversions. In short, it will (attempt to) resolve the structure of any chemical identifier that you throw at it. Under the hood it uses a combination of [OPSIN](http://opsin.ch.cam.ac.uk/), [ChemSpider](http://www.chemspider.com/) and CIR's own database.

CIRpy makes interacting with CIR through Python easy. There's no need to construct url requests and parse XML responses - CIRPy does all this for you.

## Basic usage

The simplest way to use CIRpy is with the `resolve` function:

    import cirpy

    smiles_string = cirpy.resolve('Aspirin','smiles')
    
The first parameter is the input string and the second parameter is the desired output representation. The available options for the second parameter are:

    stdinchi
    stdinchikey
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
    mw						# Molecular weight
    formula
    
All return a string, apart from `names` which returns a list of strings.

There are also a number of structure based properties that can be specified using the second parameter in the same way:

    h_bond_donor_count
    h_bond_acceptor_count
    h_bond_center_count
    rule_of_5_violation_count
    rotor_count
    effective_rotor_count
    ring_count
    ringsys_count

## Resolving names

By default, CIR resolves names first by using OPSIN, and if that fails, using a lookup in its own name index ([More info on the CIR blog](http://cactus.nci.nih.gov/blog/?p=1386)). A ChemSpider lookup is also available, but not used by default. With CIRpy you can tell CIR to use any combination of these three services, and also specify the order of precedence.

Just use the `resolve` function with a third parameter - a list containing any of the strings `opsin_name`, `cir_name` and `chemspider_name`, in the order in which they should be tried.

    i = cirpy.resolve('Aspirin', 'inchi', ['opsin_name','cir_name','chemspider_name'] )
    i = cirpy.resolve('Aspirin', 'inchi', ['chemspider_name','cir_name'] )

## Other resolvers

CIR interprets input strings using "resolvers". `opsin_name`, `cir_name` and `chemspider_name` are just three examples. When no resolvers are specified, each one is tried in turn until one is successful.

The available resolvers are not well documented, but the ones that I can identify, roughly in the order that they are tried by default, are:

    smiles
    stdinchikey
    stdinchi
    ncicadd_identifier		# (for FICTS, FICuS, uuuuu)
    hashisy
    cas_number
    chemspider_id			# input must be chemspider_id=1234567
    opsin_name
    cir_name
    chemspider_name

**Note:** `chemspider_name` is not used unless explicitly specified.

You can customise which resolvers are used (and their order) in exactly the same way as shown for the name resolvers above:

    sdf = cirpy.resolve('Aspirin','sdf', ['smiles','inchi','opsin_name','cir_name'] )
    name_list = cirpy.resolve('C1=CC=CC(=C1C(O)=O)OC(C)=O','names', ['smiles'] )

## Multiple results

The `resolve` function will only return the top match for a given input. However, sometimes multiple resolvers will match an input (e.g. the name resolvers), and individual resolvers can even return multiple results (e.g. chemspider_name). The `query` function will return every result.

    result = cirpy.query('Aspirin', 'inchi')

As with the `resolve` function, it is possible to specify which resolvers are used:    
    
    result = cirpy.query('Aspirin', 'smiles', ['opsin_name','cir_name'])

Example result:
    
    [ {'resolver':'opsin_name', 'value':'N[C@@H](C)C(=O)O', notation:'Aspirin'},
      {'resolver':'cir_name', 'value':'[C@@H](C(O)=O)(C)N', notation:'Aspirin'} ]

## Pattern matching

There is an additional `name_pattern` resolver that allows for Google-like searches. For example:

    results = query('Morphine','smiles', ['name_pattern'])
    
The `notation` field of each item in the results will show you the name of the match (e.g. "Morphine N-oxide", "Morphine Sulfate") and the `value` field will be the representation specified in the query (SMILES in the above example).

[More info on the CIR blog](http://cactus.nci.nih.gov/blog/?p=1456).

## Tautomers

To get Tautomers, use `tautomers:` before your input:

    tautomers = query('tautomers:warfarin','smiles')

## The Molecule object

The Molecule class provides an easy way to collect and store various structure representations and properties for a given input.

    from cirpy import Molecule

    mol = Molecule('N[C@@H](C)C(=O)O', ['smiles'])


mol then has the following properties:

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
    mol.chemspider_id
    mol.image_url			    # The url of a GIF image
    mol.twirl_url			    # The url of a TwirlyMol 3D viewer
    mol.mw				    	# Molecular weight
    mol.formula
    mol.h_bond_donor_count
    mol.h_bond_acceptor_count
    mol.h_bond_center_count
    mol.rule_of_5_violation_count
    mol.rotor_count
    mol.effective_rotor_count
    mol.ring_count
    mol.ringsys_count

The first time you access each one of these properties, a request is made to the CIR servers. The result is cached, however, so subsequent access is much faster.

## Downloading files

To resolve an identifier to a structure in a specific file format, use the `download` function:

	cirpy.download('Aspirin', 'test.sdf', 'sdf')
	cirpy.download('Aspirin', 'test.sdf', 'sdf', True)
	
The first parameter is the input, the second is the file name, and the third is the file format. There is an optional fourth parameter to specify whether any existing file should be overwritten. The available formats are:

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
sdf
sdf3000
sln
smiles
xyz

Alternatively, if you have a `Molecule` object you can use the `download` method in a similar way:

    mol = Molecule('warfarin')
    mol.download('test.cml', 'cml', True)

## Acknowledgements

All of CIRpy's functionality relies on the fantastic [CIR web service](cactus.nci.nih.gov/chemical/structure) created by the CADD Group at the NCI/NIH.
