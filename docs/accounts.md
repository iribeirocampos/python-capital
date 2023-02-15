Accounts
=================


Read more about their specifics in the [Accounts](https://open-api.capital.com/#tag/Accounts)
section of the official API.


## [Returns all accounts](https://open-api.capital.com/#tag/Accounts/paths/~1api~1v1~1accounts/get)

Returns a list of accounts belonging to the logged-in client


```python
    client.all_accounts()
```


<details><summary>JSON response</summary>
<p>


```yaml
{
  "accounts": [
    {
      "accountId": "12345678901234567",
      "accountName": "USD",
      "status": "ENABLED",
      "accountType": "CFD",
      "preferred": true,
      "balance": {
        "balance": 124.95,
        "deposit": 125.18,
        "profitLoss": -0.23,
        "available": 116.93
      },
      "currency": "USD"
    },
  ]
}
```
</p>
</details>

## [Returns account preferences](https://open-api.capital.com/#tag/Accounts/paths/~1api~1v1~1accounts~1preferences/get)

Returns account preferences, i.e. leverage settings and trading mode

```python
    client.account_pref()
```

<details><summary>JSON response</summary>
<p>


```yaml
{
   "hedgingMode": false,
   "leverages": {
      "SHARES": {
         "current": 2,
         "available": [
            1,
            2,
            3,
            5
         ]
      },
      "CURRENCIES": {
         "current": 1,
         "available": [
            1,
            10,
            20,
            30
         ]
      },
      "INDICES": {
         "current": 10,
         "available": [
            1,
            10,
            20
         ]
      },
      "CRYPTOCURRENCIES": {
         "current": 1,
         "available": [
            1,
            2
         ]
      },
      "COMMODITIES": {
         "current": 5,
         "available": [
            1,
            5,
            10,
            20
         ]
      }
   }
}
```
</p>
</details>

## [Updates account preferences](https://open-api.capital.com/#tag/Accounts/paths/~1api~1v1~1accounts~1preferences/put)

Update account preferences

Both parameters are optional, hedging_mode default is False and default leverages are below. 


<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|leverages|json object|NO|Set new leverage values
|hedging_mode|boolean|NO|Enable or disable hedging mode

```python
    client.update_account_pref(leverages, hedging_mode)
```


<details><summary>JSON payload</summary>
<p>

```yaml
{
  "leverages": {
    "SHARES": 5,
    "INDICES": 20,
    "CRYPTOCURRENCIES": 2,
  }
}
```
</p>
</details>
