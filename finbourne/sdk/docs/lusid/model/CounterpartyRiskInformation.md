# CounterpartyRiskInformation

In the event that the legal entity is a counterparty to an OTC transaction  (as signatory to a counterparty agreement such as an ISDA 2002 Master Agreement),  this information would be needed for calculations  such as Credit-Valuation-Adjustments and Debit-Valuation-Adjustments (CVA, DVA, XVA etc).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **country_of_risk** | **str** | Required | The country to which one would naturally ascribe risk, typically the legal entity&#39;s country of registration. This can be used to infer funding currency and related market data in the absence of a specific preference. |
| **credit_ratings** | [List[CreditRating]](CreditRating.md) | Required |  |
| **industry_classifiers** | [List[IndustryClassifier]](IndustryClassifier.md) | Required |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CounterpartyRiskInformation import CounterpartyRiskInformation

instance = CounterpartyRiskInformation(
    country_of_risk="...",  # required — The country to which one would naturally ascribe risk, typically the legal entity&#39;s country of registration. This can be used to infer funding currency and related market data in the absence of a specific preference.
    credit_ratings=[],  # required — 
    industry_classifiers=[]  # required — 
)
```

- [CreditRating](CreditRating.md) — used in `credit_ratings`
- [IndustryClassifier](IndustryClassifier.md) — used in `industry_classifiers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

