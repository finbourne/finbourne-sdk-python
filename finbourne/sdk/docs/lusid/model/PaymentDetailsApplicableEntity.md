# PaymentDetailsApplicableEntity

Identifies the LUSID entity that holds the payment details (e.g. an InvestorRecord or Portfolio).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of the LUSID entity holding the payment details. e.g. \&quot;InvestorRecord\&quot;, \&quot;InvestmentAccount\&quot;, \&quot;Portfolio\&quot;. |
| **entity_scope** | **str** | Optional | The scope of the entity. Optional — required depends on the entity type. |
| **identifier_type** | **str** | Required | The identifier type used to identify the entity. e.g. \&quot;lusidInvestmentAccountId\&quot;. |
| **identifier_scope** | **str** | Optional | The scope of the identifier used to identify the entity. Optional — null for native LUSID identifiers such as code. |
| **identifier_value** | **str** | Required | The identifier value for the entity. e.g. \&quot;LUID_00003DNL\&quot;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentDetailsApplicableEntity import PaymentDetailsApplicableEntity

instance = PaymentDetailsApplicableEntity(
    entity_type="...",  # required — The type of the LUSID entity holding the payment details. e.g. \&quot;InvestorRecord\&quot;, \&quot;InvestmentAccount\&quot;, \&quot;Portfolio\&quot;.
    entity_scope="...",  # optional — The scope of the entity. Optional — required depends on the entity type.
    identifier_type="...",  # required — The identifier type used to identify the entity. e.g. \&quot;lusidInvestmentAccountId\&quot;.
    identifier_scope="...",  # optional — The scope of the identifier used to identify the entity. Optional — null for native LUSID identifiers such as code.
    identifier_value="..."  # required — The identifier value for the entity. e.g. \&quot;LUID_00003DNL\&quot;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

