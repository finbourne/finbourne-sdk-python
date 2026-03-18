# CleardownModuleRequest

A Cleardown Module request definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Cleardown Module. |
| **display_name** | **str** | Required | The name of the Cleardown Module. |
| **description** | **str** | Optional | A description for the Cleardown Module. |
| **rules** | [List[CleardownModuleRule]](CleardownModuleRule.md) | Optional | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CleardownModuleRequest import CleardownModuleRequest

instance = CleardownModuleRequest(
    code="...",  # required — The code of the Cleardown Module.
    display_name="...",  # required — The name of the Cleardown Module.
    description="...",  # optional — A description for the Cleardown Module.
    rules=[]  # optional — The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection.
)
```

- [CleardownModuleRule](CleardownModuleRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

