.. role:: raw-html(raw)
    :format: html

Power-supply Considerations
---------------------------

Voltage
^^^^^^^
Most modules require their VIN pin to be between 3.3V and 5.0V

They shouldn't have more than 5.2V as it can cause damage to your module.

The `E32-443T37S` module is a special case as it requires between 4.5V and 15V.

Extra Passive Components
^^^^^^^^^^^^^^^^^^^^^^^^

Low power modules
"""""""""""""""""
You should preferably put a small decoupling capacitor as close to the `VIN` and `GND` pins as possible.

Some people on `mischianti.org <https://mischianti.org/forums/topic/lora-e32-decupling-capacitor/>`_
have apparently emailed Ebyte and were recommended the following:

    `A capacitor between 100nF/0.1µF and 1000nF/1µF.`

High power modules
""""""""""""""""""
The `E32-443T37S` module requires a more complex setup as shown below:

.. image:: _static/e32-443t37s-wiring.png
   :width: 90%
   :align: center

:raw-html:`<br>`
