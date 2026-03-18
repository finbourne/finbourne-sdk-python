# PackageSetRequest

A request to create or update multiple Packages.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[PackageRequest]](PackageRequest.md) | Optional | A collection of PackageRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PackageSetRequest import PackageSetRequest

instance = PackageSetRequest(
    requests=[]  # optional — A collection of PackageRequests.
)
```


## Related Models

- [PackageRequest](PackageRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

