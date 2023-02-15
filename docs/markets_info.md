Markets Info
=================


Read more about their specifics in the [Markets Info](https://open-api.capital.com/#tag/Markets-Info-greater-Markets)
section of the official API.


## [All top-level market categories](https://open-api.capital.com/#tag/Markets-Info-greater-Markets/paths/~1api~1v1~1marketnavigation/get)

Returns all top-level nodes (market categories) in the market navigation hierarchy

```python
    client.all_top()
```

<details><summary>JSON response</summary>
<p>


```yaml
{
  "nodes": [
    {
      "id": "hierarchy_v1.commons_group",
      "name": "commons_group"
    },
    {
      "id": "hierarchy_v1.commodities_group",
      "name": "commodities_group"
    },
    {
      "id": "hierarchy_v1.oil_markets_group",
      "name": "oil_markets_group"
    }
  ]
}
```
</p>
</details>

## [All category sub-nodes](https://open-api.capital.com/#tag/Markets-Info-greater-Markets/paths/~1api~1v1~1marketnavigation~1%7BnodeId%7D/get)

Returns all sub-nodes (markets) of the given node (market category) in the market navigation hierarchy

<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|node_id|string|YES|Identifier of the node to browse

```python
    client.all_top_sub(node_id)
```

<details><summary>JSON response</summary>
<p>


```yaml
example for node_id = "hierarchy_v1.commons_group"
{
  "nodes": [
    {
      "id": "hierarchy_v1.commons.most_traded",
      "name": "Most Traded"
    },
    {
      "id": "hierarchy_v1.commons.recently_traded",
      "name": "Recently Traded"
    },
    {
      "id": "hierarchy_v1.commons.new",
      "name": "New"
    },
    {
      "id": "hierarchy_v1.commons.top_gainers",
      "name": "Top Risers"
    },
    {
      "id": "hierarchy_v1.commons.top_losers",
      "name": "Top Fallers"
    },
    {
      "id": "hierarchy_v1.commons.most_volatile",
      "name": "Most Volatile"
    },
    {
      "id": "hierarchy_v1.commons.weekend_trading",
      "name": "Weekend Trading"
    }
  ]
}
```
</p>
</details>

## [Markets details](https://open-api.capital.com/#tag/Markets-Info-greater-Markets/paths/~1api~1v1~1markets/get)

Returns the details of the given markets
Request should include one of the query parameters: searchTerm or epics
example: market = "silver"
<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|market|string|YES|The term to be used in the search. 
|     |       |   |Example: market = "silver"
```python
    client.market_details(market)
```

<details><summary>JSON response</summary>
<p>

```yaml
{
  "markets": [
    {
      "delayTime": 0,
      "epic": "SILVER",
      "netChange": -0.219,
      "lotSize": 1,
      "expiry": "-",
      "instrumentType": "COMMODITIES",
      "instrumentName": "Silver",
      "high": 24.405,
      "low": 24.119,
      "percentageChange": -0.8929,
      "updateTime": "2022-04-06T15:17:38.477",
      "updateTimeUTC": "2022-04-06T13:17:38.477",
      "bid": 24.366,
      "offer": 24.386,
      "streamingPricesAvailable": true,
      "marketStatus": "TRADEABLE",
      "scalingFactor": 1
    },
    {
      "delayTime": 0,
      "epic": "5CPSG",
      "netChange": 0.005,
      "lotSize": 1,
      "expiry": "-",
      "instrumentType": "SHARES",
      "instrumentName": "Silverlake Axis",
      "high": 0.318,
      "low": 0.313,
      "percentageChange": 1.5974,
      "updateTime": "2022-04-06T11:00:00.440",
      "updateTimeUTC": "2022-04-06T09:00:00.440",
      "bid": 0.318,
      "offer": 0.327,
      "streamingPricesAvailable": true,
      "marketStatus": "CLOSED",
      "scalingFactor": 1
    },
    {
      "delayTime": 0,
      "epic": "SI",
      "lotSize": 1,
      "expiry": "-",
      "instrumentType": "SHARES",
      "instrumentName": "Silvergate Capital Corporation",
      "updateTime": "2022-04-05T21:59:59.446",
      "updateTimeUTC": "2022-04-05T19:59:59.446",
      "bid": 142.7,
      "offer": 143.67,
      "streamingPricesAvailable": true,
      "marketStatus": "CLOSED",
      "scalingFactor": 1
    }
  ]
}
```

</p>
</details>


## [Single Markets details](https://open-api.capital.com/#tag/Markets-Info-greater-Markets/paths/~1api~1v1~1markets/get)

Returns the details of the given market
<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|epic|string|YES|The epic of the market 
|     |       |   |Example: market = "SILVER"

```python
    client.single_market_details(epic)
```



<details><summary>JSON response</summary>
<p>

```yaml
{
  "instrument": {
    "epic": "SILVER",
    "expiry": "-",
    "name": "Silver",
    "lotSize": 1,
    "type": "COMMODITIES",
    "controlledRiskAllowed": true,
    "streamingPricesAvailable": true,
    "currency": "USD",
    "marginFactor": 10,
    "marginFactorUnit": "PERCENTAGE",
    "openingHours": {
      "mon": [
        "00:00 - 22:00",
        "23:05 - 00:00"
      ],
      "tue": [
        "00:00 - 22:00",
        "23:05 - 00:00"
      ],
      "wed": [
        "00:00 - 22:00",
        "23:05 - 00:00"
      ],
      "thu": [
        "00:00 - 22:00",
        "23:05 - 00:00"
      ],
      "fri": [
        "00:00 - 22:00"
      ],
      "sat": [],
      "sun": [
        "23:05 - 00:00"
      ],
      "zone": "UTC"
    },
    "country": ""
  },
  "dealingRules": {
    "minStepDistance": {
      "unit": "POINTS",
      "value": 0.001
    },
    "minDealSize": {
      "unit": "POINTS",
      "value": 0.1
    },
    "minControlledRiskStopDistance": {
      "unit": "PERCENTAGE",
      "value": 2
    },
    "minNormalStopOrLimitDistance": {
      "unit": "PERCENTAGE",
      "value": 0.01
    },
    "maxStopOrLimitDistance": {
      "unit": "PERCENTAGE",
      "value": 60
    },
    "marketOrderPreference": "AVAILABLE_DEFAULT_ON",
    "trailingStopsPreference": "NOT_AVAILABLE"
  },
  "snapshot": {
    "marketStatus": "TRADEABLE",
    "netChange": -0.313,
    "percentageChange": -1.2762,
    "updateTime": "2022-04-06T13:17:42.113",
    "delayTime": 0,
    "bid": 24.203,
    "offer": 24.223,
    "high": 24.405,
    "low": 24.193,
    "decimalPlacesFactor": 3,
    "scalingFactor": 1
  }
}
```
</p>
</details>


## [Historical prices](https://open-api.capital.com/#tag/Markets-Info-greater-Prices/paths/~1api~1v1~1prices~1%7Bepic%7D/get)

Returns historical prices for a particular instrument

By default returns the minute prices within the last 10 minutes

<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|epic|string|YES|The epic of the market 
|     |       |   |Example: market = "SILVER"
|resolution|string|NO|Defines the resolution of requested prices. Possible values are MINUTE, MINUTE_5, MINUTE_15, MINUTE_30, HOUR, HOUR_4, DAY, WEEK|
|max|integer|NO |The maximum number of the values in answer. Default = 10, max = 1000|

```python
    client.prices(epic)
```



<details><summary>JSON response</summary>
<p>

```yaml
{
  "prices": [
    {
      "snapshotTime": "2022-04-06T15:18:00",
      "snapshotTimeUTC": "2022-04-06T13:18:00",
      "openPrice": {
        "bid": 24.356,
        "ask": 24.376
      },
      "closePrice": {
        "bid": 24.378,
        "ask": 24.398
      },
      "highPrice": {
        "bid": 24.378,
        "ask": 24.398
      },
      "lowPrice": {
        "bid": 24.355,
        "ask": 24.375
      },
      "lastTradedVolume": 187
    },
    {
      "snapshotTime": "2022-04-06T15:19:00",
      "snapshotTimeUTC": "2022-04-06T13:19:00",
      "openPrice": {
        "bid": 24.379,
        "ask": 24.399
      },
      "closePrice": {
        "bid": 24.379,
        "ask": 24.399
      },
      "highPrice": {
        "bid": 24.389,
        "ask": 24.409
      },
      "lowPrice": {
        "bid": 24.373,
        "ask": 24.393
      },
      "lastTradedVolume": 168
    },
    {
      "snapshotTime": "2022-04-06T15:20:00",
      "snapshotTimeUTC": "2022-04-06T13:20:00",
      "openPrice": {
        "bid": 24.378,
        "ask": 24.398
      },
      "closePrice": {
        "bid": 24.4,
        "ask": 24.42
      },
      "highPrice": {
        "bid": 24.4,
        "ask": 24.42
      },
      "lowPrice": {
        "bid": 24.375,
        "ask": 24.395
      },
      "lastTradedVolume": 183
    },
    {
      "snapshotTime": "2022-04-06T15:21:00",
      "snapshotTimeUTC": "2022-04-06T13:21:00",
      "openPrice": {
        "bid": 24.399,
        "ask": 24.419
      },
      "closePrice": {
        "bid": 24.395,
        "ask": 24.415
      },
      "highPrice": {
        "bid": 24.405,
        "ask": 24.425
      },
      "lowPrice": {
        "bid": 24.388,
        "ask": 24.408
      },
      "lastTradedVolume": 196
    },
    {
      "snapshotTime": "2022-04-06T15:22:00",
      "snapshotTimeUTC": "2022-04-06T13:22:00",
      "openPrice": {
        "bid": 24.394,
        "ask": 24.414
      },
      "closePrice": {
        "bid": 24.399,
        "ask": 24.419
      },
      "highPrice": {
        "bid": 24.4,
        "ask": 24.42
      },
      "lowPrice": {
        "bid": 24.383,
        "ask": 24.403
      },
      "lastTradedVolume": 171
    },
    {
      "snapshotTime": "2022-04-06T15:23:00",
      "snapshotTimeUTC": "2022-04-06T13:23:00",
      "openPrice": {
        "bid": 24.398,
        "ask": 24.418
      },
      "closePrice": {
        "bid": 24.381,
        "ask": 24.401
      },
      "highPrice": {
        "bid": 24.405,
        "ask": 24.425
      },
      "lowPrice": {
        "bid": 24.38,
        "ask": 24.4
      },
      "lastTradedVolume": 161
    },
    {
      "snapshotTime": "2022-04-06T15:24:00",
      "snapshotTimeUTC": "2022-04-06T13:24:00",
      "openPrice": {
        "bid": 24.38,
        "ask": 24.4
      },
      "closePrice": {
        "bid": 24.387,
        "ask": 24.407
      },
      "highPrice": {
        "bid": 24.399,
        "ask": 24.419
      },
      "lowPrice": {
        "bid": 24.38,
        "ask": 24.4
      },
      "lastTradedVolume": 155
    },
    {
      "snapshotTime": "2022-04-06T15:25:00",
      "snapshotTimeUTC": "2022-04-06T13:25:00",
      "openPrice": {
        "bid": 24.388,
        "ask": 24.408
      },
      "closePrice": {
        "bid": 24.389,
        "ask": 24.409
      },
      "highPrice": {
        "bid": 24.393,
        "ask": 24.413
      },
      "lowPrice": {
        "bid": 24.384,
        "ask": 24.404
      },
      "lastTradedVolume": 118
    },
    {
      "snapshotTime": "2022-04-06T15:26:00",
      "snapshotTimeUTC": "2022-04-06T13:26:00",
      "openPrice": {
        "bid": 24.389,
        "ask": 24.409
      },
      "closePrice": {
        "bid": 24.373,
        "ask": 24.393
      },
      "highPrice": {
        "bid": 24.39,
        "ask": 24.41
      },
      "lowPrice": {
        "bid": 24.37,
        "ask": 24.39
      },
      "lastTradedVolume": 143
    },
    {
      "snapshotTime": "2022-04-06T15:27:00",
      "snapshotTimeUTC": "2022-04-06T13:27:00",
      "openPrice": {
        "bid": 24.372,
        "ask": 24.392
      },
      "closePrice": {
        "bid": 24.375,
        "ask": 24.395
      },
      "highPrice": {
        "bid": 24.376,
        "ask": 24.396
      },
      "lowPrice": {
        "bid": 24.371,
        "ask": 24.391
      },
      "lastTradedVolume": 44
    }
  ],
  "instrumentType": "COMMODITIES"
}
```
</p>
</details>


## [Client sentiment for market](https://open-api.capital.com/#tag/Markets-Info-greater-Client-Sentiment/paths/~1api~1v1~1clientsentiment~1%7BmarketId%7D/get)

Returns the client sentiment for the given market

<strong>Parameters</strong>
|Parameter|	Format|	Required?|	Description|
|---|---|---|---|
|market_id|string|YES|Market identifier


```python
    client.client_sentiment(market_id)
```

<details><summary>JSON response</summary>
<p>

```yaml
{
  "marketId": "SILVER",
  "longPositionPercentage": 91.85,
  "shortPositionPercentage": 8.15
}

```
</p>
</details>