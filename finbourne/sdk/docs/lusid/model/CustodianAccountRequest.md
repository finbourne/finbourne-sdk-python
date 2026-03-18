# CustodianAccountRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Optional | The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used |
| **code** | **str** | Required | Unique Code representing the Custodian Account |
| **status** | **str** | Optional | The Account status. Can be Active, Inactive or Deleted. |
| **account_number** | **str** | Required | The Custodian Account Number |
| **account_name** | **str** | Required | The identifiable name given to the Custodian Account |
| **accounting_method** | **str** | Required | The Accounting method to be used |
| **currency** | **str** | Required | The Currency for the Account |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. |
| **custodian_identifier** | [TypedResourceId](TypedResourceId.md) | Required | *No description available.* |
| **account_type** | **str** | Optional | The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustodianAccountRequest import CustodianAccountRequest

instance = CustodianAccountRequest(
    scope="...",  # optional — The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used
    code="...",  # required — Unique Code representing the Custodian Account
    status="...",  # optional — The Account status. Can be Active, Inactive or Deleted.
    account_number="...",  # required — The Custodian Account Number
    account_name="...",  # required — The identifiable name given to the Custodian Account
    accounting_method="...",  # required — The Accounting method to be used
    currency="...",  # required — The Currency for the Account
    properties=ModelProperty(...),  # optional — Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain.
    custodian_identifier=TypedResourceId(...),  # required
    account_type="..."  # optional — The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [TypedResourceId](TypedResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

