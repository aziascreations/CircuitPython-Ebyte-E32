UART Configuration
------------------
These examples will show you how to configure the UART bus for non-sleep modes.

The ``E32Device`` class will automatically re-instantiate a ``UART`` class with the correct parameters when
changing the module's mode.

Baudrate
^^^^^^^^
.. literalinclude:: ../examples/uart/baudrate.py
    :caption: examples/uart/baudrate.py
    :emphasize-lines: 18-19,22-23,25-27
    :linenos:

Parity
^^^^^^
.. literalinclude:: ../examples/uart/parity.py
    :caption: examples/uart/parity.py
    :emphasize-lines: 18-19,22-23,25-27
    :linenos:
