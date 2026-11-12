# CollateralAllocation

Which of our assets to move for a margin call and why: every holding considered, with its rank or the constraint  that excluded it, and the lines chosen cheapest first, each carrying what a transaction moving it needs. Amounts  are in the agreement's base currency.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run the call belongs to. |
| **call_id** | **str** | Required | The business key of the call within the run: agreement scope and code, item, margin type and direction joined with &#39;/&#39;. |
| **direction** | **str** | Required | Whether the collateral is delivered to the counterparty or recalled from it. One of Deliver or Recall. |
| **inventory_source** | **str** | Required | Where the holdings were read from: RunStore for the proposal the run made, Live for a ranking against the holdings as they stand now. |
| **as_at** | **datetime** | Required | The asAt the holdings and terms were read at. |
| **agreement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **item** | **str** | Optional | The margin item of the call. |
| **counterparty** | [CounterpartyIdentifier](CounterpartyIdentifier.md) | Optional | *No description available.* |
| **business_date** | **datetime** | Optional | The business date of the call, which a transaction for a line trades on. |
| **deadline** | **datetime** | Optional | When the movement must have settled under the agreement&#39;s cut label. Null when the agreement sets none. |
| **margin_account** | **str** | Optional | The code of the custodian account the item names for collateral we post, which a delivery moves assets into and a recall moves them out of. Null when the item names none. |
| **base_currency** | **str** | Required | The agreement&#39;s base currency, which every amount is in. |
| **required_amount** | **float** | Required | The collateral value to deliver, or for a recall the excess to take back. |
| **covered_amount** | **float** | Required | The collateral value of the lines chosen: below the requirement when the inventory ran out, above it when a lot could not be split. |
| **carry_per_day** | **float** | Required | What the chosen lines cost the fund a day to leave locked up, in the base currency. |
| **all_cash_carry_per_day** | **float** | Optional | What covering the whole call in base-currency cash would cost a day. Null when the cash rate is unavailable or for a recall. |
| **candidates** | [List[CollateralAllocationCandidate]](CollateralAllocationCandidate.md) | Required | Every holding considered, ranked ones first by rank, then the excluded with the constraint that excluded them. |
| **allocation** | [List[CollateralAllocationLine]](CollateralAllocationLine.md) | Required | The assets chosen, cheapest first, each with what a transaction moving it needs. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAllocation import CollateralAllocation

instance = CollateralAllocation(
    run_id="...",  # required — The run the call belongs to.
    call_id="...",  # required — The business key of the call within the run: agreement scope and code, item, margin type and direction joined with &#39;/&#39;.
    direction="...",  # required — Whether the collateral is delivered to the counterparty or recalled from it. One of Deliver or Recall.
    inventory_source="...",  # required — Where the holdings were read from: RunStore for the proposal the run made, Live for a ranking against the holdings as they stand now.
    as_at=datetime.now(),  # required — The asAt the holdings and terms were read at.
    agreement_id=ResourceId(...),  # optional
    item="...",  # optional — The margin item of the call.
    counterparty=CounterpartyIdentifier(...),  # optional
    business_date=datetime.now(),  # optional — The business date of the call, which a transaction for a line trades on.
    deadline=datetime.now(),  # optional — When the movement must have settled under the agreement&#39;s cut label. Null when the agreement sets none.
    margin_account="...",  # optional — The code of the custodian account the item names for collateral we post, which a delivery moves assets into and a recall moves them out of. Null when the item names none.
    base_currency="...",  # required — The agreement&#39;s base currency, which every amount is in.
    required_amount=0.0,  # required — The collateral value to deliver, or for a recall the excess to take back.
    covered_amount=0.0,  # required — The collateral value of the lines chosen: below the requirement when the inventory ran out, above it when a lot could not be split.
    carry_per_day=0.0,  # required — What the chosen lines cost the fund a day to leave locked up, in the base currency.
    all_cash_carry_per_day=0.0,  # optional — What covering the whole call in base-currency cash would cost a day. Null when the cash rate is unavailable or for a recall.
    candidates=[],  # required — Every holding considered, ranked ones first by rank, then the excluded with the constraint that excluded them.
    allocation=[]  # required — The assets chosen, cheapest first, each with what a transaction moving it needs.
)
```

- [ResourceId](ResourceId.md)
- [CounterpartyIdentifier](CounterpartyIdentifier.md)
- [CollateralAllocationCandidate](CollateralAllocationCandidate.md) — used in `candidates`
- [CollateralAllocationLine](CollateralAllocationLine.md) — used in `allocation`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

