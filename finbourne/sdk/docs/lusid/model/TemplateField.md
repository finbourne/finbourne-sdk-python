# TemplateField

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | *No description available.* |
| **specificity** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **type** | **str** | Required | *No description available.* |
| **availability** | **str** | Required | *No description available.* |
| **usage** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TemplateField import TemplateField

instance = TemplateField(
    field_name="...",  # required
    specificity="...",  # required
    description="...",  # required
    type="...",  # required
    availability="...",  # required
    usage=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

