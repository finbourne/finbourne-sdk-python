# CustomMultiQueryItem

One query within a Finbourne.Honeycomb.WebApi.BackgroundQueries.MultiQuery.CustomMultiQueryRequest, given as either raw LuminesceSql or a saved query reference.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Unique name of the query, of at most 31 characters. Later queries refer to this one&#39;s results as &#x60;@Name&#x60;, and it names the result in any export. |
| **sql** | **str** | Optional | The LuminesceSql to run.  Exactly one of this and &#x60;SavedQuery&#x60; must be given. |
| **saved_query** | **str** | Optional | A key within the Saved Queries (of the Workspaces API) to load the SQL from.  Exactly one of this and &#x60;Sql&#x60; must be given. e.g. &#x60;personal/YourUserId/items/queries/SomeQuery&#x60; or &#x60;shared/SomeWorkspace/items/queries/SomeQuery&#x60;. |
| **is_external_result** | **bool** | Optional | Should the results of this query be fetchable / exported?  If false it is only an intermediate step for later queries. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryItem import CustomMultiQueryItem

instance = CustomMultiQueryItem(
    name="...",  # required — Unique name of the query, of at most 31 characters. Later queries refer to this one&#39;s results as &#x60;@Name&#x60;, and it names the result in any export.
    sql="...",  # optional — The LuminesceSql to run.  Exactly one of this and &#x60;SavedQuery&#x60; must be given.
    saved_query="...",  # optional — A key within the Saved Queries (of the Workspaces API) to load the SQL from.  Exactly one of this and &#x60;Sql&#x60; must be given. e.g. &#x60;personal/YourUserId/items/queries/SomeQuery&#x60; or &#x60;shared/SomeWorkspace/items/queries/SomeQuery&#x60;.
    is_external_result=True  # optional — Should the results of this query be fetchable / exported?  If false it is only an intermediate step for later queries.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

