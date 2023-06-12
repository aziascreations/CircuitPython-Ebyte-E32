.. role:: raw-html(raw)
    :format: html

Fixed Transmissions
-------------------
These examples will show you how to send and receive messages in fixed mode in unicast and broadcast.

In this mode, each message needs to contain the target channel and address before the actual data.
:raw-html:`<br>`
You can also use the special ``0xFFFF`` address to monitor or broadcast messages on a given channel.

Unicast Receiver
^^^^^^^^^^^^^^^^
Waits on channel `4` with the `0x1337` address for any incoming unicast or broadcast messages.

⚠️ **Received messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/receiver_unicast.py
    :caption: examples/transmit_fixed/receiver_unicast.py
    :emphasize-lines: 19,22,26-40
    :linenos:

Monitoring Receiver
^^^^^^^^^^^^^^^^^^^
Waits on channel `4` with the special `0xFFFF` address for any unicast or broadcast messages on that channel.

⚠️ **Received messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/receiver_broadcast.py
    :caption: examples/transmit_fixed/receiver_broadcast.py
    :emphasize-lines: 19,22,26-40
    :linenos:

Unicast Sender
^^^^^^^^^^^^^^
Sends a unicast message to any modules on channel `4` with the `0x1337` address.

⚠️ **Sent messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/sender_unicast.py
    :caption: examples/transmit_fixed/sender_unicast.py
    :emphasize-lines: 19,22,28,30-31
    :linenos:

Broadcast Sender
^^^^^^^^^^^^^^^^
Sends a broadcast message to any modules on channel `4` by using the target address `0xFFFF`.

⚠️ **Sent messages may be truncated at specific lengths depending on the frequencies and operating parameters used
due to RF regulations.**

.. literalinclude:: ../examples/transmit_fixed/sender_broadcast.py
    :caption: examples/transmit_fixed/sender_broadcast.py
    :emphasize-lines: 19,22,28,30-31
    :linenos:
