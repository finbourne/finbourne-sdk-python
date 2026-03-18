# ScanSummary


## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fixable** | **int** | Optional | The number of vulnerabilities that have a known fix |
| **total** | **int** | Optional | The total number of vulnerabilities |
| **critical** | **int** | Optional | The number of Critical severity vulnerabilities |
| **high** | **int** | Optional | The number of High severity vulnerabilities |
| **medium** | **int** | Optional | The number of Medium severity vulnerabilities |
| **low** | **int** | Optional | The number of Low severity vulnerabilities |
| **negligible** | **int** | Optional | The number of Negligible severity vulnerabilities |
| **unknown** | **int** | Optional | The number of Unknown severity vulnerabilities |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.ScanSummary import ScanSummary

instance = ScanSummary(
    fixable=0,  # optional — The number of vulnerabilities that have a known fix
    total=0,  # optional — The total number of vulnerabilities
    critical=0,  # optional — The number of Critical severity vulnerabilities
    high=0,  # optional — The number of High severity vulnerabilities
    medium=0,  # optional — The number of Medium severity vulnerabilities
    low=0,  # optional — The number of Low severity vulnerabilities
    negligible=0,  # optional — The number of Negligible severity vulnerabilities
    unknown=0  # optional — The number of Unknown severity vulnerabilities
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

