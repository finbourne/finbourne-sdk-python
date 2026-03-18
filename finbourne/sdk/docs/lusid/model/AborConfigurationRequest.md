# AborConfigurationRequest

The request used to create an AborConfiguration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Abor Configuration. |
| **display_name** | **str** | Optional | The name of the Abor Configuration. |
| **description** | **str** | Optional | A description for the Abor Configuration. |
| **recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **posting_module_codes** | **List[str]** | Optional | The Posting Module Codes from which the rules to be applied are retrieved. |
| **cleardown_module_codes** | **List[str]** | Optional | The Cleardown Module Codes from which the rules to be applied are retrieved. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Abor Configuration. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AborConfigurationRequest import AborConfigurationRequest

instance = AborConfigurationRequest(
    code="...",  # required — The code given for the Abor Configuration.
    display_name="...",  # optional — The name of the Abor Configuration.
    description="...",  # optional — A description for the Abor Configuration.
    recipe_id=ResourceId(...),  # required
    chart_of_accounts_id=ResourceId(...),  # required
    posting_module_codes=,  # optional — The Posting Module Codes from which the rules to be applied are retrieved.
    cleardown_module_codes=,  # optional — The Cleardown Module Codes from which the rules to be applied are retrieved.
    properties=ModelProperty(...)  # optional — A set of properties for the Abor Configuration.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

