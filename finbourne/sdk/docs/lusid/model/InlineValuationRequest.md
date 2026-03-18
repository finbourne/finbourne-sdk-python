# InlineValuationRequest

Specification object for the parameters of an inline valuation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | The asAt date to use |
| **metrics** | [List[AggregateSpec]](AggregateSpec.md) | Required | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#39;Valuation/PV&#39;,&#39;Sum&#39;) for returning the PV (present value) of holdings  AggregateSpec(&#39;Holding/default/Units&#39;,&#39;Sum&#39;) for returning the units of holidays  AggregateSpec(&#39;Instrument/default/LusidInstrumentId&#39;,&#39;Value&#39;) for returning the Lusid Instrument identifier |
| **group_by** | **List[str]** | Optional | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. |
| **filters** | [List[PropertyFilter]](PropertyFilter.md) | Optional | A set of filters to use to reduce the data found in a request. Equivalent to the &#39;where ...&#39; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. |
| **sort** | [List[OrderBySpec]](OrderBySpec.md) | Optional | A (possibly empty/null) set of specifications for how to order the results. |
| **report_currency** | **str** | Optional | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place. |
| **equip_with_subtotals** | **bool** | Optional | Flag directing the Valuation call to populate the results with subtotals of aggregates. |
| **return_result_as_expanded_types** | **bool** | Optional | Financially meaningful results can be presented as either simple flat types or more complex expanded types.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied)  or as a decimal-currency pair. This flag allows either representation to be returned. In the PV example,  the returned value would be the decimal-currency pair if this flag is true, or the decimal only if this flag is false. |
| **valuation_schedule** | [ValuationSchedule](ValuationSchedule.md) | Optional | *No description available.* |
| **instruments** | [List[WeightedInstrument]](WeightedInstrument.md) | Required | The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. |
| **market_data_overrides** | [MarketDataOverrides](MarketDataOverrides.md) | Optional | *No description available.* |
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InlineValuationRequest import InlineValuationRequest

instance = InlineValuationRequest(
    recipe_id=ResourceId(...),  # optional
    as_at=datetime.now(),  # optional — The asAt date to use
    metrics=[],  # required — The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#39;Valuation/PV&#39;,&#39;Sum&#39;) for returning the PV (present value) of holdings  AggregateSpec(&#39;Holding/default/Units&#39;,&#39;Sum&#39;) for returning the units of holidays  AggregateSpec(&#39;Instrument/default/LusidInstrumentId&#39;,&#39;Value&#39;) for returning the Lusid Instrument identifier
    group_by=,  # optional — The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.
    filters=[],  # optional — A set of filters to use to reduce the data found in a request. Equivalent to the &#39;where ...&#39; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.
    sort=[],  # optional — A (possibly empty/null) set of specifications for how to order the results.
    report_currency="...",  # optional — Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.
    equip_with_subtotals=True,  # optional — Flag directing the Valuation call to populate the results with subtotals of aggregates.
    return_result_as_expanded_types=True,  # optional — Financially meaningful results can be presented as either simple flat types or more complex expanded types.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied)  or as a decimal-currency pair. This flag allows either representation to be returned. In the PV example,  the returned value would be the decimal-currency pair if this flag is true, or the decimal only if this flag is false.
    valuation_schedule=ValuationSchedule(...),  # optional
    instruments=[],  # required — The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.
    market_data_overrides=MarketDataOverrides(...),  # optional
    corporate_action_source_id=ResourceId(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [AggregateSpec](AggregateSpec.md) — used in `metrics`
- [PropertyFilter](PropertyFilter.md) — used in `filters`
- [OrderBySpec](OrderBySpec.md) — used in `sort`
- [ValuationSchedule](ValuationSchedule.md)
- [WeightedInstrument](WeightedInstrument.md) — used in `instruments`
- [MarketDataOverrides](MarketDataOverrides.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

