# TaxClassificationDetail

A single instrument's classification with the version history of every input behind it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **classification** | [TaxClassification](TaxClassification.md) | Required | *No description available.* |
| **history** | [List[TaxClassificationFieldVersion]](TaxClassificationFieldVersion.md) | Required | Every version of every classification input and override for the instrument, oldest first. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationDetail import TaxClassificationDetail

instance = TaxClassificationDetail(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    classification=TaxClassification(...),  # required
    history=[],  # required — Every version of every classification input and override for the instrument, oldest first.
    links=[]  # optional
)
```

- [TaxClassification](TaxClassification.md)
- [TaxClassificationFieldVersion](TaxClassificationFieldVersion.md) — used in `history`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

