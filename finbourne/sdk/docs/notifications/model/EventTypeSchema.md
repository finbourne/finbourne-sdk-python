# EventTypeSchema

An EventType object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The identifier of the event type |
| **display_name** | **str** | Optional | Identifier name of the event |
| **description** | **str** | Optional | The summary of the event |
| **application** | **str** | Optional | The application associated with the event |
| **header_schema** | [List[EventFieldDefinition]](EventFieldDefinition.md) | Optional | The header schema for the event type *(read-only)* |
| **body_schema** | [List[EventFieldDefinition]](EventFieldDefinition.md) | Optional | The body schema for the event type *(read-only)* |
| **href** | **str** | Optional | A URI for retrieving this schema |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.EventTypeSchema import EventTypeSchema

instance = EventTypeSchema(
    id="...",  # optional — The identifier of the event type
    display_name="...",  # optional — Identifier name of the event
    description="...",  # optional — The summary of the event
    application="...",  # optional — The application associated with the event
    header_schema=[],  # optional — The header schema for the event type
    body_schema=[],  # optional — The body schema for the event type
    href="..."  # optional — A URI for retrieving this schema
)
```

- [EventFieldDefinition](EventFieldDefinition.md) — used in `header_schema`
- [EventFieldDefinition](EventFieldDefinition.md) — used in `body_schema`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

