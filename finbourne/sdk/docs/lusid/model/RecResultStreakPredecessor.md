# RecResultStreakPredecessor

The same result in the previous instance, and which streaks it extends.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result** | [RecAgedResult](RecAgedResult.md) | Required | *No description available.* |
| **streak_types** | **List[str]** | Required | Which streaks the predecessor extends: always Core, and Difference if the aggregate rule differences are unchanged. Open is not set yet. Available values: Core, Difference, Open. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultStreakPredecessor import RecResultStreakPredecessor

instance = RecResultStreakPredecessor(
    result=RecAgedResult(...),  # required
    streak_types=  # required — Which streaks the predecessor extends: always Core, and Difference if the aggregate rule differences are unchanged. Open is not set yet. Available values: Core, Difference, Open.
)
```


## Related Models

- [RecAgedResult](RecAgedResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

