# BucketSetDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **nav_types** | **List[str]** | Optional | *No description available.* |
| **unitised** | **bool** | Required | *No description available.* |
| **buckets** | [../model/List[BucketDefinition]](BucketDefinition.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetDefinition import BucketSetDefinition

instance = BucketSetDefinition(
    code="...",  # required
    display_name="...",  # required
    nav_types=,  # optional
    unitised=True,  # required
    buckets=[]  # required
)
```

- [BucketDefinition](BucketDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

