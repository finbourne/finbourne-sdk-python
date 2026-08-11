# AccessEvaluationLog

Holds logged information about an access check performed on an API.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **timestamp** | **datetime** | Required | The timestamp of the access evaluation. |
| **application** | **str** | Required | The name of the application that the request was made from. |
| **id** | **str** | Required | The ID of the access evaluation. |
| **request_id** | **str** | Optional | The identifier of the request. |
| **session_id** | **str** | Optional | The identifier of the session that the request was made in. |
| **user** | **str** | Required | The user who made the request. |
| **user_type** | **str** | Optional | The type of the user who made the request. |
| **duration** | **float** | Required | The duration of the access evaluation. |
| **result** | **str** | Optional | The result of the access evaluation. |
| **authoritative_role_id** | **str** | Optional | The role that matched the access evaluation to provide a result. |
| **authoritative_policy_id** | **str** | Optional | The policy that matched the access evaluation to provide a result. |
| **authoritative_selector** | **str** | Optional | The selector that matched the access evaluation to provide a result. |
| **resource_type** | **str** | Optional | The type of the resource that the access evaluation is for. |
| **action** | **str** | Optional | The action key of the access evaluation. |
| **resource** | **Dict[str, Optional[str]]** | Optional | The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \&quot;resourceId\&quot;. |
| **resource_from_effective_date** | **str** | Optional | The From effective date of the resource. |
| **resource_to_effective_date** | **str** | Optional | The To effective date of the resource. |
| **resource_from_as_at** | **str** | Optional | The From AsAt date of the resource. |
| **resource_to_as_at** | **str** | Optional | The To AsAt date of the resource. |
| **access_execution_time** | **str** | Optional | The execution time of the entitlement. |
| **access_as_at_time** | **str** | Optional | The AsAt time of the entitlement. |
| **required_licence_policy_id** | **str** | Optional | ID of the required licence policy. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AccessEvaluationLog import AccessEvaluationLog

instance = AccessEvaluationLog(
    timestamp=datetime.now(),  # required — The timestamp of the access evaluation.
    application="...",  # required — The name of the application that the request was made from.
    id="...",  # required — The ID of the access evaluation.
    request_id="...",  # optional — The identifier of the request.
    session_id="...",  # optional — The identifier of the session that the request was made in.
    user="...",  # required — The user who made the request.
    user_type="...",  # optional — The type of the user who made the request.
    duration=0.0,  # required — The duration of the access evaluation.
    result="...",  # optional — The result of the access evaluation.
    authoritative_role_id="...",  # optional — The role that matched the access evaluation to provide a result.
    authoritative_policy_id="...",  # optional — The policy that matched the access evaluation to provide a result.
    authoritative_selector="...",  # optional — The selector that matched the access evaluation to provide a result.
    resource_type="...",  # optional — The type of the resource that the access evaluation is for.
    action="...",  # optional — The action key of the access evaluation.
    resource=,  # optional — The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \&quot;resourceId\&quot;.
    resource_from_effective_date="...",  # optional — The From effective date of the resource.
    resource_to_effective_date="...",  # optional — The To effective date of the resource.
    resource_from_as_at="...",  # optional — The From AsAt date of the resource.
    resource_to_as_at="...",  # optional — The To AsAt date of the resource.
    access_execution_time="...",  # optional — The execution time of the entitlement.
    access_as_at_time="...",  # optional — The AsAt time of the entitlement.
    required_licence_policy_id="...",  # optional — ID of the required licence policy.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

