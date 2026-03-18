# LusidGridData

Representation of the data we will get from the dashboard
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_grid_design** | [TableView](TableView.md) | Required | *No description available.* |
| **resource_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **dashboard_type** | [DashboardType](DashboardType.md) | Optional | *No description available.* |
| **use_settle_date** | **bool** | Optional | Whether to use the Settlement date or the Transaction date |
| **dates** | [DateParameters](DateParameters.md) | Optional | *No description available.* |
| **recipe** | **str** | Optional | The recipe to use for valuations |
| **currency** | **str** | Optional | The currency to use for valuations |
| **tenor** | **str** | Optional | The tenor to use for valuations |
| **order_flow** | **str** | Optional | Type of order flow to include |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.LusidGridData import LusidGridData

instance = LusidGridData(
    lusid_grid_design=TableView(...),  # required
    resource_id=ResourceId(...),  # required
    dashboard_type=DashboardType(...),  # optional
    use_settle_date=True,  # optional — Whether to use the Settlement date or the Transaction date
    dates=DateParameters(...),  # optional
    recipe="...",  # optional — The recipe to use for valuations
    currency="...",  # optional — The currency to use for valuations
    tenor="...",  # optional — The tenor to use for valuations
    order_flow="..."  # optional — Type of order flow to include
)
```


## Related Models

- [TableView](TableView.md)
- [ResourceId](ResourceId.md)
- [DashboardType](DashboardType.md)
- [DateParameters](DateParameters.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

