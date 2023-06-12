# CircuitPython Ebyte E32 Library (W.I.P.)
CircuitPython driver for Ebyte's E32 UART LoRa modules.

## Features
* Supports all standard E32 UART modules.
* Extra support on a per-frequency and per-power basis:
  * More descriptive constants for TX power.
  * Channel <-> frequency converters.
  * ~~Maximum packet size calculators~~.  (TODO)
  * Entirely optional via separate modules.
* Minified versions for devices with tiny storage space:
  * ~75% smaller for `.py` files
  * ~5% smaller for `.mpy` files  *(Due to shortened local variables, mostly)*

## Limitations
* **No built-in packet size limit:**
  * Wildly different between frequencies & operating parameters.
  * Not documented clearly enough in LoRA and LoRaWAN documentation.
* No built-in protocol:
  * All LoRa packets are glued back-to-back when received.
  * **No LoraWAN support**
* Missing extra support for some modules:
  * Modules with `170`, `400`, `868`, `900`, and `915` prefix.  *(Will improve overtime)*

## Dependencies
This driver depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka)

## Installing
TODO

## Usage
Usage examples can be found in the [examples](examples) folder,
or in the *Examples* section of the [documentation](https://aziascreations.github.io/CircuitPython-Ebyte-E32/).

### Wiring
| E32 Module | MCU                             |
|------------|---------------------------------|
| `M0`       | Any digital output pin          |
| `M1`       | Any digital output pin          |
| `RXD`      | Any UART **TX** capable pin*    |
| `TXD`      | Any UART **RX** capable pin*    |
| `AUX`      | Any digital input pin**         |
| `VCC`      | Power supply 2.3V to 5.2V DC*** |

*: Some devices like the *STM32 Black Pill* may require you to use very specific pins for the UART bus.<br>
**: Analogue input pins might work, but this type of setup isn't supported !<br>
***: More than 5.2V can cause damage, and make sure to double-check the datasheet !

### *"Making sure it works"*
The `E32Device` class will raise a `RuntimeError` exception during instantiation if it can't communicate to
your module.

The same error may be raised when you change any operating setting.

## Links

### Resources
* [Effevee's E32 driver for MicroPython](https://github.com/effevee/loraE32/)

* [LoRa frequency plan by country (By The Things Network)](https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/)

* [Ebyte documentation for most E32 170/400/433/868/900/915 modules](https://www.ebyte.com/en/data-download.html?id=214&cid=31)

* [Ebyte documentation for most E32-433T33D  (On manualslib.com)](https://www.manualslib.com/manual/2924523/Ebyte-E32-433t33d.html?page=2#manual)

* [???](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/lora-and-lorawan)

* [???](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/the-book/packet-size-considerations/)

* [???](https://resources.lora-alliance.org/home/rp002-1-0-4-regional-parameters)

* [???](https://www.rfwireless-world.com/calculators/LoRa-Data-Rate-Calculator.html)

### Datasheets
All datasheets are hosted by Ebyte on ebyte.com unless specified otherwise.

* [E32-443T20DT](https://www.ebyte.com/en/downpdf.aspx?id=660)
* [E32-443T30D](https://www.ebyte.com/en/downpdf.aspx?id=108)
* [E32-433T33S](https://www.manualslib.com/manual/2938896/Ebyte-E32-433t33s.html) (manualslib.com)

If any datasheet become unavailable, please open an issue.<br>
We also keep copies of them over at [files.nibblepoker.lu](https://files.nibblepoker.lu/datasheets/ebyte/e32/) just in case.

## Legal Disclaimer
Proper usage of E32 modules and adherence to your local laws and other RF-related laws all fall under your
responsibility.<br>
Improper use can result in physical damage to your module, and may also break some of your local laws,
especially those regarding RF transmissions.

An example of these law-related issues would be the usage of `E32-443T30D` / `TTL-1W` modules in most of europe.<br>
Unless you have the proper authorizations, you most likely can't legally own or use them,
and you would typically be limited to modules with a maximum of 20dBm / 100mW TX power on the EU443 band.<br>

I cannot be held responsible for what you do with your own devices in your free time.<br>

## License
This project is licensed under the [MIT license](LICENSE).
