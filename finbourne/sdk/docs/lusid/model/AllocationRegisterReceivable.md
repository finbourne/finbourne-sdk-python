# AllocationRegisterReceivable

What one register is owed on a booked capital call, across every record called on its lines.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **called** | **float** | Optional | What was called on the register&#39;s lines. |
| **received** | **float** | Optional | What has settled the register&#39;s lines so far. |
| **outstanding** | **float** | Optional | What the register is still owed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationRegisterReceivable import AllocationRegisterReceivable

instance = AllocationRegisterReceivable(
    portfolio=ResourceId(...),  # optional
    called=0.0,  # optional — What was called on the register&#39;s lines.
    received=0.0,  # optional — What has settled the register&#39;s lines so far.
    outstanding=0.0  # optional — What the register is still owed.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

