# TpfTransactionSearchRequest

Request body for the POST transaction-search endpoint. Multiple values in TransactionIds and InstrumentIdentifiers are OR'd within each filter; both filters together are AND'd.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_ids** | **List[str]** | Optional | One or more LUSID transaction IDs to search for (max 50). Values are OR&#39;d. |
| **instrument_identifiers** | **List[str]** | Optional | One or more instrument identifiers to search for (max 50). Values are OR&#39;d. Accepts LusidInstrumentId, Isin, Figi, Ticker, Cusip, Sedol or ClientInternal values. Every value is matched exactly against the stored instrument id; non-LUID values are also resolved against LUSID instruments in the default scope, whose own matching rules (including case) apply. |
| **instance_id** | **str** | Optional | Instance ID to filter by. Omit or leave null to search all instances the caller has access to. |
| **var_from** | **datetime** | Optional | Start of the date range (inclusive). Defaults to 30 days ago if neither From nor To is provided. |
| **to** | **datetime** | Optional | End of the date range (inclusive). Defaults to now if not provided. |
| **limit** | **int** | Optional | Maximum number of results to return per page. |
| **page** | **str** | Optional | Pagination token from a previous response NextPage or PreviousPage. Omit for the first page. |
| **status** | **str** | Optional | Publication status to filter by. Valid values: Sent, Skipped, Failed. Optional. |
| **filter** | **str** | Optional | Filter expression to apply to the results, in the format \&quot;property operator value\&quot; (e.g., eq, ne, gt, lt), combined with \&quot;and\&quot;/\&quot;or\&quot; as needed. Filterable properties are transactionId, instanceName, runStartTime, instrumentName, instrumentType, instrumentId, tradeDate, settlementDate, skipReason, failureReason, fileName, portfolioScope, portfolioCode, and runId. PublicationStatus is not filterable here — use the Status body parameter instead. Dates are quoted ISO-8601. Destinations is not filterable. Must remain the same across pages — the page token includes a hash of both filter and sortBy. |
| **sort_by** | **List[str]** | Optional | Up to two sortable fields, each optionally suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Deterministic tiebreakers are appended automatically: RunStartTime DESC, TransactionId ASC, BatchUuid ASC, FileName ASC. Must remain the same across pages — the page token includes a hash of both filter and sortBy. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfTransactionSearchRequest import TpfTransactionSearchRequest

instance = TpfTransactionSearchRequest(
    transaction_ids=,  # optional — One or more LUSID transaction IDs to search for (max 50). Values are OR&#39;d.
    instrument_identifiers=,  # optional — One or more instrument identifiers to search for (max 50). Values are OR&#39;d. Accepts LusidInstrumentId, Isin, Figi, Ticker, Cusip, Sedol or ClientInternal values. Every value is matched exactly against the stored instrument id; non-LUID values are also resolved against LUSID instruments in the default scope, whose own matching rules (including case) apply.
    instance_id="...",  # optional — Instance ID to filter by. Omit or leave null to search all instances the caller has access to.
    var_from=datetime.now(),  # optional — Start of the date range (inclusive). Defaults to 30 days ago if neither From nor To is provided.
    to=datetime.now(),  # optional — End of the date range (inclusive). Defaults to now if not provided.
    limit=0,  # optional — Maximum number of results to return per page.
    page="...",  # optional — Pagination token from a previous response NextPage or PreviousPage. Omit for the first page.
    status="...",  # optional — Publication status to filter by. Valid values: Sent, Skipped, Failed. Optional.
    filter="...",  # optional — Filter expression to apply to the results, in the format \&quot;property operator value\&quot; (e.g., eq, ne, gt, lt), combined with \&quot;and\&quot;/\&quot;or\&quot; as needed. Filterable properties are transactionId, instanceName, runStartTime, instrumentName, instrumentType, instrumentId, tradeDate, settlementDate, skipReason, failureReason, fileName, portfolioScope, portfolioCode, and runId. PublicationStatus is not filterable here — use the Status body parameter instead. Dates are quoted ISO-8601. Destinations is not filterable. Must remain the same across pages — the page token includes a hash of both filter and sortBy.
    sort_by=  # optional — Up to two sortable fields, each optionally suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Deterministic tiebreakers are appended automatically: RunStartTime DESC, TransactionId ASC, BatchUuid ASC, FileName ASC. Must remain the same across pages — the page token includes a hash of both filter and sortBy.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

