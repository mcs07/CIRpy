# -*- coding: utf-8 -*-
"""
Unit tests for cirpy.py

Python interface for the Chemical Identifier Resolver (CIR) by the CADD Group at the NCI/NIH.
https://github.com/mcs07/CIRpy
"""


import unittest

from cirpy import *
from urllib2 import HTTPError

class TestCIRpy(unittest.TestCase):

    def setUp(self):
        self.alanine_smiles = 'N[C@@H](C)C(=O)O'
        self.morphine_inchi = [{'value': 'InChI=1/C17H19NO3/c1-18-7-6-17-10-3-5-13(20)16(17)21-15-12(19)4-2-9(14(15)17)8-11(10)18/h2-5,10-11,13,16,19-20H,6-8H2,1H3/t10-,11+,13?,16-,17-/m0/s1', 'notation': 'Morphine', 'resolver': 'cir_name'}]

    def test_resolve(self):
        self.assertEqual(resolve('Alanine','smiles'), self.alanine_smiles)
        self.assertEqual(resolve('aruighaelirugaerg','inchi'), None)
        self.assertRaises(HTTPError, resolve, 'Alanine', 'arguergbaiurg')

    def test_query(self):
        self.assertEqual(query('Morphine','inchi'), self.morphine_inchi)
        self.assertEqual(query('sjkvhaldfu','inchi'), None)
        self.assertRaises(HTTPError, query, 'Morphine', 'ogiuewrgpw')


if __name__ == '__main__':
    unittest.main()

