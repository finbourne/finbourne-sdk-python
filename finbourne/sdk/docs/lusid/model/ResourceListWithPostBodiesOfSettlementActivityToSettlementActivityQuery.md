# ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery

A version of the resource list for use with list endpoints that use the POST verb instead of GET, allowing  the endpoint to return the POST body(s) that can be sent in conjunction with the Next Page and/or Previous  Page links to retrieve the next/previous page of results. This should make it easier for SDK consumers to  fluently page through results. The PagedResourceList only exposes a page token string, typically for use in  a query parameter, and thus is more suited to GET endpoints.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[SettlementActivity]](SettlementActivity.md) | Required | The resources to list. |
| **href** | **str** | Optional | The URI of the resource list. |
| **post_body** | [SettlementActivityQuery](SettlementActivityQuery.md) | Optional | *No description available.* |
| **next_page** | [SettlementActivityQuery](SettlementActivityQuery.md) | Optional | *No description available.* |
| **previous_page** | [SettlementActivityQuery](SettlementActivityQuery.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery import ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery

instance = ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery(
    values=[],  # required — The resources to list.
    href="...",  # optional — The URI of the resource list.
    post_body=SettlementActivityQuery(...),  # optional
    next_page=SettlementActivityQuery(...),  # optional
    previous_page=SettlementActivityQuery(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [SettlementActivity](SettlementActivity.md) — used in `values`
- [SettlementActivityQuery](SettlementActivityQuery.md)
- [SettlementActivityQuery](SettlementActivityQuery.md)
- [SettlementActivityQuery](SettlementActivityQuery.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

