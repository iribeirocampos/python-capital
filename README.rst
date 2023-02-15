=================================
Welcome to python-capital.com v0.1.0
=================================

Updated 14th Feb 2023


This is an unofficial Python wrapper for the `Capital.com Public API v1 <https://open-api.capital.com/>`_. I am in no way affiliated with Capital.com, use at your own risk.

If you came here looking for the `Capital.com exchange <https://capital.com/>`_ to invest in CFDs, then `go here <https://capital.com/>`_.
If you want to automate interactions with Capital.com stick around.



Source code
  https://github.com/


Features
--------

- Simple handling of authentication
- Password encryption end-to-end
- Response exception handling
- Positions opening/closing
- Market Prices and sentiment


Quick Start
-----------

`Register an account with Capital.com <https://capital.com/>`_.

`Generate an API Key <https://capital.com/trading/platform/?popup=settings&tab=APISettings>`_.

To use the `Demo accounts, pass `demo=True` when creating the client, default is set to False.


.. code:: bash

    pip install python-capital.com


.. code:: python

    from capital.capital_api import Client
    
    client = Client(username, api_key, api_password)

    # get all open possitions
    positions = client.all_positions()

    # to create a position
    order = client.create_position(epic, direction, size)

    # to close a position
    close = client.close_position(deal_id)


Donate
------

If this library helped you out feel free to donate.

- ETH: 0x16b86e034d544bc2e7d5f985fb079d7a7f206471
- BTC: 14iP5aKTJuCCZicUSvLVP3fUKK7awJW1hL

