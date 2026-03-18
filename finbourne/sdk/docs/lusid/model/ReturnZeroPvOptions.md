# ReturnZeroPvOptions

Options to indicate which errors to ignore when performing valuation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_matured** | **bool** | Optional | Indicates whether attempting to value an instrument after its maturity date should produce a failure (false)  or a zero PV (true). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReturnZeroPvOptions import ReturnZeroPvOptions

instance = ReturnZeroPvOptions(
    instrument_matured=True  # optional — Indicates whether attempting to value an instrument after its maturity date should produce a failure (false)  or a zero PV (true).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

