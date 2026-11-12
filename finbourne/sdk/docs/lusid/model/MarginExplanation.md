# MarginExplanation

How the margin figures of a call or a line were arrived at: the working behind each figure as a tree of components,  with the working of portfolios the caller may not read replaced by a redacted component.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The URI of this explanation. |
| **run_id** | **str** | Required | The run whose figures are explained. |
| **agreement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **item** | **str** | Optional | The margin item of the call explained or, for a line, of the line. |
| **margin_type** | **str** | Optional | The margin type of the call explained. Null when a line is explained. |
| **direction** | **str** | Optional | Who posts under the call explained: WePost, TheyPost or None. Null when a line is explained. |
| **line_key** | **str** | Optional | The key of the line explained. Null when a call is explained. |
| **currency** | **str** | Required | The agreement&#39;s base currency, in which a component&#39;s value is expressed unless the component names another. |
| **scenario** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **components** | [List[MarginExplanationComponent]](MarginExplanationComponent.md) | Required | The working behind each figure explained, one root component per figure: for a call its required amount, named InitialMarginRequired, and for a line each figure asked for that the run explained, named VariationMargin or InitialMargin. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginExplanation import MarginExplanation

instance = MarginExplanation(
    href="...",  # optional — The URI of this explanation.
    run_id="...",  # required — The run whose figures are explained.
    agreement_id=ResourceId(...),  # required
    item="...",  # optional — The margin item of the call explained or, for a line, of the line.
    margin_type="...",  # optional — The margin type of the call explained. Null when a line is explained.
    direction="...",  # optional — Who posts under the call explained: WePost, TheyPost or None. Null when a line is explained.
    line_key="...",  # optional — The key of the line explained. Null when a call is explained.
    currency="...",  # required — The agreement&#39;s base currency, in which a component&#39;s value is expressed unless the component names another.
    scenario=ResourceId(...),  # optional
    components=[]  # required — The working behind each figure explained, one root component per figure: for a call its required amount, named InitialMarginRequired, and for a line each figure asked for that the run explained, named VariationMargin or InitialMargin.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [MarginExplanationComponent](MarginExplanationComponent.md) — used in `components`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

