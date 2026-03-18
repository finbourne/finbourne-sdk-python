# ClosedPeriod

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **closed_period_id** | **str** | Optional | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period |
| **display_name** | **str** | Optional | The name of the Closed Period. |
| **description** | **str** | Optional | A description for the Closed Period. |
| **effective_start** | **datetime** | Optional | The effective start of the Closed Period |
| **effective_end** | **datetime** | Optional | The effective end of the Closed Period |
| **as_at_closed** | **datetime** | Optional | The asAt closed datetime for the Closed Period |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **post_close_activities** | [List[PostCloseActivity]](PostCloseActivity.md) | Optional | All the post close activities for the closed period. |
| **holdings_as_at_closed_override** | **datetime** | Optional | The optional AsAtClosed Override to use for building holdings in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used. |
| **valuation_as_at_closed_override** | **datetime** | Optional | The optional AsAtClosed Override to use for performing valuations in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used. |
| **branch_status** | **str** | Optional | The branch status of the closed period, e.g. Confirmed/Unconfirmed. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ClosedPeriod import ClosedPeriod

instance = ClosedPeriod(
    closed_period_id="...",  # optional — The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period
    display_name="...",  # optional — The name of the Closed Period.
    description="...",  # optional — A description for the Closed Period.
    effective_start=datetime.now(),  # optional — The effective start of the Closed Period
    effective_end=datetime.now(),  # optional — The effective end of the Closed Period
    as_at_closed=datetime.now(),  # optional — The asAt closed datetime for the Closed Period
    properties=ModelProperty(...),  # optional — The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain.
    version=Version(...),  # optional
    post_close_activities=[],  # optional — All the post close activities for the closed period.
    holdings_as_at_closed_override=datetime.now(),  # optional — The optional AsAtClosed Override to use for building holdings in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used.
    valuation_as_at_closed_override=datetime.now(),  # optional — The optional AsAtClosed Override to use for performing valuations in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used.
    branch_status="...",  # optional — The branch status of the closed period, e.g. Confirmed/Unconfirmed.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [PostCloseActivity](PostCloseActivity.md) — used in `post_close_activities`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

