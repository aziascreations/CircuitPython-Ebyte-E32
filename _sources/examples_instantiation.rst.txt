Instantiation
-------------
These two examples show you how to properly prepare the E32 module's class.

Basic
^^^^^
Shows you how to instantiate a `E32Device` with raw pins grabbed from the `board` module.
The constructor will handle the process of making `DigitalInOut` class out of them.

None of the module's parameters are customized in this example.

.. literalinclude:: ../examples/instantiation_basic.py
    :caption: examples/instantiation_basic.py
    :emphasize-lines: 15
    :linenos:

Complete
^^^^^^^^
Shows you how to instantiate a `E32Device` with all the module's parameters specified and left at their default value.

.. literalinclude:: ../examples/instantiation_full.py
    :caption: examples/instantiation_full.py
    :emphasize-lines: 15-32
    :linenos:
