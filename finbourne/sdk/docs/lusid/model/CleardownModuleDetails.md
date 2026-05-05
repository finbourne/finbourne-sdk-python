# CleardownModuleDetails

A Cleardown Module request definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the Cleardown Module. |
| **description** | **str** | Optional | A description for the Cleardown Module. |
| **status** | **str** | Required | The Cleardown Module status. Default value: Active. Available values: Active, Inactive. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CleardownModuleDetails import CleardownModuleDetails

instance = CleardownModuleDetails(
    display_name="...",  # required — The name of the Cleardown Module.
    description="...",  # optional — A description for the Cleardown Module.
    status="..."  # required — The Cleardown Module status. Default value: Active. Available values: Active, Inactive.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

