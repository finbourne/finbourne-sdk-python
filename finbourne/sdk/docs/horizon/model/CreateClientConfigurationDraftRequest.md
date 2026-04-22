# CreateClientConfigurationDraftRequest

Request to create a new draft client configuration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **major_version** | **int** | Optional | The major version for the new draft. Must be supplied together with minorVersion, or both omitted to auto-assign the next version. |
| **minor_version** | **int** | Optional | The minor version for the new draft. Must be supplied together with MajorVersion, or both omitted to auto-assign the next version. |
| **source_major_version** | **int** | Optional | The major version of an existing record to copy the value from. Must be supplied together with SourceMinorVersion. If omitted, the new draft is initialised with an empty JSON object. |
| **source_minor_version** | **int** | Optional | The minor version of an existing record to copy the value from. Must be supplied together with SourceMajorVersion. If omitted, the new draft is initialised with an empty JSON object. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.CreateClientConfigurationDraftRequest import CreateClientConfigurationDraftRequest

instance = CreateClientConfigurationDraftRequest(
    major_version=0,  # optional — The major version for the new draft. Must be supplied together with minorVersion, or both omitted to auto-assign the next version.
    minor_version=0,  # optional — The minor version for the new draft. Must be supplied together with MajorVersion, or both omitted to auto-assign the next version.
    source_major_version=0,  # optional — The major version of an existing record to copy the value from. Must be supplied together with SourceMinorVersion. If omitted, the new draft is initialised with an empty JSON object.
    source_minor_version=0  # optional — The minor version of an existing record to copy the value from. Must be supplied together with SourceMajorVersion. If omitted, the new draft is initialised with an empty JSON object.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

