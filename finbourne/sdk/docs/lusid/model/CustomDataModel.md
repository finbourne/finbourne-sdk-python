# CustomDataModel

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_model_summary** | [DataModelSummary](DataModelSummary.md) | Optional | *No description available.* |
| **inherited** | [CustomDataModelCriteria](CustomDataModelCriteria.md) | Optional | *No description available.* |
| **incremental** | [CustomDataModelCriteria](CustomDataModelCriteria.md) | Optional | *No description available.* |
| **applied** | [CustomDataModelCriteria](CustomDataModelCriteria.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomDataModel import CustomDataModel

instance = CustomDataModel(
    data_model_summary=DataModelSummary(...),  # optional
    inherited=CustomDataModelCriteria(...),  # optional
    incremental=CustomDataModelCriteria(...),  # optional
    applied=CustomDataModelCriteria(...),  # optional
    version=Version(...)  # optional
)
```


## Related Models

- [DataModelSummary](DataModelSummary.md)
- [CustomDataModelCriteria](CustomDataModelCriteria.md)
- [CustomDataModelCriteria](CustomDataModelCriteria.md)
- [CustomDataModelCriteria](CustomDataModelCriteria.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

