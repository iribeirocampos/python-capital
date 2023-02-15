Create New Session
=================


# Session


With capital.com API we can encrypt users password end-to-end. When creating a new session with python-capital.com automatically encrypts users password.

Read more about their specifics in the [Session](https://open-api.capital.com/#tag/Session)
section of the official API.


## [Create new Session](https://open-api.capital.com/#tag/Session/paths/~1api~1v1~1session/post)


<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|username|string|YES|Client login identifier|
|api_key|string|YES|The API key obtained from Settings > API Integrations page on the Capital.com trading platform|
|api_password|string|YES|The password obtained when creating api_key|
|demo|boolean|NO| Default = False

### Live Account

```python
    from python-capital import Client

    client = Client(username, api_key, api_password)

```

### Demo Account

```python
    from python-capital import Client

    client = Client(username, api_key, api_password, demo=True)
```

