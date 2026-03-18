# ExternalLogRecord

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **logid** | **int** | Required | *No description available.* |
| **parentlogid** | **int** | Optional | *No description available.* |
| **loglevel** | **str** | Required | *No description available.* |
| **logstatus** | **str** | Required | *No description available.* |
| **sourcerecordtype** | **str** | Optional | *No description available.* |
| **sourceprimaryidtype** | **str** | Optional | *No description available.* |
| **sourceprimaryidvalue** | **str** | Optional | *No description available.* |
| **targetrecordtype** | **str** | Optional | *No description available.* |
| **targetrecordaction** | **str** | Optional | *No description available.* |
| **targetprimaryidtype** | **str** | Optional | *No description available.* |
| **targetprimaryidvalue** | **str** | Optional | *No description available.* |
| **message** | **str** | Optional | *No description available.* |
| **messagetype** | **str** | Optional | *No description available.* |
| **timestamp** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ExternalLogRecord import ExternalLogRecord

instance = ExternalLogRecord(
    logid=0,  # required
    parentlogid=0,  # optional
    loglevel="...",  # required
    logstatus="...",  # required
    sourcerecordtype="...",  # optional
    sourceprimaryidtype="...",  # optional
    sourceprimaryidvalue="...",  # optional
    targetrecordtype="...",  # optional
    targetrecordaction="...",  # optional
    targetprimaryidtype="...",  # optional
    targetprimaryidvalue="...",  # optional
    message="...",  # optional
    messagetype="...",  # optional
    timestamp="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

