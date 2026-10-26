# AllocationPostingFundLine

One transaction a booking writes on the fund's own books.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side. |
| **portfolio** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_type** | **str** | Optional | The transaction type the booking writes on the fund side, for instance PECall: the type the fund&#39;s configuration maps the partnership transaction type to. |
| **partnership_transaction_type** | **str** | Optional | The partnership transaction type the fund-side posting is classified as, for instance PA.ContributionCalled. |
| **amount** | **float** | Optional | The amount posted, in the event currency. |
| **component** | **str** | Optional | The component of the event the posting carries. |
| **investor_record_id** | **str** | Optional | The investor record the posting is for. |
| **via_vehicle** | **str** | Optional | The vehicle the investor&#39;s share reached the fund through, when it did not come direct. |
| **admission_vehicle** | **str** | Optional | The vehicle the investor was admitted to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPostingFundLine import AllocationPostingFundLine

instance = AllocationPostingFundLine(
    id="...",  # optional — The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side.
    portfolio=ResourceId(...),  # optional
    transaction_type="...",  # optional — The transaction type the booking writes on the fund side, for instance PECall: the type the fund&#39;s configuration maps the partnership transaction type to.
    partnership_transaction_type="...",  # optional — The partnership transaction type the fund-side posting is classified as, for instance PA.ContributionCalled.
    amount=0.0,  # optional — The amount posted, in the event currency.
    component="...",  # optional — The component of the event the posting carries.
    investor_record_id="...",  # optional — The investor record the posting is for.
    via_vehicle="...",  # optional — The vehicle the investor&#39;s share reached the fund through, when it did not come direct.
    admission_vehicle="..."  # optional — The vehicle the investor was admitted to.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

