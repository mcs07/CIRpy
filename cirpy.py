# -*- coding: utf-8 -*-
"""
CIRpy

Python interface for the Chemical Identifier Resolver (CIR) by the CADD Group at the NCI/NIH.
https://github.com/mcs07/CIRpy
"""


import urllib2
from xml.etree import ElementTree as ET


def resolve(input, representation, resolvers=None):
    """ Resolve input to the specified output representation """
    resultdict = query(input, representation, resolvers)
    result = resultdict[0]['value'] if resultdict else None
    if result and len(result) == 1:
        result = result[0]
    return result


def query(input, representation, resolvers=None):
    """ Get all results for resolving input to the specified output representation """
    apiurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/%s/xml' % (urllib2.quote(input), representation)
    if resolvers is not None:
        r = ",".join(resolvers)
        apiurl += '?resolver=%s' % r
    result = []
    tree = ET.parse(urllib2.urlopen(apiurl))
    for data in tree.findall(".//data"):
        datadict = {'resolver':data.attrib['resolver'],
                    'notation':data.attrib['notation'],
                    'value':[]}
        for item in data.findall("item"):
            datadict['value'].append(item.text)
        if len(datadict['value']) == 1:
            datadict['value'] = datadict['value'][0]
        result.append(datadict)
    return result if result else None


class CacheProperty(object):
    """ Descriptor for caching Molecule properties. """

    def __init__(self, func):
        self._func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __get__(self, obj, obj_class=None):
        if obj is None: return None
        result = obj.__dict__[self.__name__] = self._func(obj)
        return result


class Molecule(object):
    """Class to hold and cache the structure information for a given CIR input"""

    def __init__(self, input, resolvers=None):
        """ Initialize with a query input """
        self.input = input
        self.resolvers = resolvers

    def __repr__(self):
        return "Molecule(%r, %r)" % (self.input, self.resolvers)

    @CacheProperty
    def stdinchi(self): return resolve(self.input, 'stdinchi', self.resolvers)

    @CacheProperty
    def stdinchikey(self): return resolve(self.input, 'stdinchikey', self.resolvers)

    @CacheProperty
    def smiles(self): return resolve(self.input, 'smiles', self.resolvers)

    @CacheProperty
    def ficts(self): return resolve(self.input, 'ficts', self.resolvers)

    @CacheProperty
    def ficus(self): return resolve(self.input, 'ficus', self.resolvers)

    @CacheProperty
    def uuuuu(self): return resolve(self.input, 'uuuuu', self.resolvers)

    @CacheProperty
    def hashisy(self): return resolve(self.input, 'hashisy', self.resolvers)

    @CacheProperty
    def sdf(self): return resolve(self.input, 'sdf', self.resolvers)

    @CacheProperty
    def names(self): return resolve(self.input, 'names', self.resolvers)

    @CacheProperty
    def iupac_name(self): return resolve(self.input, 'iupac_name', self.resolvers)

    @CacheProperty
    def cas(self): return resolve(self.input, 'cas', self.resolvers)

    @CacheProperty
    def chemspider_id(self): return resolve(self.input, 'chemspider_id', self.resolvers)

    @CacheProperty
    def mw(self): return resolve(self.input, 'mw', self.resolvers)

    @CacheProperty
    def formula(self): return resolve(self.input, 'formula', self.resolvers)

    @CacheProperty
    def h_bond_donor_count(self): return resolve(self.input, 'h_bond_donor_count', self.resolvers)

    @CacheProperty
    def h_bond_acceptor_count(self): return resolve(self.input, 'h_bond_acceptor_count', self.resolvers)

    @CacheProperty
    def h_bond_center_count(self): return resolve(self.input, 'h_bond_center_count', self.resolvers)

    @CacheProperty
    def rule_of_5_violation_count(self): return resolve(self.input, 'rule_of_5_violation_count', self.resolvers)

    @CacheProperty
    def rotor_count(self): return resolve(self.input, 'rotor_count', self.resolvers)

    @CacheProperty
    def effective_rotor_count(self): return resolve(self.input, 'effective_rotor_count', self.resolvers)

    @CacheProperty
    def ring_count(self): return resolve(self.input, 'ring_count', self.resolvers)

    @CacheProperty
    def ringsys_count(self): return resolve(self.input, 'ringsys_count', self.resolvers)

    @property
    def image_url(self):
        url = 'http://cactus.nci.nih.gov/chemical/structure/%s/image' % self.input
        if self.resolvers is not None:
            r = ",".join(self.resolvers)
        url += '?resolver=%s' % r
        return url

    @property
    def twirl_url(self):
        url = 'http://cactus.nci.nih.gov/chemical/structure/%s/twirl' % self.input
        if self.resolvers is not None:
            r = ",".join(self.resolvers)
        url += '?resolver=%s' % r
        return url

if __name__ == '__main__':
    r = query('Morphine','smiles', ['name_pattern'])
    print r