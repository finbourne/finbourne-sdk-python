# MarketDataFieldConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_category** | **str** | Required | The category of market data this configuration applies to. Available values: Quote, Complex. |
| **scope** | **str** | Required | The scope of the market data field configuration. |
| **metadata_field_schema** | [List[MetadataFieldDefinition]](MetadataFieldDefinition.md) | Required | The metadata field definitions for this configuration. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketDataFieldConfiguration import MarketDataFieldConfiguration

instance = MarketDataFieldConfiguration(
    market_data_category="...",  # required — The category of market data this configuration applies to. Available values: Quote, Complex.
    scope="...",  # required — The scope of the market data field configuration.
    metadata_field_schema=[],  # required — The metadata field definitions for this configuration.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [MetadataFieldDefinition](MetadataFieldDefinition.md) — used in `metadata_field_schema`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

