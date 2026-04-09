# FundBookmark

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry. |
| **display_name** | **str** | Required | The name of the Fund Calendar entry. |
| **description** | **str** | Optional | A description for the Fund Calendar entry. |
| **nav_type_code** | **str** | Required | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. |
| **timeline_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **previous_entry** | [PreviousFundCalendarEntry](PreviousFundCalendarEntry.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Optional | The effective at of the Calendar Entry. |
| **as_at** | **datetime** | Required | The asAt datetime for the Calendar Entry. |
| **entry_type** | **str** | Required | The type of the Fund Calendar Entry. The available values are: ValuationPointFundCalendarEntry, BookmarkFundCalendarEntry |
| **status** | **str** | Optional | The status of the Fund Calendar Entry. Can be &#39;Estimate&#39;, &#39;Unofficial&#39; or &#39;Final&#39;. |
| **apply_clear_down** | **bool** | Optional | Set to true if that closed period should have the clear down applied. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. |
| **leader_nav_type_code** | **str** | Optional | The code of the Nav Type that this Nav Type will follow when set. |
| **fund_calendar_entries_type** | **str** | Required | The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundBookmark import FundBookmark

instance = FundBookmark(
    code="...",  # required — The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry.
    display_name="...",  # required — The name of the Fund Calendar entry.
    description="...",  # optional — A description for the Fund Calendar entry.
    nav_type_code="...",  # required — The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with.
    timeline_id=ResourceId(...),  # optional
    previous_entry=PreviousFundCalendarEntry(...),  # optional
    effective_at=datetime.now(),  # optional — The effective at of the Calendar Entry.
    as_at=datetime.now(),  # required — The asAt datetime for the Calendar Entry.
    entry_type="...",  # required — The type of the Fund Calendar Entry. The available values are: ValuationPointFundCalendarEntry, BookmarkFundCalendarEntry
    status="...",  # optional — The status of the Fund Calendar Entry. Can be &#39;Estimate&#39;, &#39;Unofficial&#39; or &#39;Final&#39;.
    apply_clear_down=True,  # optional — Set to true if that closed period should have the clear down applied.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt.
    valuations_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt.
    properties=ModelProperty(...),  # optional — The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain.
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.
    leader_nav_type_code="...",  # optional — The code of the Nav Type that this Nav Type will follow when set.
    fund_calendar_entries_type="..."  # required — The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark
)
```

- [ResourceId](ResourceId.md)
- [PreviousFundCalendarEntry](PreviousFundCalendarEntry.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

