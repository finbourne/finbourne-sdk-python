# AvailableField

Information about a field that can be designed on (regardless if it currently is) Kind of a \"mini-available catalog entry\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name of the Field |
| **data_type** | [DataType](DataType.md) | Optional | *No description available.* |
| **field_type** | [FieldType](FieldType.md) | Required | *No description available.* |
| **is_main** | **bool** | Optional | Is this a Main Field within the Provider |
| **is_primary_key** | **bool** | Optional | Is this a member of the PrimaryKey of the Provider |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.AvailableField import AvailableField

instance = AvailableField(
    name="...",  # required — Name of the Field
    data_type=DataType(...),  # optional
    field_type=FieldType(...),  # required
    is_main=True,  # optional — Is this a Main Field within the Provider
    is_primary_key=True  # optional — Is this a member of the PrimaryKey of the Provider
)
```

- [DataType](DataType.md)
- [FieldType](FieldType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

