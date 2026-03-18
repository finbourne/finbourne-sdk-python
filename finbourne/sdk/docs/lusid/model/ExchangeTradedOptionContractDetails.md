# ExchangeTradedOptionContractDetails

Most, if not all, information about contracts is standardised. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.  There is a lot of overlap with this and FuturesContractDetails but as that is an established DTO we must duplicate a number of fields here
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dom_ccy** | **str** | Required | Currency in which the contract is paid. |
| **strike** | **float** | Required | The option strike, this can be negative for some options. |
| **contract_size** | **float** | Required | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. |
| **country** | **str** | Required | Country (code) for the exchange. |
| **delivery_type** | **str** | Required | The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical]. |
| **description** | **str** | Required | Description of contract |
| **exchange_code** | **str** | Required | Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code). |
| **exercise_date** | **datetime** | Required | The last exercise date of the option. |
| **exercise_type** | **str** | Required | The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American]. |
| **option_code** | **str** | Required | Option Contract Code, typically one or two letters, e.g. OG &#x3D;&gt; Option on Gold. |
| **option_type** | **str** | Required | The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put]. |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Required | *No description available.* |
| **underlying_code** | **str** | Required | Code of the underlying, for an option on futures this should be the futures code. |
| **delivery_days** | **int** | Optional | Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set. |
| **business_day_convention** | **str** | Optional | The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  Defaults to \&quot;F\&quot; if not set. |
| **settlement_calendars** | **List[str]** | Optional | An array of strings denoting calendars used in calculating the option settlement date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExchangeTradedOptionContractDetails import ExchangeTradedOptionContractDetails

instance = ExchangeTradedOptionContractDetails(
    dom_ccy="...",  # required — Currency in which the contract is paid.
    strike=0.0,  # required — The option strike, this can be negative for some options.
    contract_size=0.0,  # required — Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such.
    country="...",  # required — Country (code) for the exchange.
    delivery_type="...",  # required — The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical].
    description="...",  # required — Description of contract
    exchange_code="...",  # required — Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code).
    exercise_date=datetime.now(),  # required — The last exercise date of the option.
    exercise_type="...",  # required — The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American].
    option_code="...",  # required — Option Contract Code, typically one or two letters, e.g. OG &#x3D;&gt; Option on Gold.
    option_type="...",  # required — The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put].
    underlying=LusidInstrument(...),  # required
    underlying_code="...",  # required — Code of the underlying, for an option on futures this should be the futures code.
    delivery_days=0,  # optional — Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set.
    business_day_convention="...",  # optional — The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  Defaults to \&quot;F\&quot; if not set.
    settlement_calendars=  # optional — An array of strings denoting calendars used in calculating the option settlement date.
)
```

- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

