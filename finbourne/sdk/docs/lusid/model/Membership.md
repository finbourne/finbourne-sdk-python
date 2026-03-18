# Membership

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the unique identifier associated with the Custom Data Model. |
| **code** | **str** | Required | The code of the unique identifier associated with the Custom Data Model. |
| **display_name** | **str** | Required | The name of the Custom Data Model. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Membership import Membership

instance = Membership(
    scope="...",  # required — The scope of the unique identifier associated with the Custom Data Model.
    code="...",  # required — The code of the unique identifier associated with the Custom Data Model.
    display_name="..."  # required — The name of the Custom Data Model.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

