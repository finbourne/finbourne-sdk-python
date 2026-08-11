# PaymentDetailsReference

A pointer to a Payment Details relational dataset series for a payor or payee entity.  No PII is stored here — bank account details are resolved at read time from the referenced series.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_scope** | **str** | Required | The scope of the relational datapoint. May differ from the scope of the dataset definition. |
| **applicable_entity** | [PaymentDetailsApplicableEntity](PaymentDetailsApplicableEntity.md) | Required | *No description available.* |
| **series_identifiers** | [PaymentDetailsSeriesIdentifiers](PaymentDetailsSeriesIdentifiers.md) | Required | *No description available.* |
| **effective_date** | **datetime** | Required | The effective date of the relational datapoint observation to retrieve. ISO 8601 datetime. |
| **as_at_date** | **datetime** | Required | The as-at date of the relational datapoint observation to retrieve. ISO 8601 datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentDetailsReference import PaymentDetailsReference

instance = PaymentDetailsReference(
    series_scope="...",  # required — The scope of the relational datapoint. May differ from the scope of the dataset definition.
    applicable_entity=PaymentDetailsApplicableEntity(...),  # required
    series_identifiers=PaymentDetailsSeriesIdentifiers(...),  # required
    effective_date=datetime.now(),  # required — The effective date of the relational datapoint observation to retrieve. ISO 8601 datetime.
    as_at_date=datetime.now()  # required — The as-at date of the relational datapoint observation to retrieve. ISO 8601 datetime.
)
```

- [PaymentDetailsApplicableEntity](PaymentDetailsApplicableEntity.md)
- [PaymentDetailsSeriesIdentifiers](PaymentDetailsSeriesIdentifiers.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

