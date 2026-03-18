# DataMapKey

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | **str** | Optional | The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it. |
| **code** | **str** | Optional | A unique name to semantically identify the mapping set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataMapKey import DataMapKey

instance = DataMapKey(
    version="...",  # optional — The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it.
    code="..."  # optional — A unique name to semantically identify the mapping set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

