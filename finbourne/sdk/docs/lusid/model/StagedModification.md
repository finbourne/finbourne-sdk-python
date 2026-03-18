# StagedModification

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The unique Id for the staged modification |
| **as_at_staged** | **datetime** | Optional | Time at which the modification was staged. |
| **user_id_staged** | **str** | Optional | Id of the user who created the stage modification request. |
| **requested_id_staged** | **str** | Optional | The Request Id that initiated this staged modification. |
| **request_reason** | **str** | Optional | The Request Reason from the context that initiated this staged modification. |
| **action** | **str** | Optional | Type of action of the staged modification, either create, update or delete. |
| **staging_rule** | [StagedModificationStagingRule](StagedModificationStagingRule.md) | Optional | *No description available.* |
| **decisions** | [List[StagedModificationDecision]](StagedModificationDecision.md) | Optional | Object containing information relating to the decision on the staged modification. |
| **decisions_count** | **int** | Optional | Number of decisions made. |
| **status** | **str** | Optional | The status of the staged modification. |
| **as_at_closed** | **datetime** | Optional | Time at which the modification was closed by either rejection or approval. |
| **entity_type** | **str** | Optional | The type of the entity that the staged modification applies to. |
| **scope** | **str** | Optional | The scope of the entity that this staged modification applies to. |
| **entity_unique_id** | **str** | Optional | The unique Id of the entity the staged modification applies to. |
| **requested_changes** | [RequestedChanges](RequestedChanges.md) | Optional | *No description available.* |
| **entity_hrefs** | [StagedModificationsEntityHrefs](StagedModificationsEntityHrefs.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | The display name of the entity the staged modification applies to. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModification import StagedModification

instance = StagedModification(
    id="...",  # optional — The unique Id for the staged modification
    as_at_staged=datetime.now(),  # optional — Time at which the modification was staged.
    user_id_staged="...",  # optional — Id of the user who created the stage modification request.
    requested_id_staged="...",  # optional — The Request Id that initiated this staged modification.
    request_reason="...",  # optional — The Request Reason from the context that initiated this staged modification.
    action="...",  # optional — Type of action of the staged modification, either create, update or delete.
    staging_rule=StagedModificationStagingRule(...),  # optional
    decisions=[],  # optional — Object containing information relating to the decision on the staged modification.
    decisions_count=0,  # optional — Number of decisions made.
    status="...",  # optional — The status of the staged modification.
    as_at_closed=datetime.now(),  # optional — Time at which the modification was closed by either rejection or approval.
    entity_type="...",  # optional — The type of the entity that the staged modification applies to.
    scope="...",  # optional — The scope of the entity that this staged modification applies to.
    entity_unique_id="...",  # optional — The unique Id of the entity the staged modification applies to.
    requested_changes=RequestedChanges(...),  # optional
    entity_hrefs=StagedModificationsEntityHrefs(...),  # optional
    display_name="...",  # optional — The display name of the entity the staged modification applies to.
    links=[]  # optional
)
```

- [StagedModificationStagingRule](StagedModificationStagingRule.md)
- [StagedModificationDecision](StagedModificationDecision.md) — used in `decisions`
- [RequestedChanges](RequestedChanges.md)
- [StagedModificationsEntityHrefs](StagedModificationsEntityHrefs.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

