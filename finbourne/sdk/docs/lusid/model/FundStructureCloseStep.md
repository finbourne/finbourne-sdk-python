# FundStructureCloseStep

One member's step in a fund structure close.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **member_short_code** | **str** | Required | The node code of the member in the structure. |
| **fund** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **step** | **int** | Required | The position of the member in the close order. |
| **status** | **str** | Required | What happened to the member. Available values: Finalised, AlreadyFinal, Failed, Skipped. |
| **failure** | **str** | Optional | The failure that stopped the member finalising, if any. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureCloseStep import FundStructureCloseStep

instance = FundStructureCloseStep(
    member_short_code="...",  # required — The node code of the member in the structure.
    fund=ResourceId(...),  # required
    step=0,  # required — The position of the member in the close order.
    status="...",  # required — What happened to the member. Available values: Finalised, AlreadyFinal, Failed, Skipped.
    failure="..."  # optional — The failure that stopped the member finalising, if any.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

