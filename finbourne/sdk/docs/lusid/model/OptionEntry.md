# OptionEntry

Strike price against par and associated date for a bond call.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **strike** | **float** | Required | The strike on this date |
| **var_date** | **datetime** | Required | The date at which the option can be actioned at this strike |
| **end_date** | **datetime** | Optional | If American exercise, this is the end of the exercise period.  Optional field. Defaults to the Date field if not set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OptionEntry import OptionEntry

instance = OptionEntry(
    strike=0.0,  # required — The strike on this date
    var_date=datetime.now(),  # required — The date at which the option can be actioned at this strike
    end_date=datetime.now()  # optional — If American exercise, this is the end of the exercise period.  Optional field. Defaults to the Date field if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

