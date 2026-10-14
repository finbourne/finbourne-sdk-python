# AllocationEventBasisDiagnostics

What the basis source found when it read the register for an Allocation Event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **participant_count** | **int** | Optional | The number of investor records whose basis values were read. |
| **excluded** | **List[str]** | Optional | The investor records the map&#39;s exceptions kept out of the event. |
| **warnings** | [List[AllocationEventBasisWarning]](AllocationEventBasisWarning.md) | Optional | Anything the source had to work around, for example MissingFeeRate on a line without a management fee rate. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBasisDiagnostics import AllocationEventBasisDiagnostics

instance = AllocationEventBasisDiagnostics(
    participant_count=0,  # optional — The number of investor records whose basis values were read.
    excluded=,  # optional — The investor records the map&#39;s exceptions kept out of the event.
    warnings=[]  # optional — Anything the source had to work around, for example MissingFeeRate on a line without a management fee rate.
)
```

- [AllocationEventBasisWarning](AllocationEventBasisWarning.md) — used in `warnings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

