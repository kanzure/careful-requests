careful-requests
~~~~~~~~~~~~~~~

This module provides an HTTP adapter for servers that are over-sensitive to
HTTP headers. It may be sad, but not all HTTP servers are HTTP-compliant and
some are suspicious of otherwise normal headers! Use careful-requests if you
still want to use the excellent Requests module.

Example usage
----------

here you go

.. code-block:: python

    from careful_requests import Careful

    s = Careful()

    >>> s.get("http://httpbin.org/get", omit_headers=["accept-encoding"])
    <Response [200]>

Install
----------

.. code-block:: bash

    sudo python setup.py install

Testing
----------

.. code-block:: bash

    make test

License
----------

BSD
