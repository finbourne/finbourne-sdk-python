# ApportionmentInput

One named amount that contributed to a member share class's apportionment base value - the workings behind  the figure rather than the figure alone. A member's inputs always sum to its base value.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The input&#39;s identifier within its apportionment method, for example &#39;openingNav&#39;. |
| **display_name** | **str** | Required | The input&#39;s human-readable name, for example &#39;Opening NAV&#39;. |
| **value** | **float** | Required | The input&#39;s contribution to the base value, signed as it contributes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApportionmentInput import ApportionmentInput

instance = ApportionmentInput(
    code="...",  # required — The input&#39;s identifier within its apportionment method, for example &#39;openingNav&#39;.
    display_name="...",  # required — The input&#39;s human-readable name, for example &#39;Opening NAV&#39;.
    value=0.0  # required — The input&#39;s contribution to the base value, signed as it contributes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

