Fixed Transmissions
-------------------

Receiver
^^^^^^^^
Waits on channel `4` with the `0x1337` address for any incoming unicast or broadcast messages and exits once one is
received.

⚠️ **Received messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/receiver.py
    :caption: examples/transmit_fixed/receiver.py
    :emphasize-lines: 19,22,26-41
    :linenos:

Unicast Sender
^^^^^^^^^^^^^^
Sends a unicast message to any modules on channel `4` with the `0x1337` address.

⚠️ **Sent messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/sender_unicast.py
    :caption: examples/transmit_fixed/sender_unicast.py
    :emphasize-lines: 19,22,28,30
    :linenos:

Broadcast Sender
^^^^^^^^^^^^^^^^
TODO
