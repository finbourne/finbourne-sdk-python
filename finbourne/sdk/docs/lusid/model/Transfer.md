# Transfer

A transfer and both of the transactions it booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transfer_type** | **str** | Optional | The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time. |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_out** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **transaction_in** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties of the transfer, for the requested PropertyKeys. |
| **href** | **str** | Optional | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Transfer import Transfer

instance = Transfer(
    transfer_id=ResourceId(...),  # optional
    transfer_type="...",  # optional — The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time.
    portfolio_id_out=ResourceId(...),  # optional
    portfolio_id_in=ResourceId(...),  # optional
    transaction_out=Transaction(...),  # optional
    transaction_in=Transaction(...),  # optional
    properties=ModelProperty(...),  # optional — The properties of the transfer, for the requested PropertyKeys.
    href="...",  # optional — The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Transaction](Transaction.md)
- [Transaction](Transaction.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

