# UnsettledTransactionCounterLegRevaluation

The receiving (counter) leg of an FX forward revalued into the fund's base currency at the valuation point's  FX rates. Populated only for FX forward transactions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **local_currency** | **str** | Optional | The currency of the FX forward&#39;s receiving (counter) leg. |
| **local_amount** | **float** | Optional | The amount of the receiving leg in its own currency. |
| **base_currency** | **str** | Optional | The fund&#39;s base currency. |
| **booked_base_amount** | **float** | Optional | The receiving leg amount in base currency at the rate booked on the transaction. Null when no booked rate was recorded. |
| **revaluation_fx_rate** | **float** | Optional | The FX rate from the counter-leg currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved. |
| **revalued_base_amount** | **float** | Optional | The receiving leg amount in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable. |
| **revaluation_fx_rate_effective_at** | **datetime** | Optional | The effective date of the quote used for the counter-leg revaluation FX rate. Null for same-currency legs or when the rate is missing. |
| **status** | **str** | Optional | Whether counter-leg revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate). |
| **problems** | [List[RevaluationProblem]](RevaluationProblem.md) | Optional | Reasons why any counter-leg amounts could not be populated. Empty when revaluation succeeded. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnsettledTransactionCounterLegRevaluation import UnsettledTransactionCounterLegRevaluation

instance = UnsettledTransactionCounterLegRevaluation(
    local_currency="...",  # optional — The currency of the FX forward&#39;s receiving (counter) leg.
    local_amount=0.0,  # optional — The amount of the receiving leg in its own currency.
    base_currency="...",  # optional — The fund&#39;s base currency.
    booked_base_amount=0.0,  # optional — The receiving leg amount in base currency at the rate booked on the transaction. Null when no booked rate was recorded.
    revaluation_fx_rate=0.0,  # optional — The FX rate from the counter-leg currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved.
    revalued_base_amount=0.0,  # optional — The receiving leg amount in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable.
    revaluation_fx_rate_effective_at=datetime.now(),  # optional — The effective date of the quote used for the counter-leg revaluation FX rate. Null for same-currency legs or when the rate is missing.
    status="...",  # optional — Whether counter-leg revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate).
    problems=[]  # optional — Reasons why any counter-leg amounts could not be populated. Empty when revaluation succeeded.
)
```

- [RevaluationProblem](RevaluationProblem.md) — used in `problems`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

