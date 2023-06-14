Transparent Transmissions
-------------------------
These examples will show you how to send and receive messages in transparent mode.

In this mode, each device who share the same channel and address will be able to communicate with each other.

Receiver
^^^^^^^^
Waits on channel `4` with the `0x1337` address for any incoming messages.

⚠️ **Received messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_transparent/receiver.py
    :caption: examples/transmit_transparent/receiver.py
    :emphasize-lines: 19,22,26-40
    :linenos:

Monitor
^^^^^^^
Monitors channel `4` for messages by using the `0xFFFF` address.

⚠️ **Received messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_transparent/monitor.py
    :caption: examples/transmit_transparent/monitor.py
    :emphasize-lines: 19,22,26-40
    :linenos:

Sender
^^^^^^
Sends a message to any modules on channel `4` with the `0x1337` address.

⚠️ **Sent messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_transparent/sender.py
    :caption: examples/transmit_transparent/sender.py
    :emphasize-lines: 19,22,27,30,35-38
    :linenos:


Broadcast
^^^^^^^^^
Broadcasts a messages to all modules on channel `4` by using the `0xFFFF` address.

⚠️ **Sent messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_transparent/broadcast.py
    :caption: examples/transmit_transparent/broadcast.py
    :emphasize-lines: 19,22,27,30,35-38
    :linenos:
