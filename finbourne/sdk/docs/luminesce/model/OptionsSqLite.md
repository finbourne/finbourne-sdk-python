# OptionsSqLite

Additional options applicable to the given SourceType
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **table** | **str** | Optional | Table name to read.  If missing then an error will be raised if there is any number of tables other than one. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OptionsSqLite import OptionsSqLite

instance = OptionsSqLite(
    table="..."  # optional — Table name to read.  If missing then an error will be raised if there is any number of tables other than one.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

