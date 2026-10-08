# CreateTransferResponse

The transfer that was created, and the transaction legs it booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transfer_type** | **str** | Optional | The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time. |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_id_out** | **str** | Optional | The transaction id of the created outgoing leg. |
| **transaction_id_in** | **str** | Optional | The transaction id of the created incoming leg. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTransferResponse import CreateTransferResponse

instance = CreateTransferResponse(
    transfer_id=ResourceId(...),  # optional
    transfer_type="...",  # optional — The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time.
    portfolio_id_out=ResourceId(...),  # optional
    portfolio_id_in=ResourceId(...),  # optional
    transaction_id_out="...",  # optional — The transaction id of the created outgoing leg.
    transaction_id_in="..."  # optional — The transaction id of the created incoming leg.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

