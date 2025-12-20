# Welcome to python-capital v0.2.0

_Updated 19th Dec 2025_

This is an unofficial Python wrapper for the [Capital.com Public API v1](https://open-api.capital.com/).  
I am in no way affiliated with Capital.com, use at your own risk.

If you came here looking for the [Capital.com exchange](https://capital.com/) to invest in CFDs, then [go here](https://capital.com/).  
If you want to automate interactions with Capital.com, stick around.

**Source code:**  
https://github.com/

## Features

- Simple handling of authentication
- Password encryption end-to-end
- Response exception handling
- Positions opening/closing
- Market prices and sentiment

## Quick Start

[Register an account with Capital.com](https://capital.com/).

[Generate an API Key](https://capital.com/trading/platform/?popup=settings&tab=APISettings).

To use the Demo accounts, pass `demo=True` when creating the client (default is set to `False`).

```bash
pip install python-capital.com
```

```python
from capital.client import Client

client = Client(username, api_key, api_password)

# get all open positions
positions = client.all_positions()

# to create a position
order = client.create_position(epic, direction, size)

# to close a position
close = client.close_position(deal_id)
```

