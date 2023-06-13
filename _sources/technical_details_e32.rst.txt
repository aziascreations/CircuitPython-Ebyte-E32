.. role:: raw-html(raw)
    :format: html

E32 Modules
-----------

Wiring
^^^^^^
+------------+---------------------------------+
| E32 Module | MCU                             |
+============+=================================+
| `M0`       | Any digital output pin          |
+------------+---------------------------------+
| `M1`       | Any digital output pin          |
+------------+---------------------------------+
| `RXD`      | Any UART **TX** capable pin*    |
+------------+---------------------------------+
| `TXD`      | Any UART **RX** capable pin*    |
+------------+---------------------------------+
| `AUX`      | Any digital input pin**         |
+------------+---------------------------------+
| `VCC`      | Power supply***                 |
+------------+---------------------------------+

\*: Some devices may require you to use very specific pins for the UART bus.
:raw-html:`<br>`
\*\*: This pin can be left floating, but the module's AUX response times will be estimated and inaccurate.
:raw-html:`<br>`
\*\*\*: Should be between 3.3V and 5.0V, more than 5.2V can cause damage, and some modules support 2.3V !

Model Number Structure
^^^^^^^^^^^^^^^^^^^^^^
The E32 modules all have a unique name that can help you

``E32-{Frequency}{Interface}{TX Power Max dBm}{Form Factor + Suffix}``

Frequency
"""""""""
``170``, ``400``, ``433``, ``900``

Interface
"""""""""
``T`` ➜ UART
:raw-html:`<br>`
``M`` ➜ SPI

Max Power
"""""""""
``20``, ``30``, ``33``, ``37``

Form Factor & Suffix
""""""""""""""""""""
``D`` ➜ DIP (Dual In-line Package)
:raw-html:`<br>`
``DC`` ➜ ???
:raw-html:`<br>`
``DT`` ➜ ???

``S`` ➜ SMD (Surface Mount Device)
:raw-html:`<br>`
``S2`` ➜ ???
:raw-html:`<br>`
``S2T`` ➜ ???
:raw-html:`<br>`
``S3`` ➜ ???

Supported Modules
^^^^^^^^^^^^^^^^^
+-------------------+-----------------+-------------+---------+
| Model             | Max TX Power    | Frequencies | Chipset |
+===================+=================+=============+=========+
| ``E32-170T30D``   | 30 dBm / 1 W    | ISM 170 MHz | SX1278  |
+-------------------+-----------------+-------------+         |
| ``E32-400T20S``   | 20 dBm / 100 mW | ISM 443 MHz |         |
|                   |                 |             |         |
|                   |                 | ISM 470 MHz |         |
|                   |                 |             |         |
|                   |                 | EU433       |         |
+-------------------+-----------------+-------------+         |
| ``E32-443T20DC``  | 20 dBm / 100 mW | ISM 433MHz  |         |
|                   |                 |             |         |
| ``E32-443T20DT``  |                 | EU433       |         |
|                   |                 |             |         |
| ``E32-443T20S``   |                 |             |         |
|                   |                 |             |         |
| ``E32-443T20S2T`` |                 |             |         |
+-------------------+-----------------+-------------+         |
| ``E32-443T30D``   | 30 dBm / 1 W    | ISM 433MHz  |         |
|                   |                 |             |         |
| ``E32-443T30S``   |                 | EU433       |         |
+-------------------+-----------------+             |         |
| ``E32-443T33S``   | 33 dBm / 2W     |             |         |
+-------------------+-----------------+             |         |
| ``E32-443T37S``   | 37 dBm / 5W     |             |         |
+-------------------+-----------------+-------------+---------+
| ``E32-868T20D``   | TODO            | TODO        | SX1276  |
|                   |                 |             |         |
| ``E32-868T20S``   |                 |             |         |
|                   |                 |             |         |
| ``E32-868T30D``   |                 |             |         |
|                   |                 |             |         |
| ``E32-868T30S``   |                 |             |         |
|                   |                 |             |         |
| ``E32-915T20D``   |                 |             |         |
|                   |                 |             |         |
| ``E32-915T20S``   |                 |             |         |
|                   |                 |             |         |
| ``E32-915T30D``   |                 |             |         |
|                   |                 |             |         |
| ``E32-915T30S``   |                 |             |         |
+-------------------+-----------------+-------------+---------+

All frequencies with another non-ISM name can be used for LoRaWAN.

Unsupported Modules
^^^^^^^^^^^^^^^^^^^
+-------------------+-----------------+-------------+---------+
| Model             | Max TX Power    | Frequencies | Chipset |
+===================+=================+=============+=========+
| ``E32-400M20S``   | 20 dBm / 100 mW | 433/470MHz  | SX1278  |
+-------------------+-----------------+             |         |
| ``E32-400M20S``   | 30 dBm / 1 W    |             |         |
+-------------------+-----------------+-------------+---------+
| ``E32-443T27D``   | ???             | ???         | ???     |
+-------------------+-----------------+-------------+---------+
| ``E32-900M20S``   | 20 dBm / 100 mW | 868/915MHz  | SX1276  |
+-------------------+-----------------+             |         |
| ``E32-900M30S``   | 30 dBm / 1 W    |             |         |
+-------------------+-----------------+-------------+---------+

The ``E32-***M**S`` variants has very basic datasheets, no concrete frequencies could be found.

The ``E32-433T27D`` variant is mentionned in the `E32 V1.30 User Manual
<https://www.ebyte.com/en/pdf-down.aspx?id=775>`_,
but no other datasheet or product listing could be found for it.

Datasheets
^^^^^^^^^^
All datasheets are hosted by Ebyte on *ebyte.com* and *cdebyte.com* unless specified otherwise.

* `E32-170T30D <https://www.cdebyte.com/pdf-down.aspx?id=896>`_

* `E32-400M20S <https://www.cdebyte.com/pdf-down.aspx?id=1794>`_
* `E32-400M30S <https://www.ebyte.com/en/downpdf.aspx?id=1624>`_
* `E32-400T20S <https://www.cdebyte.com/pdf-down.aspx?id=895>`_

* `E32-443T20DC <https://www.ebyte.com/en/downpdf.aspx?id=130>`_
* `E32-443T20DT <https://www.cdebyte.com/pdf-down.aspx?id=858>`_
* `E32-443T20S <https://www.cdebyte.com/pdf-down.aspx?id=1957>`_
* `E32-443T20S2T <https://www.ebyte.com/en/downpdf.aspx?id=227>`_
* `E32-443T30D <https://www.ebyte.com/en/downpdf.aspx?id=108>`_
* `E32-443T30S <https://www.cdebyte.com/pdf-down.aspx?id=2347>`_
* `E32-433T33S <https://www.manualslib.com/manual/2938896/Ebyte-E32-433t33s.html>`_ (manualslib.com)
* `E32-443T37S <https://www.cdebyte.com/pdf-down.aspx?id=2215>`_

* `E32-900M20S <https://www.ebyte.com/en/downpdf.aspx?id=1613>`_
* `E32-900M30S <https://www.ebyte.com/en/downpdf.aspx?id=1515>`_

If any datasheet becomes unavailable, please open an issue.
:raw-html:`<br>`
We also keep copies of them over at `files.nibblepoker.lu <https://files.nibblepoker.lu/datasheets/ebyte/e32/>`_
just in case.

Alternatively, `manualslib.com <https://www.manualslib.com/products/Ebyte-E32-Series-10450561.html>`_ has a pretty good
collection of them.
