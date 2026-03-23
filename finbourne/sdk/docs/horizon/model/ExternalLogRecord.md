# ExternalLogRecord

Represents an external log record.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **logid** | **int** | Required | The unique log identifier. |
| **parentlogid** | **int** | Optional | The parent log identifier (null is allowed). |
| **loglevel** | **str** | Required | The log level. |
| **logstatus** | **str** | Required | The log status. |
| **sourcerecordtype** | **str** | Optional | The source record type. |
| **sourceprimaryidtype** | **str** | Optional | The source primary ID type. |
| **sourceprimaryidvalue** | **str** | Optional | The source primary ID value. |
| **targetrecordtype** | **str** | Optional | The target record type. |
| **targetrecordaction** | **str** | Optional | The target record action. |
| **targetprimaryidtype** | **str** | Optional | The target primary ID type. |
| **targetprimaryidvalue** | **str** | Optional | The target primary ID value. |
| **message** | **str** | Optional | The log message. |
| **messagetype** | **str** | Optional | The message type. |
| **timestamp** | **str** | Required | The timestamp of the log record. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ExternalLogRecord import ExternalLogRecord

instance = ExternalLogRecord(
    logid=0,  # required — The unique log identifier.
    parentlogid=0,  # optional — The parent log identifier (null is allowed).
    loglevel="...",  # required — The log level.
    logstatus="...",  # required — The log status.
    sourcerecordtype="...",  # optional — The source record type.
    sourceprimaryidtype="...",  # optional — The source primary ID type.
    sourceprimaryidvalue="...",  # optional — The source primary ID value.
    targetrecordtype="...",  # optional — The target record type.
    targetrecordaction="...",  # optional — The target record action.
    targetprimaryidtype="...",  # optional — The target primary ID type.
    targetprimaryidvalue="...",  # optional — The target primary ID value.
    message="...",  # optional — The log message.
    messagetype="...",  # optional — The message type.
    timestamp="..."  # required — The timestamp of the log record.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

