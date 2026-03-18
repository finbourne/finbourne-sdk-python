# AddressDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the address key. |
| **type** | **str** | Optional | The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json |
| **description** | **str** | Optional | The description for this result. |
| **life_cycle_status** | **str** | Optional | What is the status of the address path. If it is not Production then it might be removed at some point in the future.  See the removal date for the likely timing of that if any. |
| **removal_date** | **datetime** | Optional | If the life-cycle status of the address is Deprecated then this is the date at which support of the address will be suspended.  After that date it will be removed at the earliest possible point subject to any specific contractual support and development constraints. |
| **documentation_link** | **str** | Optional | Contains a link to the documentation for this AddressDefinition in KnowledgeBase. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddressDefinition import AddressDefinition

instance = AddressDefinition(
    display_name="...",  # optional — The display name of the address key.
    type="...",  # optional — The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json
    description="...",  # optional — The description for this result.
    life_cycle_status="...",  # optional — What is the status of the address path. If it is not Production then it might be removed at some point in the future.  See the removal date for the likely timing of that if any.
    removal_date=datetime.now(),  # optional — If the life-cycle status of the address is Deprecated then this is the date at which support of the address will be suspended.  After that date it will be removed at the earliest possible point subject to any specific contractual support and development constraints.
    documentation_link="..."  # optional — Contains a link to the documentation for this AddressDefinition in KnowledgeBase.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

