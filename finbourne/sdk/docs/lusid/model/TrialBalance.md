# TrialBalance

A TrialBalance entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **general_ledger_account_code** | **str** | Required | The Account code that the trial balance results have been grouped against. |
| **description** | **str** | Optional | The description of the record. |
| **levels** | **List[str]** | Required | The levels that have been derived from the specified General Ledger Profile. |
| **account_type** | **str** | Required | The account type attributed to the record. |
| **local_currency** | **str** | Required | The local currency for the amounts specified. Defaults to base currency if multiple different currencies present in the grouped line. |
| **opening** | [MultiCurrencyAmounts](MultiCurrencyAmounts.md) | Required | *No description available.* |
| **closing** | [MultiCurrencyAmounts](MultiCurrencyAmounts.md) | Required | *No description available.* |
| **debit** | [MultiCurrencyAmounts](MultiCurrencyAmounts.md) | Required | *No description available.* |
| **credit** | [MultiCurrencyAmounts](MultiCurrencyAmounts.md) | Required | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Properties found on the mapped &#39;Account&#39;, as specified in request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TrialBalance import TrialBalance

instance = TrialBalance(
    general_ledger_account_code="...",  # required — The Account code that the trial balance results have been grouped against.
    description="...",  # optional — The description of the record.
    levels=,  # required — The levels that have been derived from the specified General Ledger Profile.
    account_type="...",  # required — The account type attributed to the record.
    local_currency="...",  # required — The local currency for the amounts specified. Defaults to base currency if multiple different currencies present in the grouped line.
    opening=MultiCurrencyAmounts(...),  # required
    closing=MultiCurrencyAmounts(...),  # required
    debit=MultiCurrencyAmounts(...),  # required
    credit=MultiCurrencyAmounts(...),  # required
    properties=ModelProperty(...),  # optional — Properties found on the mapped &#39;Account&#39;, as specified in request.
    links=[]  # optional
)
```

- [MultiCurrencyAmounts](MultiCurrencyAmounts.md)
- [MultiCurrencyAmounts](MultiCurrencyAmounts.md)
- [MultiCurrencyAmounts](MultiCurrencyAmounts.md)
- [MultiCurrencyAmounts](MultiCurrencyAmounts.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

