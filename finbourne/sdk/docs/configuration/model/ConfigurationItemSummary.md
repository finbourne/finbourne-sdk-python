# ConfigurationItemSummary

A single configuration object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
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
from finbourne.sdk.services.configuration.models.ConfigurationItemSummary import ConfigurationItemSummary

instance = ConfigurationItemSummary(
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

