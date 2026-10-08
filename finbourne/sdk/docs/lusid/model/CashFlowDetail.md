# CashFlowDetail

An individual cashflow inside a cashflow bucket, annotated with the source that produced it  in the cash flow waterfall (SRS > Transaction > Instrument).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Required | The date on which the cashflow is paid. |
| **amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **source_type** | **str** | Required | The source that produced the cashflow in the cash flow waterfall. One of &#39;Instrument&#39; (produced by the valuation engine), &#39;Transaction&#39; (produced from a booked transaction or movement) or &#39;SRS&#39; (sourced from the structured results store). |
| **instrument_id** | **str** | Required | The LUSID instrument identifier of the instrument that produced the cashflow. |
| **instrument_display_name** | **str** | Optional | The display name of the instrument that produced the cashflow. Not present when the instrument cannot be resolved (e.g. deleted, no permission). |
| **transaction_id** | **str** | Optional | The identifier of the transaction from which the cashflow originates, where known. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **flow_type** | **str** | Optional | The type of the cashflow, e.g. Coupon, Principal or Premium. |
| **movement_name** | **str** | Optional | The name of the movement that produced the cashflow (e.g. Coupon, Side1), falling back to the flow type when the movement is unnamed. Not present when the cashflow could not be valued. |
| **pay_receive** | **str** | Optional | Indicates whether the cashflow is paid or received. |
| **gross_amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **haircut_fraction** | **float** | Optional | The fraction of the gross amount removed by the haircut, in the range [0, 1]. Zero for outflows and for cashflows no rule matched. Only populated when haircut rules were supplied on the request. |
| **net_amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **haircut_rule_applied** | **str** | Optional | The identifier of the haircut rule that was applied to the cashflow, or not present when no rule matched or no haircut rules were supplied on the request. |
| **error** | **str** | Optional | Present when the cashflow could not be valued, for example because of missing market data: the valuation error, matching the CashflowError diagnostic reported by the QueryCashFlows endpoint. In that case the amount is null rather than zero. Error may also be set when only the report-currency FX lookup failed (see ReportCurrencyAmount), in which case the base Amount remains populated and only ReportCurrencyAmount and TradeToReportCurrencyRate are null. |
| **report_currency_amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **trade_to_report_currency_rate** | **float** | Optional | The FX rate used to convert the cashflow amount from its own payment currency (see Amount) into the request&#39;s report currency, resolved at the cashflow&#39;s transaction (trade) date, not its payment date. Only present when ReportCurrency was supplied on the request; not present when it was omitted, or when the rate could not be resolved (see Error). |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowDetail import CashFlowDetail

instance = CashFlowDetail(
    payment_date=datetime.now(),  # required — The date on which the cashflow is paid.
    amount=CurrencyAndAmount(...),  # optional
    source_type="...",  # required — The source that produced the cashflow in the cash flow waterfall. One of &#39;Instrument&#39; (produced by the valuation engine), &#39;Transaction&#39; (produced from a booked transaction or movement) or &#39;SRS&#39; (sourced from the structured results store).
    instrument_id="...",  # required — The LUSID instrument identifier of the instrument that produced the cashflow.
    instrument_display_name="...",  # optional — The display name of the instrument that produced the cashflow. Not present when the instrument cannot be resolved (e.g. deleted, no permission).
    transaction_id="...",  # optional — The identifier of the transaction from which the cashflow originates, where known.
    portfolio_id=ResourceId(...),  # required
    flow_type="...",  # optional — The type of the cashflow, e.g. Coupon, Principal or Premium.
    movement_name="...",  # optional — The name of the movement that produced the cashflow (e.g. Coupon, Side1), falling back to the flow type when the movement is unnamed. Not present when the cashflow could not be valued.
    pay_receive="...",  # optional — Indicates whether the cashflow is paid or received.
    gross_amount=CurrencyAndAmount(...),  # optional
    haircut_fraction=0.0,  # optional — The fraction of the gross amount removed by the haircut, in the range [0, 1]. Zero for outflows and for cashflows no rule matched. Only populated when haircut rules were supplied on the request.
    net_amount=CurrencyAndAmount(...),  # optional
    haircut_rule_applied="...",  # optional — The identifier of the haircut rule that was applied to the cashflow, or not present when no rule matched or no haircut rules were supplied on the request.
    error="...",  # optional — Present when the cashflow could not be valued, for example because of missing market data: the valuation error, matching the CashflowError diagnostic reported by the QueryCashFlows endpoint. In that case the amount is null rather than zero. Error may also be set when only the report-currency FX lookup failed (see ReportCurrencyAmount), in which case the base Amount remains populated and only ReportCurrencyAmount and TradeToReportCurrencyRate are null.
    report_currency_amount=CurrencyAndAmount(...),  # optional
    trade_to_report_currency_rate=0.0,  # optional — The FX rate used to convert the cashflow amount from its own payment currency (see Amount) into the request&#39;s report currency, resolved at the cashflow&#39;s transaction (trade) date, not its payment date. Only present when ReportCurrency was supplied on the request; not present when it was omitted, or when the rate could not be resolved (see Error).
    links=[]  # optional
)
```

- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

