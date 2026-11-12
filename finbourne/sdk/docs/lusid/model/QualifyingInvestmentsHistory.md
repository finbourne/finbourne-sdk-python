# QualifyingInvestmentsHistory

The daily qualifying-investments history of one collective investment scheme and the flips within it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **luid** | **str** | Required | The LUSID instrument identifier of the collective investment scheme. |
| **threshold_percent** | **float** | Required | The qualifying investments percentage the scheme must exceed to be a bond fund. |
| **observations** | [List[QualifyingInvestmentsObservation]](QualifyingInvestmentsObservation.md) | Required | The daily qualifying investments observations in the requested window, oldest first. |
| **crossings** | [List[QualifyingInvestmentsCrossing]](QualifyingInvestmentsCrossing.md) | Required | Each pair of consecutive observations where the bond fund result flipped. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QualifyingInvestmentsHistory import QualifyingInvestmentsHistory

instance = QualifyingInvestmentsHistory(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    luid="...",  # required — The LUSID instrument identifier of the collective investment scheme.
    threshold_percent=0.0,  # required — The qualifying investments percentage the scheme must exceed to be a bond fund.
    observations=[],  # required — The daily qualifying investments observations in the requested window, oldest first.
    crossings=[],  # required — Each pair of consecutive observations where the bond fund result flipped.
    links=[]  # optional
)
```

- [QualifyingInvestmentsObservation](QualifyingInvestmentsObservation.md) — used in `observations`
- [QualifyingInvestmentsCrossing](QualifyingInvestmentsCrossing.md) — used in `crossings`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

