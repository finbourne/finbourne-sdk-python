# RequiredResources

Information related to a jobs required access to resources
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_apis** | **List[str]** | Optional | List of LUSID APIs the job needs access to |
| **lusid_file_system** | **List[str]** | Optional | List of S3 bucket or folder names that the job can access |
| **external_calls** | **List[str]** | Optional | External URLs that the job can call |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.RequiredResources import RequiredResources

instance = RequiredResources(
    lusid_apis=,  # optional — List of LUSID APIs the job needs access to
    lusid_file_system=,  # optional — List of S3 bucket or folder names that the job can access
    external_calls=  # optional — External URLs that the job can call
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

