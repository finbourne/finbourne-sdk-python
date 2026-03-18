# UpsertResourceRecordRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **deployment_scope** | **str** | Required | *No description available.* |
| **deployment_code** | **str** | Required | *No description available.* |
| **resource_id** | **str** | Required | *No description available.* |
| **format** | **str** | Required | *No description available.* |
| **resource_type** | **str** | Required | *No description available.* |
| **resource_state** | **object** | Required | *No description available.* |
| **dependencies** | **List[str]** | Required | *No description available.* |
| **tracking_state** | **object** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertResourceRecordRequest import UpsertResourceRecordRequest

instance = UpsertResourceRecordRequest(
    deployment_scope="...",  # required
    deployment_code="...",  # required
    resource_id="...",  # required
    format="...",  # required
    resource_type="...",  # required
    resource_state=,  # required
    dependencies=,  # required
    tracking_state=  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

