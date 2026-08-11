# CreatePortfolioGroupRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. |
| **created** | **datetime** | Optional | The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified. |
| **values** | [List[ResourceId]](ResourceId.md) | Optional | The resource identifiers of the portfolios to be contained within the portfolio group. |
| **sub_groups** | [List[ResourceId]](ResourceId.md) | Optional | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of unique group properties to add to the portfolio group. Each property must be from the &#39;PortfolioGroup&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;PortfolioGroup/Manager/Id&#39;. These properties must be pre-defined. |
| **display_name** | **str** | Required | The name of the portfolio group. |
| **description** | **str** | Optional | A long form description of the portfolio group. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreatePortfolioGroupRequest import CreatePortfolioGroupRequest

instance = CreatePortfolioGroupRequest(
    code="...",  # required — The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group.
    created=datetime.now(),  # optional — The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified.
    values=[],  # optional — The resource identifiers of the portfolios to be contained within the portfolio group.
    sub_groups=[],  # optional — The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups.
    properties=ModelProperty(...),  # optional — A set of unique group properties to add to the portfolio group. Each property must be from the &#39;PortfolioGroup&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;PortfolioGroup/Manager/Id&#39;. These properties must be pre-defined.
    display_name="...",  # required — The name of the portfolio group.
    description="..."  # optional — A long form description of the portfolio group.
)
```

- [ResourceId](ResourceId.md) — used in `values`
- [ResourceId](ResourceId.md) — used in `sub_groups`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

