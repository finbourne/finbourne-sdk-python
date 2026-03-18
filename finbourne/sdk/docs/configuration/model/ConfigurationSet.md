# ConfigurationSet

The full version of the configuration set
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **created_at** | **datetime** | Required | The date referring to the creation date of the configuration set |
| **created_by** | **str** | Required | Who created the configuration set |
| **last_modified_at** | **datetime** | Required | The date referring to the date when the configuration set was last modified |
| **last_modified_by** | **str** | Required | Who modified the configuration set most recently |
| **description** | **str** | Optional | Describes the configuration set |
| **items** | [List[ConfigurationItemSummary]](ConfigurationItemSummary.md) | Optional | The collection of the configuration items that this set contains. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type (personal or shared) of the configuration set |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.ConfigurationSet import ConfigurationSet

instance = ConfigurationSet(
    created_at=datetime.now(),  # required — The date referring to the creation date of the configuration set
    created_by="...",  # required — Who created the configuration set
    last_modified_at=datetime.now(),  # required — The date referring to the date when the configuration set was last modified
    last_modified_by="...",  # required — Who modified the configuration set most recently
    description="...",  # optional — Describes the configuration set
    items=[],  # optional — The collection of the configuration items that this set contains.
    id=ResourceId(...),  # required
    type="...",  # required — The type (personal or shared) of the configuration set
    links=[]  # optional
)
```

- [ConfigurationItemSummary](ConfigurationItemSummary.md) — used in `items`
- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

