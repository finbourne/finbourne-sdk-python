# CreateSequenceRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the sequence definition to create |
| **increment** | **int** | Optional | The value to increment between each value in the sequence |
| **min_value** | **int** | Optional | The minimum value of the sequence |
| **max_value** | **int** | Optional | The maximum value of the sequence |
| **start** | **int** | Optional | The start value of the sequence |
| **cycle** | **bool** | Optional | Set to true to start the sequence over again when it reaches the end. Defaults to false if not provided. |
| **pattern** | **str** | Optional | The pattern to be used to generate next values in the sequence. Defaults to null if not provided. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateSequenceRequest import CreateSequenceRequest

instance = CreateSequenceRequest(
    code="...",  # required — The code of the sequence definition to create
    increment=0,  # optional — The value to increment between each value in the sequence
    min_value=0,  # optional — The minimum value of the sequence
    max_value=0,  # optional — The maximum value of the sequence
    start=0,  # optional — The start value of the sequence
    cycle=True,  # optional — Set to true to start the sequence over again when it reaches the end. Defaults to false if not provided.
    pattern="..."  # optional — The pattern to be used to generate next values in the sequence. Defaults to null if not provided.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

