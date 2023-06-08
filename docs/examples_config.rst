Configuration
-------------
These examples will show you how to configure you device.

Manual
^^^^^^
.. literalinclude:: ../examples/config_manual.py
    :caption: examples/config_manual.py
    :emphasize-lines: 34
    :linenos:

Reading from class
^^^^^^^^^^^^^^^^^^
Each of the module's parameters can be read via the class property as shown in the `Configuration > Manual` example,
which will return the ``E32Device`` class value.

Reading from module
^^^^^^^^^^^^^^^^^^^
If you want to fetch the module's current configuration, you can use the ``E32Device.get_config()`` method and
get a named tuple with all the values.

.. literalinclude:: ../examples/config_reading.py
    :caption: examples/config_reading.py
    :emphasize-lines: 18-21,25-37
    :linenos:
