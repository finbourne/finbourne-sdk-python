# CreateComplianceTemplateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Compliance Template |
| **description** | **str** | Required | The description of the Compliance Template |
| **variations** | [List[ComplianceTemplateVariationRequest]](ComplianceTemplateVariationRequest.md) | Required | Variation details of a Compliance Template |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateComplianceTemplateRequest import CreateComplianceTemplateRequest

instance = CreateComplianceTemplateRequest(
    code="...",  # required — The code given for the Compliance Template
    description="...",  # required — The description of the Compliance Template
    variations=[]  # required — Variation details of a Compliance Template
)
```

- [ComplianceTemplateVariationRequest](ComplianceTemplateVariationRequest.md) — used in `variations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

