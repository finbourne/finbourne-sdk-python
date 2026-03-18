# TypedResourceId

Represents the user-defined identifier for a Legal Entity or Person.  Users can define their own, scoped identifiers for Legal Entities and Persons using identifier properties.  For example,  when used to identify a Person, the identifier defined by Person/myScope/username would be represented as   {     \"idTypeScope\": \"myScope\",     \"idTypeCode\": \"username\",     \"code\": \"john_doe_001\"   }
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id_type_scope** | **str** | Required | The scope of the identifier&#39;s (property) definition. |
| **id_type_code** | **str** | Required | The code of identifier&#39;s (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI. |
| **code** | **str** | Required | The value of the user-defined identifier in respect of the entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TypedResourceId import TypedResourceId

instance = TypedResourceId(
    id_type_scope="...",  # required — The scope of the identifier&#39;s (property) definition.
    id_type_code="...",  # required — The code of identifier&#39;s (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI.
    code="..."  # required — The value of the user-defined identifier in respect of the entity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

