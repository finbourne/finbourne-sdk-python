# UpdateDataTypeRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the data type. |
| **description** | **str** | Optional | The description of the data type. |
| **acceptable_values** | **List[str]** | Optional | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. |
| **acceptable_units** | [List[UpdateUnitRequest]](UpdateUnitRequest.md) | Optional | The definitions of the acceptable units. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateDataTypeRequest import UpdateDataTypeRequest

instance = UpdateDataTypeRequest(
    display_name="...",  # optional — The display name of the data type.
    description="...",  # optional — The description of the data type.
    acceptable_values=,  # optional — The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range.
    acceptable_units=[]  # optional — The definitions of the acceptable units.
)
```

- [UpdateUnitRequest](UpdateUnitRequest.md) — used in `acceptable_units`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

