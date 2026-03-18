# PortfolioResultDataKeyRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **supplier** | **str** | Required | the result resource supplier (where the data comes from) |
| **data_scope** | **str** | Required | which is the scope in which the data should be found |
| **document_code** | **str** | Required | document code that defines which document is desired |
| **quote_interval** | **str** | Optional | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago). |
| **as_at** | **datetime** | Optional | The AsAt predicate specification. |
| **portfolio_code** | **str** | Optional | *No description available.* |
| **portfolio_scope** | **str** | Optional | *No description available.* |
| **result_key_rule_type** | **str** | Required | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioResultDataKeyRule import PortfolioResultDataKeyRule

instance = PortfolioResultDataKeyRule(
    supplier="...",  # required — the result resource supplier (where the data comes from)
    data_scope="...",  # required — which is the scope in which the data should be found
    document_code="...",  # required — document code that defines which document is desired
    quote_interval="...",  # optional — Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago).
    as_at=datetime.now(),  # optional — The AsAt predicate specification.
    portfolio_code="...",  # optional
    portfolio_scope="...",  # optional
    result_key_rule_type="..."  # required — The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

