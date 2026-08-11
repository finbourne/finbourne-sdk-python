# OtcConfirmation

For the storage of any information pertinent to the confirmation of an OTC trade. e.g the Counterparty Agreement Code
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **counterparty_agreement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OtcConfirmation import OtcConfirmation

instance = OtcConfirmation(
    counterparty_agreement_id=ResourceId(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

