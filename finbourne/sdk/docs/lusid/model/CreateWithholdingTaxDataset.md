# CreateWithholdingTaxDataset

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the relational dataset definition. |
| **code** | **str** | Required | The code of the relational dataset definition. Together with the scope this uniquely identifies the definition. |
| **dimensions** | [List[CreateSeriesIdentifierField]](CreateSeriesIdentifierField.md) | Optional | The dimensions, over and above the mandatory core, that this dataset is matched on. Fully customer-defined with no platform-enforced set; each is created as a series identifier, and each requires a value source declaration on the Withholding Tax Configuration naming where the engine reads its value from. May be empty, in which case matching proceeds on tax identity alone. A dimension whose name collides with a mandatory core field is rejected. The two datasets need not carry the same dimensions - one present on only a single dataset is simply not matched on when the other is queried, an ISIN dimension on the anomaly dataset alone being the usual case. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateWithholdingTaxDataset import CreateWithholdingTaxDataset

instance = CreateWithholdingTaxDataset(
    scope="...",  # required — The scope of the relational dataset definition.
    code="...",  # required — The code of the relational dataset definition. Together with the scope this uniquely identifies the definition.
    dimensions=[]  # optional — The dimensions, over and above the mandatory core, that this dataset is matched on. Fully customer-defined with no platform-enforced set; each is created as a series identifier, and each requires a value source declaration on the Withholding Tax Configuration naming where the engine reads its value from. May be empty, in which case matching proceeds on tax identity alone. A dimension whose name collides with a mandatory core field is rejected. The two datasets need not carry the same dimensions - one present on only a single dataset is simply not matched on when the other is queried, an ISIN dimension on the anomaly dataset alone being the usual case.
)
```

- [CreateSeriesIdentifierField](CreateSeriesIdentifierField.md) — used in `dimensions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

