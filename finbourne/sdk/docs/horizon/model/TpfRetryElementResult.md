# TpfRetryElementResult

Result for a single batch element retry attempt
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **batch_element_reference_id** | **str** | Required | Batch element reference identifier |
| **status** | **str** | Required | Status of the retry attempt (e.g., \&quot;Retrying\&quot;, \&quot;NotFound\&quot;) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfRetryElementResult import TpfRetryElementResult

instance = TpfRetryElementResult(
    batch_element_reference_id="...",  # required — Batch element reference identifier
    status="..."  # required — Status of the retry attempt (e.g., \&quot;Retrying\&quot;, \&quot;NotFound\&quot;)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

