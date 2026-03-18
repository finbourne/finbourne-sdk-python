# PropertyReferenceDataValue

The ReferenceData relevant to the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the Property.  Only ReferenceData where the ReferenceData value matches the Property value is included.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **string_value** | **str** | Optional | *No description available.* |
| **numeric_value** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyReferenceDataValue import PropertyReferenceDataValue

instance = PropertyReferenceDataValue(
    string_value="...",  # optional
    numeric_value=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

