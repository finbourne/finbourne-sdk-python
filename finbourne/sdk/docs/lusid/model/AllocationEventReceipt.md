# AllocationEventReceipt

One receipt of cash against a booked capital call, as recorded.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Optional | The investor record the cash came from. |
| **amount** | **float** | Optional | The cash received, in the event currency after any FX conversion. |
| **receipt_date** | **datetime** | Optional | The date the cash was received. |
| **applied** | **float** | Optional | How much of the receipt was applied to what the investor owed. |
| **refund** | **float** | Optional | How much of the receipt exceeded what the investor owed and became a refund payable. |
| **payment_currency** | **str** | Optional | The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency. |
| **payment_fx_rate** | **float** | Optional | The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency. |
| **fx_difference** | **float** | Optional | The part of the difference between the payment converted at the notice rate and at the payment rate that the fund did not absorb; positive when the rate moved against the fund. Zero without a notice rate. |
| **bank_charge** | **float** | Optional | Any bank charge deducted from the cash before it arrived, in the event currency. |
| **bank_charge_bearer** | **str** | Optional | Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy. |
| **shortfall_written_off** | **float** | Optional | Any small shortfall within the map&#39;s tolerance that was written off rather than left outstanding. |
| **posting_id** | **str** | Optional | The identifier of the receipt posting on the investor&#39;s line. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventReceipt import AllocationEventReceipt

instance = AllocationEventReceipt(
    investor_record_id="...",  # optional — The investor record the cash came from.
    amount=0.0,  # optional — The cash received, in the event currency after any FX conversion.
    receipt_date=datetime.now(),  # optional — The date the cash was received.
    applied=0.0,  # optional — How much of the receipt was applied to what the investor owed.
    refund=0.0,  # optional — How much of the receipt exceeded what the investor owed and became a refund payable.
    payment_currency="...",  # optional — The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency.
    payment_fx_rate=0.0,  # optional — The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency.
    fx_difference=0.0,  # optional — The part of the difference between the payment converted at the notice rate and at the payment rate that the fund did not absorb; positive when the rate moved against the fund. Zero without a notice rate.
    bank_charge=0.0,  # optional — Any bank charge deducted from the cash before it arrived, in the event currency.
    bank_charge_bearer="...",  # optional — Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy.
    shortfall_written_off=0.0,  # optional — Any small shortfall within the map&#39;s tolerance that was written off rather than left outstanding.
    posting_id="..."  # optional — The identifier of the receipt posting on the investor&#39;s line.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

