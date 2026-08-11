# OrderInstructionSetRequest

A request to create or update multiple OrderInstructions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[OrderInstructionRequest]](OrderInstructionRequest.md) | Optional | A collection of OrderInstructionRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderInstructionSetRequest import OrderInstructionSetRequest

instance = OrderInstructionSetRequest(
    requests=[]  # optional — A collection of OrderInstructionRequests.
)
```


## Related Models

- [OrderInstructionRequest](OrderInstructionRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

