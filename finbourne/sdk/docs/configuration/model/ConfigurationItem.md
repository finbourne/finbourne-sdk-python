# ConfigurationItem

The full version of the configuration item
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **created_at** | **datetime** | Required | The date referring to the creation date of the configuration item |
| **created_by** | **str** | Required | Who created the configuration item |
| **last_modified_at** | **datetime** | Required | The date referring to the date when the configuration item was last modified |
| **last_modified_by** | **str** | Required | Who modified the configuration item most recently |
| **description** | **str** | Optional | Describes the configuration item |
| **key** | **str** | Required | The key which identifies the configuration item |
| **value** | **str** | Required | The value of the configuration item |
| **value_type** | **str** | Required | The type of the configuration item&#39;s value |
| **is_secret** | **bool** | Required | Defines whether or not the value is a secret. |
| **ref** | **str** | Required | The reference to the configuration item *(read-only)* |
| **block_reveal** | **bool** | Required | Defines whether the value is blocked with non-internal request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.ConfigurationItem import ConfigurationItem

instance = ConfigurationItem(
    created_at=datetime.now(),  # required — The date referring to the creation date of the configuration item
    created_by="...",  # required — Who created the configuration item
    last_modified_at=datetime.now(),  # required — The date referring to the date when the configuration item was last modified
    last_modified_by="...",  # required — Who modified the configuration item most recently
    description="...",  # optional — Describes the configuration item
    key="...",  # required — The key which identifies the configuration item
    value="...",  # required — The value of the configuration item
    value_type="...",  # required — The type of the configuration item&#39;s value
    is_secret=True,  # required — Defines whether or not the value is a secret.
    ref="...",  # required — The reference to the configuration item
    block_reveal=True,  # required — Defines whether the value is blocked with non-internal request.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

