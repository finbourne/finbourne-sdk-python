# LineageMember

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **int** | Required | Index to demonstrate position of lineage member in overall lineage |
| **label** | **str** | Required | Label of the step corresponding to this lineage member |
| **sub_label** | **str** | Required | SubLabel of the step corresponding to this lineage member |
| **info_type** | **str** | Optional | Optional. Type of Information |
| **information** | **str** | Optional | Optional. Information for the step corresponding to this lineage member, of type InfoType |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LineageMember import LineageMember

instance = LineageMember(
    index=0,  # required — Index to demonstrate position of lineage member in overall lineage
    label="...",  # required — Label of the step corresponding to this lineage member
    sub_label="...",  # required — SubLabel of the step corresponding to this lineage member
    info_type="...",  # optional — Optional. Type of Information
    information="..."  # optional — Optional. Information for the step corresponding to this lineage member, of type InfoType
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

