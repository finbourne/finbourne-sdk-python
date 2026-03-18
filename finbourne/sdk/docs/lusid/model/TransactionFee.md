# TransactionFee

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **name** | **str** | Optional | The display name of the transaction fee. |
| **description** | **str** | Optional | A description of the transaction fee. |
| **calculation** | [FeeCalculationRequest](FeeCalculationRequest.md) | Optional | *No description available.* |
| **condition** | **str** | Optional | The condition that the transaction must meet in order for the fee to be applied. |
| **capitalised** | **str** | Optional | Specifies whether the fee should be capitalised, not capitalised or conditionally capitalised. |
| **capitalisation_condition** | **str** | Optional | If the fee Capitalisation is Conditional, this condition determines whether the fee is capitalised, when applied to the transaction. |
| **txn_property_key** | **str** | Optional | The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the transaction fee. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **is_active** | **bool** | Optional | Indicates whether the transaction fee is currently active and should be applied to transactions. Optional when creating a transaction fee, defaults to true, if a value is not provided. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionFee import TransactionFee

instance = TransactionFee(
    id=ResourceId(...),  # optional
    name="...",  # optional — The display name of the transaction fee.
    description="...",  # optional — A description of the transaction fee.
    calculation=FeeCalculationRequest(...),  # optional
    condition="...",  # optional — The condition that the transaction must meet in order for the fee to be applied.
    capitalised="...",  # optional — Specifies whether the fee should be capitalised, not capitalised or conditionally capitalised.
    capitalisation_condition="...",  # optional — If the fee Capitalisation is Conditional, this condition determines whether the fee is capitalised, when applied to the transaction.
    txn_property_key="...",  # optional — The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain.
    properties=ModelProperty(...),  # optional — A set of properties for the transaction fee.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    is_active=True,  # optional — Indicates whether the transaction fee is currently active and should be applied to transactions. Optional when creating a transaction fee, defaults to true, if a value is not provided.
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

