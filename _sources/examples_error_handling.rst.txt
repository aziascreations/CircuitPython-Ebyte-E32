Error Handling ⚠️ Must-read ⚠️
------------------------------
These examples will show you how to recover from errors returned by the ``E32Device`` class.

Config Changes
^^^^^^^^^^^^^^
If you get an ``E32GenericError`` exception when changing the module's config, you will need to follow this procedure.

**Expected error:**

    ``E32GenericError: The module didn't return the new config !``

**Resolution procedure:**

* Catch error in a ``try except`` block.

* Reset the module via ``E32Device.reset()``.

* Wait some time for it to restart.

* Re-apply the config with ``E32Device.update_config()``.

* Go back into the original mode.

* Retry the code that raised the error

**Warning:**

    Failure to follow the procedure WILL result in a module that no longer applies new operating parameters
    given to it !

.. literalinclude:: ../examples/error_handling.py
    :caption: examples/error_handling.py
    :emphasize-lines: 24-45
    :linenos:
