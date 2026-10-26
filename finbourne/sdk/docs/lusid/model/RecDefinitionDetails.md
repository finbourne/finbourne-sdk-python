# RecDefinitionDetails

Base class for the part of a rec definition whose shape depends on what it reconciles. Polymorphic by  definitionType; each supported type has a corresponding inherited class.

## oneOf Type

`RecDefinitionDetails` can be one of the following types:

* [ExternalRecDefinitionDetails](./ExternalRecDefinitionDetails.md)
* [LusidEntityRecDefinitionDetails](./LusidEntityRecDefinitionDetails.md)
* [PortfolioContentsRecDefinitionDetails](./PortfolioContentsRecDefinitionDetails.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.lusid.models.RecDefinitionDetails import RecDefinitionDetails

# Construct using any of the compatible types above
external_rec_definition_details_instance = lusid.models.external_rec_definition_details.ExternalRecDefinitionDetails(
                        matching_ruleset_id = lusid.models.resource_id.ResourceId(
                            scope = '', 
                            code = '', ), 
                        left_filter = '', 
                        right_filter = '', 
                        definition_type = '', )

instance = RecDefinitionDetails(external_rec_definition_details_instance)
```

## Related Models

- [ExternalRecDefinitionDetails](./ExternalRecDefinitionDetails.md)
- [LusidEntityRecDefinitionDetails](./LusidEntityRecDefinitionDetails.md)
- [PortfolioContentsRecDefinitionDetails](./PortfolioContentsRecDefinitionDetails.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

