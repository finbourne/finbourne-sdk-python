# RecResultStreak

The run of consecutive instances, ending at this result, in which the same result was produced, with its  difference and open sub-streaks.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **predecessor** | [RecResultStreakPredecessor](RecResultStreakPredecessor.md) | Required | *No description available.* |
| **age** | **str** | Required | The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Always positive. |
| **count_instances** | **int** | Required | The number of instances in the streak, including this one. Always 2 or more. |
| **start_result** | [RecAgedResult](RecAgedResult.md) | Required | *No description available.* |
| **difference_streak** | [RecResultSubStreak](RecResultSubStreak.md) | Required | *No description available.* |
| **open_streak** | [RecResultSubStreak](RecResultSubStreak.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultStreak import RecResultStreak

instance = RecResultStreak(
    predecessor=RecResultStreakPredecessor(...),  # required
    age="...",  # required — The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Always positive.
    count_instances=0,  # required — The number of instances in the streak, including this one. Always 2 or more.
    start_result=RecAgedResult(...),  # required
    difference_streak=RecResultSubStreak(...),  # required
    open_streak=RecResultSubStreak(...)  # required
)
```


## Related Models

- [RecResultStreakPredecessor](RecResultStreakPredecessor.md)
- [RecAgedResult](RecAgedResult.md)
- [RecResultSubStreak](RecResultSubStreak.md)
- [RecResultSubStreak](RecResultSubStreak.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

