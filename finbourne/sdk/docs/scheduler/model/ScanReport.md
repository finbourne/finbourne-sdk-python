# ScanReport

Represents the details of a security scan of an image
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **severity** | **str** | Optional | The overall severity. For example : \&quot;High\&quot; or \&quot;None\&quot; |
| **status** | **str** | Optional | The status of the report |
| **start_time** | **datetime** | Optional | The start time of the scanning process |
| **end_time** | **datetime** | Optional | The end time of the scanning process |
| **scan_duration** | **int** | Optional | The duration of the scan in seconds |
| **summary** | [ScanSummary](ScanSummary.md) | Optional | *No description available.* |
| **vulnerabilities** | [List[Vulnerability]](Vulnerability.md) | Optional | List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.ScanReport import ScanReport

instance = ScanReport(
    severity="...",  # optional — The overall severity. For example : \&quot;High\&quot; or \&quot;None\&quot;
    status="...",  # optional — The status of the report
    start_time=datetime.now(),  # optional — The start time of the scanning process
    end_time=datetime.now(),  # optional — The end time of the scanning process
    scan_duration=0,  # optional — The duration of the scan in seconds
    summary=ScanSummary(...),  # optional
    vulnerabilities=[]  # optional — List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability
)
```

- [ScanSummary](ScanSummary.md)
- [Vulnerability](Vulnerability.md) — used in `vulnerabilities`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

