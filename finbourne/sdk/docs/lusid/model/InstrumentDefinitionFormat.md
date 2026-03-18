# InstrumentDefinitionFormat

What is the provenance of an instrument. This defines who creates/owns it, what format it is in (e.g. a proprietary format or a common and known one)              and what the version of that is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_system** | **str** | Required | which source system does the format originate from |
| **vendor** | **str** | Required | An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID&#39;s), some won&#39;t.              The provenance of an instrument indicates who \&quot;owns\&quot; the associated format. |
| **version** | **str** | Required | Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations&#39; trade formats. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentDefinitionFormat import InstrumentDefinitionFormat

instance = InstrumentDefinitionFormat(
    source_system="...",  # required — which source system does the format originate from
    vendor="...",  # required — An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID&#39;s), some won&#39;t.              The provenance of an instrument indicates who \&quot;owns\&quot; the associated format.
    version="..."  # required — Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations&#39; trade formats.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

