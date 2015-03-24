.. _query:

Queries
=======

The ``resolve`` function will only return the top match for a given input. However, sometimes multiple resolvers will
match an input (e.g. the name resolvers), and individual resolvers can even return multiple results. The ``query``
function will return every result::

    >>> cirpy.query('CCO', 'stdinchikey')
    [Result(resolver='smiles', value='InChIKey=LFQSCWFLJHTTHZ-UHFFFAOYSA-N'), Result(input='CCO', resolver='name_by_cir', value='InChIKey=BGDMJXZYDKFEGJ-UHFFFAOYSA-N')]


As with the ``resolve`` function, it is possible to specify which resolvers are used::

    >>> cirpy.query('2,4,6-trinitrotoluene', 'formula', ['name_by_opsin','name_by_cir'])
    [Result(resolver='name_by_opsin', value='C7H5N3O6'), Result(resolver='name_by_cir', value='C7H5N3O6')]

Results
-------

The ``query`` function results a list of ``Result`` objects. Each ``Result`` has a ``value`` attribute that corresponds
to what the ``resolve`` function would return::

    >>> results = cirpy.query('2,4,6-trinitrotoluene', 'formula')
    >>> results[0]
    Result(resolver='name_by_opsin', value='C7H5N3O6')
    >>> results[0].value
    'C7H5N3O6'

Each ``Result`` also has ``input``, ``representation``, ``resolver``, ``input_format`` and ``notation`` attributes.
:ref:`See the full API documentation for information on these attributes <api>`.
