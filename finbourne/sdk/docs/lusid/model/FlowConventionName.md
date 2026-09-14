# FlowConventionName

Representation of an abstract definition of a flow convention set consisting of currency, tenor and an index name (arbitrary string but likely something like \"IBOR\").
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency** | **str** | Required | Currency of the flow convention name. |
| **index_name** | **str** | Optional | The index, if present, that is required. e.g. \&quot;IBOR\&quot;, \&quot;OIS\&quot; or \&quot;SONIA\&quot;. |
| **tenor** | **str** | Required | Tenor for the convention name.    For more information on tenors, see [Specifying tenors in LUSID](https://support.lusid.com/docs/specifying-tenors-in-lusid) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FlowConventionName import FlowConventionName

instance = FlowConventionName(
    currency="...",  # required — Currency of the flow convention name.
    index_name="...",  # optional — The index, if present, that is required. e.g. \&quot;IBOR\&quot;, \&quot;OIS\&quot; or \&quot;SONIA\&quot;.
    tenor="..."  # required — Tenor for the convention name.    For more information on tenors, see [Specifying tenors in LUSID](https://support.lusid.com/docs/specifying-tenors-in-lusid)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

