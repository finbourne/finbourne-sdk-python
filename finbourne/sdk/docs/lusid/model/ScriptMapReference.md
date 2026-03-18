# ScriptMapReference

Provides information about the location of a script map within the configuration store
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the configuration store entry where the translation map is located. |
| **code** | **str** | Required | The code of the configuration store entry where the translation map is located. |
| **key** | **str** | Required | The key of the configuration store entry where the translation map is located. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScriptMapReference import ScriptMapReference

instance = ScriptMapReference(
    scope="...",  # required — The scope of the configuration store entry where the translation map is located.
    code="...",  # required — The code of the configuration store entry where the translation map is located.
    key="..."  # required — The key of the configuration store entry where the translation map is located.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

