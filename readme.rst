CircuitPython Ebyte E32 Library
###############################

CircuitPython driver for Ebyte's E32 LoRa modules.

Legal Preamble
**************
You are responsible.

I cannot be held responsible for what you do with your devices.

Check your local laws !

Hardware
********

Model Number Structure
======================

The E32 modules all have a unique name that can help you

`E32-{Frequency}-T{TX Power Max dBm}{Form Factor}`

`S` => SDM (Surface Mount Device)

`D` => DIP (Dual In-line Package)

`DT` => ???

`DC` => ???

List
====
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

Links
*****
* `LoRa frequency plan by country (By The Things Network) <https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/>`_

* `Ebyte documentation for most E32 170/400/433/868/900/915 modules <https://www.ebyte.com/en/data-download.html?id=214&cid=31>`_

* `Ebyte documentation for most E32-433T33D  (On manualslib.com) <https://www.manualslib.com/manual/2924523/Ebyte-E32-433t33d.html?page=2#manual>`_

License
*******
This project is licensed under the `MIT license <LICENSE>`_.
