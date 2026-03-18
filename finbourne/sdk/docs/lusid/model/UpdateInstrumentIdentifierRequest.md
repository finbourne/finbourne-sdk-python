# UpdateInstrumentIdentifierRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The allowable instrument identifier to update, insert or remove e.g. &#39;Figi&#39;. |
| **value** | **str** | Optional | The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument. |
| **effective_at** | **str** | Optional | The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateInstrumentIdentifierRequest import UpdateInstrumentIdentifierRequest

instance = UpdateInstrumentIdentifierRequest(
    type="...",  # required — The allowable instrument identifier to update, insert or remove e.g. &#39;Figi&#39;.
    value="...",  # optional — The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument.
    effective_at="..."  # optional — The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

