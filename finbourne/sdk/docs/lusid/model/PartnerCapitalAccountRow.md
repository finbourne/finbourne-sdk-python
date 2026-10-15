# PartnerCapitalAccountRow

One row of the capital account statement with its quarter-, year- and inception-to-date amounts.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **row_type** | **str** | Required | The row type: BeginningCapital, Contributions, Distributions, TransfersIn, TransfersOut, NetOperatingIncome, ManagementFeesGross, ManagementFeeOffsets, RealisedGainLoss, UnrealisedGainLoss, CarriedInterest or EndingCapital. |
| **qtd** | **float** | Required | The quarter-to-date amount for the row. |
| **ytd** | **float** | Required | The year-to-date amount for the row. |
| **itd** | **float** | Required | The inception-to-date amount for the row. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerCapitalAccountRow import PartnerCapitalAccountRow

instance = PartnerCapitalAccountRow(
    row_type="...",  # required — The row type: BeginningCapital, Contributions, Distributions, TransfersIn, TransfersOut, NetOperatingIncome, ManagementFeesGross, ManagementFeeOffsets, RealisedGainLoss, UnrealisedGainLoss, CarriedInterest or EndingCapital.
    qtd=0.0,  # required — The quarter-to-date amount for the row.
    ytd=0.0,  # required — The year-to-date amount for the row.
    itd=0.0  # required — The inception-to-date amount for the row.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

