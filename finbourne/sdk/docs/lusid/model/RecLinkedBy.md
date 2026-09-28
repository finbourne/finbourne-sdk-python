# RecLinkedBy

The item pairings a link between two rec results was established on, per side.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [List[RecResultLinkKey]](RecResultLinkKey.md) | Required | The pairings between the two results&#39; left-side items, one entry per pairing. May be empty. |
| **right** | [List[RecResultLinkKey]](RecResultLinkKey.md) | Required | The pairings between the two results&#39; right-side items, one entry per pairing. May be empty. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecLinkedBy import RecLinkedBy

instance = RecLinkedBy(
    left=[],  # required — The pairings between the two results&#39; left-side items, one entry per pairing. May be empty.
    right=[]  # required — The pairings between the two results&#39; right-side items, one entry per pairing. May be empty.
)
```


## Related Models

- [RecResultLinkKey](RecResultLinkKey.md) — used in `left`
- [RecResultLinkKey](RecResultLinkKey.md) — used in `right`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

