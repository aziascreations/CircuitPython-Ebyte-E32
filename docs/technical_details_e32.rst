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
| `VCC`      | Power supply 2.3V to 5.2V DC*** |
+------------+---------------------------------+

\*: Some devices may require you to use very specific pins for the UART bus.
:raw-html:`<br>`
\*\*: Analogue input pins might work, but this type of setup isn't supported !
:raw-html:`<br>`
\*\*\*: More than 5.2V can cause damage, and make sure to double-check the datasheet !

Model Number Structure
^^^^^^^^^^^^^^^^^^^^^^
The E32 modules all have a unique name that can help you

`E32-{Frequency}-T{TX Power Max dBm}{Form Factor}`

`S` => SDM (Surface Mount Device)

`D` => DIP (Dual In-line Package)

`DT` => ???

`DC` => ???

Modules specifications
^^^^^^^^^^^^^^^^^^^^^^
abc

+-------------------+------------+-----------------+-------------+---------+
| Model             | Supported  | Max TX Power    | Frequencies | Chipset |
+===================+============+=================+=============+=========+
| The 1xx and 400   |            |                 |             |         |
+-------------------+------------+-----------------+-------------+---------+
| ``E32-443T20DC``  | ✔️         | 20 dBm / 100 mW | EU433       | SX1278  |
|                   |            |                 |             |         |
| ``E32-443T20S``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-443T20S2T`` |            |                 |             |         |
+-------------------+------------+-----------------+-------------+         |
| ``E32-443T27D``   | ✖️         | ???             | ???         |         |
+-------------------+------------+-----------------+-------------+         |
| ``E32-443T30D``   | ❔         | 30 dBm / 1 W    | EU433       |         |
|                   |            |                 |             |         |
| ``E32-443T30S``   |            |                 |             |         |
+-------------------+------------+-----------------+             |         |
| ``E32-443T33S``   | ❔         | 33 dBm / 2W     |             |         |
+-------------------+------------+-----------------+-------------+---------+
| ``E32-868T20D``   | ❔         | ???             | ???         | SX1276  |
|                   |            |                 |             |         |
| ``E32-868T20S``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-868T30D``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-868T30S``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-915T20D``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-915T20S``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-915T30D``   |            |                 |             |         |
|                   |            |                 |             |         |
| ``E32-915T30S``   |            |                 |             |         |
+-------------------+------------+-----------------+-------------+---------+

The ``E32-433T27D`` variant is mentionned in the `E32 V1.30 User Manual
<https://www.ebyte.com/en/pdf-down.aspx?id=775>`_,
but no other datasheet or product listing could be found for it.

All non EU433 variant aren't supported as I cannot own and test them legally right now.

Datasheets
^^^^^^^^^^
All datasheets are hosted by Ebyte on *ebyte.com* and *cdebyte.com* unless specified otherwise.

* [E32-443T20DT](https://www.ebyte.com/en/downpdf.aspx?id=660)
* [E32-443T30D](https://www.ebyte.com/en/downpdf.aspx?id=108)
* [E32-433T33S](https://www.manualslib.com/manual/2938896/Ebyte-E32-433t33s.html) (manualslib.com)

If any datasheet become unavailable, please open an issue.<br>
We also keep copies of them over at [files.nibblepoker.lu](https://files.nibblepoker.lu/datasheets/ebyte/e32/) just in case.
