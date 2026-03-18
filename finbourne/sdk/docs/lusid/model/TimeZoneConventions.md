# TimeZoneConventions

Provides information on the primary time zone of an instrument and optional cut labels  for defining times to be used by instrument events.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **primary_time_zone** | **str** | Required | The IANA time zone code for the instrument. |
| **start_of_day** | **str** | Optional | A LUSID Cut Label code used for generating instrument events at a time other than local midnight. |
| **primary_market_open** | **str** | Optional | A LUSID Cut Label code used for delaying the transaction time of certain instrument events until market open. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TimeZoneConventions import TimeZoneConventions

instance = TimeZoneConventions(
    primary_time_zone="...",  # required — The IANA time zone code for the instrument.
    start_of_day="...",  # optional — A LUSID Cut Label code used for generating instrument events at a time other than local midnight.
    primary_market_open="..."  # optional — A LUSID Cut Label code used for delaying the transaction time of certain instrument events until market open.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

