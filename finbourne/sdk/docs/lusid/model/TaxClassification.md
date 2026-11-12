# TaxClassification

The UK life-company tax classification of one instrument at one effective and asAt point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **luid** | **str** | Required | The LUSID instrument identifier of the classified instrument. |
| **instrument_name** | **str** | Optional | The name of the classified instrument. |
| **instrument_type** | **str** | Optional | The LUSID instrument type of the classified instrument, where known. |
| **within_blagab** | **bool** | Optional | Whether the instrument is held within the basic life assurance and general annuity business of the fund. Absent when the input has not been set. |
| **inputs** | [TaxClassificationInputs](TaxClassificationInputs.md) | Required | *No description available.* |
| **treatment_override** | **str** | Optional | The user-supplied treatment leaf that replaces the system-derived one, if any. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. |
| **leaf** | **str** | Optional | The treatment leaf the decision tree arrived at. Absent when the instrument could not be classified. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. |
| **treatment** | **str** | Required | The tax treatment class implied by the leaf: ChargeableGains, LoanRelationship, Excluded or Unclassified. Available values: ChargeableGains, LoanRelationship, Excluded, Unclassified. |
| **status** | **str** | Required | Classified, Overridden, Rejected or Unclassified. Available values: Classified, Overridden, Rejected, Unclassified. |
| **source** | **str** | Required | Whether the leaf came from the System decision tree or a User override. Available values: System, User. |
| **rule_fired** | **str** | Required | The name of the decision-tree rule that produced the leaf. |
| **trace** | [List[TaxClassificationDecisionStep]](TaxClassificationDecisionStep.md) | Optional | The ordered questions the decision tree asked and the answers it took, for audit. |
| **exception** | [TaxClassificationException](TaxClassificationException.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Required | The effective date the classification was evaluated at. |
| **as_at** | **datetime** | Required | The asAt time the classification was evaluated at. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassification import TaxClassification

instance = TaxClassification(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    luid="...",  # required — The LUSID instrument identifier of the classified instrument.
    instrument_name="...",  # optional — The name of the classified instrument.
    instrument_type="...",  # optional — The LUSID instrument type of the classified instrument, where known.
    within_blagab=True,  # optional — Whether the instrument is held within the basic life assurance and general annuity business of the fund. Absent when the input has not been set.
    inputs=TaxClassificationInputs(...),  # required
    treatment_override="...",  # optional — The user-supplied treatment leaf that replaces the system-derived one, if any. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt.
    leaf="...",  # optional — The treatment leaf the decision tree arrived at. Absent when the instrument could not be classified. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt.
    treatment="...",  # required — The tax treatment class implied by the leaf: ChargeableGains, LoanRelationship, Excluded or Unclassified. Available values: ChargeableGains, LoanRelationship, Excluded, Unclassified.
    status="...",  # required — Classified, Overridden, Rejected or Unclassified. Available values: Classified, Overridden, Rejected, Unclassified.
    source="...",  # required — Whether the leaf came from the System decision tree or a User override. Available values: System, User.
    rule_fired="...",  # required — The name of the decision-tree rule that produced the leaf.
    trace=[],  # optional — The ordered questions the decision tree asked and the answers it took, for audit.
    exception=TaxClassificationException(...),  # optional
    effective_at=datetime.now(),  # required — The effective date the classification was evaluated at.
    as_at=datetime.now(),  # required — The asAt time the classification was evaluated at.
    links=[]  # optional
)
```

- [TaxClassificationInputs](TaxClassificationInputs.md)
- [TaxClassificationDecisionStep](TaxClassificationDecisionStep.md) — used in `trace`
- [TaxClassificationException](TaxClassificationException.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

