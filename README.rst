********************
jsquery - A CLI Tool
********************

This module implements a CLI tool for parsing a valid JSON schema provided in a file
returning the type for the given key path.

Usage
-----
::

    Usage: jsquery [OPTIONS] SCHEMA_FILE KEY_PATH

      Given a valid JSON Schema and a valid key path, return the type value

    Options:
      --help  Show this message and exit.


Examples
--------
::

    $ jsquery tests/test_schema.json Age
    Schema File = tests/test_schema.json
    Key Path    = Age
    Type        = integer

    $ jsquery tests/test_schema.json EmploymentInformation.Beneficiary.Name
    Schema File = tests/test_schema.json
    Key Path    = EmploymentInformation.Beneficiary.Name
    Type        = string


Installation
------------
::

    $ python -m venv test_jsquery  # NOTE: Must have Python 3.8
    $ cd test_jsquery
    $ source bin/activate
    $ pip install git+https://github.com/wjdecorte/sct_jschema.git@master


Dev Installation
----------------
::

    $ python -m venv sct_jschema  # NOTE: Must have Python 3.8
    $ cd sct_jschema
    $ source bin/activate
    $ mkdir src
    $ cd src
    $ git clone https://github.com/wjdecorte/sct_jschema.git
    $ cd sct_jschema
    $ poetry install

.. note:: If poetry is not available, a setup.py can be generated using the package `dephell <https://dephell.org/>`_.


Testing
-------
::

    $ cd src/sct_jschema
    $ pytest

