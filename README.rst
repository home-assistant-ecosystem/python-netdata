python-netdata
==============

Python API for interacting with `Netdata <https://my-netdata.io/>`_. Currently
are the ``data``, the ``allmetrics`` and the ``alarms`` endpoint supported.

This module is not official, developed, supported or endorsed by Netdata.

Installation
------------

The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install netdata

On a Fedora-based system or on a CentOS/RHEL machine which has EPEL enabled.

.. code:: bash

    $ sudo dnf -y install python3-netdata

For Nix or NixOS users is a package available. Keep in mind that the lastest releases might only
be present in the ``unstable`` channel.

.. code:: bash

    $ nix-env -iA nixos.python3Packages.netdata

Usage
-----

The file ``example.py`` contains an example about how to use this module.

Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3 -m venv .
    $ source bin/activate
    $ python3 setup.py develop

License
-------

``python-netdata`` is licensed under MIT, for more details check LICENSE.
