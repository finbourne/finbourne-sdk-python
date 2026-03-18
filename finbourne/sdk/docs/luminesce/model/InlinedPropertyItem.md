# InlinedPropertyItem

Information about a inlined property so that decorated properties can be inlined into luminesce
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | Key of the property |
| **name** | **str** | Optional | Name of the property |
| **is_main** | **bool** | Optional | Is Main indicator for the property |
| **description** | **str** | Optional | Description of the property |
| **data_type** | **str** | Optional | Data type of the property |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.InlinedPropertyItem import InlinedPropertyItem

instance = InlinedPropertyItem(
    key="...",  # required — Key of the property
    name="...",  # optional — Name of the property
    is_main=True,  # optional — Is Main indicator for the property
    description="...",  # optional — Description of the property
    data_type="..."  # optional — Data type of the property
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

