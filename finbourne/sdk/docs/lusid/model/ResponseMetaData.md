# ResponseMetaData

Metadata related to an api response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of meta data information being provided |
| **description** | **str** | Optional | The description of what occured for this specific piece of meta data |
| **identifier_type** | **str** | Optional | The type of the listed identifiers |
| **identifiers** | **List[str]** | Optional | The related identifiers that were impacted by this event |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResponseMetaData import ResponseMetaData

instance = ResponseMetaData(
    type="...",  # optional — The type of meta data information being provided
    description="...",  # optional — The description of what occured for this specific piece of meta data
    identifier_type="...",  # optional — The type of the listed identifiers
    identifiers=  # optional — The related identifiers that were impacted by this event
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

