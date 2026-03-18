# FuturesContractDetails

Most, if not all, information about contracts is standardized. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dom_ccy** | **str** | Required | Currency in which the contract is paid. |
| **fgn_ccy** | **str** | Optional | Currency of the underlying, for use with FX Futures |
| **asset_class** | **str** | Optional | The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. |
| **contract_code** | **str** | Required | The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc. |
| **contract_month** | **str** | Optional | Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  Defaults to \&quot;Unknown\&quot; if not set. |
| **contract_size** | **float** | Required | Size of a single contract. |
| **convention** | **str** | Optional | If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. |
| **country** | **str** | Optional | Country (code) for the exchange. |
| **description** | **str** | Optional | Description of contract. |
| **exchange_code** | **str** | Required | Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code). |
| **exchange_name** | **str** | Optional | Exchange name (for when code is not automatically recognised). |
| **ticker_step** | **float** | Optional | Minimal step size change in ticker. |
| **unit_value** | **float** | Optional | The value in the currency of a 1 unit change in the contract price. |
| **calendars** | **List[str]** | Optional | Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures). |
| **delivery_type** | **str** | Optional | Delivery type to be used on settling the contract.  Optional: Defaults to DeliveryType.Physical if not provided.    Supported string (enumeration) values are: [Cash, Physical]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FuturesContractDetails import FuturesContractDetails

instance = FuturesContractDetails(
    dom_ccy="...",  # required — Currency in which the contract is paid.
    fgn_ccy="...",  # optional — Currency of the underlying, for use with FX Futures
    asset_class="...",  # optional — The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].
    contract_code="...",  # required — The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc.
    contract_month="...",  # optional — Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  Defaults to \&quot;Unknown\&quot; if not set.
    contract_size=0.0,  # required — Size of a single contract.
    convention="...",  # optional — If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].
    country="...",  # optional — Country (code) for the exchange.
    description="...",  # optional — Description of contract.
    exchange_code="...",  # required — Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code).
    exchange_name="...",  # optional — Exchange name (for when code is not automatically recognised).
    ticker_step=0.0,  # optional — Minimal step size change in ticker.
    unit_value=0.0,  # optional — The value in the currency of a 1 unit change in the contract price.
    calendars=,  # optional — Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures).
    delivery_type="..."  # optional — Delivery type to be used on settling the contract.  Optional: Defaults to DeliveryType.Physical if not provided.    Supported string (enumeration) values are: [Cash, Physical].
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

