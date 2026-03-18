# Bucket

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tax_lot_id** | **str** | Optional | The identifier of the tax lot this bucket is for. |
| **movement_name** | **str** | Optional | The name of the movement. |
| **holding_type** | **str** | Optional | The type of the holding. |
| **economic_bucket** | **str** | Optional | The economic bucket. |
| **economic_bucket_component** | **str** | Optional | The economic bucket component. |
| **economic_bucket_variant** | **str** | Optional | The economic bucket component. |
| **holding_sign** | **str** | Optional | The holding sign. |
| **local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **base** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **units** | **float** | Optional | The units. |
| **activity_date** | **datetime** | Optional | The activity date of the bucket. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Bucket import Bucket

instance = Bucket(
    tax_lot_id="...",  # optional — The identifier of the tax lot this bucket is for.
    movement_name="...",  # optional — The name of the movement.
    holding_type="...",  # optional — The type of the holding.
    economic_bucket="...",  # optional — The economic bucket.
    economic_bucket_component="...",  # optional — The economic bucket component.
    economic_bucket_variant="...",  # optional — The economic bucket component.
    holding_sign="...",  # optional — The holding sign.
    local=CurrencyAndAmount(...),  # optional
    base=CurrencyAndAmount(...),  # optional
    units=0.0,  # optional — The units.
    activity_date=datetime.now()  # optional — The activity date of the bucket.
)
```

- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

