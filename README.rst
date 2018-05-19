python-netdata
==============

Python API for interacting with `Netdata <https://my-netdata.io/>`_. Currently
are the ``data``, the ``allmetrics`` and the ``alarms`` endpoint supported.

Installation
------------
The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install netdata

Usage
-----

The file ``example.py`` contains an example about how to use this module.

Development
-----------
For development is recommended to use a ``venv``.

.. code:: bash

    $ python3.6 -m venv .
    $ source bin/activate
    $ python3 setup.py develop

License
-------
``python-netdata`` is licensed under MIT, for more details check LICENSE.
