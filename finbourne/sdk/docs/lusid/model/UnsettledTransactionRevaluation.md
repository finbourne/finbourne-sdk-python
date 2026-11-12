# UnsettledTransactionRevaluation

The transaction's total consideration in base currency, both at the rate it was booked at and revalued at the  valuation point's FX rate. Rates and amounts are null when they could not be resolved; Problems explains why.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **local_currency** | **str** | Optional | The settlement currency of the transaction (the &#39;local&#39; currency for revaluation purposes). |
| **local_amount** | **float** | Optional | The total consideration in the settlement currency, as booked. |
| **base_currency** | **str** | Optional | The fund&#39;s base currency. |
| **base_fx_rate** | **float** | Optional | The FX rate from settlement currency to base currency at the time the transaction was booked. Null when no booked rate was recorded. |
| **base_amount** | **float** | Optional | The total consideration in base currency at the booked FX rate. Null when the booked rate is unavailable. |
| **revaluation_fx_rate** | **float** | Optional | The FX rate from settlement currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved. |
| **revalued_base_amount** | **float** | Optional | The total consideration in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable. |
| **revaluation_fx_rate_effective_at** | **datetime** | Optional | The effective date of the quote used for the revaluation FX rate. Null for same-currency transactions or when the rate is missing. |
| **status** | **str** | Optional | Whether revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate). |
| **problems** | [List[RevaluationProblem]](RevaluationProblem.md) | Optional | Reasons why any of the amounts could not be populated. Empty when revaluation succeeded. |
| **counter_leg** | [UnsettledTransactionCounterLegRevaluation](UnsettledTransactionCounterLegRevaluation.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnsettledTransactionRevaluation import UnsettledTransactionRevaluation

instance = UnsettledTransactionRevaluation(
    local_currency="...",  # optional — The settlement currency of the transaction (the &#39;local&#39; currency for revaluation purposes).
    local_amount=0.0,  # optional — The total consideration in the settlement currency, as booked.
    base_currency="...",  # optional — The fund&#39;s base currency.
    base_fx_rate=0.0,  # optional — The FX rate from settlement currency to base currency at the time the transaction was booked. Null when no booked rate was recorded.
    base_amount=0.0,  # optional — The total consideration in base currency at the booked FX rate. Null when the booked rate is unavailable.
    revaluation_fx_rate=0.0,  # optional — The FX rate from settlement currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved.
    revalued_base_amount=0.0,  # optional — The total consideration in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable.
    revaluation_fx_rate_effective_at=datetime.now(),  # optional — The effective date of the quote used for the revaluation FX rate. Null for same-currency transactions or when the rate is missing.
    status="...",  # optional — Whether revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate).
    problems=[],  # optional — Reasons why any of the amounts could not be populated. Empty when revaluation succeeded.
    counter_leg=UnsettledTransactionCounterLegRevaluation(...)  # optional
)
```

- [RevaluationProblem](RevaluationProblem.md) — used in `problems`
- [UnsettledTransactionCounterLegRevaluation](UnsettledTransactionCounterLegRevaluation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

