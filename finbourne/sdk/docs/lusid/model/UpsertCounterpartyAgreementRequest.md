# UpsertCounterpartyAgreementRequest

Counterparty Agreement that is to be stored in the convention data store.  There must be only one of these present.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **counterparty_agreement** | [CounterpartyAgreement](CounterpartyAgreement.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertCounterpartyAgreementRequest import UpsertCounterpartyAgreementRequest

instance = UpsertCounterpartyAgreementRequest(
    counterparty_agreement=CounterpartyAgreement(...)  # required
)
```


## Related Models

- [CounterpartyAgreement](CounterpartyAgreement.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

