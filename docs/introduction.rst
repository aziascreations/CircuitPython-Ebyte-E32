.. image:: _static/computer_v1_happy_strong.png
   :scale: 50 %
   :alt: Drawing of an old computer with a warning sign shown on its screen.
   :align: right

.. role:: raw-html(raw)
    :format: html

CircuitPython Ebyte E32 Library
===============================
CircuitPython driver for Ebyte's E32 LoRa modules.

Legal Preamble
^^^^^^^^^^^^^^
You should really check the :ref:`ref-legal-aside` section.
:raw-html:`<br>`
Im' not responsible for what you do with your module, act responsibly.

Features
^^^^^^^^
- Supports all standard E32 UART modules.

- Extra support on a per-frequency and per-power basis:

  - More descriptive constants for TX power.
  - Channel <-> frequency converters.
  - Maximum packet size calculators.  (TODO)
  - Entirely optional via separate modules.

- Minified versions for devices with tiny storage space:

  - ~75% smaller for `.py` files
  - ~5% smaller for `.mpy` files  *(Due to shortened local variables, mostly)*

Limitations
^^^^^^^^^^^
- **No built-in packet size limit:**

  - Wildly different between frequencies & operating parameters.
  - Not documented clearly enough in LoRA and LoRaWAN documentation.

- No built-in protocol:

  - All LoRa packets are glued back-to-back when received.
  - **No LoraWAN support**

- Missing extra support for some modules:

  - Modules with `170`, `400`, `868`, `900`, and `915` prefix.  *(Will improve overtime)*

Dependencies
^^^^^^^^^^^^
* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

* `Adafruit Blinka <https://github.com/adafruit/Adafruit_Blinka>`_

Recommended Links
^^^^^^^^^^^^^^^^^
* `LoRa and LoRaWAN quick overview  (By SemTech) <https://lora-developers.semtech.com/documentation/tech-papers-and-guides/lora-and-lorawan>`_

* `LoRa frequency plan by country (By The Things Network) <https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/>`_

* `LoRa RF modulation basics  (On wiki.lahoud.fr) <http://wiki.lahoud.fr/lib/exe/fetch.php?media=an1200.22.pdf>`_

* `Ebyte documentation for most E32 170/400/433/868/900/915 modules  (On ebyte.com) <https://www.ebyte.com/en/data-download.html?id=214&cid=31>`_

* `Ebyte documentation for most E32-433T33D  (On manualslib.com) <https://www.manualslib.com/manual/2924523/Ebyte-E32-433t33d.html?page=2#manual>`_

* `LoRaWAN Regional Parameters  (By LoRa Alliance) <https://resources.lora-alliance.org/home/rp002-1-0-4-regional-parameters>`_

License
^^^^^^^
This project is licensed under the `MIT license <https://github.com/aziascreations/CircuitPython_Ebyte_E32/blob/master/LICENSE>`_.

:raw-html:`<hr>`
