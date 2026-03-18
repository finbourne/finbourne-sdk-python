# GroupedResultOfAddressKey

Holder class for a group of results. It consists of a list of columns and values for that column.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **columns** | **List[str]** | Optional | The columns, or keys, for a particular group of results |
| **values** | [List[ResultValue]](ResultValue.md) | Optional | The values for the list of results |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupedResultOfAddressKey import GroupedResultOfAddressKey

instance = GroupedResultOfAddressKey(
    columns=,  # optional — The columns, or keys, for a particular group of results
    values=[]  # optional — The values for the list of results
)
```

- [ResultValue](ResultValue.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

