# CashElection

Cash election for Events that result in a cash payment.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | Unique key used to identify this election. |
| **exchange_rate** | **float** | Optional | The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared. |
| **dividend_rate** | **float** | Optional | The payment rate for this CashElection. |
| **is_chosen** | **bool** | Optional | Has this election been chosen.  Only one Election may be Chosen per Event. |
| **is_declared** | **bool** | Optional | Is this the declared CashElection.  Only one Election may be Declared per Event. |
| **is_default** | **bool** | Optional | Is this election the default.  Only one Election may be Default per Event |
| **dividend_currency** | **str** | Required | The payment currency for this CashElection. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashElection import CashElection

instance = CashElection(
    election_key="...",  # required — Unique key used to identify this election.
    exchange_rate=0.0,  # optional — The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared.
    dividend_rate=0.0,  # optional — The payment rate for this CashElection.
    is_chosen=True,  # optional — Has this election been chosen.  Only one Election may be Chosen per Event.
    is_declared=True,  # optional — Is this the declared CashElection.  Only one Election may be Declared per Event.
    is_default=True,  # optional — Is this election the default.  Only one Election may be Default per Event
    dividend_currency="..."  # required — The payment currency for this CashElection.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

