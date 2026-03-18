# PermIdData

PermId Data Structure
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **figi** | **str** | Required | FIGI assigned to the instrument. |
| **ticker** | **str** | Required | Ticker assigned to the instrument |
| **mic** | **str** | Required | ISO market identification code(MIC) of the desired instrument(s) |
| **quote_perm_id** | **str** | Required | QuotePermId of the instrument |
| **is_primary_quote** | **bool** | Required | If the quote is primary |
| **legal_entity_identifier** | **str** | Optional | LEI assigned to the instrument |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.PermIdData import PermIdData

instance = PermIdData(
    figi="...",  # required — FIGI assigned to the instrument.
    ticker="...",  # required — Ticker assigned to the instrument
    mic="...",  # required — ISO market identification code(MIC) of the desired instrument(s)
    quote_perm_id="...",  # required — QuotePermId of the instrument
    is_primary_quote=True,  # required — If the quote is primary
    legal_entity_identifier="..."  # optional — LEI assigned to the instrument
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

