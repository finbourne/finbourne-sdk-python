# RecResultSubStreak

The part of a streak, ending at this result, over which a stricter condition held: same difference, or open.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **age** | **str** | Required | The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Zero when the predecessor does not extend the sub-streak. |
| **count_instances** | **int** | Optional | The number of instances in the sub-streak, including this one. Null when the predecessor does not extend the sub-streak; otherwise 2 or more. |
| **start_result** | [RecAgedResult](RecAgedResult.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultSubStreak import RecResultSubStreak

instance = RecResultSubStreak(
    age="...",  # required — The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Zero when the predecessor does not extend the sub-streak.
    count_instances=0,  # optional — The number of instances in the sub-streak, including this one. Null when the predecessor does not extend the sub-streak; otherwise 2 or more.
    start_result=RecAgedResult(...)  # optional
)
```

- [RecAgedResult](RecAgedResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

