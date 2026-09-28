# WithholdingTaxDataset

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the relational dataset definition. |
| **code** | **str** | Required | The code of the relational dataset definition. Together with the scope this uniquely identifies the definition. |
| **dimensions** | [List[SeriesIdentifierField]](SeriesIdentifierField.md) | Required | The dimensions created on this dataset as series identifiers, as stored. The mandatory core is not returned here; read the full field schema from the relational dataset definition at Href. |
| **href** | **str** | Optional | The specific Uri of the relational dataset definition. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxDataset import WithholdingTaxDataset

instance = WithholdingTaxDataset(
    scope="...",  # required — The scope of the relational dataset definition.
    code="...",  # required — The code of the relational dataset definition. Together with the scope this uniquely identifies the definition.
    dimensions=[],  # required — The dimensions created on this dataset as series identifiers, as stored. The mandatory core is not returned here; read the full field schema from the relational dataset definition at Href.
    href="...",  # optional — The specific Uri of the relational dataset definition.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [SeriesIdentifierField](SeriesIdentifierField.md) — used in `dimensions`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

