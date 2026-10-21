# WithholdingTaxResolution

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **resolution_status** | **str** | Required | Match or NoMatch: the status booking stamps on a transaction. |
| **matched_rule** | [WithholdingTaxMatchedRule](WithholdingTaxMatchedRule.md) | Optional | *No description available.* |
| **rate_tiers** | [WithholdingTaxRateTiers](WithholdingTaxRateTiers.md) | Optional | *No description available.* |
| **ras_flags** | [WithholdingTaxReliefAtSourceFlags](WithholdingTaxReliefAtSourceFlags.md) | Optional | *No description available.* |
| **derived_split** | [WithholdingTaxRateSplit](WithholdingTaxRateSplit.md) | Optional | *No description available.* |
| **provenance** | [WithholdingTaxResolutionProvenance](WithholdingTaxResolutionProvenance.md) | Optional | *No description available.* |
| **resolved_dimensions** | **Dict[str, Optional[str]]** | Required | Each dimension of either dataset, with the value used. Null where there is no value. |
| **is_what_if** | **bool** | Required | False when the saved configuration&#39;s datasets and source order are used as they are. True when a dataset or the source order differs from the configuration&#39;s, or when no configuration was given. |
| **unresolved_dimensions** | [Dict[str, WithholdingTaxUnresolvedDimension]](WithholdingTaxUnresolvedDimension.md) | Required | Each dimension that booking reads from the transaction, portfolio or fund, that dimensions does not supply, and that a couldAlsoMatch entry needs. It is null, so only rows blank on it match. Empty in Raw mode. |
| **could_also_match** | [List[WithholdingTaxAlternativeMatch]](WithholdingTaxAlternativeMatch.md) | Required | Each other row that booking would choose with its own values for the unresolved dimensions, fewest values first, up to the limit. Where one entry&#39;s values include another&#39;s, the one with more values applies. |
| **has_more_alternatives** | **bool** | Required | True when the limit stopped the lookup before it tried every combination of values, so couldAlsoMatch may miss rows. Ask again with a higher limit. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxResolution import WithholdingTaxResolution

instance = WithholdingTaxResolution(
    resolution_status="...",  # required — Match or NoMatch: the status booking stamps on a transaction.
    matched_rule=WithholdingTaxMatchedRule(...),  # optional
    rate_tiers=WithholdingTaxRateTiers(...),  # optional
    ras_flags=WithholdingTaxReliefAtSourceFlags(...),  # optional
    derived_split=WithholdingTaxRateSplit(...),  # optional
    provenance=WithholdingTaxResolutionProvenance(...),  # optional
    resolved_dimensions=,  # required — Each dimension of either dataset, with the value used. Null where there is no value.
    is_what_if=True,  # required — False when the saved configuration&#39;s datasets and source order are used as they are. True when a dataset or the source order differs from the configuration&#39;s, or when no configuration was given.
    unresolved_dimensions=WithholdingTaxUnresolvedDimension(...),  # required — Each dimension that booking reads from the transaction, portfolio or fund, that dimensions does not supply, and that a couldAlsoMatch entry needs. It is null, so only rows blank on it match. Empty in Raw mode.
    could_also_match=[],  # required — Each other row that booking would choose with its own values for the unresolved dimensions, fewest values first, up to the limit. Where one entry&#39;s values include another&#39;s, the one with more values applies.
    has_more_alternatives=True  # required — True when the limit stopped the lookup before it tried every combination of values, so couldAlsoMatch may miss rows. Ask again with a higher limit.
)
```

- [WithholdingTaxMatchedRule](WithholdingTaxMatchedRule.md)
- [WithholdingTaxRateTiers](WithholdingTaxRateTiers.md)
- [WithholdingTaxReliefAtSourceFlags](WithholdingTaxReliefAtSourceFlags.md)
- [WithholdingTaxRateSplit](WithholdingTaxRateSplit.md)
- [WithholdingTaxResolutionProvenance](WithholdingTaxResolutionProvenance.md)
- [WithholdingTaxUnresolvedDimension](WithholdingTaxUnresolvedDimension.md) — used in `unresolved_dimensions`
- [WithholdingTaxAlternativeMatch](WithholdingTaxAlternativeMatch.md) — used in `could_also_match`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

