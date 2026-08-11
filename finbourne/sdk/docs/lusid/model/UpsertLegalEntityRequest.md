# UpsertLegalEntityRequest

Request to create or update an legal entity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Legal Entity. |
| **display_name** | **str** | Required | The display name of the Legal Entity |
| **description** | **str** | Optional | The description of the Legal Entity |
| **counterparty_risk_information** | [CounterpartyRiskInformation](CounterpartyRiskInformation.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertLegalEntityRequest import UpsertLegalEntityRequest

instance = UpsertLegalEntityRequest(
    identifiers=ModelProperty(...),  # required — The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code
    properties=ModelProperty(...),  # optional — A set of properties associated to the Legal Entity.
    display_name="...",  # required — The display name of the Legal Entity
    description="...",  # optional — The description of the Legal Entity
    counterparty_risk_information=CounterpartyRiskInformation(...)  # optional
)
```


## Related Models

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [CounterpartyRiskInformation](CounterpartyRiskInformation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

