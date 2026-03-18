# UpsertFundBookmarkRequest

A definition for the period you wish to close
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bookmark_code** | **str** | Required | Unique code for the Bookmark. |
| **display_name** | **str** | Required | Identifiable Name assigned to the Bookmark. |
| **description** | **str** | Optional | Description assigned to the Bookmark. |
| **effective_at** | **datetime** | Required | The effective time of the Bookmark. |
| **query_as_at** | **datetime** | Optional | The query time of the Bookmark. Defaults to latest. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Bookmark. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Bookmark. Defaults to Latest. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Bookmark. Defaults to Latest. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertFundBookmarkRequest import UpsertFundBookmarkRequest

instance = UpsertFundBookmarkRequest(
    bookmark_code="...",  # required — Unique code for the Bookmark.
    display_name="...",  # required — Identifiable Name assigned to the Bookmark.
    description="...",  # optional — Description assigned to the Bookmark.
    effective_at=datetime.now(),  # required — The effective time of the Bookmark.
    query_as_at=datetime.now(),  # optional — The query time of the Bookmark. Defaults to latest.
    properties=ModelProperty(...),  # optional — A set of properties for the Bookmark.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Bookmark. Defaults to Latest.
    valuations_as_at_override=datetime.now()  # optional — The optional AsAt Override to use for performing valuations in the Bookmark. Defaults to Latest.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

