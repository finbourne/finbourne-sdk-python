# lusid.FundsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_estimate_valuation_point**](FundsApi.md#accept_estimate_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$acceptestimate | [EARLY ACCESS] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.
[**accrue_carry**](FundsApi.md#accrue_carry) | **POST** /api/api/funds/{scope}/{code}/carry/$accrue | [EARLY ACCESS] AccrueCarry: [EXPERIMENTAL] AccrueCarry: Accrue carried interest to the Fund&#39;s partners.
[**add_allocation_groups**](FundsApi.md#add_allocation_groups) | **POST** /api/api/funds/{scope}/{code}/allocationgroups | [EARLY ACCESS] AddAllocationGroups: Add Allocation Groups to a Fund.
[**add_series**](FundsApi.md#add_series) | **POST** /api/api/funds/{scope}/{code}/series | [EARLY ACCESS] AddSeries: Add Series to a Fund.
[**advance_tax_return**](FundsApi.md#advance_tax_return) | **POST** /api/api/funds/{scope}/{code}/tax/return/advance | [EARLY ACCESS] AdvanceTaxReturn: [EARLY ACCESS] AdvanceTaxReturn: Advance the tax return one workflow step.
[**approve_tax_provision**](FundsApi.md#approve_tax_provision) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode}/tax/provision/approve | [EARLY ACCESS] ApproveTaxProvision: [EARLY ACCESS] ApproveTaxProvision: Approve the deferred-tax provision of a Valuation Point.
[**calculate_management_fees**](FundsApi.md#calculate_management_fees) | **POST** /api/api/funds/{scope}/{code}/fees/$calculate | [EARLY ACCESS] CalculateManagementFees: [EXPERIMENTAL] CalculateManagementFees: Calculate the management fee per partner for a period.
[**create_facility**](FundsApi.md#create_facility) | **POST** /api/api/funds/{scope}/{code}/facilities | [EXPERIMENTAL] CreateFacility: [EXPERIMENTAL] CreateFacility: Create a Facility.
[**create_fee**](FundsApi.md#create_fee) | **POST** /api/api/funds/{scope}/{code}/fees | [EARLY ACCESS] CreateFee: Create a Fee.
[**create_fund**](FundsApi.md#create_fund) | **POST** /api/api/funds/{scope} | [EARLY ACCESS] CreateFund: Create a Fund.
[**create_fund_v2**](FundsApi.md#create_fund_v2) | **POST** /api/api/funds/v2/{scope} | [EARLY ACCESS] CreateFundV2: Create a Fund V2 (Preview).
[**create_valuation_point**](FundsApi.md#create_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$create | [EARLY ACCESS] CreateValuationPoint: Create a Valuation Point.
[**deactivate_nav_types**](FundsApi.md#deactivate_nav_types) | **POST** /api/api/funds/{scope}/{code}/deactivateNavTypes | [EARLY ACCESS] DeactivateNavTypes: Deactivate NAV types on a Fund.
[**delete_bookmark**](FundsApi.md#delete_bookmark) | **DELETE** /api/api/funds/{scope}/{code}/bookmarks/{bookmarkCode} | [EARLY ACCESS] DeleteBookmark: Delete a Bookmark.
[**delete_facility**](FundsApi.md#delete_facility) | **DELETE** /api/api/funds/{scope}/{code}/facilities/{facilityCode} | [EXPERIMENTAL] DeleteFacility: [EXPERIMENTAL] DeleteFacility: Delete a Facility.
[**delete_fee**](FundsApi.md#delete_fee) | **DELETE** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] DeleteFee: Delete a Fee.
[**delete_fund**](FundsApi.md#delete_fund) | **DELETE** /api/api/funds/{scope}/{code} | [EARLY ACCESS] DeleteFund: Delete a Fund.
[**delete_nav_activity_adjustments**](FundsApi.md#delete_nav_activity_adjustments) | **POST** /api/api/funds/{scope}/{code}/navAdjustment/$delete | [EARLY ACCESS] DeleteNavActivityAdjustments: Delete Nav activity adjustments.
[**delete_series**](FundsApi.md#delete_series) | **DELETE** /api/api/funds/{scope}/{code}/shareclasses/{shareClassCode}/series/{seriesIdentifier} | [EARLY ACCESS] DeleteSeries: [EARLY ACCESS] DeleteSeries: Remove a Series from a Share Class of a Fund.
[**delete_tax_cost_record**](FundsApi.md#delete_tax_cost_record) | **DELETE** /api/api/funds/{scope}/{code}/taxcostrecords/{taxCostRecordCode} | [EXPERIMENTAL] DeleteTaxCostRecord: [EXPERIMENTAL] DeleteTaxCostRecord: Delete a Tax Cost Record.
[**delete_valuation_point**](FundsApi.md#delete_valuation_point) | **DELETE** /api/api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode} | [EARLY ACCESS] DeleteValuationPoint: Delete a Valuation Point.
[**diff_partner_statement**](FundsApi.md#diff_partner_statement) | **GET** /api/api/funds/{scope}/{code}/partners/{investorRecordId}/statements/{statementId}/$diff | [EARLY ACCESS] DiffPartnerStatement: [EXPERIMENTAL] DiffPartnerStatement: Compare two of a partner&#39;s statements.
[**finalise_candidate_valuation_point**](FundsApi.md#finalise_candidate_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$finalisecandidate | [EARLY ACCESS] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.
[**get_a2_b_data_for_fund**](FundsApi.md#get_a2_b_data_for_fund) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/a2b/$query | [EARLY ACCESS] GetA2BDataForFund: Get A2B data for a Fund.
[**get_a2_b_movements_for_fund**](FundsApi.md#get_a2_b_movements_for_fund) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/a2bmovements/$query | [EARLY ACCESS] GetA2BMovementsForFund: Get A2B movements for transaction portfolios in a Fund.
[**get_facility**](FundsApi.md#get_facility) | **GET** /api/api/funds/{scope}/{code}/facilities/{facilityCode} | [EXPERIMENTAL] GetFacility: [EXPERIMENTAL] GetFacility: Get a Facility for a specified Fund.
[**get_fee**](FundsApi.md#get_fee) | **GET** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] GetFee: Get a Fee for a specified Fund.
[**get_fee_properties**](FundsApi.md#get_fee_properties) | **GET** /api/api/funds/{scope}/{code}/fees/{feeCode}/properties | [EARLY ACCESS] GetFeeProperties: Get Fee properties.
[**get_fund**](FundsApi.md#get_fund) | **GET** /api/api/funds/{scope}/{code} | [EARLY ACCESS] GetFund: Get a Fund.
[**get_fund_performance**](FundsApi.md#get_fund_performance) | **GET** /api/api/funds/{scope}/{code}/performance | [EARLY ACCESS] GetFundPerformance: [EARLY ACCESS] GetFundPerformance: Get a fund&#39;s performance measures over all its partners.
[**get_fund_properties**](FundsApi.md#get_fund_properties) | **GET** /api/api/funds/{scope}/{code}/properties | [EARLY ACCESS] GetFundProperties: Get Fund properties.
[**get_fund_tax_scope**](FundsApi.md#get_fund_tax_scope) | **GET** /api/api/funds/{scope}/{code}/tax/scope | [EARLY ACCESS] GetFundTaxScope: [EARLY ACCESS] GetFundTaxScope: Get the UK chargeable-gains tax scope of a fund.
[**get_holding_contributors_for_fund**](FundsApi.md#get_holding_contributors_for_fund) | **POST** /api/api/funds/{scope}/{code}/holdings/{holdingId}/contributors | [EARLY ACCESS] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.
[**get_holdings_for_fund**](FundsApi.md#get_holdings_for_fund) | **POST** /api/api/funds/{scope}/{code}/$holdings | [EARLY ACCESS] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.
[**get_partner_capital_account**](FundsApi.md#get_partner_capital_account) | **GET** /api/api/funds/{scope}/{code}/partners/{irScope}/{irCode}/capitalaccount | [EARLY ACCESS] GetPartnerCapitalAccount: [EARLY ACCESS] GetPartnerCapitalAccount: Get a partner&#39;s capital account statement.
[**get_partner_performance**](FundsApi.md#get_partner_performance) | **GET** /api/api/funds/{scope}/{code}/partners/{irScope}/{irCode}/performance | [EARLY ACCESS] GetPartnerPerformance: [EARLY ACCESS] GetPartnerPerformance: Get a partner&#39;s performance measures.
[**get_partner_unfunded_reconciliation**](FundsApi.md#get_partner_unfunded_reconciliation) | **GET** /api/api/funds/{scope}/{code}/partners/{investorRecordId}/unfundedreconciliation | [EARLY ACCESS] GetPartnerUnfundedReconciliation: [EARLY ACCESS] GetPartnerUnfundedReconciliation: Get a partner&#39;s unfunded commitment statement.
[**get_partners**](FundsApi.md#get_partners) | **GET** /api/api/funds/{scope}/{code}/partners | [EARLY ACCESS] GetPartners: [EARLY ACCESS] GetPartners: Get the partners of a partnership fund.
[**get_partnership_config_pack**](FundsApi.md#get_partnership_config_pack) | **GET** /api/api/funds/{scope}/{code}/partnershipaccounting/configpack | [EARLY ACCESS] GetPartnershipConfigPack: [EXPERIMENTAL] GetPartnershipConfigPack: Get the partnership configuration pack of a Fund.
[**get_series**](FundsApi.md#get_series) | **GET** /api/api/funds/{scope}/{code}/series | [EARLY ACCESS] GetSeries: [EARLY ACCESS] GetSeries: List the Series of a Fund.
[**get_tax_deemed_disposal**](FundsApi.md#get_tax_deemed_disposal) | **GET** /api/api/funds/{scope}/{code}/tax/deemed-disposals/{holdingId}/{date} | [EARLY ACCESS] GetTaxDeemedDisposal: [EARLY ACCESS] GetTaxDeemedDisposal: Get one deemed disposal.
[**get_tax_deemed_disposals**](FundsApi.md#get_tax_deemed_disposals) | **GET** /api/api/funds/{scope}/{code}/tax/deemed-disposals | [EARLY ACCESS] GetTaxDeemedDisposals: [EARLY ACCESS] GetTaxDeemedDisposals: List the deemed disposals of a Fund or company.
[**get_tax_fund_reconciliation**](FundsApi.md#get_tax_fund_reconciliation) | **GET** /api/api/funds/{scope}/{code}/tax/fund-reconciliation | [EARLY ACCESS] GetTaxFundReconciliation: [EARLY ACCESS] GetTaxFundReconciliation: Reconcile a company&#39;s tax figures to its member funds.
[**get_tax_fund_reconciliation_holding**](FundsApi.md#get_tax_fund_reconciliation_holding) | **GET** /api/api/funds/{scope}/{code}/tax/fund-reconciliation/holdings/{holdingId} | [EARLY ACCESS] GetTaxFundReconciliationHolding: [EARLY ACCESS] GetTaxFundReconciliationHolding: Drill into one holding of the company-to-funds reconciliation.
[**get_tax_ledger_reconciliation**](FundsApi.md#get_tax_ledger_reconciliation) | **GET** /api/api/funds/{scope}/{code}/tax/ledger-reconciliation | [EARLY ACCESS] GetTaxLedgerReconciliation: [EARLY ACCESS] GetTaxLedgerReconciliation: Reconcile the tax figures of a Fund or company to its ledger.
[**get_tax_ledger_reconciliation_holding**](FundsApi.md#get_tax_ledger_reconciliation_holding) | **GET** /api/api/funds/{scope}/{code}/tax/ledger-reconciliation/holdings/{holdingId} | [EARLY ACCESS] GetTaxLedgerReconciliationHolding: [EARLY ACCESS] GetTaxLedgerReconciliationHolding: Drill into one holding of the tax-to-ledger reconciliation.
[**get_tax_provision**](FundsApi.md#get_tax_provision) | **GET** /api/api/funds/{scope}/{code}/tax/provision | [EARLY ACCESS] GetTaxProvision: [EARLY ACCESS] GetTaxProvision: Get the deferred-tax provision of a Valuation Point.
[**get_tax_return**](FundsApi.md#get_tax_return) | **GET** /api/api/funds/{scope}/{code}/tax/return | [EARLY ACCESS] GetTaxReturn: [EARLY ACCESS] GetTaxReturn: Get the year-end tax return of a Fund or company.
[**get_tax_sync_status**](FundsApi.md#get_tax_sync_status) | **GET** /api/api/funds/{scope}/{code}/tax/sync | [EARLY ACCESS] GetTaxSyncStatus: [EARLY ACCESS] GetTaxSyncStatus: Get the tax sync position of each portfolio in a Fund.
[**get_valuation_for_fund**](FundsApi.md#get_valuation_for_fund) | **POST** /api/api/funds/{scope}/{code}/$valuation | [EARLY ACCESS] GetValuationForFund: Perform valuation for a Fund.
[**get_valuation_point_data**](FundsApi.md#get_valuation_point_data) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$query | [EARLY ACCESS] GetValuationPointData: Get Valuation Point Data for a Fund.
[**get_valuation_point_journal_entry_lines**](FundsApi.md#get_valuation_point_journal_entry_lines) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/journalentrylines/$query | [EARLY ACCESS] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.
[**get_valuation_point_pnl_summary**](FundsApi.md#get_valuation_point_pnl_summary) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/pnlsummary/$query | [EARLY ACCESS] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.
[**get_valuation_point_quotes**](FundsApi.md#get_valuation_point_quotes) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/quotes/$query | [EARLY ACCESS] GetValuationPointQuotes: Get the Quotes for the given Fund and Valuation Point.
[**get_valuation_point_transactions**](FundsApi.md#get_valuation_point_transactions) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/transactions/$query | [EARLY ACCESS] GetValuationPointTransactions: Get the Transactions for the given Fund.
[**get_valuation_point_trial_balance**](FundsApi.md#get_valuation_point_trial_balance) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/trialbalance/$query | [EARLY ACCESS] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.
[**get_valuation_point_unsettled_transactions**](FundsApi.md#get_valuation_point_unsettled_transactions) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/unsettledtransactions/$query | [EARLY ACCESS] GetValuationPointUnsettledTransactions: Get Unsettled Transactions for the given Fund.
[**list_facilities**](FundsApi.md#list_facilities) | **GET** /api/api/funds/{scope}/{code}/facilities | [EXPERIMENTAL] ListFacilities: [EXPERIMENTAL] ListFacilities: List Facilities for a specified Fund.
[**list_fees**](FundsApi.md#list_fees) | **GET** /api/api/funds/{scope}/{code}/fees | [EARLY ACCESS] ListFees: List Fees for a specified Fund.
[**list_fund_calendar**](FundsApi.md#list_fund_calendar) | **GET** /api/api/funds/{scope}/{code}/calendar | [EARLY ACCESS] ListFundCalendar: List Fund Calendar.
[**list_fund_calendar_entries**](FundsApi.md#list_fund_calendar_entries) | **GET** /api/api/funds/{scope}/{code}/calendars | [EARLY ACCESS] ListFundCalendarEntries: List Fund Calendar Entries.
[**list_funds**](FundsApi.md#list_funds) | **GET** /api/api/funds | [EARLY ACCESS] ListFunds: List Funds.
[**list_nav_activity_adjustments**](FundsApi.md#list_nav_activity_adjustments) | **GET** /api/api/funds/{scope}/{code}/navAdjustment | [EARLY ACCESS] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point
[**list_partner_capital_accounts**](FundsApi.md#list_partner_capital_accounts) | **GET** /api/api/funds/{scope}/{code}/capitalaccounts | [EARLY ACCESS] ListPartnerCapitalAccounts: [EARLY ACCESS] ListPartnerCapitalAccounts: List the capital account statements of a fund&#39;s partners.
[**list_partner_statements**](FundsApi.md#list_partner_statements) | **GET** /api/api/funds/{scope}/{code}/partners/{investorRecordId}/statements | [EARLY ACCESS] ListPartnerStatements: [EXPERIMENTAL] ListPartnerStatements: List the statements produced for a partner.
[**list_tax_cost_records**](FundsApi.md#list_tax_cost_records) | **GET** /api/api/funds/{scope}/{code}/taxcostrecords | [EXPERIMENTAL] ListTaxCostRecords: [EXPERIMENTAL] ListTaxCostRecords: List Tax Cost Records for a specified Fund.
[**list_tax_exceptions**](FundsApi.md#list_tax_exceptions) | **GET** /api/api/funds/{scope}/{code}/tax/exceptions | [EARLY ACCESS] ListTaxExceptions: [EARLY ACCESS] ListTaxExceptions: List the open tax exceptions of a Fund.
[**list_tax_exceptions_across_funds**](FundsApi.md#list_tax_exceptions_across_funds) | **GET** /api/api/tax/exceptions | [EARLY ACCESS] ListTaxExceptionsAcrossFunds: [EARLY ACCESS] ListTaxExceptionsAcrossFunds: List the open tax exceptions across every Fund.
[**list_tax_provisions**](FundsApi.md#list_tax_provisions) | **GET** /api/api/funds/{scope}/{code}/tax/provisions | [EARLY ACCESS] ListTaxProvisions: [EARLY ACCESS] ListTaxProvisions: List the deferred-tax provisions of a Fund.
[**list_valuation_point_complex_market_data**](FundsApi.md#list_valuation_point_complex_market_data) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/complexmarketdata/$query | [EARLY ACCESS] ListValuationPointComplexMarketData: List the Complex Market Data for the given Fund and Valuation Point.
[**list_valuation_point_instruments**](FundsApi.md#list_valuation_point_instruments) | **GET** /api/api/funds/{scope}/{code}/valuationpoints/instruments/$query | [EARLY ACCESS] ListValuationPointInstruments: List Instruments inside a valuation point
[**list_valuation_point_overview**](FundsApi.md#list_valuation_point_overview) | **GET** /api/api/funds/{scope}/{code}/valuationPointOverview | [EARLY ACCESS] ListValuationPointOverview: List Valuation Points Overview for a given Fund.
[**patch_fee**](FundsApi.md#patch_fee) | **PATCH** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] PatchFee: Patch Fee.
[**patch_fund**](FundsApi.md#patch_fund) | **PATCH** /api/api/funds/{scope}/{code} | [EARLY ACCESS] PatchFund: Patch a Fund.
[**produce_partner_statement**](FundsApi.md#produce_partner_statement) | **POST** /api/api/funds/{scope}/{code}/partners/{investorRecordId}/statements | [EARLY ACCESS] ProducePartnerStatement: [EXPERIMENTAL] ProducePartnerStatement: Produce a partner&#39;s capital statement for a period.
[**query_cash_statement**](FundsApi.md#query_cash_statement) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/cashstatement/$query | [DEPRECATED] QueryCashStatement: [DEPRECATED] QueryCashStatement: Query cash statement for a Fund valuation point.
[**query_cash_statement_local_currency**](FundsApi.md#query_cash_statement_local_currency) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/cashstatementlocalcurrency/$query | [EARLY ACCESS] QueryCashStatementLocalCurrency: [EXPERIMENTAL] QueryCashStatementLocalCurrency: Query the local-currency cash statement for a Fund valuation point.
[**revert_valuation_point_to_estimate**](FundsApi.md#revert_valuation_point_to_estimate) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$reverttoestimate | [EARLY ACCESS] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.
[**run_partner_allocations**](FundsApi.md#run_partner_allocations) | **POST** /api/api/funds/{scope}/{code}/partnerallocations/$run | [EARLY ACCESS] RunPartnerAllocations: [EXPERIMENTAL] RunPartnerAllocations: Allocate a period&#39;s income to the Fund&#39;s partners.
[**send_back_tax_return**](FundsApi.md#send_back_tax_return) | **POST** /api/api/funds/{scope}/{code}/tax/return/send-back | [EARLY ACCESS] SendBackTaxReturn: [EARLY ACCESS] SendBackTaxReturn: Send the tax return back one workflow step.
[**set_share_class_instruments**](FundsApi.md#set_share_class_instruments) | **PUT** /api/api/funds/{scope}/{code}/shareclasses | [EARLY ACCESS] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.
[**update_valuation_point**](FundsApi.md#update_valuation_point) | **PUT** /api/api/funds/{scope}/{code}/valuationpoints | [EARLY ACCESS] UpdateValuationPoint: Update a Valuation Point.
[**upsert_bookmark**](FundsApi.md#upsert_bookmark) | **POST** /api/api/funds/{scope}/{code}/bookmarks | [EARLY ACCESS] UpsertBookmark: Upsert a bookmark.
[**upsert_diary_entry_type_valuation_point**](FundsApi.md#upsert_diary_entry_type_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints | [EARLY ACCESS] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.
[**upsert_external_dealing_estimates**](FundsApi.md#upsert_external_dealing_estimates) | **POST** /api/api/funds/{scope}/{code}/dealingestimates/$external | [EARLY ACCESS] UpsertExternalDealingEstimates: Load dealing estimates sent by an external transfer agent
[**upsert_fee_properties**](FundsApi.md#upsert_fee_properties) | **POST** /api/api/funds/{scope}/{code}/fees/{feeCode}/properties/$upsert | [EARLY ACCESS] UpsertFeeProperties: Upsert Fee properties.
[**upsert_fund_properties**](FundsApi.md#upsert_fund_properties) | **POST** /api/api/funds/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertFundProperties: Upsert Fund properties.
[**upsert_nav_activity_adjustments**](FundsApi.md#upsert_nav_activity_adjustments) | **POST** /api/api/funds/{scope}/{code}/navAdjustment | [EARLY ACCESS] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point
[**upsert_tax_cost_records**](FundsApi.md#upsert_tax_cost_records) | **POST** /api/api/funds/{scope}/{code}/taxcostrecords | [EXPERIMENTAL] UpsertTaxCostRecords: [EXPERIMENTAL] UpsertTaxCostRecords: Upsert Tax Cost Records for a specified Fund.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.funds_api import FundsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FundsApi)
```

---

# **accept_estimate_valuation_point**
> AcceptEstimateValuationPointResponse acceptEstimateValuationPoint = accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.

Accepts the specified estimate Valuation Point.  Should the Valuation Point differ since the Valuation Point was last run, both Valuation Points will be returned and status will be marked as 'Candidate',  otherwise it will be marked as 'Final'.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_request = ValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](../model/ValuationPointDataRequest.md)| The valuationPointDataRequest which contains the Diary Entry code for the Estimate Valuation Point to move to Candidate or Final state. | [required] 
 **nav_type_code** | **str**| When provided, accepts the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**AcceptEstimateValuationPointResponse**](../model/AcceptEstimateValuationPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accepted Estimate point and status after being Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **accrue_carry**
> CarryAccrualResult accrueCarry = accrue_carry(scope, code, carry_accrual_request, as_at=as_at)

[EARLY ACCESS] AccrueCarry: [EXPERIMENTAL] AccrueCarry: Accrue carried interest to the Fund's partners.

Take the carry each partner has earned to the period end, as the waterfall states it, and book the movement  against what is already accrued on the books.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
carry_accrual_request = CarryAccrualRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.accrue_carry(scope, code, carry_accrual_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **carry_accrual_request** | [**CarryAccrualRequest**](../model/CarryAccrualRequest.md)| The carry to accrue. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**CarryAccrualResult**](../model/CarryAccrualResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The carry accrual movement per partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **add_allocation_groups**
> Fund addAllocationGroups = add_allocation_groups(scope, code, allocation_group_definition)

[EARLY ACCESS] AddAllocationGroups: Add Allocation Groups to a Fund.

Add the given Allocation Group definitions to the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_group_definition = [{"classes":[{"shareClassShortCode":"ScA","apportionmentFactor":0.6},{"shareClassShortCode":"ScB","apportionmentFactor":0.4}],"name":"Allocation Group 1","shareClassShortCode":"ScA"}] # List[AllocationGroupDefinition]
api_response = api_instance.add_allocation_groups(scope, code, allocation_group_definition)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **allocation_group_definition** | [**List[AllocationGroupDefinition]**](../model/AllocationGroupDefinition.md)| The definitions of the Allocation Groups to add to the Fund. | [required] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the added Allocation Groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **add_series**
> Fund addSeries = add_series(scope, code, series_definition_request)

[EARLY ACCESS] AddSeries: Add Series to a Fund.

Add the given Series definitions to the specified Share Classes of the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
series_definition_request = [{"shareClassCode":"ShareClass1","seriesDefinitions":[{"seriesIdentifier":"Series1","seriesType":"Lead","launchDate":"2024-01-01T00:00:00.0000000+00:00","launchPriceType":"Manual","domCcy":"GBP","properties":{}}]}] # List[SeriesDefinitionRequest]
api_response = api_instance.add_series(scope, code, series_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **series_definition_request** | [**List[SeriesDefinitionRequest]**](../model/SeriesDefinitionRequest.md)| The definitions of the Series to add. | [required] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the added Series. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **advance_tax_return**
> TaxReturnResponse advanceTaxReturn = advance_tax_return(scope, code, tax_return_transition_request, effective_at=effective_at, tax_period=tax_period)

[EARLY ACCESS] AdvanceTaxReturn: [EARLY ACCESS] AdvanceTaxReturn: Advance the tax return one workflow step.

Moves the return from Draft to Prepared, Prepared to Reviewed, Reviewed to SignedOff or SignedOff to Final. Advancing past Reviewed requires the tax records to be in sync with the ledger. Each step is recorded with the supplied reason.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
tax_return_transition_request = TaxReturnTransitionRequest()
effective_at = 'effective_at_example' # str (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.advance_tax_return(scope, code, tax_return_transition_request, effective_at=effective_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **tax_return_transition_request** | [**TaxReturnTransitionRequest**](../model/TaxReturnTransitionRequest.md)| The reason for advancing the return. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxReturnResponse**](../model/TaxReturnResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax return after the transition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **approve_tax_provision**
> TaxProvision approveTaxProvision = approve_tax_provision(scope, code, diary_entry_code, nav_type_code=nav_type_code)

[EARLY ACCESS] ApproveTaxProvision: [EARLY ACCESS] ApproveTaxProvision: Approve the deferred-tax provision of a Valuation Point.

Moves the Valuation Point's deferred-tax provision from Estimate to Approved, stores it as the official  document and books the movement since the previous approved Valuation Point as an accrual on the Fund.  Approving an already approved provision fails. Until tax elections can be configured on the Fund every  provision is struck under the default elections: a 20% rate, indexation allowance applied and losses carried  forward.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_code = 'diary_entry_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.approve_tax_provision(scope, code, diary_entry_code, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **diary_entry_code** | **str**| The Diary Entry code of the Valuation Point whose provision is approved. | [required] 
 **nav_type_code** | **str**| When provided, approves the provision of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**TaxProvision**](../model/TaxProvision.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The approved deferred-tax provision |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **calculate_management_fees**
> ManagementFeeResult calculateManagementFees = calculate_management_fees(scope, code, management_fee_request, as_at=as_at)

[EARLY ACCESS] CalculateManagementFees: [EXPERIMENTAL] CalculateManagementFees: Calculate the management fee per partner for a period.

Charge the Fund's management fee on each partner's capital base for the period, net of any fee income offsets,  and book the net fee unless the request asks only for the calculation.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
management_fee_request = ManagementFeeRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.calculate_management_fees(scope, code, management_fee_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **management_fee_request** | [**ManagementFeeRequest**](../model/ManagementFeeRequest.md)| The fee period, basis and offsets. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**ManagementFeeResult**](../model/ManagementFeeResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The management fee per partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_facility**
> Facility createFacility = create_facility(scope, code, facility_request)

[EXPERIMENTAL] CreateFacility: [EXPERIMENTAL] CreateFacility: Create a Facility.

Create the given Facility against a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
facility_request = FacilityRequest()
api_response = api_instance.create_facility(scope, code, facility_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **facility_request** | [**FacilityRequest**](../model/FacilityRequest.md)| The Facility to create. | [required] 

### Return type

[**Facility**](../model/Facility.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Facility. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fee**
> Fee createFee = create_fee(scope, code, fee_request, nav_type_code=nav_type_code)

[EARLY ACCESS] CreateFee: Create a Fee.

Create the given Fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_request = FeeRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.create_fee(scope, code, fee_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_request** | [**FeeRequest**](../model/FeeRequest.md)| The Fee to create. | [required] 
 **nav_type_code** | **str**| When provided, creates the Fee against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**Fee**](../model/Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fund**
> Fund createFund = create_fund(scope, fund_request)

[EARLY ACCESS] CreateFund: Create a Fund.

Create the given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
fund_request = FundRequest()
api_response = api_instance.create_fund(scope, fund_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **fund_request** | [**FundRequest**](../model/FundRequest.md)| The definition of the Fund. | [required] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fund_v2**
> Fund createFundV2 = create_fund_v2(scope, fund_definition_request)

[EARLY ACCESS] CreateFundV2: Create a Fund V2 (Preview).

Create the given V2 Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
fund_definition_request = FundDefinitionRequest()
api_response = api_instance.create_fund_v2(scope, fund_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **fund_definition_request** | [**FundDefinitionRequest**](../model/FundDefinitionRequest.md)| The definition of the Fund. | [required] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_valuation_point**
> ValuationPoint createValuationPoint = create_valuation_point(scope, code, create_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] CreateValuationPoint: Create a Valuation Point.

Insert the estimate Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_valuation_point_request = CreateValuationPointRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.create_valuation_point(scope, code, create_valuation_point_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **create_valuation_point_request** | [**CreateValuationPointRequest**](../model/CreateValuationPointRequest.md)| The Valuation Point Estimate definition to create. | [required] 
 **nav_type_code** | **str**| When provided, creates the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPoint**](../model/ValuationPoint.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **deactivate_nav_types**
> Fund deactivateNavTypes = deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)

[EARLY ACCESS] DeactivateNavTypes: Deactivate NAV types on a Fund.

Deactivate the given NAV types on the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = ["NavTypeCode1","NavTypeCode2"] # List[str]
delete_mode = 'delete_mode_example' # str (optional)
api_response = api_instance.deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **request_body** | [**List[str]**](../model/str.md)| The codes of the nav types to be deactivated. | [required] 
 **delete_mode** | **str**| The delete mode to use. Default value: Soft. Available values: Soft, Hard. | [optional] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the specified NAV types deactivated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_bookmark**
> DeletedEntityResponse deleteBookmark = delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)

[EARLY ACCESS] DeleteBookmark: Delete a Bookmark.

Deletes the given Bookmark.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
bookmark_code = 'bookmark_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **bookmark_code** | **str**| The bookmark code for the bookmark to be deleted. | [required] 
 **nav_type_code** | **str**| When provided, deletes the Bookmark against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Bookmark was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_facility**
> DeletedEntityResponse deleteFacility = delete_facility(scope, code, facility_code)

[EXPERIMENTAL] DeleteFacility: [EXPERIMENTAL] DeleteFacility: Delete a Facility.

Delete the given Facility.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
facility_code = 'facility_code_example' # str
api_response = api_instance.delete_facility(scope, code, facility_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **facility_code** | **str**| The code of the Facility to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Facility was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_fee**
> DeletedEntityResponse deleteFee = delete_fee(scope, code, fee_code)

[EARLY ACCESS] DeleteFee: Delete a Fee.

Delete the given Fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
api_response = api_instance.delete_fee(scope, code, fee_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fee was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_fund**
> DeletedEntityResponse deleteFund = delete_fund(scope, code)

[EARLY ACCESS] DeleteFund: Delete a Fund.

Delete the given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_fund(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to be deleted. | [required] 
 **code** | **str**| The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fund was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_nav_activity_adjustments**
> DeletedEntityResponse deleteNavActivityAdjustments = delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment_response, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] DeleteNavActivityAdjustments: Delete Nav activity adjustments.

Delete Nav activity adjustments on a Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_activity_adjustment_response = [{"navActivityAdjustmentSource":"Undefined","asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransactionAdjustment"},{"navActivityAdjustmentSource":"Undefined","asAt":"2024-01-01T00:00:00.0000000+00:00","corporateActionSourceScope":"corporateActionSourceScope1","corporateActionSourceCode":"corporateActionSourceCode1","instrumentEventId":"instrumentEventId1","navActivityAdjustmentType":"InstrumentEventActivityAdjustment"}] # List[NavActivityAdjustmentResponse]
nav_type_code = 'nav_type_code_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment_response, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| The valuation point Code to delete the adjustment from | [required] 
 **nav_activity_adjustment_response** | [**List[NavActivityAdjustmentResponse]**](../model/NavActivityAdjustmentResponse.md)| The request describing the Nav activity adjustments to delete from a specific valuation point and nav type | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Nav activity adjustments were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_series**
> DeletedEntityResponse deleteSeries = delete_series(scope, code, share_class_code, series_identifier)

[EARLY ACCESS] DeleteSeries: [EARLY ACCESS] DeleteSeries: Remove a Series from a Share Class of a Fund.

Removes the Series from the Share Class. A Series that still has units in issue cannot be removed.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
share_class_code = 'share_class_code_example' # str
series_identifier = 'series_identifier_example' # str
api_response = api_instance.delete_series(scope, code, share_class_code, series_identifier)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **share_class_code** | **str**| The short code of the Share Class the Series belongs to. | [required] 
 **series_identifier** | **str**| The identifier of the Series to remove. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Series was removed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_tax_cost_record**
> DeletedEntityResponse deleteTaxCostRecord = delete_tax_cost_record(scope, code, tax_cost_record_code)

[EXPERIMENTAL] DeleteTaxCostRecord: [EXPERIMENTAL] DeleteTaxCostRecord: Delete a Tax Cost Record.

Delete the given Tax Cost Record.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
tax_cost_record_code = 'tax_cost_record_code_example' # str
api_response = api_instance.delete_tax_cost_record(scope, code, tax_cost_record_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **tax_cost_record_code** | **str**| The code of the Tax Cost Record to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Tax Cost Record was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_valuation_point**
> DeletedEntityResponse deleteValuationPoint = delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)

[EARLY ACCESS] DeleteValuationPoint: Delete a Valuation Point.

Deletes the given Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_code = 'diary_entry_code_example' # str
diary_entry_code_variant = 'diary_entry_code_variant_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **diary_entry_code** | **str**| The diary entry code for the valuation Point to be deleted. | [required] 
 **diary_entry_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. This is working only for the Estimates. | [optional] 
 **nav_type_code** | **str**| When provided, deletes the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Valuation Point was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **diff_partner_statement**
> PartnerStatementDiff diffPartnerStatement = diff_partner_statement(scope, code, investor_record_id, statement_id, against)

[EARLY ACCESS] DiffPartnerStatement: [EXPERIMENTAL] DiffPartnerStatement: Compare two of a partner's statements.

Compare a partner's statement against another produced for the same partner, figure by figure.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
statement_id = 'statement_id_example' # str
against = 'against_example' # str
api_response = api_instance.diff_partner_statement(scope, code, investor_record_id, statement_id, against)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **investor_record_id** | **str**| The investor record the statements are for. | [required] 
 **statement_id** | **str**| The identifier of the statement to compare. | [required] 
 **against** | **str**| The identifier of the statement to compare against. | [required] 

### Return type

[**PartnerStatementDiff**](../model/PartnerStatementDiff.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The figures that differ between the two statements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **finalise_candidate_valuation_point**
> ValuationPointDataResponse finaliseCandidateValuationPoint = finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.

Moves a 'Candidate' status Valuation Point to status 'Final'.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_request = ValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](../model/ValuationPointDataRequest.md)| The details of the Valuation Point to mark as final. | [required] 
 **nav_type_code** | **str**| When provided, finalises the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](../model/ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Valuation Point response as a result of it be marked as Final. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_a2_b_data_for_fund**
> VersionedResourceListOfFundA2BDataRecord getA2BDataForFund = get_a2_b_data_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)

[EARLY ACCESS] GetA2BDataForFund: Get A2B data for a Fund.

Get the A2B data for transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_a2_b_data_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the A2B data. This includes start and end dates. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the A2B data. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**VersionedResourceListOfFundA2BDataRecord**](../model/VersionedResourceListOfFundA2BDataRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The A2B data for transaction portfolios in a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_a2_b_movements_for_fund**
> VersionedResourceListOfFundA2BMovementRecord getA2BMovementsForFund = get_a2_b_movements_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)

[EARLY ACCESS] GetA2BMovementsForFund: Get A2B movements for transaction portfolios in a Fund.

Get the A2B movement records of transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_a2_b_movements_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the A2B movements. This includes start and end dates. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the A2B movements. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**VersionedResourceListOfFundA2BMovementRecord**](../model/VersionedResourceListOfFundA2BMovementRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The A2B movement records of transaction portfolios for a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_facility**
> Facility getFacility = get_facility(scope, code, facility_code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetFacility: [EXPERIMENTAL] GetFacility: Get a Facility for a specified Fund.

Retrieve a Facility for a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
facility_code = 'facility_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_facility(scope, code, facility_code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **facility_code** | **str**| The code of the Facility. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Facility. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Facility. Defaults to returning the latest version of the Facility if not specified. | [optional] 

### Return type

[**Facility**](../model/Facility.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Facility definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee**
> Fee getFee = get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetFee: Get a Fee for a specified Fund.

Retrieve a fee for a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fee**](../model/Fee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee_properties**
> FeeProperties getFeeProperties = get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetFeeProperties: Get Fee properties.

Get all the properties of a single fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to get the properties for. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fee&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fee&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FeeProperties**](../model/FeeProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fee |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund**
> Fund getFund = get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetFund: Get a Fund.

Retrieve the definition of a particular Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_performance**
> PartnerPerformance getFundPerformance = get_fund_performance(scope, code, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetFundPerformance: [EARLY ACCESS] GetFundPerformance: Get a fund's performance measures over all its partners.

The fund's PIC, DPI, RVPI, TVPI and net IRR built from the capital activity of every partner on the  register, open or closed, with the same optional with- and without-facility views as the partner read.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fund_performance(scope, code, nav_type_code=nav_type_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerPerformance**](../model/PartnerPerformance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fund&#39;s performance measures over all its partners. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_properties**
> FundProperties getFundProperties = get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetFundProperties: Get Fund properties.

Get all the properties of a single fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to list the properties for. | [required] 
 **code** | **str**| The code of the Fund to list the properties for. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fund&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fund&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FundProperties**](../model/FundProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_tax_scope**
> FundTaxScope getFundTaxScope = get_fund_tax_scope(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetFundTaxScope: [EARLY ACCESS] GetFundTaxScope: Get the UK chargeable-gains tax scope of a fund.

Returns the fund's portfolios within the UK chargeable-gains regime and the exclusions the regime's figures  apply. A fund portfolio is in scope when its own details elect the regime. A NAV type that elects the regime  puts its derived portfolio for each fund portfolio in scope, since that is where the fund accounts for the  holdings under the election.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fund_tax_scope(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the tax scope. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the tax scope. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**FundTaxScope**](../model/FundTaxScope.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax scope of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_holding_contributors_for_fund**
> VersionedResourceListOfHoldingContributor getHoldingContributorsForFund = get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)

[EARLY ACCESS] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
holding_id = 56 # int
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
include_historic = False # bool (optional)
tax_lot_id = 'tax_lot_id_example' # str (optional)
include_unsettled_movements = False # bool (optional)
limit = 56 # int (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
api_response = api_instance.get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **holding_id** | **int**| The unique holding identifier | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the holdings.This can be a date, valuationPoint or a bookmark. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **include_unsettled_movements** | **bool**| If true, contributing transaction which have not settled yet will also be returned. False by default | [optional] [default to False]
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](../model/VersionedResourceListOfHoldingContributor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors from the specified Fund and NavType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_holdings_for_fund**
> VersionedResourceListOfPortfolioHolding getHoldingsForFund = get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)

[EARLY ACCESS] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
single_valuation_point_query_parameters = SingleValuationPointQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
by_taxlots = True # bool (optional)
include_settlement_events_after_days = 56 # int (optional)
api_response = api_instance.get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **single_valuation_point_query_parameters** | [**SingleValuationPointQueryParameters**](../model/SingleValuationPointQueryParameters.md)| The arguments to use for querying the holdings. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of transaction portfolios in the Fund. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot;,\&quot;CustodianAccount\&quot; or \&quot;LegalEntity\&quot; domain to decorate onto domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether to expand the holdings to return the underlying tax-lots. Defaults to False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](../model/VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings of transaction portfolios for a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_partner_capital_account**
> PartnerCapitalAccount getPartnerCapitalAccount = get_partner_capital_account(scope, code, ir_scope, ir_code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetPartnerCapitalAccount: [EARLY ACCESS] GetPartnerCapitalAccount: Get a partner's capital account statement.

One partner's capital account over a period, rolled from beginning capital through contributions,  distributions, transfers, allocated income, fees, gains and carried interest to ending capital, with  quarter-, year- and inception-to-date columns. The memo block carries the commitment position. The  statement is an estimate until a final valuation point covers the period end.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
ir_scope = 'ir_scope_example' # str
ir_code = 'ir_code_example' # str
period_start = '2013-10-20T19:20:30+01:00' # datetime (optional)
period_end = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_partner_capital_account(scope, code, ir_scope, ir_code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **ir_scope** | **str**| The scope of the partner&#39;s investor record. | [required] 
 **ir_code** | **str**| The code of the partner&#39;s investor record. | [required] 
 **period_start** | **datetime**| The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. | [optional] 
 **period_end** | **datetime**| The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. | [optional] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerCapitalAccount**](../model/PartnerCapitalAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s capital account statement over the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_partner_performance**
> PartnerPerformance getPartnerPerformance = get_partner_performance(scope, code, ir_scope, ir_code, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetPartnerPerformance: [EARLY ACCESS] GetPartnerPerformance: Get a partner's performance measures.

One partner's paid-in to committed (PIC), distributions to paid-in (DPI), residual value to paid-in (RVPI),  total value to paid-in (TVPI) and net IRR, together with the dated cash flows the IRR was solved from.  Where any of the partner's events were financed by a subscription facility, the measures are also given  with and without the facility, the latter re-dating facility-funded calls to the deal funding date.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
ir_scope = 'ir_scope_example' # str
ir_code = 'ir_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_partner_performance(scope, code, ir_scope, ir_code, nav_type_code=nav_type_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **ir_scope** | **str**| The scope of the partner&#39;s investor record. | [required] 
 **ir_code** | **str**| The code of the partner&#39;s investor record. | [required] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerPerformance**](../model/PartnerPerformance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s performance measures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_partner_unfunded_reconciliation**
> FundPartnerUnfundedReconciliation getPartnerUnfundedReconciliation = get_partner_unfunded_reconciliation(scope, code, investor_record_id, var_from, to=to, as_at=as_at)

[EARLY ACCESS] GetPartnerUnfundedReconciliation: [EARLY ACCESS] GetPartnerUnfundedReconciliation: Get a partner's unfunded commitment statement.

Reconciles one partner's unfunded commitment over a period: the register's opening unfunded, less capital  called inside the commitment, plus recallable distributions, less recallable distributions that expired,  plus or minus commitment changes and transfers, gives the closing unfunded, which is checked against the  register's unfunded at the close. Every booked allocation to the partner in the period is listed with the  ILPA transaction type it is reported under.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
var_from = 'var_from_example' # str
to = 'to_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_partner_unfunded_reconciliation(scope, code, investor_record_id, var_from, to=to, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **investor_record_id** | **str**| The investor record of the partner. | [required] 
 **var_from** | **str**| The effective datetime or cut label the statement opens at. | [required] 
 **to** | **str**| The effective datetime or cut label the statement closes at. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the register and the booked events. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**FundPartnerUnfundedReconciliation**](../model/FundPartnerUnfundedReconciliation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s unfunded commitment statement over the period. |  -  |
**400** | The details of the input related failure |  -  |
**404** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_partners**
> PagedResourceListOfFundPartner getPartners = get_partners(scope, code, effective_at=effective_at, as_at=as_at, include_closed=include_closed, page=page, limit=limit)

[EARLY ACCESS] GetPartners: [EARLY ACCESS] GetPartners: Get the partners of a partnership fund.

Lists the register lines of a partnership-accounting fund with each partner's capital balances at the  requested effective date, together with totals across the whole register. Committed capital is totalled per  commitment currency, and each line's share of commitments is of the total in its own currency; amounts in  different currencies are never added together.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
include_closed = True # bool (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.get_partners(scope, code, effective_at=effective_at, as_at=as_at, include_closed=include_closed, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the register. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the register. Defaults to returning the latest version if not specified. | [optional] 
 **include_closed** | **bool**| Whether to include register lines with no remaining commitment or funded capital. Defaults to false. | [optional] 
 **page** | **str**| The pagination token to use to continue listing partners; this value is returned from the previous call.              If a pagination token is provided, the effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 

### Return type

[**PagedResourceListOfFundPartner**](../model/PagedResourceListOfFundPartner.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partners of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_partnership_config_pack**
> PartnershipConfigPack getPartnershipConfigPack = get_partnership_config_pack(scope, code, as_at=as_at)

[EARLY ACCESS] GetPartnershipConfigPack: [EXPERIMENTAL] GetPartnershipConfigPack: Get the partnership configuration pack of a Fund.

Resolve the partnership configuration pack the Fund's configuration names: the partnership transaction types,  the accounts partner capital is posted to and the rules that move each type between them.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_partnership_config_pack(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the pack. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnershipConfigPack**](../model/PartnershipConfigPack.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partnership configuration pack the Fund runs on. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_series**
> ResourceListOfSeries getSeries = get_series(scope, code, share_class_code=share_class_code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetSeries: [EARLY ACCESS] GetSeries: List the Series of a Fund.

Lists the Series defined on the Share Classes of the Fund, optionally restricted to a single Share Class.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
share_class_code = 'share_class_code_example' # str (optional)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_series(scope, code, share_class_code=share_class_code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **share_class_code** | **str**| Optionally, the short code of the Share Class whose Series to list. Defaults to all Share Classes. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Fund. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfSeries**](../model/ResourceListOfSeries.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Series of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_deemed_disposal**
> TaxDeemedDisposalResponse getTaxDeemedDisposal = get_tax_deemed_disposal(scope, code, holding_id, var_date, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxDeemedDisposal: [EARLY ACCESS] GetTaxDeemedDisposal: Get one deemed disposal.

Returns the deemed disposal of a holding on a given date.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
holding_id = 'holding_id_example' # str
var_date = 'var_date_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_deemed_disposal(scope, code, holding_id, var_date, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **holding_id** | **str**| The identifier of the holding to drill into, as returned by the parent reconciliation. | [required] 
 **var_date** | **str**| The date of the deemed disposal. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the deemed disposal. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxDeemedDisposalResponse**](../model/TaxDeemedDisposalResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deemed disposal. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_deemed_disposals**
> TaxDeemedDisposalsResponse getTaxDeemedDisposals = get_tax_deemed_disposals(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxDeemedDisposals: [EARLY ACCESS] GetTaxDeemedDisposals: List the deemed disposals of a Fund or company.

Returns the period-end deemed disposals, the vintages they roll into and the seven-year spreading matrix. A company's disposals are actual and a fund's are notional.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_deemed_disposals(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the deemed disposals. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxDeemedDisposalsResponse**](../model/TaxDeemedDisposalsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deemed disposals for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_fund_reconciliation**
> TaxFundReconciliationResponse getTaxFundReconciliation = get_tax_fund_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxFundReconciliation: [EARLY ACCESS] GetTaxFundReconciliation: Reconcile a company's tax figures to its member funds.

Compares the company's return total to the sum of its member funds' notional figures and explains each difference by scope, pool averaging, matching, indexation, the kink test or an out-of-sync holding. Only available for a company; a fund returns a failure.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_fund_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the reconciliation. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxFundReconciliationResponse**](../model/TaxFundReconciliationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The company-to-funds reconciliation for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_fund_reconciliation_holding**
> TaxFundReconciliationHoldingResponse getTaxFundReconciliationHolding = get_tax_fund_reconciliation_holding(scope, code, holding_id, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxFundReconciliationHolding: [EARLY ACCESS] GetTaxFundReconciliationHolding: Drill into one holding of the company-to-funds reconciliation.

Returns the company figure for a holding beside each member fund's notional figure, with the category and explanation of any difference.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
holding_id = 'holding_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_fund_reconciliation_holding(scope, code, holding_id, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **holding_id** | **str**| The identifier of the holding to drill into, as returned by the parent reconciliation. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the reconciliation. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxFundReconciliationHoldingResponse**](../model/TaxFundReconciliationHoldingResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holding-level reconciliation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_ledger_reconciliation**
> TaxLedgerReconciliationResponse getTaxLedgerReconciliation = get_tax_ledger_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxLedgerReconciliation: [EARLY ACCESS] GetTaxLedgerReconciliation: Reconcile the tax figures of a Fund or company to its ledger.

Compares the ledger's capital gain or loss for the period to the comparable tax figure, explains each difference as an excluded holding, a tax cost adjustment or an out-of-sync holding, and bridges from the ledger figure to the return total.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_ledger_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the reconciliation. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxLedgerReconciliationResponse**](../model/TaxLedgerReconciliationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax-to-ledger reconciliation for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_ledger_reconciliation_holding**
> TaxLedgerReconciliationHoldingResponse getTaxLedgerReconciliationHolding = get_tax_ledger_reconciliation_holding(scope, code, holding_id, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxLedgerReconciliationHolding: [EARLY ACCESS] GetTaxLedgerReconciliationHolding: Drill into one holding of the tax-to-ledger reconciliation.

Returns the ledger and tax figures of a single holding side by side with the category and explanation of any difference.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
holding_id = 'holding_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_ledger_reconciliation_holding(scope, code, holding_id, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **holding_id** | **str**| The identifier of the holding to drill into, as returned by the parent reconciliation. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the reconciliation. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxLedgerReconciliationHoldingResponse**](../model/TaxLedgerReconciliationHoldingResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holding-level reconciliation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_provision**
> TaxProvision getTaxProvision = get_tax_provision(scope, code, diary_entry_code, as_at=as_at, nav_type_code=nav_type_code)

[EARLY ACCESS] GetTaxProvision: [EARLY ACCESS] GetTaxProvision: Get the deferred-tax provision of a Valuation Point.

Returns the deferred-tax provision struck for the specified Valuation Point. Where the provision has been  approved by the asAt it is returned as stored, otherwise a live estimate is returned. Until tax elections  can be configured on the Fund every provision is struck under the default elections: a 20% rate, indexation  allowance applied and losses carried forward.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_code = 'diary_entry_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_tax_provision(scope, code, diary_entry_code, as_at=as_at, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **diary_entry_code** | **str**| The Diary Entry code of the Valuation Point the provision is for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the provision. Defaults to returning the latest version if not specified. | [optional] 
 **nav_type_code** | **str**| When provided, the provision of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**TaxProvision**](../model/TaxProvision.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deferred-tax provision of the Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_return**
> TaxReturnResponse getTaxReturn = get_tax_return(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)

[EARLY ACCESS] GetTaxReturn: [EARLY ACCESS] GetTaxReturn: Get the year-end tax return of a Fund or company.

Returns the chargeable gains on actual disposals (line A), the spread instalments of deemed disposals (line D), the loan relationship net credit or debit (line LR, company level), the holdings outside the regime, the memo rows and the workflow history for the accounting period containing effectiveAt.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.get_tax_return(scope, code, effective_at=effective_at, as_at=as_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the return. Defaults to returning the latest version if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxReturnResponse**](../model/TaxReturnResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax return for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tax_sync_status**
> TaxSyncStatus getTaxSyncStatus = get_tax_sync_status(scope, code, as_at=as_at)

[EARLY ACCESS] GetTaxSyncStatus: [EARLY ACCESS] GetTaxSyncStatus: Get the tax sync position of each portfolio in a Fund.

For each portfolio in the Fund, compares the asAt the tax engine last processed the Fund (its latest valuation  point) with the asAt of the latest transaction booked to the portfolio, and says whether the tax position has  caught up.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_tax_sync_status(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**TaxSyncStatus**](../model/TaxSyncStatus.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax sync position of each portfolio in the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_for_fund**
> ListAggregationResponse getValuationForFund = get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)

[EARLY ACCESS] GetValuationForFund: Perform valuation for a Fund.

Perform valuation on a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
fund_valuation_request = FundValuationRequest()
api_response = api_instance.get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **fund_valuation_request** | [**FundValuationRequest**](../model/FundValuationRequest.md)| The request specifying the dates (or DiaryEntry) on which to calculate a set of valuation metrics. | [optional] 

### Return type

[**ListAggregationResponse**](../model/ListAggregationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_data**
> ValuationPointDataResponse getValuationPointData = get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointData: Get Valuation Point Data for a Fund.

Retrieves the Valuation Point data between given dates or Valuation Point codes.  The endpoint will internally extract all 'Assets' and 'Liabilities' from the Fund's Trial balance to produce a GAV.  Start date will be assumed from the last 'official' ValuationPoint and EndDate will be as provided.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the Valuation Point data. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](../model/ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Valuation Point data for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_journal_entry_lines**
> ValuationPointResourceListOfFundJournalEntryLine getValuationPointJournalEntryLines = get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, bucket_set_code=bucket_set_code)

[EARLY ACCESS] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.

Gets the Journal Entry Lines for the given Valuation Point for a Fund.                The Journal Entry Lines have been generated from transactions, translated via posting rules and used in the valuation point.                Lines are returned grouped by portfolio, ordered by portfolio scope and then code (ordinal), with each portfolio's lines in the order the accounting engine produced them, so the order is stable across pages.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
bucket_set_code = 'bucket_set_code_example' # str (optional)
api_response = api_instance.get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, bucket_set_code=bucket_set_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the Journal Entry Lines. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve Journal Entry Lines. Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Journal Entry Lines from a previous call to GetValuationPointJournalEntryLines. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the Journal Entry Lines. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **bucket_set_code** | **str**| When provided, each line&#39;s bucketMemberships report only this bucket set&#39;s classification of it.               Otherwise, every bucket set covering the NAV Type is reported. | [optional] 

### Return type

[**ValuationPointResourceListOfFundJournalEntryLine**](../model/ValuationPointResourceListOfFundJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Journal Entry Lines for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_pnl_summary**
> ValuationPointResourceListOfPnlJournalEntryLine getValuationPointPnlSummary = get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.

Gets the PnL Summary lines from the Journal Entry Lines produced when calculating the Valuation Point.                Rows are returned ordered by PnL bucket (ordinal), then portfolio scope and code (ordinal), then accounting date, activity date and source id, with the remaining Journal Entry Line fields as tie-breakers, so the order is total and stable across pages.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for generating the PnL summary. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve PnL summary. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing results from a previous call to GetValuationPointPnlSummary. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfPnlJournalEntryLine**](../model/ValuationPointResourceListOfPnlJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested PnL summary for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_quotes**
> ValuationPointResourceListOfAccountedQuote getValuationPointQuotes = get_valuation_point_quotes(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointQuotes: Get the Quotes for the given Fund and Valuation Point.

Gets all quotes within the effective date range of the specified Valuation Point for a Fund,  including any quotes added via a Complex Close (Post-Close Activity).

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_quotes(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the quotes. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve quotes. Defaults to returning the latest version              of each quote if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to GetValuationPointQuotes. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedQuote**](../model/ValuationPointResourceListOfAccountedQuote.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_transactions**
> ValuationPointResourceListOfAccountedTransaction getValuationPointTransactions = get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type, return_excluded_transactions=return_excluded_transactions)

[EARLY ACCESS] GetValuationPointTransactions: Get the Transactions for the given Fund.

Gets the Transactions for the given Valuation Point for a Fund.                Transactions are returned grouped by portfolio, ordered by portfolio scope and then code (ordinal), with each portfolio's transactions in the order the accounting engine produced them, so the order is stable across pages.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
show_cancelled_transactions = True # bool (optional)
membership_type = 'membership_type_example' # str (optional)
return_excluded_transactions = True # bool (optional)
api_response = api_instance.get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type, return_excluded_transactions=return_excluded_transactions)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the transactions. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetValuationPointTransactions. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the transactions. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Default value: Member. Available values: All, Member, Candidate. | [optional] 
 **return_excluded_transactions** | **bool**| Option to specify whether or not to include transactions excluded by the               NavType&#39;s TransactionExclusionFilter, flagged with isExcluded. The reversal of a previously included version of               a transaction that has since been amended to be excluded is returned regardless of this option.               Defaults to False if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedTransaction**](../model/ValuationPointResourceListOfAccountedTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_trial_balance**
> ValuationPointResourceListOfTrialBalance getValuationPointTrialBalance = get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)

[EARLY ACCESS] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.

Gets the Trial Balance for the given Valuation Point for a Fund.                The Trial Balance has been generated from transactions, translated via Posting Rules  and aggregated based on a General Ledger Profile (where specified).                Rows are returned ordered by General Ledger Account Code (ordinal, with rows no posting rule mapped first) and then by Levels, so the order is stable across pages.                Supplying the X-LUSID-SuppressImbalanceValidation header suppresses the imbalance check.  Any caller with access to this endpoint may use it; it is not role-restricted.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
exclude_cleardown_module = False # bool (optional)
api_response = api_instance.get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for generating the Trial Balance. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Trial Balance.               Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.               For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number.               Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Trial Balances.               This token is returned from the previous call.               If a pagination token is provided, the filter, effectiveAt and asAt fields               must not have changed since the original request. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the TrialBalance. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **exclude_cleardown_module** | **bool**| If this is set to true, no Cleardown Module will be applied to the Trial Balance. Defaults to false. | [optional] [default to False]

### Return type

[**ValuationPointResourceListOfTrialBalance**](../model/ValuationPointResourceListOfTrialBalance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Trial Balance for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_unsettled_transactions**
> ValuationPointResourceListOfUnsettledTransaction getValuationPointUnsettledTransactions = get_valuation_point_unsettled_transactions(scope, code, single_valuation_point_query_parameters, as_at=as_at, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, filter=filter)

[EARLY ACCESS] GetValuationPointUnsettledTransactions: Get Unsettled Transactions for the given Fund.

Gets all transactions that remain unsettled as at the specified Valuation Point for a Fund,  looking back from inception. Settlement status is point-in-time: post-cutoff settlement  activity does not alter the result.                Rows are returned ordered by portfolio (scope then code, ordinal), then by trade date, entry time, transaction id (ordinal) and sub-holding keys, so the order is total and stable across pages.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
single_valuation_point_query_parameters = SingleValuationPointQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.get_valuation_point_unsettled_transactions(scope, code, single_valuation_point_query_parameters, as_at=as_at, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **single_valuation_point_query_parameters** | [**SingleValuationPointQueryParameters**](../model/SingleValuationPointQueryParameters.md)| The arguments to use for querying the unsettled transactions. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the report. Defaults to latest. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing from a previous call. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, or &#39;Account&#39;               domain to decorate onto the transactions. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ValuationPointResourceListOfUnsettledTransaction**](../model/ValuationPointResourceListOfUnsettledTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unsettled transactions for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_facilities**
> PagedResourceListOfFacility listFacilities = list_facilities(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFacilities: [EXPERIMENTAL] ListFacilities: List Facilities for a specified Fund.

List all the Facilities matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_facilities(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Facilities. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Facilities. Defaults to returning the latest version of each Facility if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing facilities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the lender, specify \&quot;lender eq &#39;Bank&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFacility**](../model/PagedResourceListOfFacility.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Facilities. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fees**
> PagedResourceListOfFee listFees = list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFees: List Fees for a specified Fund.

List all the Fees matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the treatment, specify \&quot;treatment eq &#39;Monthly&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFee**](../model/PagedResourceListOfFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fees. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fund_calendar**
> PagedResourceListOfFundCalendarEntry listFundCalendar = list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFundCalendar: List Fund Calendar.

List all the Calendar Entries associated with the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntry**](../model/PagedResourceListOfFundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fund_calendar_entries**
> PagedResourceListOfFundCalendarEntries listFundCalendarEntries = list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFundCalendarEntries: List Fund Calendar Entries.

List all the Calendar Entries associated with the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntries**](../model/PagedResourceListOfFundCalendarEntries.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_funds**
> PagedResourceListOfFund listFunds = list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFunds: List Funds.

List all the Funds matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Fund code, specify \&quot;id.Code eq &#39;Fund1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFund**](../model/PagedResourceListOfFund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Funds. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_nav_activity_adjustments**
> ResourceListOfNavActivityAdjustmentResponse listNavActivityAdjustments = list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point

Lists the NAV adjustment activities applied to the specified valuation point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| Fetch all NAV adjustment activities for this valuation point. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Nav activity adjustments. Defaults to returning the latest version of each adjustment if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Nav activity adjustments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**ResourceListOfNavActivityAdjustmentResponse**](../model/ResourceListOfNavActivityAdjustmentResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested NAV activity adjustments for the specific valuation point and Nav type for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_partner_capital_accounts**
> PagedResourceListOfPartnerCapitalAccount listPartnerCapitalAccounts = list_partner_capital_accounts(scope, code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListPartnerCapitalAccounts: [EARLY ACCESS] ListPartnerCapitalAccounts: List the capital account statements of a fund's partners.

The capital account statement of every open partner on the fund's register over a period, paged in  register order.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
period_start = '2013-10-20T19:20:30+01:00' # datetime (optional)
period_end = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.list_partner_capital_accounts(scope, code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **period_start** | **datetime**| The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. | [optional] 
 **period_end** | **datetime**| The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. | [optional] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing statements from a previous call. This value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 

### Return type

[**PagedResourceListOfPartnerCapitalAccount**](../model/PagedResourceListOfPartnerCapitalAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The capital account statements of the fund&#39;s partners over the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_partner_statements**
> ResourceListOfPartnerStatement listPartnerStatements = list_partner_statements(scope, code, investor_record_id)

[EARLY ACCESS] ListPartnerStatements: [EXPERIMENTAL] ListPartnerStatements: List the statements produced for a partner.

List every statement produced for the partner on this Fund, most recent first.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
api_response = api_instance.list_partner_statements(scope, code, investor_record_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **investor_record_id** | **str**| The investor record the statements are for. | [required] 

### Return type

[**ResourceListOfPartnerStatement**](../model/ResourceListOfPartnerStatement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The statements produced for the partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tax_cost_records**
> PagedResourceListOfTaxCostRecord listTaxCostRecords = list_tax_cost_records(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListTaxCostRecords: [EXPERIMENTAL] ListTaxCostRecords: List Tax Cost Records for a specified Fund.

List all the Tax Cost Records matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_tax_cost_records(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Tax Cost Records. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Tax Cost Records. Defaults to returning the latest version of each record if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Tax Cost Records; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the portfolio code, specify \&quot;portfolioCode eq &#39;MyPortfolio&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfTaxCostRecord**](../model/PagedResourceListOfTaxCostRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Tax Cost Records. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tax_exceptions**
> ResourceListOfTaxExceptionItem listTaxExceptions = list_tax_exceptions(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] ListTaxExceptions: [EARLY ACCESS] ListTaxExceptions: List the open tax exceptions of a Fund.

Lists the conditions blocking, or casting doubt on, the Fund's tax computation at the given effective and asAt  datetimes, ordered by tax at stake descending with unknown amounts last. A Fund outside the UK chargeable gains  regime has no exceptions.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_tax_exceptions(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Fund. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfTaxExceptionItem**](../model/ResourceListOfTaxExceptionItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The open tax exceptions of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tax_exceptions_across_funds**
> ResourceListOfFundTaxExceptionItem listTaxExceptionsAcrossFunds = list_tax_exceptions_across_funds(effective_at=effective_at, as_at=as_at, root_cause=root_cause)

[EARLY ACCESS] ListTaxExceptionsAcrossFunds: [EARLY ACCESS] ListTaxExceptionsAcrossFunds: List the open tax exceptions across every Fund.

Lists the conditions blocking, or casting doubt on, the tax computation of every Fund the caller can see, each  row carrying the Fund and, where known, the owning entity. Rows are ordered by tax at stake descending with  unknown amounts last. Funds outside the UK chargeable gains regime contribute no rows.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
root_cause = 'root_cause_example' # str (optional)
api_response = api_instance.list_tax_exceptions_across_funds(effective_at=effective_at, as_at=as_at, root_cause=root_cause)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to read the Funds. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the Funds. Defaults to returning the latest version if not specified. | [optional] 
 **root_cause** | **str**| Optionally, the root cause code to restrict the exceptions to, for example \&quot;PoolOutOfSync\&quot;. Defaults to all root causes. | [optional] 

### Return type

[**ResourceListOfFundTaxExceptionItem**](../model/ResourceListOfFundTaxExceptionItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The open tax exceptions across the Funds the caller can see. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tax_provisions**
> ResourceListOfTaxProvision listTaxProvisions = list_tax_provisions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, nav_type_code=nav_type_code)

[EARLY ACCESS] ListTaxProvisions: [EARLY ACCESS] ListTaxProvisions: List the deferred-tax provisions of a Fund.

Returns the deferred-tax provision of every Valuation Point whose effective date lies in the window, oldest first.  Unapproved Valuation Points are estimated live, so the window may cover at most 100 Valuation Points. Until tax  elections can be configured on the Fund every provision is struck under the default elections: a 20% rate,  indexation allowance applied and losses carried forward.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_effective_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
to_effective_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.list_tax_provisions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **from_effective_at** | **datetime**| The lower bound effective datetime (inclusive) of the Valuation Points to include. Defaults to the start of the Fund if not specified. | [optional] 
 **to_effective_at** | **datetime**| The upper bound effective datetime (inclusive) of the Valuation Points to include. Defaults to the latest Valuation Point if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the provisions. Defaults to returning the latest version if not specified. | [optional] 
 **nav_type_code** | **str**| When provided, the provisions of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ResourceListOfTaxProvision**](../model/ResourceListOfTaxProvision.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deferred-tax provisions of the Fund&#39;s Valuation Points in the window |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_valuation_point_complex_market_data**
> ValuationPointResourceListOfAccountedComplexMarketData listValuationPointComplexMarketData = list_valuation_point_complex_market_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] ListValuationPointComplexMarketData: List the Complex Market Data for the given Fund and Valuation Point.

Lists all complex market data within the effective date range of the specified Valuation Point for a Fund,  including any items added via a Complex Close (Post-Close Activity).

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.list_valuation_point_complex_market_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](../model/ValuationPointDataQueryParameters.md)| The arguments to use for querying the complex market data. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve complex market data. Defaults to returning the latest version              of each item if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing complex market data from a previous call to ListValuationPointComplexMarketData. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedComplexMarketData**](../model/ValuationPointResourceListOfAccountedComplexMarketData.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested complex market data for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_valuation_point_instruments**
> PagedResourceListOfValuationPointInstrument listValuationPointInstruments = list_valuation_point_instruments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, instrument_property_keys=instrument_property_keys, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] ListValuationPointInstruments: List Instruments inside a valuation point

Lists the Instruments linked to Transactions within a Valuation Point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
instrument_property_keys = ['instrument_property_keys_example'] # List[str] (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.list_valuation_point_instruments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, instrument_property_keys=instrument_property_keys, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| Fetch all instruments for this valuation point. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the instruments. Defaults to returning the latest version of each instrument if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instruments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **instrument_property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;Instrument&#39; domain to decorate onto              instruments, or from any domain that supports relationships to decorate onto related entities.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**PagedResourceListOfValuationPointInstrument**](../model/PagedResourceListOfValuationPointInstrument.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments held at the specified valuation point for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_valuation_point_overview**
> PagedResourceListOfValuationPointOverview listValuationPointOverview = list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)

[EARLY ACCESS] ListValuationPointOverview: List Valuation Points Overview for a given Fund.

List the overview of all the Valuation Points that match the given criteria for a given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Valuation Points. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Valuation Points. Defaults to returning the latest version of each Valuation Point if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Valuation Points; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.              For example, to filter on the NAV, specify \&quot;NAV gt 300\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each ValuationPoint.              These must take the format {domain}/{scope}/{code}, for example &#39;DiaryEntry/ValuationPoint/Id&#39;. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**PagedResourceListOfValuationPointOverview**](../model/PagedResourceListOfValuationPointOverview.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The overviews of the requested Valuation Points. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_fee**
> Fee patchFee = patch_fee(scope, code, fee_code, operation)

[EARLY ACCESS] PatchFee: Patch Fee.

Create or update certain fields for a particular Fee.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: EndDate, ShareClasses.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
operation = [{"value":"2027-12-31T00:00:00.0000000+00:00","path":"/endDate","op":"add"}] # List[Operation]
api_response = api_instance.patch_fee(scope, code, fee_code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee. | [required] 
 **operation** | [**List[Operation]**](../model/Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**Fee**](../model/Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_fund**
> Fund patchFund = patch_fund(scope, code, operation, effective_at=effective_at)

[EARLY ACCESS] PatchFund: Patch a Fund.

Update fields on a Fund.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: ShortCode, DisplayName, Description, BaseCurrency, PortfolioIds, FundConfigurationId, ShareClassInstruments, Type, TaxTransparency, InceptionDate, DecimalPlaces, PrimaryNavType, AdditionalNavTypes, ShareClasses, PricingMethodology, ReportingPrices, DealingEstimates, WhtParameters, ValuationTemplateId.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"UpdatedFundName","path":"/displayName","op":"add"},{"path":"/description","op":"remove"},{"value":{"scope":"myFundConfigScope","code":"myFundConfigCode"},"path":"/fundConfigurationId","op":"add"},{"value":{"instrumentIdentifiers":{"Instrument/default/ClientInternal":"shareClass526"},"launchPrice":2.5,"launchDate":"2024-02-01T00:00:00.0000000+00:00"},"path":"/shareClassInstruments/-","op":"add"},{"value":"Standalone","path":"/type","op":"add"},{"value":"2024-01-01","path":"/inceptionDate","op":"add"},{"value":2,"path":"/decimalPlaces","op":"add"}] # List[Operation]
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.patch_fund(scope, code, operation, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **operation** | [**List[Operation]**](../model/Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the patch applies. If not specified, the patch applies for all time.              Only displayName, description, pricingMethodology, reportingPrices and dealingEstimates, or a field inside the first              and last, can be patched with an effectiveAt, and the Fund is returned as at that datetime.              A value patched with an effectiveAt stays in force from that datetime. A later patch of the same field without an effectiveAt              changes it only before that datetime; to change it from that datetime, patch it again with the same effectiveAt.              A field patched with an effectiveAt merges over the block in force at that datetime and does not carry into a version of              the block that starts later: a whole pricingMethodology or dealingEstimates set from a later datetime keeps its own values. | [optional] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **produce_partner_statement**
> PartnerStatement producePartnerStatement = produce_partner_statement(scope, code, investor_record_id, partner_statement_request, as_at=as_at)

[EARLY ACCESS] ProducePartnerStatement: [EXPERIMENTAL] ProducePartnerStatement: Produce a partner's capital statement for a period.

Produce the capital account statement of one partner for the period: opening capital, contributions,  distributions, allocated income, carry and fees, and closing capital. The statement is kept so later  statements for the same period can be compared against it.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
partner_statement_request = PartnerStatementRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.produce_partner_statement(scope, code, investor_record_id, partner_statement_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **investor_record_id** | **str**| The investor record the statement is for. | [required] 
 **partner_statement_request** | [**PartnerStatementRequest**](../model/PartnerStatementRequest.md)| The statement period. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnerStatement**](../model/PartnerStatement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s statement for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_cash_statement**
> ValuationPointResourceListOfFundCashStatementRow queryCashStatement = query_cash_statement(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)

[DEPRECATED] QueryCashStatement: [DEPRECATED] QueryCashStatement: Query cash statement for a Fund valuation point.

Deprecated: use QueryCashStatementLocalCurrency instead. Returns settled cash movements with  running balance, cost basis, average FX rate, and realised FX PnL for the specified Fund  valuation point period. The cash statement is derived from Journal Entry Lines filtered to  settled cash (HoldType='B', SourceType=LusidTransaction). Use the DisplayMode parameter on the  request body to choose between ShowReversal (full reversal/TrueUp detail) and Consolidated  (collapses reversals into AvgRateCorrection rows).

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
query_fund_cash_statement_parameters = QueryFundCashStatementParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.query_cash_statement(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **query_fund_cash_statement_parameters** | [**QueryFundCashStatementParameters**](../model/QueryFundCashStatementParameters.md)| The query parameters specifying the diary entry period and display mode. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to get the next page of results. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys to decorate onto the cash statement rows. | [optional] 
 **nav_type_code** | **str**| The code of the NAV type to use. Defaults to the primary NAV type if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfFundCashStatementRow**](../model/ValuationPointResourceListOfFundCashStatementRow.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cash statement for the specified Fund valuation point. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_cash_statement_local_currency**
> ValuationPointResourceListOfFundCashStatementLocalCurrency queryCashStatementLocalCurrency = query_cash_statement_local_currency(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)

[EARLY ACCESS] QueryCashStatementLocalCurrency: [EXPERIMENTAL] QueryCashStatementLocalCurrency: Query the local-currency cash statement for a Fund valuation point.

Returns settled cash movements with a running balance in local currency for the specified Fund  valuation point period. The cash statement is derived from Journal Entry Lines filtered to  settled cash (HoldType='B', SourceType=LusidTransaction). Use the DisplayMode parameter on the  request body to choose between ShowReversal (full reversal/TrueUp detail) and Consolidated  (collapses each transaction's system-generated reversal/TrueUp rows into a single SystemCorrection  row carrying their net cashflow, while user-entered rows are always shown individually). Base  currency columns are out of scope for this variant and are not returned.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
query_fund_cash_statement_parameters = QueryFundCashStatementParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.query_cash_statement_local_currency(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **query_fund_cash_statement_parameters** | [**QueryFundCashStatementParameters**](../model/QueryFundCashStatementParameters.md)| The query parameters specifying the diary entry period and display mode. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to get the next page of results. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys to decorate onto the cash statement rows. | [optional] 
 **nav_type_code** | **str**| The code of the NAV type to use. Defaults to the primary NAV type if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfFundCashStatementLocalCurrency**](../model/ValuationPointResourceListOfFundCashStatementLocalCurrency.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The local-currency cash statement for the specified Fund valuation point. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **revert_valuation_point_to_estimate**
> RevertValuationPointResponse revertValuationPointToEstimate = revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.

Moves a 'Final' status Valuation Point to status 'Estimate'.  Returns the reverted Valuation Point alongside every variant that  finalising it had rejected.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
revert_valuation_point_data_request = RevertValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **revert_valuation_point_data_request** | [**RevertValuationPointDataRequest**](../model/RevertValuationPointDataRequest.md)| The revertValuationPointRequest which contains the Diary Entry code for the Final Valuation Point to move to Estimate status. | [required] 
 **nav_type_code** | **str**| When provided, sets the status of the Valuation Point of the specified NAV Type to be Estimate.              Otherwise, the Primary NAV Type will be used. | [optional] 

### Return type

[**RevertValuationPointResponse**](../model/RevertValuationPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reverted Estimate Valuation Point, with every variant resurrected by the revert |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_partner_allocations**
> PartnerAllocationRunResult runPartnerAllocations = run_partner_allocations(scope, code, partner_allocation_run_request, as_at=as_at)

[EARLY ACCESS] RunPartnerAllocations: [EXPERIMENTAL] RunPartnerAllocations: Allocate a period's income to the Fund's partners.

Share the Fund's income, gains and expenses for the period across the partners on its register, pool by pool,  and book the allocation unless the run is a dry run.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
partner_allocation_run_request = PartnerAllocationRunRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.run_partner_allocations(scope, code, partner_allocation_run_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **partner_allocation_run_request** | [**PartnerAllocationRunRequest**](../model/PartnerAllocationRunRequest.md)| The period to allocate and how. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnerAllocationRunResult**](../model/PartnerAllocationRunResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The allocation of the period to the partners. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **send_back_tax_return**
> TaxReturnResponse sendBackTaxReturn = send_back_tax_return(scope, code, tax_return_transition_request, effective_at=effective_at, tax_period=tax_period)

[EARLY ACCESS] SendBackTaxReturn: [EARLY ACCESS] SendBackTaxReturn: Send the tax return back one workflow step.

Moves the return one step towards Draft, recording the supplied reason. A Final return cannot be sent back.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
tax_return_transition_request = TaxReturnTransitionRequest()
effective_at = 'effective_at_example' # str (optional)
tax_period = 'tax_period_example' # str (optional)
api_response = api_instance.send_back_tax_return(scope, code, tax_return_transition_request, effective_at=effective_at, tax_period=tax_period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **tax_return_transition_request** | [**TaxReturnTransitionRequest**](../model/TaxReturnTransitionRequest.md)| The reason for sending the return back. | [required] 
 **effective_at** | **str**| The effective datetime or cut label that selects the accounting period. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **tax_period** | **str**| An optional accounting period label that overrides the period selected by effectiveAt. | [optional] 

### Return type

[**TaxReturnResponse**](../model/TaxReturnResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax return after the transition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_share_class_instruments**
> Fund setShareClassInstruments = set_share_class_instruments(scope, code, set_share_class_instruments_request)

[EARLY ACCESS] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.

Update the ShareClass Instruments on an existing Fund with the set of instruments provided.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
set_share_class_instruments_request = SetShareClassInstrumentsRequest()
api_response = api_instance.set_share_class_instruments(scope, code, set_share_class_instruments_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **set_share_class_instruments_request** | [**SetShareClassInstrumentsRequest**](../model/SetShareClassInstrumentsRequest.md)| The scopes and instrument identifiers for the instruments to be set. | [required] 

### Return type

[**Fund**](../model/Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_valuation_point**
> ValuationPoint updateValuationPoint = update_valuation_point(scope, code, update_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpdateValuationPoint: Update a Valuation Point.

Updates an existing Valuation Point. Supplying a pricingMethodologyOverride approves or overrides the swing  decision the Valuation Point deals at, which additionally requires the ApprovePricingMethodology action on the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_valuation_point_request = UpdateValuationPointRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.update_valuation_point(scope, code, update_valuation_point_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **update_valuation_point_request** | [**UpdateValuationPointRequest**](../model/UpdateValuationPointRequest.md)| The Valuation Point Estimate definition to upsert. | [required] 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPoint**](../model/ValuationPoint.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**404** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_bookmark**
> FundCalendarEntry upsertBookmark = upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpsertBookmark: Upsert a bookmark.

This method will update or upsert a Bookmark for the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_fund_bookmark_request = UpsertFundBookmarkRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **upsert_fund_bookmark_request** | [**UpsertFundBookmarkRequest**](../model/UpsertFundBookmarkRequest.md)| The bookmark definition to upsert. | [required] 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**FundCalendarEntry**](../model/FundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted Bookmark |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_diary_entry_type_valuation_point**
> DiaryEntry upsertDiaryEntryTypeValuationPoint = upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.

Insert the estimate Valuation Point.                If the Valuation Point does not exist, this method will create it in estimate state.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_valuation_point_request = UpsertValuationPointRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **upsert_valuation_point_request** | [**UpsertValuationPointRequest**](../model/UpsertValuationPointRequest.md)| The Valuation Point Estimate definition to upsert. | [required] 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DiaryEntry**](../model/DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_external_dealing_estimates**
> UpsertExternalDealingEstimatesResponse upsertExternalDealingEstimates = upsert_external_dealing_estimates(scope, code, request_body)

[EARLY ACCESS] UpsertExternalDealingEstimates: Load dealing estimates sent by an external transfer agent

Loads the dealing estimates a third-party transfer agent dealt for the fund at a dealing point. Each request  key names one set: a dealing point, the sending source and the orders it dealt, each keyed by the source's own  line id. The orders are written in the fund's scope with the code  `{fundCode}-{source}-{yyyyMMddHHmmss}-{lineId}`, the dealing point written in UTC to the second, in the  External order state, priced at the dealing point, so the fund's External dealing source reads them at that  valuation point. A line whose code would exceed 64 characters is refused.                A set replaces what the same source sent before: every External order of that source for the fund's share  classes at the dealing point that the set does not restate is deleted, and the response names them. Two  sets in one request naming the same source and dealing point are refused after the first.                The fund must list External among its dealing estimate sources. Each line must name a share class of the  fund and exactly one of a positive number of units or a positive amount in a valid currency. A set sent  after its dealing point is loaded and flagged late; one sent exactly at the dealing point is on time.  Whether the set is complete is recorded on each order and is not yet enforced at pricing.                Each order carries the properties `Order/TA/PriceDate` (date), `Order/TA/DealingSource` (string),  `Order/TA/DealingSourceReference` (string), `Order/TA/Complete` (string, `True` or `False`),  `Order/TA/Late` (string, `True` or `False`) and `Order/TA/SentAt` (date). LUSID defines these as transfer  agency system properties.                Sets are validated independently: a set that fails validation is reported under failures and the others  still load. The sets that pass are then written together in one command, so a reader never sees half a  dealing point, and a refusal at write time fails the whole request and leaves the book as it was. A request  carries at most 200 sets and at most 2000 lines across all of them.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Set1":{"dealingPoint":"2025-06-02T12:00:00.0000000+00:00","source":{"system":"ExampleTA","reference":"BATCH-20250602-001"},"complete":true,"sentAt":"2025-06-02T11:45:00.0000000+00:00","lines":{"line-1":{"instrumentIdentifierType":"ClientInternal","instrumentIdentifier":"FUND-1-CLASS-A","instrumentScope":"example-scope","tradeType":"Subscription","amount":{"value":100000.0,"currency":"GBP"}},"line-2":{"instrumentIdentifierType":"ClientInternal","instrumentIdentifier":"FUND-1-CLASS-A","instrumentScope":"example-scope","tradeType":"Redemption","units":2500.0}}}} # Dict[str, UpsertExternalDealingEstimatesRequest]
api_response = api_instance.upsert_external_dealing_estimates(scope, code, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the fund. | [required] 
 **code** | **str**| The code of the fund. Together with the scope this uniquely identifies the fund. | [required] 
 **request_body** | [**Dict[str, UpsertExternalDealingEstimatesRequest]**](../model/UpsertExternalDealingEstimatesRequest.md)| The sets to load, keyed by a correlation key of the caller&#39;s choosing. | [required] 

### Return type

[**UpsertExternalDealingEstimatesResponse**](../model/UpsertExternalDealingEstimatesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sets loaded and any that failed, keyed by the request key. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_fee_properties**
> FeeProperties upsertFeeProperties = upsert_fee_properties(scope, code, fee_code, request_body=request_body)

[EARLY ACCESS] UpsertFeeProperties: Upsert Fee properties.

Update or insert one or more properties onto a single Fee. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fee'.                Upserting a property that exists for an Fee, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
request_body = {"Fee/MyScope/FundManagerName":{"key":"Fee/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fee/MyScope/SomeProperty":{"key":"Fee/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/AnotherProperty":{"key":"Fee/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/ReBalanceInterval":{"key":"Fee/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_fee_properties(scope, code, fee_code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to update or insert the properties onto. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](../model/ModelProperty.md)| The properties to be updated or inserted onto the Fee. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fee/Manager/Id\&quot;. | [optional] 

### Return type

[**FeeProperties**](../model/FeeProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_fund_properties**
> FundProperties upsertFundProperties = upsert_fund_properties(scope, code, request_body=request_body)

[EARLY ACCESS] UpsertFundProperties: Upsert Fund properties.

Update or insert one or more properties onto a single Fund. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fund'.                Upserting a property that exists for an Fund, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Fund/MyScope/FundManagerName":{"key":"Fund/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fund/MyScope/SomeProperty":{"key":"Fund/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/AnotherProperty":{"key":"Fund/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/ReBalanceInterval":{"key":"Fund/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_fund_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](../model/ModelProperty.md)| The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fund/Manager/Id\&quot;. | [optional] 

### Return type

[**FundProperties**](../model/FundProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_nav_activity_adjustments**
> datetime upsertNavActivityAdjustments = upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point

Upserts the NAV adjustment activities to the specified valuation point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_activity_adjustment = [{"asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransaction"},{"asAt":"2024-01-01T00:00:00.0000000+00:00","corporateActionSourceScope":"corporateActionSourceScope1","corporateActionSourceCode":"corporateActionSourceCode1","instrumentEventId":"instrumentEventId1","navActivityAdjustmentType":"InstrumentEventActivity"}] # List[NavActivityAdjustment]
nav_type_code = 'nav_type_code_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| The valuation point Code to apply the adjustment to | [required] 
 **nav_activity_adjustment** | [**List[NavActivityAdjustment]**](../model/NavActivityAdjustment.md)| The request describing the Nav activity adjustments to apply to a specific valuation point and nav type | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The date and time of the successfully applied Nav Activity Adjustments. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_tax_cost_records**
> UpsertTaxCostRecordsResponse upsertTaxCostRecords = upsert_tax_cost_records(scope, code, request_body)

[EXPERIMENTAL] UpsertTaxCostRecords: [EXPERIMENTAL] UpsertTaxCostRecords: Upsert Tax Cost Records for a specified Fund.

Create or update Tax Cost Records for the given Fund. Each record is keyed by its code; a record with an  existing code is replaced in full.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"TaxCostRecordCode":{"portfolioScope":"PortfolioScope","portfolioCode":"PortfolioCode","instrumentIdentifier":"LUID_00003D4X","navTypeCode":"DefaultNavType","taxCost":1250.5,"carriedForwardAmount":75.25,"effectivePeriodEnd":"2024-12-31T00:00:00.0000000+00:00","sourceValuationPointId":"VP-2024-12-31"}} # Dict[str, TaxCostRecordRequest]
api_response = api_instance.upsert_tax_cost_records(scope, code, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **request_body** | [**Dict[str, TaxCostRecordRequest]**](../model/TaxCostRecordRequest.md)| The Tax Cost Records to upsert, keyed by the code of each record. | [required] 

### Return type

[**UpsertTaxCostRecordsResponse**](../model/UpsertTaxCostRecordsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Tax Cost Records upserted and any that failed, keyed by the record code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

