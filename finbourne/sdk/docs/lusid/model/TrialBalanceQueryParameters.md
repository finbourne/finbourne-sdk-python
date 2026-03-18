# TrialBalanceQueryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **end** | [DateOrDiaryEntry](DateOrDiaryEntry.md) | Optional | *No description available.* |
| **date_mode** | **str** | Optional | The mode of calculation of the trial balance. The available values are: ActivityDate, AccountingDate. |
| **general_ledger_profile_code** | **str** | Optional | The optional code of a general ledger profile used to decorate trial balance with levels. |
| **property_keys** | **List[str]** | Optional | A list of property keys from the &#39;Account&#39; domain to decorate onto the trial balance. |
| **exclude_cleardown_module** | **bool** | Optional | By deafult this flag is set to false, if this is set to true, no cleardown module will be applied to the trial balance. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TrialBalanceQueryParameters import TrialBalanceQueryParameters

instance = TrialBalanceQueryParameters(
    start=DateOrDiaryEntry(...),  # optional
    end=DateOrDiaryEntry(...),  # optional
    date_mode="...",  # optional — The mode of calculation of the trial balance. The available values are: ActivityDate, AccountingDate.
    general_ledger_profile_code="...",  # optional — The optional code of a general ledger profile used to decorate trial balance with levels.
    property_keys=,  # optional — A list of property keys from the &#39;Account&#39; domain to decorate onto the trial balance.
    exclude_cleardown_module=True  # optional — By deafult this flag is set to false, if this is set to true, no cleardown module will be applied to the trial balance.
)
```


## Related Models

- [DateOrDiaryEntry](DateOrDiaryEntry.md)
- [DateOrDiaryEntry](DateOrDiaryEntry.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

