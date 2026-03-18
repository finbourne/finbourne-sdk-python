# IntegrationDescription

Response containing the description of an integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Unique identifier of the integration e.g. \&quot;copp-clark\&quot;. |
| **name** | **str** | Required | Readable name of the integration e.g. \&quot;Copp Clark\&quot;. |
| **description** | **str** | Required | Describes the purpose of the integration. |
| **supported_trigger_types** | **List[str]** | Required | Trigger types (Time, File) the integration supports. |
| **licensed** | **bool** | Required | True if your domain is licensed to use this integration, otherwise false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationDescription import IntegrationDescription

instance = IntegrationDescription(
    type="...",  # required — Unique identifier of the integration e.g. \&quot;copp-clark\&quot;.
    name="...",  # required — Readable name of the integration e.g. \&quot;Copp Clark\&quot;.
    description="...",  # required — Describes the purpose of the integration.
    supported_trigger_types=,  # required — Trigger types (Time, File) the integration supports.
    licensed=True  # required — True if your domain is licensed to use this integration, otherwise false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

