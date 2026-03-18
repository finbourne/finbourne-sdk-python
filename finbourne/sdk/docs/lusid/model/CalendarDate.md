# CalendarDate

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **date_identifier** | **str** | Required | *No description available.* |
| **from_utc** | **datetime** | Required | *No description available.* |
| **to_utc** | **datetime** | Required | *No description available.* |
| **local_date** | **str** | Required | *No description available.* |
| **timezone** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **type** | **str** | Optional | *No description available.* |
| **attributes** | [DateAttributes](DateAttributes.md) | Optional | *No description available.* |
| **source_data** | **Dict[str, Optional[str]]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CalendarDate import CalendarDate

instance = CalendarDate(
    href="...",  # optional
    date_identifier="...",  # required
    from_utc=datetime.now(),  # required
    to_utc=datetime.now(),  # required
    local_date="...",  # required
    timezone="...",  # required
    description="...",  # required
    type="...",  # optional
    attributes=DateAttributes(...),  # optional
    source_data=  # optional
)
```

- [DateAttributes](DateAttributes.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

