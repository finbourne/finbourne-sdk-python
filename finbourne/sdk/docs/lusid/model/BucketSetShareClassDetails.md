# BucketSetShareClassDetails

Identifying detail for the share class a bucket set node is for.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier for the share class&#39; instrument. Absent where the instrument has not been resolved. |
| **instrument_scope** | **str** | Optional | The scope in which the share class instrument lies. Absent where the instrument has not been resolved. |
| **short_code** | **str** | Required | The unique code within the fund for the share class. |
| **dom_currency** | **str** | Optional | The domestic currency declared for the share class. |
| **instrument_active** | **bool** | Required | Whether the share class&#39; instrument is active. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetShareClassDetails import BucketSetShareClassDetails

instance = BucketSetShareClassDetails(
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier for the share class&#39; instrument. Absent where the instrument has not been resolved.
    instrument_scope="...",  # optional — The scope in which the share class instrument lies. Absent where the instrument has not been resolved.
    short_code="...",  # required — The unique code within the fund for the share class.
    dom_currency="...",  # optional — The domestic currency declared for the share class.
    instrument_active=True  # required — Whether the share class&#39; instrument is active.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

