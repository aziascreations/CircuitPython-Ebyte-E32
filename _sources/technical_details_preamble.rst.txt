.. image:: _static/computer_v1_danger_strong.png
   :scale: 50 %
   :alt: Drawing of an old computer with a warning sign shown on its screen.
   :align: right

.. role:: raw-html(raw)
    :format: html

Preamble  ⚠️ Must-read ⚠️
--------------------------
Communications using LoRa can be extremely complicated to properly understand and execute due to a variety of reasons.

This entire `Technical Details` section will aim to explain and clarify some of the specificities that are likely to
impact the way will be programmed and will handle data while using E32 LoRa module.

Here is a small of common issues that will be covered here:

* Wide variety of transmission methods
* Transmission power
* Frequencies used
* Local RF regulations
* Max packet size calculation
* Confusion and conflation of LoRa and LoRaWAN specifications

If you need a simple example to motivate you into ready this section, read the following:

    Depending on the frequencies, region and data rates, **a LoRa packet cannot be larger than 11 bytes** under
    unfavorable conditions, **or 250 bytes** under favorable ones.

You can go to ??? for more information on this limitation.

.. _ref-legal-aside:

Legal Aside
^^^^^^^^^^^
Please keep in mind that I'm only one person writing, researching and synthesizing most of this information.

I am not infallible and especially not professionally versed in all the local regulations and laws that pertain to RF.

These types of laws can be extremely hard to understand and get right due to the fact they not only mix legal lingo,
but also to the fact that the domain they apply to is extremely technical and very easy to get wrong.
:raw-html:`<br>`
If possible, you should refer to a lawyer that is well versed in those domains or at the very least to knowledgeable
people who are licensed to use and operate such equipment.

Do not mess around with RF, if its not the FCC/IBPT/`{Any other RF regulatory body}` that come after you,
its likely gonna be the HAMs.
:raw-html:`<br>`
Both of them are extremely efficient at tracking and finding offending parties if necessary, trust me...
