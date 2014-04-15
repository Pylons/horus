Getting Started
=================================

.. code-block::

    $ git clone git@github.com:Pylons/horus.git
    $ cd horus
    $ pip install -e .

If you would like to run the tests you should run:

.. code-block::

   $ pip install -e .[testing]


Design Decisions
=================================

Views
------------------------------------
A view will be the utility functions needed to interface with
Pyramid.  They will be extremely light weight, they should validate and
parse JSON/form data, then create any services and facades required and
should contain no business logic.


Service
------------------------------------
A service is a class that will represent all the business logic
required to do a certain responsibility like creating authenticating a user.

The facade should not have any access to Pyramid or a persistence store. So
there should be no DBSession or Request available, if the facade needs
database access it should be done through a service.


Backend
------------------------------------
A backend is an abstraction around the data access.  There should
be as little business logic in a repository as possible, it should be for
connecting to a data store (postgres, zodb, mongodb) and returning the result set.

Mapping functions from database rows to model classes should be done here.


Example Configuration
=====================

.. code-block:: ini

    pyramid.includes = horus

    horus.backend = horus.backends.sqla
    horus.backend.sqlalchemy_url = postgresql://

    horus.flows =
      local
      fb

    local.impl = horus.flows.local
    local.

    fb.impl = horus.flows.facebook
    fb.access_token = 
    fb.

.. code-block:: python

    config.override_assets(
      to_override='horus.flows.local:templates/',
      override_with='myapp.templates/')
