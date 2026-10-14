# AllocationMapIlpaTransactionType

The ILPA transaction type an Allocation Map reports one kind of allocation event under, overriding the default.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The kind of allocation event the ILPA transaction type applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. |
| **ilpa_transaction_type** | **str** | Required | The ILPA transaction type events of this kind are reported under, for example &#39;Capital Call: Investments&#39; or &#39;Distribution: Recallable&#39;. Must be a value of the system IlpaTransactionType data type. |
| **component** | **str** | Optional | The component of the event the ILPA transaction type applies to, for example MgmtFee or ROC. Absent means the entry is the default for every component of the event type without an entry of its own. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapIlpaTransactionType import AllocationMapIlpaTransactionType

instance = AllocationMapIlpaTransactionType(
    event_type="...",  # required — The kind of allocation event the ILPA transaction type applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding.
    ilpa_transaction_type="...",  # required — The ILPA transaction type events of this kind are reported under, for example &#39;Capital Call: Investments&#39; or &#39;Distribution: Recallable&#39;. Must be a value of the system IlpaTransactionType data type.
    component="..."  # optional — The component of the event the ILPA transaction type applies to, for example MgmtFee or ROC. Absent means the entry is the default for every component of the event type without an entry of its own.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

