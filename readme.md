# CircuitPython Ebyte E32 Library
CircuitPython driver for Ebyte's E32 UART LoRa modules that use the SX1278/SX1276 chipsets.

## Features
* Supports all standard E32 UART modules.
* Extra support on a per-frequency and per-power basis:
  * More descriptive constants for TX power.
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
* Missing support for some modules:
  * Modules with `170`, `400` and `900` prefix.  *(Will improve overtime)*

## Dependencies
This driver depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka)

## Installing
Go to the [Releases page](https://github.com/aziascreations/CircuitPython-Ebyte-E32/releases/) and download one of the
packages.

Here is a short description of the available packages:

| Package suffix | Description                                         |
|----------------|-----------------------------------------------------|
| `py`           | Python files from [ebyte_e32/](ebyte_e32)           |
| `py-min`       | Minified version of this repository's code.         |
| `mpy-8`        | Python files compiled using *mpy-cross v8*          |
| `mpy-8-min`    | Minified python files compiled using *mpy-cross v8* |

## Usage
Usage examples can be found in the [examples](examples) folder,
or in the *Examples* section of the [documentation](https://aziascreations.github.io/CircuitPython-Ebyte-E32/).

### Wiring
| E32 Module | MCU                                                             |
|------------|-----------------------------------------------------------------|
| `M0`       | Any digital output pin                                          |
| `M1`       | Any digital output pin                                          |
| `RXD`      | Any UART **TX** capable pin*                                    |
| `TXD`      | Any UART **RX** capable pin*                                    |
| `AUX`      | Any digital input pin**                                         |
| `VCC`      | Power supply 2.3V to 5.2V DC, or 4.5V to 15V for E32-443T37S*** |

*: Some devices like the *STM32 Black Pill* may require you to use very specific pins for the UART bus.<br>
**: Analogue input pins might work, but this type of setup isn't supported !<br>
***: Higher voltages can cause damage, make sure to double-check the datasheet !

### *"Making sure it works"*
The `E32Device` class will raise a `ebyte_e32.exceptions.E32GenericError` exception during instantiation if
it can't communicate to your module.

The same error may be raised when you change any operating setting.

## Links

### Resources
* [xreef's E32 driver for Arduino](https://github.com/xreef/LoRa_E32_Series_Library)
* [Effevee's E32 driver for MicroPython](https://github.com/effevee/loraE32/)
* [LoRa and LoRaWAN quick overview  (By SemTech)](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/lora-and-lorawan)
* [LoRa frequency plan by country (By The Things Network)](https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/)
* [LoRa RF modulation basics  (On wiki.lahoud.fr)](http://wiki.lahoud.fr/lib/exe/fetch.php?media=an1200.22.pdf)
* [Ebyte documentation for most E32 170/400/433/868/900/915 modules  (On ebyte.com)](https://www.ebyte.com/en/data-download.html?id=214&cid=31)
* [Ebyte documentation for most E32-433T33D  (On manualslib.com)](https://www.manualslib.com/manual/2924523/Ebyte-E32-433t33d.html?page=2#manual)
* [LoRaWAN Regional Parameters  (By LoRa Alliance)](https://resources.lora-alliance.org/home/rp002-1-0-4-regional-parameters)
* [LoRa - Packet size considerations  (By SemTech)](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/the-book/packet-size-considerations/)
* [LoRaWAN - Regional parameters  (By LoRa Alliance)](https://resources.lora-alliance.org/home/rp002-1-0-4-regional-parameters)
* [LoRa data rate calculator (By rfwireless-world.com)](https://www.rfwireless-world.com/calculators/LoRa-Data-Rate-Calculator.html)

### Datasheets
All datasheets can be found in
[the documentation](https://aziascreations.github.io/CircuitPython-Ebyte-E32/technical_details_e32.html#datasheets).

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
