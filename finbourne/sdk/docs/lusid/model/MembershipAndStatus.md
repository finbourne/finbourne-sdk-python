# MembershipAndStatus

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | Describes whether the entity is still a valid member of the data model. |
| **scope** | **str** | Required | The scope of the unique identifier associated with the Custom Data Model. |
| **code** | **str** | Required | The code of the unique identifier associated with the Custom Data Model. |
| **display_name** | **str** | Required | The name of the Custom Data Model. |
| **validation_failures** | **List[str]** | Required | A list of validation failures returned when the entity&#39;s status with respect to the current model is &#39;Invalid&#39; or &#39;Inadmissible&#39; |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MembershipAndStatus import MembershipAndStatus

instance = MembershipAndStatus(
    status="...",  # required — Describes whether the entity is still a valid member of the data model.
    scope="...",  # required — The scope of the unique identifier associated with the Custom Data Model.
    code="...",  # required — The code of the unique identifier associated with the Custom Data Model.
    display_name="...",  # required — The name of the Custom Data Model.
    validation_failures=  # required — A list of validation failures returned when the entity&#39;s status with respect to the current model is &#39;Invalid&#39; or &#39;Inadmissible&#39;
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

