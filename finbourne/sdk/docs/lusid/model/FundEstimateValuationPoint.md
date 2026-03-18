# FundEstimateValuationPoint

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry. |
| **nav_type_code** | **str** | Required | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. |
| **timeline_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **previous_entry** | [PreviousFundCalendarEntry](PreviousFundCalendarEntry.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Optional | The effective at of the Calendar Entry. |
| **entry_type** | **str** | Required | The type of the Fund Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark |
| **status** | **str** | Optional | The status of the Fund Calendar Entry. Can be &#39;Estimate&#39;, &#39;Unofficial&#39; or &#39;Final&#39;. |
| **apply_clear_down** | **bool** | Optional | Set to true if that closed period should have the clear down applied. |
| **leader_nav_type_code** | **str** | Optional | The code of the Nav Type that this Nav Type will follow when set. |
| **variants** | [List[EstimateVariant]](EstimateVariant.md) | Optional | The variants of the Estimate Valuation Point.  |
| **fund_calendar_entries_type** | **str** | Required | The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundEstimateValuationPoint import FundEstimateValuationPoint

instance = FundEstimateValuationPoint(
    code="...",  # required — The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry.
    nav_type_code="...",  # required — The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with.
    timeline_id=ResourceId(...),  # optional
    previous_entry=PreviousFundCalendarEntry(...),  # optional
    effective_at=datetime.now(),  # optional — The effective at of the Calendar Entry.
    entry_type="...",  # required — The type of the Fund Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark
    status="...",  # optional — The status of the Fund Calendar Entry. Can be &#39;Estimate&#39;, &#39;Unofficial&#39; or &#39;Final&#39;.
    apply_clear_down=True,  # optional — Set to true if that closed period should have the clear down applied.
    leader_nav_type_code="...",  # optional — The code of the Nav Type that this Nav Type will follow when set.
    variants=[],  # optional — The variants of the Estimate Valuation Point. 
    fund_calendar_entries_type="..."  # required — The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark
)
```

- [ResourceId](ResourceId.md)
- [PreviousFundCalendarEntry](PreviousFundCalendarEntry.md)
- [EstimateVariant](EstimateVariant.md) — used in `variants`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

