# BasketIdentifier

Descriptive information that describes a particular basket of instruments. Most commonly required with a CDS Index or similarly defined instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **str** | Required | Index set, e.g. iTraxx or CDX. |
| **name** | **str** | Required | The index name within the set, e.g. \&quot;MAIN\&quot; or \&quot;Crossover\&quot;. |
| **region** | **str** | Required | Applicable geographic country or region. Typically something like \&quot;Europe\&quot;, \&quot;Asia ex-Japan\&quot;, \&quot;Japan\&quot; or \&quot;Australia\&quot;. |
| **series_id** | **int** | Required | The series identifier. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BasketIdentifier import BasketIdentifier

instance = BasketIdentifier(
    index="...",  # required — Index set, e.g. iTraxx or CDX.
    name="...",  # required — The index name within the set, e.g. \&quot;MAIN\&quot; or \&quot;Crossover\&quot;.
    region="...",  # required — Applicable geographic country or region. Typically something like \&quot;Europe\&quot;, \&quot;Asia ex-Japan\&quot;, \&quot;Japan\&quot; or \&quot;Australia\&quot;.
    series_id=0  # required — The series identifier.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

