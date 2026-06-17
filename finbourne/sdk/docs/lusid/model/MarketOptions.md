# MarketOptions

The set of options that control miscellaneous and default market resolution behaviour.  A default scope entered here will cause duplicate (\"default\") rules to be created across all asset types, pointing at that scope.  These are aimed at a 'crude' level of control for those who do not wish to fine tune the way that data is resolved.  For clients who wish to simply match instruments to prices this is quite possibly sufficient. For those wishing to control market data sources  according to requirements based on accuracy or timeliness it is not recommended. In more advanced cases the options should largely be ignored and rules specified  per source.  If no default scope is supplied, no default rules are created.  Where a default scope is supplied, a default rule is constructed per asset type, pointing at that scope, and appended  after all specified rules so it is only tried as a last resort. Each default rule is wild-carded within its asset type  (for example Quote.{instrumentCodeType}.* or Fx.*.*) rather than being a single fully wild-carded rule, and one (two for  Rates) is generated per asset type. Consequently, where no specified rule matches a dependency, the failure reported is  this constructed default rule in the provided default scope.  It is not recommended to rely on this behaviour, as these rules match a wide range of data and are likely to be slow to resolve.  It is better to specify rules for the data you require in the MarketRules of the MarketContext.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **default_supplier** | **str** | Optional | The default supplier of data. This controls which &#39;dialect&#39; is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId |
| **default_instrument_code_type** | **str** | Optional | When instrument quotes are searched for, what identifier should be used by default |
| **default_scope** | **str** | Optional | The scope in which to search for data when applying default rules. This is optional: if omitted, no default rules  are created and market data is resolved only via the explicitly specified market data key rules. |
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
    default_scope="...",  # optional — The scope in which to search for data when applying default rules. This is optional: if omitted, no default rules  are created and market data is resolved only via the explicitly specified market data key rules.
    attempt_to_infer_missing_fx=True,  # optional — if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD
    calendar_scope="...",  # optional — The scope in which holiday calendars stored
    convention_scope="..."  # optional — The scope in which conventions stored
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

