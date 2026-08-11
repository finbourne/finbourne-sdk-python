# TransactionFeeType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | The display name of the transaction fee type. |
| **description** | **str** | Optional | A description of the transaction fee type. |
| **calculation** | [FeeCalculationRequest](FeeCalculationRequest.md) | Optional | *No description available.* |
| **condition** | **str** | Optional | The condition that the transaction must meet in order for the fee to be applied. |
| **txn_property_key** | **str** | Optional | The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the transaction fee type. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **is_active** | **bool** | Optional | Indicates whether the transaction fee type is currently active and should be applied to transactions. Optional when creating a transaction fee type, defaults to true, if a value is not provided. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionFeeType import TransactionFeeType

instance = TransactionFeeType(
    id=ResourceId(...),  # optional
    display_name="...",  # optional — The display name of the transaction fee type.
    description="...",  # optional — A description of the transaction fee type.
    calculation=FeeCalculationRequest(...),  # optional
    condition="...",  # optional — The condition that the transaction must meet in order for the fee to be applied.
    txn_property_key="...",  # optional — The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain.
    properties=ModelProperty(...),  # optional — A set of properties for the transaction fee type.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    is_active=True,  # optional — Indicates whether the transaction fee type is currently active and should be applied to transactions. Optional when creating a transaction fee type, defaults to true, if a value is not provided.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [FeeCalculationRequest](FeeCalculationRequest.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

