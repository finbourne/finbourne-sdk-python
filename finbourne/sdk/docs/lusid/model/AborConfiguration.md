# AborConfiguration

An AborConfiguration entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Abor Configuration. |
| **description** | **str** | Optional | A description for the Abor Configuration. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **posting_module_codes** | **List[str]** | Optional | The Posting Module Codes from which the rules to be applied are retrieved. |
| **cleardown_module_codes** | **List[str]** | Optional | The Cleardown Module Codes from which the rules to be applied are retrieved. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Abor Configuration. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AborConfiguration import AborConfiguration

instance = AborConfiguration(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Abor Configuration.
    description="...",  # optional — A description for the Abor Configuration.
    recipe_id=ResourceId(...),  # optional
    chart_of_accounts_id=ResourceId(...),  # required
    posting_module_codes=,  # optional — The Posting Module Codes from which the rules to be applied are retrieved.
    cleardown_module_codes=,  # optional — The Cleardown Module Codes from which the rules to be applied are retrieved.
    properties=ModelProperty(...),  # optional — A set of properties for the Abor Configuration.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

