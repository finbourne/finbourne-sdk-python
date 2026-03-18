# LusidUniqueId

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type for the LUSID unique id, this will depend on the type of entity found, for instance &#39;Instrument&#39; would have a value of &#39;LusidInstrumentId&#39; |
| **value** | **str** | Required | The value for the LUSID unique id |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LusidUniqueId import LusidUniqueId

instance = LusidUniqueId(
    type="...",  # required — The type for the LUSID unique id, this will depend on the type of entity found, for instance &#39;Instrument&#39; would have a value of &#39;LusidInstrumentId&#39;
    value="..."  # required — The value for the LUSID unique id
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

