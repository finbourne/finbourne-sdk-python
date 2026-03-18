# FundJournalEntryLine

A Journal Entry line entity specifically for fund valuation point lines.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **accounting_date** | **datetime** | Required | The Journal Entry Line accounting date. |
| **activity_date** | **datetime** | Required | The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument_id** | **str** | Required | To indicate the instrument of the transaction that the Journal Entry Line posted for, if applicable. |
| **instrument_scope** | **str** | Required | The scope in which the Journal Entry Line instrument is in. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which are part of the AccountingKey. |
| **tax_lot_id** | **str** | Optional | If the holding type is &#39;B&#39; (settled cash balance), this is 1. Otherwise, this is the ID of a tax lot if applicable, or the source ID of the original transaction if not. |
| **general_ledger_account_code** | **str** | Required | The code of the account in the general ledger the Journal Entry was posted to. |
| **local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **base** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **units** | **float** | Required | Units held for the Journal Entry Line. |
| **posting_module_code** | **str** | Optional | The code of the posting module where the posting rules derived the Journal Entry lines. |
| **posting_rule** | **str** | Required | The rule generating the Journal Entry Line. |
| **as_at_date** | **datetime** | Required | The corresponding input date and time of the Transaction generating the Journal Entry Line. |
| **activities_description** | **str** | Optional | This would be the description of the business activities this Journal Entry Line is for. |
| **source_type** | **str** | Required | So far are 4 types: LusidTxn, LusidValuation, Manual and External. |
| **source_id** | **str** | Required | For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Abor. |
| **movement_name** | **str** | Optional | If the JE Line is generated from a transaction, the name of the side in the transaction type&#39;s movement. If from a valuation, this is &#39;MarkToMarket&#39;. |
| **holding_type** | **str** | Required | One of the LUSID holding types such as &#39;P&#39; for position or &#39;B&#39; for settled cash balance. |
| **economic_bucket** | **str** | Required | LUSID automatically categorises a JE Line into a broad economic bucket such as &#39;NA_Cost&#39; or &#39;PL_RealPriceGL&#39;. |
| **economic_bucket_component** | **str** | Optional | Sub bucket of the economic bucket. |
| **economic_bucket_variant** | **str** | Optional | Categorisation of a Mark-to-market journal entry line into LongTerm or ShortTerm based on whether the ActivityDate is more than a year after the purchase trade date or not. |
| **levels** | **List[str]** | Optional | Resolved data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. |
| **source_levels** | **List[str]** | Optional | Source data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. |
| **movement_sign** | **str** | Optional | Indicates if the Journal Entry Line corresponds to a Long or Short movement. |
| **holding_sign** | **str** | Optional | Indicates if the Journal Entry Line is operating against a Long or Short holding. |
| **ledger_column** | **str** | Optional | Indicates if the Journal Entry Line is credit or debit. |
| **journal_entry_line_type** | **str** | Optional | Indicates the Journal Entry Line type |
| **share_class_breakdowns** | [List[JournalEntryLineShareClassBreakdown]](JournalEntryLineShareClassBreakdown.md) | Optional | Share Class breakdown data for this Journal Entry Line. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundJournalEntryLine import FundJournalEntryLine

instance = FundJournalEntryLine(
    accounting_date=datetime.now(),  # required — The Journal Entry Line accounting date.
    activity_date=datetime.now(),  # required — The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period.
    portfolio_id=ResourceId(...),  # required
    instrument_id="...",  # required — To indicate the instrument of the transaction that the Journal Entry Line posted for, if applicable.
    instrument_scope="...",  # required — The scope in which the Journal Entry Line instrument is in.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which are part of the AccountingKey.
    tax_lot_id="...",  # optional — If the holding type is &#39;B&#39; (settled cash balance), this is 1. Otherwise, this is the ID of a tax lot if applicable, or the source ID of the original transaction if not.
    general_ledger_account_code="...",  # required — The code of the account in the general ledger the Journal Entry was posted to.
    local=CurrencyAndAmount(...),  # required
    base=CurrencyAndAmount(...),  # required
    units=0.0,  # required — Units held for the Journal Entry Line.
    posting_module_code="...",  # optional — The code of the posting module where the posting rules derived the Journal Entry lines.
    posting_rule="...",  # required — The rule generating the Journal Entry Line.
    as_at_date=datetime.now(),  # required — The corresponding input date and time of the Transaction generating the Journal Entry Line.
    activities_description="...",  # optional — This would be the description of the business activities this Journal Entry Line is for.
    source_type="...",  # required — So far are 4 types: LusidTxn, LusidValuation, Manual and External.
    source_id="...",  # required — For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates.
    properties=ModelProperty(...),  # optional — A set of properties for the Abor.
    movement_name="...",  # optional — If the JE Line is generated from a transaction, the name of the side in the transaction type&#39;s movement. If from a valuation, this is &#39;MarkToMarket&#39;.
    holding_type="...",  # required — One of the LUSID holding types such as &#39;P&#39; for position or &#39;B&#39; for settled cash balance.
    economic_bucket="...",  # required — LUSID automatically categorises a JE Line into a broad economic bucket such as &#39;NA_Cost&#39; or &#39;PL_RealPriceGL&#39;.
    economic_bucket_component="...",  # optional — Sub bucket of the economic bucket.
    economic_bucket_variant="...",  # optional — Categorisation of a Mark-to-market journal entry line into LongTerm or ShortTerm based on whether the ActivityDate is more than a year after the purchase trade date or not.
    levels=,  # optional — Resolved data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body.
    source_levels=,  # optional — Source data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body.
    movement_sign="...",  # optional — Indicates if the Journal Entry Line corresponds to a Long or Short movement.
    holding_sign="...",  # optional — Indicates if the Journal Entry Line is operating against a Long or Short holding.
    ledger_column="...",  # optional — Indicates if the Journal Entry Line is credit or debit.
    journal_entry_line_type="...",  # optional — Indicates the Journal Entry Line type
    share_class_breakdowns=[],  # optional — Share Class breakdown data for this Journal Entry Line.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [JournalEntryLineShareClassBreakdown](JournalEntryLineShareClassBreakdown.md) — used in `share_class_breakdowns`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

