# MarketOptions

The set of options that control miscellaneous and default market resolution behaviour.  These are aimed at a 'crude' level of control for those who do not wish to fine tune the way that data is resolved.  For clients who wish to simply match instruments to prices this is quite possibly sufficient. For those wishing to control market data sources  according to requirements based on accuracy or timeliness it is not. In more advanced cases the options should largely be ignored and rules specified  per source. Be aware that where no specified rule matches the final fallback is on to the logic implied here.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **default_supplier** | **str** | Optional | The default supplier of data. This controls which &#39;dialect&#39; is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId |
| **default_instrument_code_type** | **str** | Optional | When instrument quotes are searched for, what identifier should be used by default |
| **default_scope** | **str** | Required | For default rules, which scope should data be searched for in |
| **attempt_to_infer_missing_fx** | **bool** | Optional | if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD |
| **calendar_scope** | **str** | Optional | The scope in which holiday calendars stored |
| **convention_scope** | **str** | Optional | The scope in which conventions stored |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketOptions import MarketOptions

instance = MarketOptions(
    default_supplier="...",  # optional — The default supplier of data. This controls which &#39;dialect&#39; is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId
    default_instrument_code_type="...",  # optional — When instrument quotes are searched for, what identifier should be used by default
    default_scope="...",  # required — For default rules, which scope should data be searched for in
    attempt_to_infer_missing_fx=True,  # optional — if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD
    calendar_scope="...",  # optional — The scope in which holiday calendars stored
    convention_scope="..."  # optional — The scope in which conventions stored
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

