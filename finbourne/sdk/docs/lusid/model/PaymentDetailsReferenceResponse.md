# PaymentDetailsReferenceResponse

Response representation of a Payment Details reference. Extends the request shape with  a system-populated relational dataset definition identifier.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **relational_dataset_definition_id** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **series_scope** | **str** | Required | The scope of the relational datapoint. May differ from the scope of the dataset definition. |
| **applicable_entity** | [../model/PaymentDetailsApplicableEntity](PaymentDetailsApplicableEntity.md) | Required | *No description available.* |
| **series_identifiers** | [../model/PaymentDetailsSeriesIdentifiers](PaymentDetailsSeriesIdentifiers.md) | Required | *No description available.* |
| **effective_date** | **datetime** | Required | The effective date of the relational datapoint observation to retrieve. ISO 8601 datetime. |
| **as_at_date** | **datetime** | Required | The as-at date of the relational datapoint observation to retrieve. ISO 8601 datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentDetailsReferenceResponse import PaymentDetailsReferenceResponse

instance = PaymentDetailsReferenceResponse(
    relational_dataset_definition_id=ResourceId(...),  # optional
    series_scope="...",  # required — The scope of the relational datapoint. May differ from the scope of the dataset definition.
    applicable_entity=PaymentDetailsApplicableEntity(...),  # required
    series_identifiers=PaymentDetailsSeriesIdentifiers(...),  # required
    effective_date=datetime.now(),  # required — The effective date of the relational datapoint observation to retrieve. ISO 8601 datetime.
    as_at_date=datetime.now()  # required — The as-at date of the relational datapoint observation to retrieve. ISO 8601 datetime.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PaymentDetailsApplicableEntity](PaymentDetailsApplicableEntity.md)
- [PaymentDetailsSeriesIdentifiers](PaymentDetailsSeriesIdentifiers.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

