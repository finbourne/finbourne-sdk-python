# RecyclingTerms

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **enabled** | **bool** | Required | *No description available.* |
| **cap_percentage_of_commitments** | **float** | Optional | *No description available.* |
| **recycling_end_date** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecyclingTerms import RecyclingTerms

instance = RecyclingTerms(
    enabled=True,  # required
    cap_percentage_of_commitments=0.0,  # optional
    recycling_end_date=datetime.now()  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

