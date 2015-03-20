# -*- coding: utf-8 -*-
"""
CIRpy

Python interface for the Chemical Identifier Resolver (CIR) by the CADD Group at the NCI/NIH.
https://github.com/mcs07/CIRpy
"""

import os
import functools

try:
    from urllib.error import HTTPError
    from urllib.parse import quote, urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import quote, urlopen, HTTPError

try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        import xml.etree.ElementTree as etree


__author__ = 'Matt Swain'
__email__ = 'm.swain@me.com'
__version__ = '1.0.0'
__license__ = 'MIT'


API_BASE = 'http://cactus.nci.nih.gov/chemical/structure'


def resolve(input, representation, resolvers=None, **kwargs):
    """Resolve input to the specified output representation."""
    resultdict = query(input, representation, resolvers, **kwargs)
    result = resultdict[0]['value'] if resultdict else None
    if result and len(result) == 1:
        result = result[0]
    return result


def query(input, representation, resolvers=None, **kwargs):
    """Get all results for resolving input to the specified output representation."""
    apiurl = '%s/%s/%s/xml' % (API_BASE, quote(input), representation)
    if resolvers:
        kwargs['resolver'] = ','.join(resolvers)
    if kwargs:
        apiurl += '?%s' % urlencode(kwargs)
    result = []
    try:
        tree = etree.parse(urlopen(apiurl))
        for data in tree.findall('.//data'):
            datadict = {'resolver': data.attrib['resolver'], 'notation': data.attrib['notation'], 'value': []}
            for item in data.findall('item'):
                datadict['value'].append(item.text)
            if len(datadict['value']) == 1:
                datadict['value'] = datadict['value'][0]
            result.append(datadict)
    except HTTPError:
        # TODO: Proper handling of 404, for now just returns None
        pass
    return result if result else None


def download(input, filename, format='sdf', overwrite=False, resolvers=None, **kwargs):
    """Resolve and download structure as a file."""
    kwargs['format'] = format
    if resolvers:
        kwargs['resolver'] = ','.join(resolvers)
    url = '%s/%s/file?%s' % (API_BASE, quote(input), urlencode(kwargs))
    try:
        servefile = urlopen(url)
        if not overwrite and os.path.isfile(filename):
            raise IOError("%s already exists. Use 'overwrite=True' to overwrite it." % filename)
        with open(filename, 'w') as f:
            f.write(servefile.read())
    except HTTPError:
        # TODO: Proper handling of 404, for now just does nothing
        pass


def memoized_property(fget):
    """Decorator to create memoized properties."""
    attr_name = '_{0}'.format(fget.__name__)
    
    @functools.wraps(fget)
    def fget_memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fget(self))
        return getattr(self, attr_name)
    return property(fget_memoized)


class Molecule(object):
    """Class to hold and cache the structure information for a given CIR input."""

    def __init__(self, input, resolvers=None, **kwargs):
        """Initialize with a query input."""
        self.input = input
        self.resolvers = resolvers
        self.kwargs = kwargs

    def __repr__(self):
        return 'Molecule(%r, %r)' % (self.input, self.resolvers)

    @memoized_property
    def stdinchi(self):
        return resolve(self.input, 'stdinchi', self.resolvers, **self.kwargs)

    @memoized_property
    def stdinchikey(self):
        return resolve(self.input, 'stdinchikey', self.resolvers, **self.kwargs)

    @memoized_property
    def smiles(self):
        return resolve(self.input, 'smiles', self.resolvers, **self.kwargs)

    @memoized_property
    def ficts(self):
        return resolve(self.input, 'ficts', self.resolvers, **self.kwargs)

    @memoized_property
    def ficus(self):
        return resolve(self.input, 'ficus', self.resolvers, **self.kwargs)

    @memoized_property
    def uuuuu(self):
        return resolve(self.input, 'uuuuu', self.resolvers, **self.kwargs)

    @memoized_property
    def hashisy(self):
        return resolve(self.input, 'hashisy', self.resolvers, **self.kwargs)

    @memoized_property
    def sdf(self):
        return resolve(self.input, 'sdf', self.resolvers, **self.kwargs)

    @memoized_property
    def names(self):
        return resolve(self.input, 'names', self.resolvers, **self.kwargs)

    @memoized_property
    def iupac_name(self):
        return resolve(self.input, 'iupac_name', self.resolvers, **self.kwargs)

    @memoized_property
    def cas(self):
        return resolve(self.input, 'cas', self.resolvers, **self.kwargs)

    @memoized_property
    def chemspider_id(self):
        return resolve(self.input, 'chemspider_id', self.resolvers, **self.kwargs)

    @memoized_property
    def mw(self):
        return resolve(self.input, 'mw', self.resolvers, **self.kwargs)

    @memoized_property
    def formula(self):
        return resolve(self.input, 'formula', self.resolvers, **self.kwargs)

    @memoized_property
    def h_bond_donor_count(self):
        return resolve(self.input, 'h_bond_donor_count', self.resolvers, **self.kwargs)

    @memoized_property
    def h_bond_acceptor_count(self):
        return resolve(self.input, 'h_bond_acceptor_count', self.resolvers, **self.kwargs)

    @memoized_property
    def h_bond_center_count(self):
        return resolve(self.input, 'h_bond_center_count', self.resolvers, **self.kwargs)

    @memoized_property
    def rule_of_5_violation_count(self):
        return resolve(self.input, 'rule_of_5_violation_count', self.resolvers, **self.kwargs)

    @memoized_property
    def rotor_count(self):
        return resolve(self.input, 'rotor_count', self.resolvers, **self.kwargs)

    @memoized_property
    def effective_rotor_count(self):
        return resolve(self.input, 'effective_rotor_count', self.resolvers, **self.kwargs)

    @memoized_property
    def ring_count(self):
        return resolve(self.input, 'ring_count', self.resolvers, **self.kwargs)

    @memoized_property
    def ringsys_count(self):
        return resolve(self.input, 'ringsys_count', self.resolvers, **self.kwargs)

    @property
    def image_url(self):
        url = '%s/%s/image' % (API_BASE, quote(self.input))
        qsdict = self.kwargs
        if self.resolvers:
            qsdict['resolver'] = ','.join(self.resolvers)
        if qsdict:
            url += '?%s' % urlencode(qsdict)
        return url

    @property
    def twirl_url(self):
        url = '%s/%s/twirl' % (API_BASE, quote(self.input))
        qsdict = self.kwargs
        if self.resolvers:
            qsdict['resolver'] = ','.join(self.resolvers)
        if qsdict:
            url += '?%s' % urlencode(qsdict)
        return url

    def download(self, filename, format='sdf', overwrite=False, resolvers=None, **kwargs):
        """Download the resolved structure as a file."""
        download(self.input, filename, format, overwrite, resolvers, **kwargs)

