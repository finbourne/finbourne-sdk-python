# OverrideVirtualTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to unresolved instruments or non-existent transaction types for the override transactions. |
| **instrument_event_id** | **str** | Required | The identifier of the instrument event that was overridden. |
| **cancel_instruction_id** | **str** | Required | The identifier of the cancel instruction that was created for the overridden instrument event. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OverrideVirtualTransactionsResponse import OverrideVirtualTransactionsResponse

instance = OverrideVirtualTransactionsResponse(
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    metadata=,  # optional — Contains warnings related to unresolved instruments or non-existent transaction types for the override transactions.
    instrument_event_id="...",  # required — The identifier of the instrument event that was overridden.
    cancel_instruction_id="...",  # required — The identifier of the cancel instruction that was created for the overridden instrument event.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

