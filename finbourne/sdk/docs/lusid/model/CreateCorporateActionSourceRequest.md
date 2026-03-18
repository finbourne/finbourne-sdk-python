# CreateCorporateActionSourceRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the corporate action source |
| **code** | **str** | Required | The code of the corporate action source |
| **display_name** | **str** | Required | The name of the corporate action source |
| **description** | **str** | Optional | The description of the corporate action source |
| **instrument_scopes** | **List[str]** | Optional | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateCorporateActionSourceRequest import CreateCorporateActionSourceRequest

instance = CreateCorporateActionSourceRequest(
    scope="...",  # required — The scope of the corporate action source
    code="...",  # required — The code of the corporate action source
    display_name="...",  # required — The name of the corporate action source
    description="...",  # optional — The description of the corporate action source
    instrument_scopes=  # optional — The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

