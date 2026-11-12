# TaxClassificationException

Why an instrument could not be classified, or a flip of the qualifying-investments test a reviewer must see.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **kind** | **str** | Required | MissingInputs, ConflictingSetup, ConflictingOverride or QualifyingInvestmentsCrossing. Available values: MissingInputs, ConflictingSetup, ConflictingOverride, QualifyingInvestmentsCrossing. |
| **code** | **str** | Required | The stable code of the exception, for filtering and routing. |
| **message** | **str** | Required | A description of why the instrument could not be classified or why the crossing was raised. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationException import TaxClassificationException

instance = TaxClassificationException(
    kind="...",  # required — MissingInputs, ConflictingSetup, ConflictingOverride or QualifyingInvestmentsCrossing. Available values: MissingInputs, ConflictingSetup, ConflictingOverride, QualifyingInvestmentsCrossing.
    code="...",  # required — The stable code of the exception, for filtering and routing.
    message="..."  # required — A description of why the instrument could not be classified or why the crossing was raised.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

