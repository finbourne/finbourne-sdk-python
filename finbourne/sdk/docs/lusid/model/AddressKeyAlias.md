# AddressKeyAlias

An address key alias that maps a short alias key to a real key with options.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the alias |
| **code** | **str** | Required | The code of the alias |
| **alias_key** | **str** | Required | The alias address key, must start with \&quot;Alias/\&quot; prefix (e.g., \&quot;Alias/DailyNZPnL\&quot;) |
| **real_key** | **str** | Required | The real address key this alias resolves to (e.g., \&quot;ProfitAndLoss/Total\&quot;). Must NOT start with \&quot;Alias/\&quot;. |
| **options** | **Dict[str, Optional[str]]** | Optional | Options to apply when resolving the alias (e.g., {\&quot;Window\&quot;:\&quot;Daily\&quot;,\&quot;TimeZone\&quot;:\&quot;NZ\&quot;}) |
| **display_name** | **str** | Optional | Human-readable display name |
| **description** | **str** | Optional | Description of the alias |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddressKeyAlias import AddressKeyAlias

instance = AddressKeyAlias(
    scope="...",  # required — The scope of the alias
    code="...",  # required — The code of the alias
    alias_key="...",  # required — The alias address key, must start with \&quot;Alias/\&quot; prefix (e.g., \&quot;Alias/DailyNZPnL\&quot;)
    real_key="...",  # required — The real address key this alias resolves to (e.g., \&quot;ProfitAndLoss/Total\&quot;). Must NOT start with \&quot;Alias/\&quot;.
    options=,  # optional — Options to apply when resolving the alias (e.g., {\&quot;Window\&quot;:\&quot;Daily\&quot;,\&quot;TimeZone\&quot;:\&quot;NZ\&quot;})
    display_name="...",  # optional — Human-readable display name
    description="..."  # optional — Description of the alias
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

