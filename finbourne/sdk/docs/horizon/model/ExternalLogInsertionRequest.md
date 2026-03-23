# ExternalLogInsertionRequest

A request to insert external log records.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **logs** | [List[ExternalLogRecord]](ExternalLogRecord.md) | Required | The collection of external log records to insert. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ExternalLogInsertionRequest import ExternalLogInsertionRequest

instance = ExternalLogInsertionRequest(
    logs=[]  # required — The collection of external log records to insert.
)
```


## Related Models

- [ExternalLogRecord](ExternalLogRecord.md) — used in `logs`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

