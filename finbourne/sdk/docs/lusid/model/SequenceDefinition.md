# SequenceDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **increment** | **int** | Required | The Resource Id of the sequence definition |
| **min_value** | **int** | Required | The minimum value of the sequence |
| **max_value** | **int** | Required | The maximum value of the sequence |
| **start** | **int** | Required | The start value of the sequence |
| **value** | **int** | Optional | The last used value of the sequence |
| **cycle** | **bool** | Required | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. |
| **pattern** | **str** | Optional | The pattern to be used to generate next values in the sequence. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SequenceDefinition import SequenceDefinition

instance = SequenceDefinition(
    id=ResourceId(...),  # required
    increment=0,  # required — The Resource Id of the sequence definition
    min_value=0,  # required — The minimum value of the sequence
    max_value=0,  # required — The maximum value of the sequence
    start=0,  # required — The start value of the sequence
    value=0,  # optional — The last used value of the sequence
    cycle=True,  # required — Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value.
    pattern="...",  # optional — The pattern to be used to generate next values in the sequence.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

