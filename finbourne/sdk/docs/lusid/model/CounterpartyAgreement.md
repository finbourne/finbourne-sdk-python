# CounterpartyAgreement

Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | A user-defined display label for the Counterparty Agreement. |
| **agreement_type** | **str** | Required | A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;. |
| **counterparty_signatory** | [CounterpartySignatory](CounterpartySignatory.md) | Required | *No description available.* |
| **dated_as_of** | **datetime** | Required | The date on which the CounterpartyAgreement was signed by both parties. |
| **credit_support_annex_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CounterpartyAgreement import CounterpartyAgreement

instance = CounterpartyAgreement(
    display_name="...",  # required — A user-defined display label for the Counterparty Agreement.
    agreement_type="...",  # required — A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;.
    counterparty_signatory=CounterpartySignatory(...),  # required
    dated_as_of=datetime.now(),  # required — The date on which the CounterpartyAgreement was signed by both parties.
    credit_support_annex_id=ResourceId(...),  # required
    id=ResourceId(...)  # required
)
```

- [CounterpartySignatory](CounterpartySignatory.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

