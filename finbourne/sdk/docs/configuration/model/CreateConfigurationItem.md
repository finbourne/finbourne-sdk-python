# CreateConfigurationItem

The information required to create a configuration item
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key of the new configuration item |
| **value** | **str** | Required | The value of the new configuration item              The maximum size for secrets is 4KB and for text values is 2MB |
| **value_type** | **str** | Optional | The type (text, number, boolean, textCollection, numberCollection) of the new configuration item&#39;s value. The validation for each type is as follows: - text: any value - number: double (e.g. \&quot;5.5\&quot;) - boolean: true/false - textCollection: comma separated list (e.g. \&quot;a,b,c\&quot;) - numberCollection: comma separated list of doubles (e.g. \&quot;1,2,3\&quot;) |
| **is_secret** | **bool** | Required | Defines whether or not the value is a secret |
| **description** | **str** | Optional | The description of the new configuration item |
| **block_reveal** | **bool** | Optional | A property to indicate if revealing the value is blocked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.CreateConfigurationItem import CreateConfigurationItem

instance = CreateConfigurationItem(
    key="...",  # required — The key of the new configuration item
    value="...",  # required — The value of the new configuration item              The maximum size for secrets is 4KB and for text values is 2MB
    value_type="...",  # optional — The type (text, number, boolean, textCollection, numberCollection) of the new configuration item&#39;s value. The validation for each type is as follows: - text: any value - number: double (e.g. \&quot;5.5\&quot;) - boolean: true/false - textCollection: comma separated list (e.g. \&quot;a,b,c\&quot;) - numberCollection: comma separated list of doubles (e.g. \&quot;1,2,3\&quot;)
    is_secret=True,  # required — Defines whether or not the value is a secret
    description="...",  # optional — The description of the new configuration item
    block_reveal=True  # optional — A property to indicate if revealing the value is blocked.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

