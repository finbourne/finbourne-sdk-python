# CounterpartySignatory

The counterpartyAgreement is signed by two parties, one of which is implicitly the LUSID user.  The CounterpartySignatory represents the 'other side' of the agreement.  It comprises a name and identifier for a Legal Entity in LUSID.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \&quot;displayName\&quot; of the legal entity. |
| **legal_entity_identifier** | [TypedResourceId](TypedResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CounterpartySignatory import CounterpartySignatory

instance = CounterpartySignatory(
    name="...",  # required — A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \&quot;displayName\&quot; of the legal entity.
    legal_entity_identifier=TypedResourceId(...)  # required
)
```

- [TypedResourceId](TypedResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

