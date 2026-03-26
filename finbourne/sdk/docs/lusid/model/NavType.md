# NavType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | The Status of the Nav Type. Can be &#39;Active&#39; or &#39;Inactive&#39;. |
| **code** | **str** | Optional | The Code for the Nav Type. Must be unique within the Fund. |
| **display_name** | **str** | Optional | The Display Name for the Nav Type. Must be unique within the Fund. |
| **description** | **str** | Optional | The Description for the Nav Type. |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **posting_module_codes** | **List[str]** | Optional | The Posting Module Codes from which the rules to be applied are retrieved. |
| **cleardown_module_codes** | **List[str]** | Optional | The Cleardown Module Codes from which the rules to be applied are retrieved. |
| **valuation_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **holding_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **accounting_method** | **str** | Required | Determines the accounting treatment given to the simple position portfolio&#39;s tax lots. A non-default value is required. |
| **sub_holding_keys** | **List[str]** | Optional | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. |
| **amortisation_method** | **str** | Required | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate |
| **transaction_type_scope** | **str** | Required | The scope of the transaction types. |
| **cash_gain_loss_calculation_date** | **str** | Required | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. A non-default value is required. |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **leader_nav_type_code** | **str** | Optional | The code of the Nav Type that this Nav Type will follow when set. |
| **transaction_template_scope** | **str** | Required | The Transaction Template Scope used by the NavType. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NavType import NavType

instance = NavType(
    status="...",  # required — The Status of the Nav Type. Can be &#39;Active&#39; or &#39;Inactive&#39;.
    code="...",  # optional — The Code for the Nav Type. Must be unique within the Fund.
    display_name="...",  # optional — The Display Name for the Nav Type. Must be unique within the Fund.
    description="...",  # optional — The Description for the Nav Type.
    chart_of_accounts_id=ResourceId(...),  # required
    posting_module_codes=,  # optional — The Posting Module Codes from which the rules to be applied are retrieved.
    cleardown_module_codes=,  # optional — The Cleardown Module Codes from which the rules to be applied are retrieved.
    valuation_recipe_id=ResourceId(...),  # required
    holding_recipe_id=ResourceId(...),  # required
    accounting_method="...",  # required — Determines the accounting treatment given to the simple position portfolio&#39;s tax lots. A non-default value is required.
    sub_holding_keys=,  # optional — A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information.
    amortisation_method="...",  # required — The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
    transaction_type_scope="...",  # required — The scope of the transaction types.
    cash_gain_loss_calculation_date="...",  # required — The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. A non-default value is required.
    amortisation_rule_set_id=ResourceId(...),  # optional
    leader_nav_type_code="...",  # optional — The code of the Nav Type that this Nav Type will follow when set.
    transaction_template_scope="..."  # required — The Transaction Template Scope used by the NavType.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

