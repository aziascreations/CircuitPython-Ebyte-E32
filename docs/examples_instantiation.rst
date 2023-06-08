Instantiation
-------------
These two examples show you how to properly prepare the E32 module's class.

Basic
^^^^^
Shows you how to instantiate a `E32Device` with raw pins grabbed from the `board` module.
The constructor will handle the process of making `DigitalInOut` class out of them.

None of the module's parameters will be customized.

.. literalinclude:: ../examples/instantiation_basic.py
    :caption: examples/instantiation_basic.py
    :emphasize-lines: 17
    :linenos:

Complete
^^^^^^^^
Shows you how to instantiate a `E32Device` with the `DigitalInOut` and `UART` classes for the pins,
and with all the module's parameters specified and left at their default value.

.. literalinclude:: ../examples/instantiation_full.py
    :caption: examples/instantiation_full.py
    :emphasize-lines: 18-35
    :linenos:
