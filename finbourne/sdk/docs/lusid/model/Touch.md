# Touch

Touch class for exotic FxOption
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **direction** | **str** | Required | Supported string (enumeration) values are: [Down, Up]. |
| **level** | **float** | Required | Trigger level, which the underlying should (or should not) cross/touch. |
| **monitoring** | **str** | Optional | Supported string (enumeration) values are: [European, Bermudan, American].  Defaults to \&quot;European\&quot; if not set. |
| **type** | **str** | Required | Supported string (enumeration) values are: [Touch, Notouch]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Touch import Touch

instance = Touch(
    direction="...",  # required — Supported string (enumeration) values are: [Down, Up].
    level=0.0,  # required — Trigger level, which the underlying should (or should not) cross/touch.
    monitoring="...",  # optional — Supported string (enumeration) values are: [European, Bermudan, American].  Defaults to \&quot;European\&quot; if not set.
    type="..."  # required — Supported string (enumeration) values are: [Touch, Notouch].
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

