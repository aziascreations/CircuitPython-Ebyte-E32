# CircuitPython Ebyte E32 Library (W.I.P.)
CircuitPython driver for Ebyte's E32 LoRa modules.

## Features
* Supports all standard E32 modules.
* Extra support on a per-frequency and per-power basis:
  * More descriptive constants for TX power.
  * Channel <-> frequency converters.
  * ~~Maximum packet size calculators~~.  (TODO)
  * Entirely optional.
* Beginner-friendly:
  * Automatic DigitalInOut instantiation
  * Automatic UART bus instantiation

## Limitations
* No built-in protocol:
  * All LoRa packets are glued back-to-back when received.
  * **No LoraWAN support**
* Missing extra support for some modules:
  * Modules with `170`, `400`, `868`, `900`, and `915` prefix.  *(Will improve overtime)*
  * Modules with the `27` suffix.*

<sub>

*: The `E32-433T27D` variant is mentionned in the
[E32 V1.30 User Manual](https://www.ebyte.com/en/pdf-down.aspx?id=775),
but no datasheet or product listing can be found for it,
no other modules with that suffix appear to exist.

</sub>

## Dependencies
This driver depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka)

## Installing
TODO

## Usage
TODO

## Legal Disclaimer
Proper usage of E32 modules and adherence to your local laws and other RF-related laws all fall under your
responsibility.<br>
Improper use can result in physical damage to your module, and it may also break some of your local laws,
especially those regarding RF transmissions.

An example of these law-related issues would be the usage of `E32-443T30D` / `TTL-1W` modules in most of europe.<br>
Unless you have the proper authorizations, you most likely can't legally own or use them,
and you would typically be limited to modules with a maximum of 20dBm / 100mW TX power on the EU443 band.<br>

I cannot be held responsible for what you do with your own devices in your free time.<br>

## License
This project is licensed under the [MIT license](LICENSE).
