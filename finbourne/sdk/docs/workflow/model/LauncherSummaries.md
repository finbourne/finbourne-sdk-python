# LauncherSummaries

Sentences that say what a Launcher does, meant to be shown to a person.              These are rendered on read from the stored Launcher details. They are never stored and never accepted on a write, so the same Launcher always reads back the same summaries
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **schedule** | **str** | Optional | A sentence that says when the Launcher starts a run, for example \&quot;At 09:00 every weekday, London time\&quot;.              Null for an Event Launcher, which has no schedule |
| **fields** | **Dict[str, Optional[str]]** | Optional | A sentence for each field of the root task the Launcher fills, keyed by the field name on the root task definition. Empty when the Launcher fills no fields |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LauncherSummaries import LauncherSummaries

instance = LauncherSummaries(
    schedule="...",  # optional — A sentence that says when the Launcher starts a run, for example \&quot;At 09:00 every weekday, London time\&quot;.              Null for an Event Launcher, which has no schedule
    fields=  # optional — A sentence for each field of the root task the Launcher fills, keyed by the field name on the root task definition. Empty when the Launcher fills no fields
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

