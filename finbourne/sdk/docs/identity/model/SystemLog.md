# SystemLog

A system log event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **actor** | [LogActor](LogActor.md) | Optional | *No description available.* |
| **authentication_context** | [LogAuthenticationContext](LogAuthenticationContext.md) | Optional | *No description available.* |
| **client_info** | [LogClientInfo](LogClientInfo.md) | Optional | *No description available.* |
| **debug_context** | [LogDebugContext](LogDebugContext.md) | Optional | *No description available.* |
| **display_message** | **str** | Optional | Represents a DisplayMessage resource in the Okta API |
| **event_type** | **str** | Optional | Represents a EventType resource in the Okta API |
| **legacy_event_type** | **str** | Optional | Represents a LegacyEventType resource in the Okta API |
| **outcome** | [LogOutcome](LogOutcome.md) | Optional | *No description available.* |
| **published** | **datetime** | Optional | Represents when Published in the Okta API |
| **request** | [LogRequest](LogRequest.md) | Optional | *No description available.* |
| **security_context** | [LogSecurityContext](LogSecurityContext.md) | Optional | *No description available.* |
| **severity** | [LogSeverity](LogSeverity.md) | Optional | *No description available.* |
| **target** | [List[LogTarget]](LogTarget.md) | Optional | Represents a LogTarget resource in the Okta API |
| **transaction** | [LogTransaction](LogTransaction.md) | Optional | *No description available.* |
| **uuid** | **str** | Optional | Represents Uuid in the Okta API |
| **version** | **str** | Optional | Represents a Version in the Okta API |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SystemLog import SystemLog

instance = SystemLog(
    actor=LogActor(...),  # optional
    authentication_context=LogAuthenticationContext(...),  # optional
    client_info=LogClientInfo(...),  # optional
    debug_context=LogDebugContext(...),  # optional
    display_message="...",  # optional — Represents a DisplayMessage resource in the Okta API
    event_type="...",  # optional — Represents a EventType resource in the Okta API
    legacy_event_type="...",  # optional — Represents a LegacyEventType resource in the Okta API
    outcome=LogOutcome(...),  # optional
    published=datetime.now(),  # optional — Represents when Published in the Okta API
    request=LogRequest(...),  # optional
    security_context=LogSecurityContext(...),  # optional
    severity=LogSeverity(...),  # optional
    target=[],  # optional — Represents a LogTarget resource in the Okta API
    transaction=LogTransaction(...),  # optional
    uuid="...",  # optional — Represents Uuid in the Okta API
    version="..."  # optional — Represents a Version in the Okta API
)
```


## Related Models

- [LogActor](LogActor.md)
- [LogAuthenticationContext](LogAuthenticationContext.md)
- [LogClientInfo](LogClientInfo.md)
- [LogDebugContext](LogDebugContext.md)
- [LogOutcome](LogOutcome.md)
- [LogRequest](LogRequest.md)
- [LogSecurityContext](LogSecurityContext.md)
- [LogSeverity](LogSeverity.md)
- [LogTarget](LogTarget.md) — used in `target`
- [LogTransaction](LogTransaction.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

