# AllocationMapBasisValue

The value one investor record is weighted by when an Allocation Map is resolved.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the basis value belongs to. |
| **basis_value** | **float** | Required | The value the investor record is weighted by, for example its commitment. |
| **currency** | **str** | Optional | The currency the basis value is held in. Absent means the base currency of the map&#39;s member fund. When the basis values span more than one currency, each is translated into the fund&#39;s base currency at the spot rate on the event date, from the fund&#39;s ABOR recipe, before it weights the allocation. The rate on the event date is the latest quote at or before 00:00 UTC on that date. |
| **commitment_line_id** | **str** | Optional | For a Commitment event, the commitment line the amount is recorded against. The basis value is then the signed commitment amount itself: positive commits, negative releases. Not used for other event types. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapBasisValue import AllocationMapBasisValue

instance = AllocationMapBasisValue(
    investor_record_id="...",  # required — The investor record the basis value belongs to.
    basis_value=0.0,  # required — The value the investor record is weighted by, for example its commitment.
    currency="...",  # optional — The currency the basis value is held in. Absent means the base currency of the map&#39;s member fund. When the basis values span more than one currency, each is translated into the fund&#39;s base currency at the spot rate on the event date, from the fund&#39;s ABOR recipe, before it weights the allocation. The rate on the event date is the latest quote at or before 00:00 UTC on that date.
    commitment_line_id="...",  # optional — For a Commitment event, the commitment line the amount is recorded against. The basis value is then the signed commitment amount itself: positive commits, negative releases. Not used for other event types.
    portfolio_id=ResourceId(...)  # optional
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

