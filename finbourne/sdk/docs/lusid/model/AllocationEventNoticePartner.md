# AllocationEventNoticePartner

The partner a notice is addressed to.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record identifier of the partner. |
| **display_name** | **str** | Optional | The display name of the partner. |
| **commitment** | **float** | Required | The partner&#39;s total commitment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNoticePartner import AllocationEventNoticePartner

instance = AllocationEventNoticePartner(
    investor_record_id="...",  # required — The investor record identifier of the partner.
    display_name="...",  # optional — The display name of the partner.
    commitment=0.0  # required — The partner&#39;s total commitment.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

