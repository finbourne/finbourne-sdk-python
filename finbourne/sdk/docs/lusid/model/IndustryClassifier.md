# IndustryClassifier

Object describing a particular industry classifier,  which comprises a classification code and the name of the classification system to which the code belongs.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **classification_system_name** | **str** | Required | The name of the classification system to which the classification code belongs (e.g. GICS). |
| **classification_code** | **str** | Required | The specific industry classification code assigned to the legal entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IndustryClassifier import IndustryClassifier

instance = IndustryClassifier(
    classification_system_name="...",  # required — The name of the classification system to which the classification code belongs (e.g. GICS).
    classification_code="..."  # required — The specific industry classification code assigned to the legal entity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

