Trading
=================

# Positions 

Read more about their specifics in the [Positions](https://open-api.capital.com/#tag/Trading-greater-Rositions)
section of the official API.


## [All Positions](https://open-api.capital.com/#tag/Trading-greater-Rositions)

Returns all open positions for the active account

```python
    client.all_positions()
```

<details><summary>JSON response</summary>
<p>


```yaml
{
  "positions": [
    {
      "position": {
        "contractSize": 1,
        "createdDate": "2022-04-05T12:46:01.872",
        "createdDateUTC": "2022-04-05T09:46:01.872",
        "dealId": "00018387-0001-54c4-0000-000080560014",
        "dealReference": "p_00018387-0001-54c4-0000-000080560014",
        "size": 1,
        "direction": "BUY",
        "level": 5.911,
        "currency": "USD",
        "guaranteedStop": false
      },
      "market": {
        "instrumentName": "Natural Gas",
        "expiry": "-",
        "marketStatus": "TRADEABLE",
        "epic": "NATURALGAS",
        "instrumentType": "COMMODITIES",
        "lotSize": 1000,
        "high": 6.192,
        "low": 5.799,
        "percentageChange": 6.7351,
        "netChange": 0.387,
        "bid": 6.114,
        "offer": 6.12,
        "updateTime": "2022-04-05T17:41:38.492",
        "updateTimeUTC": "2022-04-05T14:41:38.492",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1
      }
    },
    {
      "position": {
        "contractSize": 1,
        "createdDate": "2022-04-05T12:46:10.139",
        "createdDateUTC": "2022-04-05T09:46:10.139",
        "dealId": "004d0627-0001-54c4-0000-000080560017",
        "dealReference": "p_004d0627-0001-54c4-0000-000080560017",
        "size": 1,
        "direction": "BUY",
        "level": 4577.6,
        "currency": "USD",
        "controlledRisk": false
      },
      "market": {
        "instrumentName": "S&P 500",
        "expiry": "2022-02-01",
        "marketStatus": "TRADEABLE",
        "epic": "US500",
        "instrumentType": "INDICES",
        "lotSize": 1,
        "high": 4596.5,
        "low": 4556.7,
        "percentageChange": 0.2881,
        "netChange": 13.1,
        "bid": 4559.7,
        "offer": 4560.3,
        "updateTime": "2022-04-05T17:41:37.991",
        "updateTimeUTC": "2022-04-05T14:41:37.991",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1
      }
    }
  ]
}
```
</p>
</details>

## [Create Position](https://open-api.capital.com/#tag/Trading-greater-Rositions/paths/~1api~1v1~1positions/post)

Creates and confirms the position an returns a json object

<details><summary><strong>Parameters:</strong></summary>
<p>

|Parameter	|Format	|Required?	|Description|
|---|---|---|---|
|direction	|string|YES	|Deal direction: Must be BUY or SELL|
|epic	|string	|YES	|Instrument epic identifier|
|size	|number	|YES	|Deal size
|guaranteed_stop	|boolean	|NO	|Must be true if a guaranteed stop is required|
|               |           |   |  Notes:|
|               |           |   |  - Default value: false|
|               |           |   |  - If guaranteedStop equals true, then set stopLevel, stopDistance or stopAmount|
|               |           |   |  - Cannot be set if trailingStop is true|
|               |           |   |  - Cannot be set if hedgingMode is true|
|trailing_stop	|boolean	|NO	|Must be true if a trailing stop is required|
|               |           |   |  Notes:|
|               |           |   |   - Default value: false|
|               |           |   |   - If trailingStop equals true, then set stopDistance|
|               |           |   |   - Cannot be set if guaranteedStop is true|
|stop_level	|number	|NO	|Price level when a stop loss will be triggered|
|stop_distance	|number	|NO	|Distance between current and stop loss triggering price|
|               |       |   | Notes:|
|               |       |   | - Required parameter if trailingStop is true|
|stop_amount	|number	|NO	|Loss amount when a stop loss will be triggered|
|profit_level	|number	|NO	|Price level when a take profit will be triggered|
|profit_distance	|number	|NO	|Distance between current and take profit triggering price|
|profit_amount	|number	|NO	|Profit amount when a take profit will be triggered|

</p>
</details>

```python
    client.create_position(epic, direction, size)
```

<details><summary>JSON response</summary>
<p>


```yaml
{'date': '2023-02-15T11:24:36.310', 'status': 'OPEN', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'o_22b5ad89-bfb0-4a2d-9f3e-5c6581d1a84b', 'dealId': '00513301-0055-311e-0000-0000806e2b0f', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b11', 'status': 'OPENED'}], 'level': 0, 'size': 1.0, 'direction': 'SELL', 'guaranteedStop': False, 'trailingStop': False}
```
</p>
</details>

## [Update Position](https://open-api.capital.com/#tag/Trading-greater-Rositions/paths/~1api~1v1~1positions~1%7BdealId%7D/put)

Updates a certain position

<details><summary><strong>Parameters:</strong></summary>
<p>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|guaranteedStop|	boolean|	NO	|Must be true if a guaranteed stop is required|
|              |         |      |Notes:|
|              |         |      |- Default value: false|
|              |         |      |- If guaranteedStop equals true, then set stopLevel, stopDistance or stopAmount|
|              |         |      |- Cannot be set if trailingStop is true|
|              |         |      |- Cannot be set if hedgingMode is true|
|trailing_stop	|boolean|	NO|	Must be true if a trailing stop is required|
|             |       |   |Notes:|
|             |       |   |- Default value: false|
|             |       |   |- If trailingStop equals true, then set stopDistance|
|             |       |   |- Cannot be set if guaranteedStop is true|
|stop_level|	number|	NO|	Price level when a stop loss will be triggered|
|stop_distance	|number	|NO	|Distance between current and stop loss triggering price|
|             |       |   |Notes:|
|             |       |   |- Required parameter if trailingStop is true|
|stop_amount|	number|	NO	|Loss amount when a stop loss will be triggered|
|profit_level|	number|	NO|	Price level when a take profit will be triggered|
|profit_distance	|number	|NO	|Distance between current and take profit triggering price|
|profit_amount	|number|	NO	|Profit amount when a take profit will be triggered|
</p>
</details>



```python
    client.update_position(deal_id)
```

<details><summary>JSON response</summary>
<p>

```yaml
{'date': '2023-02-15T11:27:46.336', 'status': 'AMENDED', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'p_00513301-0055-311e-0000-0000806e2b11', 'dealId': '00513301-0055-311e-0000-0000806e2b11', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b11', 'status': 'AMENDED'}], 'level': 210.51, 'size': 1.0, 'direction': 'SELL', 'guaranteedStop': False, 'trailingStop': False, 'profitCurrency': 'USD'}
```

</p>
</details>


## [Close Position](https://open-api.capital.com/#tag/Trading-greater-Rositions/paths/~1api~1v1~1positions~1%7BdealId%7D/put)

Closes a certain position

<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|deal_id|string|YES|Permanent deal reference for a confirmed trade

```python
    client.close_position(deal_id)
```

<details><summary>JSON response</summary>
<p>

```yaml
{'date': '2023-02-15T11:32:17.310', 'status': 'CLOSED', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'p_00513301-0055-311e-0000-0000806e2b4c', 'dealId': '00513301-0055-311e-0000-0000806e2b4c', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b4c', 'status': 'FULLY_CLOSED'}], 'level': 210.4, 'size': 1.0, 'direction': 'BUY', 'guaranteedStop': False, 'trailingStop': False, 'profit': 
-0.13, 'profitCurrency': 'USD'}
```
</p>
</details>


# Working Orders

Read more about their specifics in the [Orders](https://open-api.capital.com/#tag/Trading-greater-Orders)
section of the official API.


## [All Working Orders](https://open-api.capital.com/#tag/Trading-greater-Orders/paths/~1api~1v1~1workingorders/get)

Returns all open working orders for the active account

```python
    client.all_working_orders()
```

<details><summary>JSON response</summary>
<p>


```yaml
{
  "workingOrders": [
    {
      "workingOrderData": {
        "dealId": "006011e7-0001-54c4-0000-000080560078",
        "direction": "BUY",
        "epic": "SILVER",
        "orderSize": 1,
        "orderLevel": 20,
        "timeInForce": "GOOD_TILL_DATE",
        "goodTillDate": "2022-06-09T04:01:00.000",
        "goodTillDateUTC": "2022-06-09T01:01:00.000",
        "createdDate": "2022-04-06T12:48:28.114",
        "createdDateUTC": "2022-04-06T09:48:28.114",
        "guaranteedStop": true,
        "orderType": "LIMIT",
        "stopDistance": -3,
        "profitDistance": 3,
        "currencyCode": "USD"
      },
      "marketData": {
        "instrumentName": "Silver",
        "expiry": "-",
        "marketStatus": "TRADEABLE",
        "epic": "SILVER",
        "instrumentType": "COMMODITIES",
        "lotSize": 50,
        "high": 24.398,
        "low": 24.193,
        "percentageChange": -0.6198,
        "netChange": -0.152,
        "bid": 24.387,
        "offer": 24.407,
        "updateTime": "2022-04-06T12:48:31.587",
        "updateTimeUTC": "2022-04-06T09:48:31.587",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1
      }
    },
    {
      "workingOrderData": {
        "dealId": "00018387-0001-54c4-0000-000080560019",
        "direction": "BUY",
        "epic": "NATURALGAS",
        "orderSize": 1,
        "orderLevel": 6,
        "timeInForce": "GOOD_TILL_CANCELLED",
        "createdDate": "2022-04-06T12:13:46.571",
        "createdDateUTC": "2022-04-06T09:13:46.571",
        "guaranteedStop": false,
        "orderType": "LIMIT",
        "currencyCode": "USD"
      },
      "marketData": {
        "instrumentName": "Natural Gas",
        "expiry": "-",
        "marketStatus": "TRADEABLE",
        "epic": "NATURALGAS",
        "instrumentType": "COMMODITIES",
        "lotSize": 1000,
        "high": 6.194,
        "low": 6.073,
        "percentageChange": 6.4472,
        "netChange": 0.374,
        "bid": 6.185,
        "offer": 6.195,
        "updateTime": "2022-04-06T12:48:24.795",
        "updateTimeUTC": "2022-04-06T09:48:24.795",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1
      }
    }
  ]
}
```
</p>
</details>

## [Create order](https://open-api.capital.com/#tag/Trading-greater-Orders/paths/~1api~1v1~1workingorders/post)

Create a limit or stop order

<details><summary><strong>Parameters:</strong></summary>
<p>

|Parameter	|Format	|Required?	|Description|
|---|---|---|---|
|direction	|string|YES	|Deal direction: Must be BUY or SELL|
|epic	|string	|YES	|Instrument epic identifier|
|size	|number	|YES	|Deal size|
|level|number|YES|Order Price|
|type|string|YES| Order Type: Must be LIMIT or STOP
|guaranteedStop	|boolean	|NO	|Must be true if a guaranteed stop is required|
|               |           |   |  Notes:|
|               |           |   |  - Default value: false|
|               |           |   |  - If guaranteedStop equals true, then set stopLevel, stopDistance or stopAmount|
|               |           |   |  - Cannot be set if trailingStop is true|
|               |           |   |  - Cannot be set if hedgingMode is true|
|trailing_stop	|boolean	|NO	|Must be true if a trailing stop is required|
|               |           |   |  Notes:|
|               |           |   |   - Default value: false|
|               |           |   |   - If trailingStop equals true, then set stopDistance|
|               |           |   |   - Cannot be set if guaranteedStop is true|
|stop_level	|number	|NO	|Price level when a stop loss will be triggered|
|stop_distance	|number	|NO	|Distance between current and stop loss triggering price|
|               |       |   | Notes:|
|               |       |   | - Required parameter if trailingStop is true|
|stop_amount	|number	|NO	|Loss amount when a stop loss will be triggered|
|profit_level	|number	|NO	|Price level when a take profit will be triggered|
|profit_distance	|number	|NO	|Distance between current and take profit triggering price|
|profit_amount	|number	|NO	|Profit amount when a take profit will be triggered|

</p>
</details>

```python
    client.create_working_order(epic, direction, size, level, type)
```

<details><summary>JSON response</summary>
<p>


```yaml
{'date': '2023-02-15T11:40:37.528', 'status': 'OPEN', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'o_89d1219f-8b28-4475-9845-a2a6ab5eb42d', 'dealId': '00513301-0055-311e-0000-0000806e2b6f', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b6f', 'status': 'OPENED'}], 'level': 180.0, 'size': 1.0, 'direction': 'BUY', 'guaranteedStop': False, 'trailingStop': False}
```
</p>
</details>

## [Update Working order](https://open-api.capital.com/#tag/Trading-greater-Orders/paths/~1api~1v1~1workingorders~1%7BdealId%7D/put)

Updates a certain working order

<details><summary><strong>Parameters:</strong></summary>
<p>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|deal_id|string|YES|Permanent deal reference for an order
|level|number|NO|Order price| 
|guaranteed_stop|	boolean|	NO	|Must be true if a guaranteed stop is required|
|              |         |      |Notes:|
|              |         |      |- Default value: false|
|              |         |      |- If guaranteedStop equals true, then set stopLevel, stopDistance or stopAmount|
|              |         |      |- Cannot be set if trailingStop is true|
|              |         |      |- Cannot be set if hedgingMode is true|
|trailing_stop	|boolean|	NO|	Must be true if a trailing stop is required|
|             |       |   |Notes:|
|             |       |   |- Default value: false|
|             |       |   |- If trailingStop equals true, then set stopDistance|
|             |       |   |- Cannot be set if guaranteedStop is true|
|stop_level|	number|	NO|	Price level when a stop loss will be triggered|
|stop_distance	|number	|NO	|Distance between current and stop loss triggering price|
|             |       |   |Notes:|
|             |       |   |- Required parameter if trailingStop is true|
|stop_amount|	number|	NO	|Loss amount when a stop loss will be triggered|
|profit_level|	number|	NO|	Price level when a take profit will be triggered|
|profit_distance	|number	|NO	|Distance between current and take profit triggering price|
|profit_amount	|number|	NO	|Profit amount when a take profit will be triggered|
</p>
</details>



```python
    client.update_working_order(deal_id)
```

<details><summary>JSON response</summary>
<p>

```yaml
{'date': '2023-02-15T11:40:37.528', 'status': 'OPEN', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'o_89d1219f-8b28-4475-9845-a2a6ab5eb42d', 'dealId': '00513301-0055-311e-0000-0000806e2b6f', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b6f', 'status': 'OPENED'}], 'level': 180.0, 'size': 1.0, 'direction': 'BUY', 'guaranteedStop': False, 'trailingStop': False}
```

</p>
</details>


## [Delete Working order](https://open-api.capital.com/#tag/Trading-greater-Orders/paths/~1api~1v1~1workingorders~1%7BdealId%7D/delete)

Delete a limit or stop order

<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|deal_id|string|YES|Permanent deal reference for a confirmed trade

```python
    client.delete_working_order(deal_id)
```

<details><summary>JSON response</summary>
<p>

```yaml
{'date': '2023-02-15T11:48:23.555', 'status': 'DELETED', 'reason': 'SUCCESS', 'dealStatus': 'ACCEPTED', 'epic': 'TSLA', 'dealReference': 'o_df55c53e-9b62-4b39-ba7d-27753935f244', 'dealId': '00513301-0055-311e-0000-0000806e2b9a', 'affectedDeals': [{'dealId': '00513301-0055-311e-0000-0000806e2b9a', 'status': 'DELETED'}], 'level': 180.0, 'size': 1.0, 'direction': 'BUY', 'guaranteedStop': False, 'trailingStop': False}
```
</p>
</details>