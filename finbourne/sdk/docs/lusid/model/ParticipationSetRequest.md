# ParticipationSetRequest

A request to create or update multiple Participations.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[ParticipationRequest]](ParticipationRequest.md) | Optional | A collection of ParticipationRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ParticipationSetRequest import ParticipationSetRequest

instance = ParticipationSetRequest(
    requests=[]  # optional — A collection of ParticipationRequests.
)
```


## Related Models

- [ParticipationRequest](ParticipationRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

