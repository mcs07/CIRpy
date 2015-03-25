# -*- coding: utf-8 -*-
"""
Unit tests for cirpy.py

Python interface for the Chemical Identifier Resolver (CIR) by the CADD Group at the NCI/NIH.
https://github.com/mcs07/CIRpy
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
import logging
import os
import time
import unittest

try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError

try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        import xml.etree.ElementTree as etree

from cirpy import request, resolve, query, Molecule, Result, resolve_image


logging.basicConfig(level=logging.DEBUG)


class RateLimitTestCase(unittest.TestCase):
    """TestCase that delays before each test according to CIRPY_TEST_DELAY environment variable."""

    def setUp(self):
        time.sleep(float(os.environ.get('CIRPY_TEST_DELAY', 0)))


class TestRequest(RateLimitTestCase):
    """Test basic requests to CIR servers return the expected XML response."""

    def test_requests(self):
        """Test a variety of basic requests to ensure they return the expected XML response."""
        self.assertEqual(request('c1ccccc1', 'names').tag, 'request')
        self.assertEqual(request('Aspirin', 'smiles').tag, 'request')
        self.assertEqual(len(request('64-17-5', 'stdinchi')), 1)

    def test_no_result_request(self):
        """Test that an empty XML response is returned when there are no results."""
        response = request('arguergbaiurg', 'smiles')
        self.assertEqual(response.tag, 'request')
        self.assertEqual(len(response), 0)

    def test_invalid_representation_request(self):
        """Test that HTTPError is raised when an invalid representation is specified."""
        with self.assertRaises(HTTPError):
            request('Morphine', 'ogiuewrgpw')


class TestQuery(RateLimitTestCase):
    """Test the query function returns expected results."""

    def test_morphine_inchi(self):
        """Test morphine query for inchi returns expected result."""
        results = query('morphine', 'inchi')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].input, 'morphine')
        self.assertEqual(results[0].representation, 'inchi')
        self.assertEqual(results[0].resolver, 'name_by_cir')
        self.assertEqual(results[0].input_format, 'chemical name (CIR)')
        self.assertEqual(results[0].notation, 'Morphine')
        self.assertEqual(results[0].value, 'InChI=1/C17H19NO3/c1-18-7-6-17-10-3-5-13(20)16(17)21-15-12(19)4-2-9(14(15)17)8-11(10)18/h2-5,10-11,13,16,19-20H,6-8H2,1H3/t10-,11+,13?,16-,17-/m0/s1')

    def test_query_dict(self):
        """Test dict-style access to result attributes."""
        results = query('Morphine', 'inchi')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['value'], 'InChI=1/C17H19NO3/c1-18-7-6-17-10-3-5-13(20)16(17)21-15-12(19)4-2-9(14(15)17)8-11(10)18/h2-5,10-11,13,16,19-20H,6-8H2,1H3/t10-,11+,13?,16-,17-/m0/s1')
        self.assertEqual(results[0]['notation'], 'Morphine')
        self.assertEqual(results[0]['resolver'], 'name_by_cir')

    def test_no_result_query(self):
        """Test that an empty list is returned when there are no results."""
        self.assertEqual(query('sjkvhaldfu', 'smiles'), [])

    def test_invalid_representation_query(self):
        """Test that HTTPError is raised when an invalid representation is specified."""
        with self.assertRaises(HTTPError):
            query('Morphine', 'ogiuewrgpw')

    def test_custom_resolvers(self):
        """Test expected results are returned when using custom name resolvers."""
        results = query('2,4,6-trinitrotoluene', 'smiles')
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], Result(input='2,4,6-trinitrotoluene', representation='smiles', resolver='name_by_opsin', input_format='IUPAC name (OPSIN)', notation='2,4,6-trinitrotoluene', value='[N+](=O)([O-])C1=C(C(=CC(=C1)[N+](=O)[O-])[N+](=O)[O-])C'))
        self.assertEqual(results[1], Result(input='2,4,6-trinitrotoluene', representation='smiles', resolver='name_by_cir', input_format='chemical name (CIR)', notation='2,4,6-Trinitrotoluene', value='C1=C(C=C(C(=C1[N+]([O-])=O)C)[N+]([O-])=O)[N+]([O-])=O'))

    def test_result_equality(self):
        """Test that identical result objects are considered equal."""
        r1 = Result('input', 'notation', 'input_format', 'resolver', 'representation', 'value')
        r2 = Result('input', 'notation', 'input_format', 'resolver', 'representation', 'value')
        r3 = Result('input', 'notation', 'input_format', 'resolver', 'representation', 'another_value')
        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)


class TestResolve(RateLimitTestCase):
    """Test the resolve function."""

    def test_alanine_smiles(self):
        """Test that alanine smiles resolves the expected result."""
        self.assertEqual(resolve('Alanine', 'smiles'), 'N[C@@H](C)C(=O)O')

    def test_no_results_resolve(self):
        """Test that None is returned when there are no results."""
        self.assertEqual(resolve('aruighaelirugaerg', 'inchi'), None)

    def test_invalid_representation_resolve(self):
        """Test that HTTPError is raised when an invalid representation is specified."""
        with self.assertRaises(HTTPError):
            resolve('Morphine', 'ogiuewrgpw')

    def test_tnt_smiles(self):
        """Test that TNT smiles resolves the expected result."""
        self.assertEqual(
            resolve('2,4,6-trinitrotoluene', 'smiles'),
            '[N+](=O)([O-])C1=C(C(=CC(=C1)[N+](=O)[O-])[N+](=O)[O-])C'
        )

    def test_tnt_smiles_custom_resolvers(self):
        """Test custom resolvers return the expected result."""
        self.assertEqual(
            resolve('2,4,6-trinitrotoluene', 'smiles', ['name_by_opsin', 'name_by_cir']),
            '[N+](=O)([O-])C1=C(C(=CC(=C1)[N+](=O)[O-])[N+](=O)[O-])C'
        )
        self.assertEqual(
            resolve('2,4,6-trinitrotoluene', 'smiles', ['name_by_cir', 'name_by_opsin']),
            'C1=C(C=C(C(=C1[N+]([O-])=O)C)[N+]([O-])=O)[N+]([O-])=O'
        )


class TestMolecule(RateLimitTestCase):
    """Test the Molecule class."""

    def test_molecule_image(self):
        """Test Molecule image_url attribute."""
        self.assertEqual(
            Molecule('C#N', ['smiles']).image_url,
            'http://cactus.nci.nih.gov/chemical/structure/C%23N/image?resolver=smiles'
        )


class TestFiles(RateLimitTestCase):
    """Test resolving to file formats."""

    def test_cml(self):
        """Test CML file format is resolved."""
        cmlstring = resolve('Aspirin', 'cml')
        cml = etree.fromstring(cmlstring)
        self.assertEqual(cml.tag, '{http://www.xml-cml.org/schema/cml2/core}list')
        self.assertEqual(len(cml.findall('.//{http://www.xml-cml.org/schema/cml2/core}molecule')), 1)

    def test_pdb(self):
        """Test PDB file format is resolved."""
        result = resolve('Aspirin', 'pdb')
        self.assertIn('HEADER', result)
        self.assertIn('ATOM', result)
        self.assertIn('CONECT', result)


class TestImage(RateLimitTestCase):
    """Test resolving to image depiction."""

    def test_png_format(self):
        """Test that response looks like valid PNG data."""
        img = resolve_image('Glucose')
        self.assertEqual(img[:8], b'\x89PNG\x0d\x0a\x1a\x0a')

    def test_gif_format(self):
        """Test that response looks like valid GIF data."""
        img = resolve_image('Glucose', fmt='gif')
        self.assertEqual(img[:4], b'GIF8')


if __name__ == '__main__':
    unittest.main()
