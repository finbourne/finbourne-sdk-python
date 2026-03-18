# TransactionTemplateSpecification

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_type** | **str** | Required | *No description available.* |
| **supported_instrument_types** | **List[str]** | Required | *No description available.* |
| **supported_participation_types** | **List[str]** | Required | *No description available.* |
| **supported_election_types** | [List[ElectionSpecification]](ElectionSpecification.md) | Required | *No description available.* |
| **supported_template_fields** | [List[TemplateField]](TemplateField.md) | Required | *No description available.* |
| **eligibility_calculation** | [EligibilityCalculation](EligibilityCalculation.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTemplateSpecification import TransactionTemplateSpecification

instance = TransactionTemplateSpecification(
    instrument_event_type="...",  # required
    supported_instrument_types=,  # required
    supported_participation_types=,  # required
    supported_election_types=[],  # required
    supported_template_fields=[],  # required
    eligibility_calculation=EligibilityCalculation(...)  # required
)
```

- [ElectionSpecification](ElectionSpecification.md)
- [TemplateField](TemplateField.md)
- [EligibilityCalculation](EligibilityCalculation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

