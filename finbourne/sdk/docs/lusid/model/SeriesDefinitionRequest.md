# SeriesDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_code** | **str** | Required | The code of the Share Class this Series belongs to. |
| **series_definitions** | [List[SeriesDefinition]](SeriesDefinition.md) | Required | The definitions of the Series to add to the Share Class. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SeriesDefinitionRequest import SeriesDefinitionRequest

instance = SeriesDefinitionRequest(
    share_class_code="...",  # required — The code of the Share Class this Series belongs to.
    series_definitions=[]  # required — The definitions of the Series to add to the Share Class.
)
```

- [SeriesDefinition](SeriesDefinition.md) — used in `series_definitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

