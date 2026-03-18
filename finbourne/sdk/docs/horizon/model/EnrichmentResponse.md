# EnrichmentResponse

Collated enrichment result information
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **enriched_instruments** | **List[str]** | Required |  |
| **ignored_instruments** | **List[str]** | Required |  |
| **error_file_id** | **str** | Optional | Error File ID, if one was created |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.EnrichmentResponse import EnrichmentResponse

instance = EnrichmentResponse(
    enriched_instruments=,  # required — 
    ignored_instruments=,  # required — 
    error_file_id="..."  # optional — Error File ID, if one was created
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

