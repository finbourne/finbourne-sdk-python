# Source

Information leading to choosing the provider
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **location** | **str** | Optional | The source location.  Start of a provider name, &#x60;Drive&#x60;, &#x60;LocalFs&#x60;, &#x60;AwsS3&#x60; etc. |
| **type** | [SourceType](SourceType.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.Source import Source

instance = Source(
    location="...",  # optional — The source location.  Start of a provider name, &#x60;Drive&#x60;, &#x60;LocalFs&#x60;, &#x60;AwsS3&#x60; etc.
    type=SourceType(...)  # optional
)
```

- [SourceType](SourceType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

