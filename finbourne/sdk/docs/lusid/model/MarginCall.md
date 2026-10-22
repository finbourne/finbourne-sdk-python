# MarginCall

A margin call a run produced under a collateral agreement: our figure, the counterparty's demand once recorded  and how they compare, and where the call is in its lifecycle.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The URI of this margin call. |
| **id** | **str** | Required | The identifier of the call: the run id and the call&#39;s business key joined with &#39;/&#39;. |
| **run_id** | **str** | Required | The run that produced the call. Filterable. |
| **agreement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **counterparty** | [CounterpartyIdentifier](CounterpartyIdentifier.md) | Optional | *No description available.* |
| **item** | **str** | Required | The margin item of the agreement the call is for. Filterable. |
| **margin_type** | **str** | Required | The type of margin called. Currently VariationMargin. Filterable. |
| **method** | **str** | Optional | The calculation method of the margin item. |
| **settlement** | **str** | Optional | Whether the item is settled or collateralised. |
| **direction** | **str** | Required | Who posts: WePost, TheyPost or None when the exposure is flat. Filterable. |
| **currency** | **str** | Required | The currency of the call, the agreement&#39;s base currency. Filterable. |
| **required** | **float** | Required | The margin required under the agreement, signed as the call. |
| **held** | **float** | Required | The collateral already held against the item, signed as the call. |
| **call** | **float** | Required | Our figure for the amount to move: required less held. Filterable. |
| **match_tolerance** | **float** | Optional | The agreement&#39;s match tolerance captured on the call. |
| **counterparty_demand** | **float** | Optional | The counterparty&#39;s figure for the call, once recorded. |
| **difference** | **float** | Optional | The counterparty&#39;s demand less our call, once recorded. |
| **match_status** | **str** | Required | How the counterparty&#39;s demand compares to our call. One of Unmatched, Matched, WithinTolerance, Break or NotRequired. Filterable. |
| **demand_received_at** | **datetime** | Optional | When the counterparty&#39;s demand was received. |
| **statement_reference** | **str** | Optional | A reference to the counterparty&#39;s statement, such as a Drive path. |
| **demand_note** | **str** | Optional | A note recorded with the counterparty&#39;s demand. |
| **agreed_amount** | **float** | Optional | The amount agreed to move, once the call is accepted or disputed. |
| **disputed_amount** | **float** | Optional | The part of the larger of our call and the counterparty&#39;s demand left in dispute. |
| **dispute_reason** | **str** | Optional | Why the call is disputed. |
| **dispute_owner** | **str** | Optional | Who owns the dispute. |
| **state** | **str** | Required | Where the call is in its lifecycle. One of Calculated, Accepted or Disputed. Filterable. |
| **deadline** | **datetime** | Optional | The time the call must be agreed by. Empty until agreements carry a notification time. |
| **supersedes** | [MarginCallReference](MarginCallReference.md) | Optional | *No description available.* |
| **carried_from** | [MarginCallReference](MarginCallReference.md) | Optional | *No description available.* |
| **carried_disputed_amount** | **float** | Optional | The amount left in dispute on the carried call. Informational; not added to this call. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginCall import MarginCall

instance = MarginCall(
    href="...",  # optional — The URI of this margin call.
    id="...",  # required — The identifier of the call: the run id and the call&#39;s business key joined with &#39;/&#39;.
    run_id="...",  # required — The run that produced the call. Filterable.
    agreement_id=ResourceId(...),  # required
    counterparty=CounterpartyIdentifier(...),  # optional
    item="...",  # required — The margin item of the agreement the call is for. Filterable.
    margin_type="...",  # required — The type of margin called. Currently VariationMargin. Filterable.
    method="...",  # optional — The calculation method of the margin item.
    settlement="...",  # optional — Whether the item is settled or collateralised.
    direction="...",  # required — Who posts: WePost, TheyPost or None when the exposure is flat. Filterable.
    currency="...",  # required — The currency of the call, the agreement&#39;s base currency. Filterable.
    required=0.0,  # required — The margin required under the agreement, signed as the call.
    held=0.0,  # required — The collateral already held against the item, signed as the call.
    call=0.0,  # required — Our figure for the amount to move: required less held. Filterable.
    match_tolerance=0.0,  # optional — The agreement&#39;s match tolerance captured on the call.
    counterparty_demand=0.0,  # optional — The counterparty&#39;s figure for the call, once recorded.
    difference=0.0,  # optional — The counterparty&#39;s demand less our call, once recorded.
    match_status="...",  # required — How the counterparty&#39;s demand compares to our call. One of Unmatched, Matched, WithinTolerance, Break or NotRequired. Filterable.
    demand_received_at=datetime.now(),  # optional — When the counterparty&#39;s demand was received.
    statement_reference="...",  # optional — A reference to the counterparty&#39;s statement, such as a Drive path.
    demand_note="...",  # optional — A note recorded with the counterparty&#39;s demand.
    agreed_amount=0.0,  # optional — The amount agreed to move, once the call is accepted or disputed.
    disputed_amount=0.0,  # optional — The part of the larger of our call and the counterparty&#39;s demand left in dispute.
    dispute_reason="...",  # optional — Why the call is disputed.
    dispute_owner="...",  # optional — Who owns the dispute.
    state="...",  # required — Where the call is in its lifecycle. One of Calculated, Accepted or Disputed. Filterable.
    deadline=datetime.now(),  # optional — The time the call must be agreed by. Empty until agreements carry a notification time.
    supersedes=MarginCallReference(...),  # optional
    carried_from=MarginCallReference(...),  # optional
    carried_disputed_amount=0.0  # optional — The amount left in dispute on the carried call. Informational; not added to this call.
)
```

- [ResourceId](ResourceId.md)
- [CounterpartyIdentifier](CounterpartyIdentifier.md)
- [MarginCallReference](MarginCallReference.md)
- [MarginCallReference](MarginCallReference.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

