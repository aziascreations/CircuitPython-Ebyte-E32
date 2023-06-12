Search.setIndex({"docnames": ["api", "examples_config", "examples_instantiation", "examples_transmit_fixed", "examples_transmit_transparent", "examples_uart", "index", "introduction", "technical_details_e32", "technical_details_lora", "technical_details_lorawan", "technical_details_preamble", "technical_details_wiring"], "filenames": ["api.rst", "examples_config.rst", "examples_instantiation.rst", "examples_transmit_fixed.rst", "examples_transmit_transparent.rst", "examples_uart.rst", "index.rst", "introduction.rst", "technical_details_e32.rst", "technical_details_lora.rst", "technical_details_lorawan.rst", "technical_details_preamble.rst", "technical_details_wiring.rst"], "titles": ["<cite>ebyte_e32</cite>", "Configuration", "Instantiation", "Fixed Transmissions", "Transparent Transmissions", "UART Configuration", "CircuitPython Ebyte E32 Library", "CircuitPython Ebyte E32 Library", "E32 Modules", "LoRa", "LoRaWAN", "Preamble  \u26a0\ufe0f Must-read \u26a0\ufe0f", "Power-supply Considerations"], "terms": {"author": 0, "": [0, 1, 2, 3, 4, 5, 6, 7, 8], "herwin": [0, 1, 2, 3, 4, 5], "bozet": [0, 1, 2, 3, 4, 5], "class": [0, 2, 5, 6], "airdatar": [0, 2, 6], "data": [0, 1, 2, 3, 4, 5, 11], "rate": [0, 1, 2, 5, 11], "bp": [0, 1, 2, 5], "which": [0, 1], "lora": [0, 6, 7, 11], "modul": [0, 2, 3, 4, 5, 6, 7, 11], "commun": [0, 4, 5, 11], "between": [0, 2, 4, 6, 7], "each": [0, 1, 3, 4], "other": [0, 1, 4, 8, 11], "thi": [0, 1, 2, 3, 4, 6, 7, 8, 9, 11], "set": [0, 5], "directli": 0, "affect": 0, "maximum": [0, 6, 7], "packet": [0, 6, 7, 11], "size": [0, 6, 7, 11], "rang": 0, "must": [0, 6], "same": [0, 2, 4, 5], "all": [0, 1, 2, 6, 7, 8, 9, 11], "rate_0_3k": [0, 6], "0": [0, 1, 2, 3, 4, 5], "equal": 0, "3": [0, 1], "kbp": [0, 1, 2], "rate_19_2k": [0, 6], "5": [0, 3, 4, 6, 7, 8], "19": 0, "2": [0, 1, 2, 8], "rate_1_2k": [0, 6], "1": [0, 1, 3, 4, 8], "rate_2_4k": [0, 6], "4": [0, 1, 2, 3, 4, 5], "rate_4_8k": [0, 6], "8": [0, 1, 2], "rate_9_6k": [0, 6], "9": 0, "6": 0, "rate_default": [0, 2, 6], "default": [0, 1, 2, 4], "air": [0, 1, 2, 5], "e32": [0, 1, 2, 3, 4, 5, 11], "devic": [0, 1, 4, 6, 7, 8], "channel_max": [0, 6], "31": [0, 2], "maxim": 0, "allow": 0, "channel": [0, 1, 2, 3, 4, 5, 6, 7], "number": [0, 6], "inclus": 0, "channel_min": [0, 6], "minim": 0, "e32devic": [0, 1, 2, 3, 4, 5, 6], "pin_m0": [0, 1, 2, 3, 4, 5], "microcontrol": 0, "pin": [0, 1, 2, 3, 4, 5, 8], "pin_m1": [0, 1, 2, 3, 4, 5], "pin_aux": [0, 1, 2, 3, 4, 5], "none": [0, 2], "pin_tx": [0, 2], "pin_rx": [0, 2], "uart_buffer_s": [0, 2], "int": 0, "64": [0, 2], "address": [0, 1, 2, 3, 4, 5, 6], "uart_par": [0, 1, 2, 5, 6], "serialpar": [0, 2, 5, 6], "uart_rat": [0, 1, 2, 5, 6], "tupl": [0, 1], "serialbaudr": [0, 2, 5, 6], "9600": [0, 1, 2, 5], "data_r": [0, 1, 2, 6], "tx_mode": [0, 1, 2, 3, 4, 6], "transmissionmod": [0, 2, 3, 4, 6], "io_drive_mod": [0, 1, 2, 6], "iodrivemod": [0, 2, 6], "wake_up_tim": [0, 1, 2, 6], "wakeuptim": [0, 2, 6], "forward_error_correct": [0, 1, 2, 6], "bool": 0, "forwarderrorcorrect": [0, 2, 6], "true": [0, 3, 4], "tx_power": [0, 1, 2, 6], "sbc": 0, "properti": [0, 1], "i": [0, 6, 7, 8, 9, 11], "us": [0, 1, 3, 4, 5, 8, 11], "fix": [0, 4, 6], "transmiss": [0, 6, 11], "ignor": 0, "when": [0, 5, 6, 7, 12], "receiv": [0, 6, 7], "broadcast": [0, 6], "messag": [0, 3, 4, 5], "0x0000": [0, 1, 2], "0xffff": [0, 3], "If": [0, 1, 3, 4, 5, 8, 11], "mode": [0, 1, 2, 3, 4, 5, 6], "you": [0, 1, 2, 3, 4, 5, 6, 7, 8, 11], "can": [0, 1, 3, 4, 8, 11], "also": [0, 3, 6, 7, 8, 11], "special": [0, 3], "monitor": [0, 6], "given": [0, 2, 3], "chang": [0, 1, 5], "caus": [0, 1, 8], "temporarili": 0, "go": [0, 1, 5], "sleep": [0, 1, 3, 4, 5], "flush": [0, 1], "uart": [0, 1, 2, 3, 4, 6, 7, 8], "buffer": [0, 1], "aux": [0, 1, 2, 6, 8], "digitalio": 0, "digitalinout": [0, 2], "indic": 0, "its": [0, 11], "work": [0, 5, 8], "statu": 0, "wake": [0, 1, 2], "up": [0, 1, 2], "mcu": [0, 8], "mai": [0, 3, 4, 8], "left": [0, 2], "float": 0, "dure": 0, "normal": [0, 3, 4, 5], "oper": [0, 1, 3, 4, 6, 7, 11], "ani": [0, 3, 4, 5, 8, 11], "non": [0, 5, 8], "both": [0, 11], "ar": [0, 2, 4, 5, 6, 7, 8, 11], "limit": 0, "target": [0, 3, 4], "one": [0, 11], "return": [0, 1], "origin": 0, "afterward": 0, "valu": [0, 1, 2], "deinit": [0, 3, 4, 6], "deiniti": 0, "instanc": 0, "liber": 0, "flush_uart": [0, 6], "empti": [0, 4], "out": [0, 2], "possibl": [0, 11], "forward": [0, 1, 2], "error": [0, 1, 2], "correct": [0, 1, 2, 5], "toggl": 0, "get_config": [0, 1, 6], "e32deviceconfig": [0, 1, 6], "get": [0, 1, 11], "name": [0, 1, 8], "contain": [0, 3], "current": [0, 1], "configur": [0, 2, 6], "A": 0, "get_raw_config": [0, 6], "byte": [0, 3, 4, 11], "fetch": [0, 1], "raw": [0, 2], "config": [0, 1, 2], "from": [0, 2, 6, 9], "The": [0, 1, 2, 3, 4, 5, 6, 7, 8], "respons": [0, 6, 7], "object": 0, "length": [0, 3, 4], "get_raw_vers": [0, 6], "version": [0, 6, 7], "get_vers": [0, 6], "e32devicevers": [0, 6], "model": [0, 6], "featur": 0, "ebyt": [0, 8], "document": [0, 3, 4, 6, 7], "doesn": 0, "t": [0, 2, 4, 8], "explain": [0, 11], "content": [0, 3, 4], "second": 0, "third": 0, "detail": [0, 11], "ant": 0, "io": [0, 1, 2], "drive": [0, 1, 2], "rx": [0, 1, 2, 3, 4, 5, 8], "tx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 12], "should": [0, 1, 2, 6, 7, 11], "repres": 0, "m0": [0, 8], "m1": [0, 8], "prepare_uart": [0, 6], "baudrat": [0, 6], "pariti": [0, 1, 2, 6], "busio": [0, 2], "prepar": [0, 2], "bu": [0, 5, 8], "further": 0, "paramet": [0, 1, 2, 3, 4, 5, 6, 7], "new": [0, 1], "reset": [0, 6], "stay_in_sleep_mod": 0, "send": [0, 3, 4, 5, 12], "command": 0, "stai": 0, "wait": [0, 3, 4], "unless": [0, 8], "instruct": 0, "prevent": [0, 3, 4], "rogu": 0, "an": [0, 4, 8], "undesir": 0, "like": [0, 11], "unrespons": 0, "coupl": 0, "whether": 0, "after": [0, 11, 12], "send_raw": [0, 3, 4, 6], "max_packet_s": 0, "wait_aux": [0, 3, 4, 6], "sent": [0, 3, 4], "truncat": [0, 3, 4], "max": [0, 8, 11], "count": 0, "method": [0, 1, 11], "written": 0, "power": [0, 1, 2, 6, 7, 8, 11], "transmit": 0, "via": [0, 1, 6, 7], "save": 0, "tx_power_min": [0, 6], "tx_power_max": [0, 6], "connect": 0, "line": [0, 8], "automat": [0, 5], "appli": [0, 11], "switch": [0, 3, 4, 5, 12], "update_config": [0, 6], "make_perman": 0, "fals": 0, "verifi": 0, "down": 0, "check": [0, 3, 4, 6, 7, 8], "rais": 0, "runtimeerror": 0, "couldn": 0, "max_wait_m": 0, "150": 0, "high": 0, "mean": 0, "readi": [0, 11], "wa": [0, 3, 4], "low": 0, "period": 0, "150m": 0, "most": [0, 6, 7, 11], "time": [0, 1, 2, 3, 4], "alia": 0, "field": 0, "7": 0, "fixm": 0, "figur": 0, "ratio": 0, "sinc": 0, "lorawan": [0, 6, 7, 11], "want": [0, 1], "fec_default": [0, 2, 6], "fec": 0, "fec_dis": [0, 6], "enabl": [0, 1, 2], "fec_en": [0, 6], "disabl": 0, "hasn": 0, "been": 0, "test": [0, 8], "yet": 0, "isn": [0, 8], "relat": 0, "differ": [0, 6, 7], "drive_default": [0, 2, 6], "drive_open": [0, 6], "push": [0, 1, 2], "pull": [0, 1, 2], "output": [0, 1, 8], "input": [0, 8], "drive_pul": [0, 6], "open": [0, 8], "collector": 0, "refer": [0, 11], "constant": [0, 6, 7], "organ": 0, "follow": [0, 11], "manner": 0, "list": [0, 8], "m1_valu": 0, "mode_norm": [0, 3, 4, 5, 6], "radio": 0, "packag": [0, 8, 12], "known": 0, "mode_power_sav": [0, 6], "incom": [0, 3, 4], "appropri": 0, "preambl": 0, "onc": 0, "goe": 0, "5m": 0, "re": [0, 5], "again": 0, "p": 0, "mode_sleep": [0, 5, 6], "put": [0, 5], "where": 0, "turn": 0, "off": 0, "mode_wake_up": [0, 6], "ad": 0, "code": 0, "depend": [0, 3, 4, 11], "baud": 0, "baud_115200": [0, 6], "115200": 0, "baud_1200": [0, 6], "1200": 0, "baud_19200": [0, 5, 6], "19200": [0, 5], "baud_2400": [0, 6], "2400": 0, "baud_38400": [0, 6], "38400": 0, "baud_4800": [0, 6], "4800": 0, "baud_57600": [0, 6], "57600": 0, "baud_9600": [0, 6], "baud_default": [0, 2, 6], "parity_default": [0, 2, 6], "parity_even": [0, 6], "8e1": 0, "parity_non": [0, 5, 6], "8n1": [0, 1, 2], "parity_odd": [0, 5, 6], "8o1": 0, "avail": [0, 1, 2], "transmission_default": [0, 2, 6], "explicitli": 0, "datasheet": [0, 6], "case": [0, 8], "practic": 0, "transmission_fix": [0, 3, 6], "In": [0, 3, 4, 8], "abl": [0, 4], "prepend": 0, "requir": [0, 8], "transmission_transpar": [0, 4, 6], "Not": [0, 6, 7], "wake_time_1000m": [0, 6], "wake_time_1250m": [0, 6], "wake_time_1500m": [0, 6], "wake_time_1750m": [0, 6], "wake_time_2000m": [0, 6], "wake_time_250m": [0, 6], "wake_time_500m": [0, 6], "wake_time_750m": [0, 6], "wake_time_default": [0, 2, 6], "frequency_maximum": [0, 6], "441": 0, "eu443": 0, "frequenc": [0, 3, 4, 6, 7, 8, 11], "mhz": 0, "correspond": 0, "frequency_minimum": [0, 6], "410": 0, "minimum": 0, "channel_to_frequ": [0, 6], "strict": 0, "convert": [0, 6, 7], "valueerror": 0, "except": 0, "invalid": 0, "frequency_to_channel": [0, 6], "409": 0, "closest": 0, "transmitpow": [0, 6], "suffix": 0, "tx_power_10dbm": [0, 6], "10": 0, "mw": [0, 8], "tx_power_14dbm": [0, 6], "25": 0, "tx_power_17dbm": [0, 6], "50": 0, "tx_power_20dbm": [0, 6], "100mw": 0, "tx_power_default": [0, 6], "tx_power_21dbm": [0, 6], "125": 0, "tx_power_24dbm": [0, 6], "250": [0, 11], "tx_power_27dbm": [0, 6], "500": 0, "tx_power_30dbm": [0, 6], "1w": 0, "1000mw": 0, "tx_power_33dbm": [0, 6], "2w": [0, 8], "2000mw": 0, "These": [1, 2, 3, 4, 5, 11], "exampl": [1, 2, 3, 4, 5, 11], "show": [1, 2, 3, 4, 5], "how": [1, 2, 3, 4, 5], "config_manu": 1, "py": [1, 2, 3, 4, 5, 6, 7], "spdx": [1, 2, 3, 4, 5], "filecopyrighttext": [1, 2, 3, 4, 5], "2023": [1, 2, 3, 4, 5], "licens": [1, 2, 3, 4, 5, 11], "identifi": [1, 2, 3, 4, 5], "unlicens": [1, 2, 3, 4, 5], "import": [1, 2, 3, 4, 5], "binascii": 1, "board": [1, 2, 3, 4, 5], "ebyte_e32": [1, 2, 3, 4, 5, 6], "io13": [1, 2, 3, 4, 5], "io12": [1, 2, 3, 4, 5], "pin_rxd": [1, 2, 3, 4, 5], "io11": [1, 2, 3, 4, 5], "mark": [1, 2, 3, 4, 5], "pin_txd": [1, 2, 3, 4, 5], "io10": [1, 2, 3, 4, 5], "io9": [1, 2, 3, 4, 5], "bit": [1, 2], "transpar": [1, 2, 6], "250m": [1, 2], "lowest": [1, 2], "print": [1, 3, 4, 5], "f": [1, 3, 4, 5], "old": 1, "0x": [1, 3, 4], "x": [1, 3, 4], "0x1337": [1, 3, 4], "todo": [1, 6, 7, 9, 10, 12], "shown": [1, 9], "config_read": 1, "grab": [1, 2, 3, 4], "b": [1, 3, 4], "x00": 1, "two": 2, "properli": [2, 11], "constructor": 2, "handl": [2, 11], "process": [2, 3, 4], "make": [2, 8, 10], "them": [2, 8, 11], "custom": 2, "instantiation_bas": 2, "specifi": [2, 8], "instantiation_ful": 2, "0b11": 2, "highest": 2, "0b00": 2, "have": [2, 8], "thei": [2, 11], "weren": 2, "need": [3, 11], "befor": 3, "actual": 3, "specif": [3, 4, 6, 11], "due": [3, 4, 6, 7, 11], "rf": [3, 4, 6, 7, 11], "regul": [3, 4, 11], "transmit_fix": 3, "receiver_unicast": 3, "b3": [3, 4], "b4": [3, 4], "a2": [3, 4], "a3": [3, 4], "b7": [3, 4], "while": [3, 4, 11, 12], "u": [3, 4], "some": [3, 4, 6, 7, 8, 11], "in_wait": [3, 4], "finish": [3, 4], "we": [3, 4, 5, 8], "here": [3, 4, 5, 11], "read": [3, 4, 6], "exit": [3, 4], "len": [3, 4], "long": [3, 4], "noth": [3, 4], "now": [3, 4, 5, 8], "receiver_broadcast": 3, "sender_unicast": 3, "0xbeef": [3, 4], "x13": 3, "x37": 3, "x04": 3, "hello": [3, 4], "world": [3, 4], "x04hello": 3, "helper": [3, 4], "spam": [3, 4], "manual": [3, 4, 6, 8], "write": [3, 4, 11], "pleas": [3, 4, 8, 11], "more": [3, 4, 6, 7, 8], "inform": [3, 4, 9, 11], "sender_broadcast": 3, "xff": 3, "who": [4, 11], "share": 4, "transmit_transpar": 4, "anoth": 4, "shouldn": 4, "instanti": [5, 6], "0x1377": 5, "speed": 5, "back": [5, 6, 7], "ll": 5, "odd": 5, "driver": [6, 7], "m": [6, 7, 11], "what": [6, 7], "do": [6, 7, 11], "your": [6, 7], "act": [6, 7], "responsibli": [6, 7], "realli": [6, 7, 12], "asid": [6, 7], "section": [6, 7, 11], "support": [6, 7, 8], "standard": [6, 7], "extra": [6, 7], "per": [6, 7], "basi": [6, 7], "descript": [6, 7], "calcul": [6, 7, 11], "entir": [6, 7, 11], "option": [6, 7], "separ": [6, 7], "minifi": [6, 7], "tini": [6, 7], "storag": [6, 7], "space": [6, 7], "75": [6, 7], "smaller": [6, 7], "file": [6, 7, 8], "mpy": [6, 7], "shorten": [6, 7], "local": [6, 7, 11], "variabl": [6, 7], "mostli": [6, 7], "No": [6, 7], "built": [6, 7], "wildli": [6, 7], "clearli": [6, 7], "enough": [6, 7], "protocol": [6, 7], "glu": [6, 7], "miss": [6, 7], "170": [6, 7], "400": [6, 7, 8], "868": [6, 7], "900": [6, 7], "915": [6, 7], "prefix": [6, 7], "Will": [6, 7], "improv": [6, 7], "overtim": [6, 7], "adafruit": [6, 7], "blinka": [6, 7], "quick": [6, 7], "overview": [6, 7], "By": [6, 7], "semtech": [6, 7], "plan": [6, 7], "countri": [6, 7], "thing": [6, 7], "network": [6, 7], "basic": [6, 7], "On": [6, 7], "wiki": [6, 7], "lahoud": [6, 7], "fr": [6, 7], "433": [6, 7], "com": [6, 7, 8], "433t33d": [6, 7], "manualslib": [6, 7, 8], "region": [6, 7, 11], "allianc": [6, 7], "project": [6, 7], "under": [6, 7, 11], "mit": [6, 7], "suppli": [6, 8], "consider": 6, "wire": 6, "structur": 6, "spread": 6, "factor": [6, 8], "complet": 6, "unicast": 6, "sender": 6, "eu433": [6, 8], "t20": 6, "t30": 6, "t33": 6, "index": 6, "search": 6, "page": [6, 9], "digit": 8, "rxd": 8, "capabl": 8, "txd": 8, "vcc": 8, "3v": 8, "2v": 8, "dc": 8, "veri": [8, 11], "analogu": 8, "might": 8, "type": [8, 11], "setup": 8, "than": [8, 11], "damag": 8, "sure": 8, "doubl": 8, "uniqu": 8, "help": 8, "dbm": 8, "form": 8, "sdm": 8, "surfac": 8, "mount": 8, "d": 8, "dip": 8, "dual": 8, "dt": 8, "abc": 8, "chipset": 8, "1xx": 8, "443t20dc": 8, "443t20": 8, "443t20s2t": 8, "20": 8, "100": 8, "sx1278": 8, "443t27d": 8, "443t30d": 8, "443t30": 8, "30": 8, "w": 8, "443t33": 8, "33": 8, "868t20d": 8, "868t20": 8, "868t30d": 8, "868t30": 8, "915t20d": 8, "915t20": 8, "915t30d": 8, "915t30": 8, "sx1276": 8, "433t27d": 8, "variant": 8, "mention": 8, "v1": 8, "user": 8, "product": 8, "could": [8, 12], "found": 8, "aren": 8, "cannot": [8, 11], "own": 8, "legal": 8, "right": [8, 11], "host": 8, "cdebyt": 8, "otherwis": 8, "443t20dt": 8, "http": 8, "www": 8, "en": 8, "downpdf": 8, "aspx": 8, "id": 8, "660": 8, "108": 8, "433t33": 8, "2938896": 8, "html": 8, "becom": 8, "unavail": 8, "issu": [8, 11], "br": 8, "keep": [8, 11], "copi": 8, "over": 8, "nibblepok": 8, "lu": 8, "just": 8, "taken": 9, "short": 10, "link": 10, "offici": 10, "spec": 10, "sheet": 10, "extrem": 11, "complic": 11, "understand": 11, "execut": 11, "varieti": 11, "reason": 11, "technic": 11, "aim": 11, "clarifi": 11, "impact": 11, "wai": 11, "program": 11, "small": 11, "common": 11, "cover": 11, "wide": 11, "confus": 11, "conflat": 11, "simpl": 11, "motiv": 11, "larger": 11, "11": 11, "unfavor": 11, "condit": 11, "favor": 11, "ones": 11, "mind": 11, "onli": 11, "person": 11, "research": 11, "synthes": 11, "am": 11, "infal": 11, "especi": 11, "profession": 11, "vers": 11, "law": 11, "pertain": 11, "hard": 11, "fact": 11, "mix": 11, "lingo": 11, "domain": 11, "easi": 11, "wrong": 11, "lawyer": 11, "well": 11, "those": 11, "least": 11, "knowledg": 11, "peopl": 11, "equip": 11, "mess": 11, "around": 11, "fcc": 11, "ibpt": 11, "regulatori": 11, "bodi": 11, "come": 11, "gonna": 11, "ham": 11, "effici": 11, "track": 11, "find": 11, "offend": 11, "parti": 11, "necessari": 11, "trust": 11, "me": 11, "problem": 12, "notic": 12, "crash": 12, "vin": 12, "rippl": 12, "involuntari": 12, "inductor": 12, "bad": 12, "5v": 12}, "objects": {"": [[0, 0, 0, "-", "ebyte_e32"]], "ebyte_e32": [[0, 1, 1, "", "AirDataRate"], [0, 3, 1, "", "CHANNEL_MAX"], [0, 3, 1, "", "CHANNEL_MIN"], [0, 1, 1, "", "E32Device"], [0, 1, 1, "", "E32DeviceConfig"], [0, 1, 1, "", "E32DeviceVersion"], [0, 1, 1, "", "ForwardErrorCorrection"], [0, 1, 1, "", "IODriveMode"], [0, 1, 1, "", "Modes"], [0, 1, 1, "", "SerialBaudRate"], [0, 1, 1, "", "SerialParity"], [0, 3, 1, "", "TX_POWER_MAX"], [0, 3, 1, "", "TX_POWER_MIN"], [0, 1, 1, "", "TransmissionMode"], [0, 1, 1, "", "WakeUpTime"], [0, 0, 0, "-", "eu433"], [0, 0, 0, "-", "t20"], [0, 0, 0, "-", "t30"], [0, 0, 0, "-", "t33"]], "ebyte_e32.AirDataRate": [[0, 2, 1, "", "RATE_0_3K"], [0, 2, 1, "", "RATE_19_2K"], [0, 2, 1, "", "RATE_1_2K"], [0, 2, 1, "", "RATE_2_4K"], [0, 2, 1, "", "RATE_4_8K"], [0, 2, 1, "", "RATE_9_6K"], [0, 2, 1, "", "RATE_DEFAULT"]], "ebyte_e32.E32Device": [[0, 4, 1, "", "address"], [0, 2, 1, "", "aux"], [0, 4, 1, "", "channel"], [0, 4, 1, "", "data_rate"], [0, 5, 1, "", "deinit"], [0, 5, 1, "", "flush_uart"], [0, 4, 1, "", "forward_error_correction"], [0, 5, 1, "", "get_config"], [0, 5, 1, "", "get_raw_config"], [0, 5, 1, "", "get_raw_version"], [0, 5, 1, "", "get_version"], [0, 4, 1, "", "io_drive_mode"], [0, 4, 1, "", "mode"], [0, 5, 1, "", "prepare_uart"], [0, 5, 1, "", "reset"], [0, 5, 1, "", "send_raw"], [0, 4, 1, "", "tx_mode"], [0, 4, 1, "", "tx_power"], [0, 2, 1, "", "uart"], [0, 4, 1, "", "uart_parity"], [0, 4, 1, "", "uart_rate"], [0, 5, 1, "", "update_config"], [0, 5, 1, "", "wait_aux"], [0, 4, 1, "", "wake_up_time"]], "ebyte_e32.E32DeviceConfig": [[0, 2, 1, "", "address"], [0, 2, 1, "", "channel"], [0, 2, 1, "", "data_rate"], [0, 2, 1, "", "forward_error_correction"], [0, 2, 1, "", "io_drive_mode"], [0, 2, 1, "", "tx_mode"], [0, 2, 1, "", "tx_power"], [0, 2, 1, "", "uart_parity"], [0, 2, 1, "", "uart_rate"], [0, 2, 1, "", "wake_up_time"]], "ebyte_e32.E32DeviceVersion": [[0, 2, 1, "", "features"], [0, 2, 1, "", "model"], [0, 2, 1, "", "version"]], "ebyte_e32.ForwardErrorCorrection": [[0, 2, 1, "", "FEC_DEFAULT"], [0, 2, 1, "", "FEC_DISABLED"], [0, 2, 1, "", "FEC_ENABLE"]], "ebyte_e32.IODriveMode": [[0, 2, 1, "", "DRIVE_DEFAULT"], [0, 2, 1, "", "DRIVE_OPEN"], [0, 2, 1, "", "DRIVE_PULL"]], "ebyte_e32.Modes": [[0, 2, 1, "", "MODE_NORMAL"], [0, 2, 1, "", "MODE_POWER_SAVE"], [0, 2, 1, "", "MODE_SLEEP"], [0, 2, 1, "", "MODE_WAKE_UP"]], "ebyte_e32.SerialBaudRate": [[0, 2, 1, "", "BAUD_115200"], [0, 2, 1, "", "BAUD_1200"], [0, 2, 1, "", "BAUD_19200"], [0, 2, 1, "", "BAUD_2400"], [0, 2, 1, "", "BAUD_38400"], [0, 2, 1, "", "BAUD_4800"], [0, 2, 1, "", "BAUD_57600"], [0, 2, 1, "", "BAUD_9600"], [0, 2, 1, "", "BAUD_DEFAULT"]], "ebyte_e32.SerialParity": [[0, 2, 1, "", "PARITY_DEFAULT"], [0, 2, 1, "", "PARITY_EVEN"], [0, 2, 1, "", "PARITY_NONE"], [0, 2, 1, "", "PARITY_ODD"]], "ebyte_e32.TransmissionMode": [[0, 2, 1, "", "TRANSMISSION_DEFAULT"], [0, 2, 1, "", "TRANSMISSION_FIXED"], [0, 2, 1, "", "TRANSMISSION_TRANSPARENT"]], "ebyte_e32.WakeUpTime": [[0, 2, 1, "", "WAKE_TIME_1000MS"], [0, 2, 1, "", "WAKE_TIME_1250MS"], [0, 2, 1, "", "WAKE_TIME_1500MS"], [0, 2, 1, "", "WAKE_TIME_1750MS"], [0, 2, 1, "", "WAKE_TIME_2000MS"], [0, 2, 1, "", "WAKE_TIME_250MS"], [0, 2, 1, "", "WAKE_TIME_500MS"], [0, 2, 1, "", "WAKE_TIME_750MS"], [0, 2, 1, "", "WAKE_TIME_DEFAULT"]], "ebyte_e32.eu433": [[0, 3, 1, "", "FREQUENCY_MAXIMUM"], [0, 3, 1, "", "FREQUENCY_MINIMUM"], [0, 6, 1, "", "channel_to_frequency"], [0, 6, 1, "", "frequency_to_channel"]], "ebyte_e32.t20": [[0, 1, 1, "", "TransmitPower"]], "ebyte_e32.t20.TransmitPower": [[0, 2, 1, "", "TX_POWER_10DBM"], [0, 2, 1, "", "TX_POWER_14DBM"], [0, 2, 1, "", "TX_POWER_17DBM"], [0, 2, 1, "", "TX_POWER_20DBM"], [0, 2, 1, "", "TX_POWER_DEFAULT"]], "ebyte_e32.t30": [[0, 1, 1, "", "TransmitPower"]], "ebyte_e32.t30.TransmitPower": [[0, 2, 1, "", "TX_POWER_21DBM"], [0, 2, 1, "", "TX_POWER_24DBM"], [0, 2, 1, "", "TX_POWER_27DBM"], [0, 2, 1, "", "TX_POWER_30DBM"], [0, 2, 1, "", "TX_POWER_DEFAULT"]], "ebyte_e32.t33": [[0, 1, 1, "", "TransmitPower"]], "ebyte_e32.t33.TransmitPower": [[0, 2, 1, "", "TX_POWER_24DBM"], [0, 2, 1, "", "TX_POWER_27DBM"], [0, 2, 1, "", "TX_POWER_30DBM"], [0, 2, 1, "", "TX_POWER_33DBM"], [0, 2, 1, "", "TX_POWER_DEFAULT"]]}, "objtypes": {"0": "py:module", "1": "py:class", "2": "py:attribute", "3": "py:data", "4": "py:property", "5": "py:method", "6": "py:function"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "class", "Python class"], "2": ["py", "attribute", "Python attribute"], "3": ["py", "data", "Python data"], "4": ["py", "property", "Python property"], "5": ["py", "method", "Python method"], "6": ["py", "function", "Python function"]}, "titleterms": {"ebyte_e32": 0, "eu433": 0, "t20": 0, "t30": 0, "t33": 0, "configur": [1, 5], "manual": 1, "read": [1, 11], "from": 1, "class": 1, "modul": [1, 8], "instanti": 2, "basic": 2, "complet": 2, "fix": 3, "transmiss": [3, 4], "unicast": 3, "receiv": [3, 4], "monitor": 3, "sender": [3, 4], "broadcast": 3, "transpar": 4, "uart": 5, "baudrat": 5, "pariti": 5, "circuitpython": [6, 7], "ebyt": [6, 7], "e32": [6, 7, 8], "librari": [6, 7], "legal": [6, 7, 11], "preambl": [6, 7, 11], "featur": [6, 7], "limit": [6, 7], "depend": [6, 7], "recommend": [6, 7], "link": [6, 7], "licens": [6, 7], "tabl": 6, "content": 6, "technic": 6, "detail": 6, "exampl": 6, "api": 6, "refer": 6, "indic": 6, "wire": 8, "model": 8, "number": 8, "structur": 8, "specif": 8, "datasheet": 8, "lora": 9, "spread": 9, "factor": 9, "lorawan": 10, "must": 11, "asid": 11, "power": 12, "suppli": 12, "consider": 12}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 8, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx": 57}, "alltitles": {"ebyte_e32": [[0, "ebyte-e32"]], "ebyte_e32.eu433": [[0, "ebyte-e32-eu433"]], "ebyte_e32.t20": [[0, "ebyte-e32-t20"]], "ebyte_e32.t30": [[0, "ebyte-e32-t30"]], "ebyte_e32.t33": [[0, "ebyte-e32-t33"]], "Configuration": [[1, "configuration"]], "Manual": [[1, "manual"]], "Reading from class": [[1, "reading-from-class"]], "Reading from module": [[1, "reading-from-module"]], "Instantiation": [[2, "instantiation"]], "Basic": [[2, "basic"]], "Complete": [[2, "complete"]], "Fixed Transmissions": [[3, "fixed-transmissions"]], "Unicast Receiver": [[3, "unicast-receiver"]], "Monitoring Receiver": [[3, "monitoring-receiver"]], "Unicast Sender": [[3, "unicast-sender"]], "Broadcast Sender": [[3, "broadcast-sender"]], "Transparent Transmissions": [[4, "transparent-transmissions"]], "Receiver": [[4, "receiver"]], "Sender": [[4, "sender"]], "UART Configuration": [[5, "uart-configuration"]], "Baudrate": [[5, "baudrate"]], "Parity": [[5, "parity"]], "CircuitPython Ebyte E32 Library": [[6, "circuitpython-ebyte-e32-library"], [7, "circuitpython-ebyte-e32-library"]], "Legal Preamble": [[6, "legal-preamble"], [7, "legal-preamble"]], "Features": [[6, "features"], [7, "features"]], "Limitations": [[6, "limitations"], [7, "limitations"]], "Dependencies": [[6, "dependencies"], [7, "dependencies"]], "Recommended Links": [[6, "recommended-links"], [7, "recommended-links"]], "License": [[6, "license"], [7, "license"]], "Table of Contents": [[6, "table-of-contents"]], "Technical Details": [[6, null]], "Examples": [[6, null]], "API Reference": [[6, null]], "Indices and tables": [[6, "indices-and-tables"]], "E32 Modules": [[8, "e32-modules"]], "Wiring": [[8, "wiring"]], "Model Number Structure": [[8, "model-number-structure"]], "Modules specifications": [[8, "modules-specifications"]], "Datasheets": [[8, "datasheets"]], "LoRa": [[9, "lora"]], "Spreading Factor": [[9, "spreading-factor"]], "LoRaWAN": [[10, "lorawan"]], "Preamble  \u26a0\ufe0f Must-read \u26a0\ufe0f": [[11, "preamble-must-read"]], "Legal Aside": [[11, "legal-aside"]], "Power-supply Considerations": [[12, "power-supply-considerations"]]}, "indexentries": {"airdatarate (class in ebyte_e32)": [[0, "ebyte_e32.AirDataRate"]], "baud_115200 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_115200"]], "baud_1200 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_1200"]], "baud_19200 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_19200"]], "baud_2400 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_2400"]], "baud_38400 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_38400"]], "baud_4800 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_4800"]], "baud_57600 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_57600"]], "baud_9600 (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_9600"]], "baud_default (ebyte_e32.serialbaudrate attribute)": [[0, "ebyte_e32.SerialBaudRate.BAUD_DEFAULT"]], "channel_max (in module ebyte_e32)": [[0, "ebyte_e32.CHANNEL_MAX"]], "channel_min (in module ebyte_e32)": [[0, "ebyte_e32.CHANNEL_MIN"]], "drive_default (ebyte_e32.iodrivemode attribute)": [[0, "ebyte_e32.IODriveMode.DRIVE_DEFAULT"]], "drive_open (ebyte_e32.iodrivemode attribute)": [[0, "ebyte_e32.IODriveMode.DRIVE_OPEN"]], "drive_pull (ebyte_e32.iodrivemode attribute)": [[0, "ebyte_e32.IODriveMode.DRIVE_PULL"]], "e32device (class in ebyte_e32)": [[0, "ebyte_e32.E32Device"]], "e32deviceconfig (class in ebyte_e32)": [[0, "ebyte_e32.E32DeviceConfig"]], "e32deviceversion (class in ebyte_e32)": [[0, "ebyte_e32.E32DeviceVersion"]], "fec_default (ebyte_e32.forwarderrorcorrection attribute)": [[0, "ebyte_e32.ForwardErrorCorrection.FEC_DEFAULT"]], "fec_disabled (ebyte_e32.forwarderrorcorrection attribute)": [[0, "ebyte_e32.ForwardErrorCorrection.FEC_DISABLED"]], "fec_enable (ebyte_e32.forwarderrorcorrection attribute)": [[0, "ebyte_e32.ForwardErrorCorrection.FEC_ENABLE"]], "frequency_maximum (in module ebyte_e32.eu433)": [[0, "ebyte_e32.eu433.FREQUENCY_MAXIMUM"]], "frequency_minimum (in module ebyte_e32.eu433)": [[0, "ebyte_e32.eu433.FREQUENCY_MINIMUM"]], "forwarderrorcorrection (class in ebyte_e32)": [[0, "ebyte_e32.ForwardErrorCorrection"]], "iodrivemode (class in ebyte_e32)": [[0, "ebyte_e32.IODriveMode"]], "mode_normal (ebyte_e32.modes attribute)": [[0, "ebyte_e32.Modes.MODE_NORMAL"]], "mode_power_save (ebyte_e32.modes attribute)": [[0, "ebyte_e32.Modes.MODE_POWER_SAVE"]], "mode_sleep (ebyte_e32.modes attribute)": [[0, "ebyte_e32.Modes.MODE_SLEEP"]], "mode_wake_up (ebyte_e32.modes attribute)": [[0, "ebyte_e32.Modes.MODE_WAKE_UP"]], "modes (class in ebyte_e32)": [[0, "ebyte_e32.Modes"]], "parity_default (ebyte_e32.serialparity attribute)": [[0, "ebyte_e32.SerialParity.PARITY_DEFAULT"]], "parity_even (ebyte_e32.serialparity attribute)": [[0, "ebyte_e32.SerialParity.PARITY_EVEN"]], "parity_none (ebyte_e32.serialparity attribute)": [[0, "ebyte_e32.SerialParity.PARITY_NONE"]], "parity_odd (ebyte_e32.serialparity attribute)": [[0, "ebyte_e32.SerialParity.PARITY_ODD"]], "rate_0_3k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_0_3K"]], "rate_19_2k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_19_2K"]], "rate_1_2k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_1_2K"]], "rate_2_4k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_2_4K"]], "rate_4_8k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_4_8K"]], "rate_9_6k (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_9_6K"]], "rate_default (ebyte_e32.airdatarate attribute)": [[0, "ebyte_e32.AirDataRate.RATE_DEFAULT"]], "serialbaudrate (class in ebyte_e32)": [[0, "ebyte_e32.SerialBaudRate"]], "serialparity (class in ebyte_e32)": [[0, "ebyte_e32.SerialParity"]], "transmission_default (ebyte_e32.transmissionmode attribute)": [[0, "ebyte_e32.TransmissionMode.TRANSMISSION_DEFAULT"]], "transmission_fixed (ebyte_e32.transmissionmode attribute)": [[0, "ebyte_e32.TransmissionMode.TRANSMISSION_FIXED"]], "transmission_transparent (ebyte_e32.transmissionmode attribute)": [[0, "ebyte_e32.TransmissionMode.TRANSMISSION_TRANSPARENT"]], "tx_power_10dbm (ebyte_e32.t20.transmitpower attribute)": [[0, "ebyte_e32.t20.TransmitPower.TX_POWER_10DBM"]], "tx_power_14dbm (ebyte_e32.t20.transmitpower attribute)": [[0, "ebyte_e32.t20.TransmitPower.TX_POWER_14DBM"]], "tx_power_17dbm (ebyte_e32.t20.transmitpower attribute)": [[0, "ebyte_e32.t20.TransmitPower.TX_POWER_17DBM"]], "tx_power_20dbm (ebyte_e32.t20.transmitpower attribute)": [[0, "ebyte_e32.t20.TransmitPower.TX_POWER_20DBM"]], "tx_power_21dbm (ebyte_e32.t30.transmitpower attribute)": [[0, "ebyte_e32.t30.TransmitPower.TX_POWER_21DBM"]], "tx_power_24dbm (ebyte_e32.t30.transmitpower attribute)": [[0, "ebyte_e32.t30.TransmitPower.TX_POWER_24DBM"]], "tx_power_24dbm (ebyte_e32.t33.transmitpower attribute)": [[0, "ebyte_e32.t33.TransmitPower.TX_POWER_24DBM"]], "tx_power_27dbm (ebyte_e32.t30.transmitpower attribute)": [[0, "ebyte_e32.t30.TransmitPower.TX_POWER_27DBM"]], "tx_power_27dbm (ebyte_e32.t33.transmitpower attribute)": [[0, "ebyte_e32.t33.TransmitPower.TX_POWER_27DBM"]], "tx_power_30dbm (ebyte_e32.t30.transmitpower attribute)": [[0, "ebyte_e32.t30.TransmitPower.TX_POWER_30DBM"]], "tx_power_30dbm (ebyte_e32.t33.transmitpower attribute)": [[0, "ebyte_e32.t33.TransmitPower.TX_POWER_30DBM"]], "tx_power_33dbm (ebyte_e32.t33.transmitpower attribute)": [[0, "ebyte_e32.t33.TransmitPower.TX_POWER_33DBM"]], "tx_power_default (ebyte_e32.t20.transmitpower attribute)": [[0, "ebyte_e32.t20.TransmitPower.TX_POWER_DEFAULT"]], "tx_power_default (ebyte_e32.t30.transmitpower attribute)": [[0, "ebyte_e32.t30.TransmitPower.TX_POWER_DEFAULT"]], "tx_power_default (ebyte_e32.t33.transmitpower attribute)": [[0, "ebyte_e32.t33.TransmitPower.TX_POWER_DEFAULT"]], "tx_power_max (in module ebyte_e32)": [[0, "ebyte_e32.TX_POWER_MAX"]], "tx_power_min (in module ebyte_e32)": [[0, "ebyte_e32.TX_POWER_MIN"]], "transmissionmode (class in ebyte_e32)": [[0, "ebyte_e32.TransmissionMode"]], "transmitpower (class in ebyte_e32.t20)": [[0, "ebyte_e32.t20.TransmitPower"]], "transmitpower (class in ebyte_e32.t30)": [[0, "ebyte_e32.t30.TransmitPower"]], "transmitpower (class in ebyte_e32.t33)": [[0, "ebyte_e32.t33.TransmitPower"]], "wake_time_1000ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_1000MS"]], "wake_time_1250ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_1250MS"]], "wake_time_1500ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_1500MS"]], "wake_time_1750ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_1750MS"]], "wake_time_2000ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_2000MS"]], "wake_time_250ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_250MS"]], "wake_time_500ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_500MS"]], "wake_time_750ms (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_750MS"]], "wake_time_default (ebyte_e32.wakeuptime attribute)": [[0, "ebyte_e32.WakeUpTime.WAKE_TIME_DEFAULT"]], "wakeuptime (class in ebyte_e32)": [[0, "ebyte_e32.WakeUpTime"]], "address (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.address"]], "address (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.address"]], "aux (ebyte_e32.e32device attribute)": [[0, "ebyte_e32.E32Device.aux"]], "channel (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.channel"]], "channel (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.channel"]], "channel_to_frequency() (in module ebyte_e32.eu433)": [[0, "ebyte_e32.eu433.channel_to_frequency"]], "data_rate (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.data_rate"]], "data_rate (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.data_rate"]], "deinit() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.deinit"]], "ebyte_e32": [[0, "module-ebyte_e32"]], "ebyte_e32.eu433": [[0, "module-ebyte_e32.eu433"]], "ebyte_e32.t20": [[0, "module-ebyte_e32.t20"]], "ebyte_e32.t30": [[0, "module-ebyte_e32.t30"]], "ebyte_e32.t33": [[0, "module-ebyte_e32.t33"]], "features (ebyte_e32.e32deviceversion attribute)": [[0, "ebyte_e32.E32DeviceVersion.features"]], "flush_uart() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.flush_uart"]], "forward_error_correction (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.forward_error_correction"]], "forward_error_correction (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.forward_error_correction"]], "frequency_to_channel() (in module ebyte_e32.eu433)": [[0, "ebyte_e32.eu433.frequency_to_channel"]], "get_config() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.get_config"]], "get_raw_config() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.get_raw_config"]], "get_raw_version() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.get_raw_version"]], "get_version() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.get_version"]], "io_drive_mode (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.io_drive_mode"]], "io_drive_mode (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.io_drive_mode"]], "mode (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.mode"]], "model (ebyte_e32.e32deviceversion attribute)": [[0, "ebyte_e32.E32DeviceVersion.model"]], "module": [[0, "module-ebyte_e32"], [0, "module-ebyte_e32.eu433"], [0, "module-ebyte_e32.t20"], [0, "module-ebyte_e32.t30"], [0, "module-ebyte_e32.t33"]], "prepare_uart() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.prepare_uart"]], "reset() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.reset"]], "send_raw() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.send_raw"]], "tx_mode (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.tx_mode"]], "tx_mode (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.tx_mode"]], "tx_power (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.tx_power"]], "tx_power (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.tx_power"]], "uart (ebyte_e32.e32device attribute)": [[0, "ebyte_e32.E32Device.uart"]], "uart_parity (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.uart_parity"]], "uart_parity (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.uart_parity"]], "uart_rate (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.uart_rate"]], "uart_rate (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.uart_rate"]], "update_config() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.update_config"]], "version (ebyte_e32.e32deviceversion attribute)": [[0, "ebyte_e32.E32DeviceVersion.version"]], "wait_aux() (ebyte_e32.e32device method)": [[0, "ebyte_e32.E32Device.wait_aux"]], "wake_up_time (ebyte_e32.e32device property)": [[0, "ebyte_e32.E32Device.wake_up_time"]], "wake_up_time (ebyte_e32.e32deviceconfig attribute)": [[0, "ebyte_e32.E32DeviceConfig.wake_up_time"]]}})