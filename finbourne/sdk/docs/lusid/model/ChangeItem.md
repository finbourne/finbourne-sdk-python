# ChangeItem

Information about a change to a field / property.  At least one of 'PreviousValue' or 'NewValue' will be set.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The name of the field or property that has been changed. |
| **previous_value** | **str** | Optional | The previous value for this field / property. |
| **new_value** | **str** | Optional | The new value for this field / property. |
| **effective_from** | **datetime** | Optional | The market data time, i.e. the time to run the change from. |
| **effective_until** | **datetime** | Optional | The market data time, i.e. the time to run the change until. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChangeItem import ChangeItem

instance = ChangeItem(
    field_name="...",  # required — The name of the field or property that has been changed.
    previous_value="...",  # optional — The previous value for this field / property.
    new_value="...",  # optional — The new value for this field / property.
    effective_from=datetime.now(),  # optional — The market data time, i.e. the time to run the change from.
    effective_until=datetime.now()  # optional — The market data time, i.e. the time to run the change until.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

