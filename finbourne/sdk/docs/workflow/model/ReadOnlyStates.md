# ReadOnlyStates

Information about which states the field can be edited in
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **state_type** | **str** | Required | The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates) |
| **selected_states** | **List[str]** | Optional | Named states for which the field will be readonly - This field can only be populated if StateType &#x3D; SelectedStates |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ReadOnlyStates import ReadOnlyStates

instance = ReadOnlyStates(
    state_type="...",  # required — The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates)
    selected_states=  # optional — Named states for which the field will be readonly - This field can only be populated if StateType &#x3D; SelectedStates
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

