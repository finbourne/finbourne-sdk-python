# FeeRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Fee. |
| **fee_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the Fee. |
| **description** | **str** | Optional | A description for the Fee. |
| **origin** | **str** | Optional | The origin or source of the Fee accrual. |
| **calculation_base** | **str** | Optional | The calculation base for a Fee that is calculated using a percentage (TotalAnnualAccrualAmount and CalculationBase cannot both be present). When the Fee is a ShareClass Fee (i.e: when ShareClasses contains at least one value), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;ShareClass.GAV\&quot;, \&quot;ShareClass.GAV - ShareClass.Fees[ShareClassFeeCode1].Amount\&quot;, \&quot;ShareClass.Fees[ShareClassFeeCode1].CalculationBase\&quot;. When the Fee is a NonShareClassSpecific Fee (i.e: when ShareClasses contains no values), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;GAV\&quot;, \&quot;GAV - Fees[NonClassSpecificFeeCode1].Amount\&quot;, \&quot;Fees[NonClassSpecificFeeCode1].CalculationBase\&quot;.  |
| **accrual_currency** | **str** | Required | The accrual currency. |
| **treatment** | **str** | Required | The accrual period of the Fee. Available values: Daily, Monthly. |
| **total_annual_accrual_amount** | **float** | Optional | The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) |
| **fee_rate_percentage** | **float** | Optional | The annual rate applied to the CalculationBase for a &#39;FixedPercentage&#39; Fee, expressed as a multiplier rather than a percentage: 0.052 means 5.2% of the base per year. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount) |
| **payable_frequency** | **str** | Required | The payable frequency for the Fee. Available values: Annually, Quarterly, Monthly. |
| **business_day_convention** | **str** | Required | The business day convention to use for Fee calculations on weekends or holidays. Available values: None, P, Previous, F, Following. |
| **start_date** | **datetime** | Required | The start date of the Fee. |
| **end_date** | **datetime** | Optional | The end date of the Fee. |
| **anchor_date** | [DayMonth](DayMonth.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Fee properties. These will be from the &#39;Fee&#39; domain. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **share_classes** | **List[str]** | Optional | The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio. |
| **fee_calculation_type** | **str** | Optional | How the Fee accrual amount is calculated. Supported values: &#39;FixedAnnual&#39; (a fixed annual amount, requires TotalAnnualAccrualAmount), &#39;FixedDaily&#39; (a fixed daily amount, requires DailyAccrualAmount), &#39;FixedPercentage&#39; (a fixed percentage of the CalculationBase, requires FeeRatePercentage), &#39;VariablePercentage&#39; (a percentage of the CalculationBase resolved from a rate source at each accrual date, requires VariablePercentageSource), &#39;Tiered&#39; (a single rate applied to the whole CalculationBase, chosen by the tier the base falls in, requires Tiers), &#39;Blended&#39; (each tier&#39;s rate applied to the portion of the CalculationBase within that tier, requires Tiers). Optional: when not provided it is inferred as &#39;FixedAnnual&#39; if TotalAnnualAccrualAmount is populated and &#39;FixedPercentage&#39; otherwise, so existing requests keep their behaviour; the new calculation types must be requested explicitly. Available values: FixedAnnual, FixedDaily, FixedPercentage, VariablePercentage, Tiered, Blended. |
| **daily_accrual_amount** | **float** | Optional | The fixed daily accrued amount for a &#39;FixedDaily&#39; Fee, in the fund currency. The amount accrues for each day of the accrual period with no annualisation or day-count proration; Treatment does not affect it. |
| **variable_percentage_source** | **str** | Optional | The source of the rate for a &#39;VariablePercentage&#39; Fee, in the form \&quot;scope/provider/instrumentIdType/instrumentId\&quot; identifying a Rate quote series in the quote store. At each accrual date the most recent rate at or before that date is used; if no rate can be found the valuation point calculation fails. The quote&#39;s normalised value (its value divided by any scale factor) is applied like FeeRatePercentage, as a multiplier of the CalculationBase: a rate of 5.2% must normalise to 0.052. |
| **variable_percentage_source_offset** | **float** | Optional | An optional adjustment added to the rate resolved from the VariablePercentageSource, expressed as a factor like FeeRatePercentage (e.g. 0.0025 adds 25 basis points). |
| **tiers** | [List[FeeRateTier]](FeeRateTier.md) | Optional | The rate tiers for a &#39;Tiered&#39; or &#39;Blended&#39; Fee: between 2 and 10 tiers over the CalculationBase. Every tier except the last must have a Threshold, and thresholds must be positive and strictly increasing; a base equal to a Threshold falls in that tier, and the final tier covers the balance above the last threshold. A &#39;Tiered&#39; Fee applies the rate of the tier the whole base falls in; a &#39;Blended&#39; Fee applies each tier&#39;s rate to the portion of the base within that tier. |
| **fee_cap** | **float** | Optional | An optional annual cap on the accrued fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency and assessed period-to-date. Each day accrues only up to the amount left under the cap for the current fee year, which runs from one AnchorDate to the next; once the cap is reached nothing further accrues until the next AnchorDate. |
| **fee_floor** | **float** | Optional | An optional annual floor on the calculated fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency. The annualised fee amount is raised to the floor before being prorated to each accrual day. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeRequest import FeeRequest

instance = FeeRequest(
    code="...",  # required — The code of the Fee.
    fee_type_id=ResourceId(...),  # required
    display_name="...",  # required — The name of the Fee.
    description="...",  # optional — A description for the Fee.
    origin="...",  # optional — The origin or source of the Fee accrual.
    calculation_base="...",  # optional — The calculation base for a Fee that is calculated using a percentage (TotalAnnualAccrualAmount and CalculationBase cannot both be present). When the Fee is a ShareClass Fee (i.e: when ShareClasses contains at least one value), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;ShareClass.GAV\&quot;, \&quot;ShareClass.GAV - ShareClass.Fees[ShareClassFeeCode1].Amount\&quot;, \&quot;ShareClass.Fees[ShareClassFeeCode1].CalculationBase\&quot;. When the Fee is a NonShareClassSpecific Fee (i.e: when ShareClasses contains no values), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;GAV\&quot;, \&quot;GAV - Fees[NonClassSpecificFeeCode1].Amount\&quot;, \&quot;Fees[NonClassSpecificFeeCode1].CalculationBase\&quot;. 
    accrual_currency="...",  # required — The accrual currency.
    treatment="...",  # required — The accrual period of the Fee. Available values: Daily, Monthly.
    total_annual_accrual_amount=0.0,  # optional — The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)
    fee_rate_percentage=0.0,  # optional — The annual rate applied to the CalculationBase for a &#39;FixedPercentage&#39; Fee, expressed as a multiplier rather than a percentage: 0.052 means 5.2% of the base per year. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount)
    payable_frequency="...",  # required — The payable frequency for the Fee. Available values: Annually, Quarterly, Monthly.
    business_day_convention="...",  # required — The business day convention to use for Fee calculations on weekends or holidays. Available values: None, P, Previous, F, Following.
    start_date=datetime.now(),  # required — The start date of the Fee.
    end_date=datetime.now(),  # optional — The end date of the Fee.
    anchor_date=DayMonth(...),  # optional
    properties=ModelProperty(...),  # optional — The Fee properties. These will be from the &#39;Fee&#39; domain.
    portfolio_id=ResourceId(...),  # optional
    share_classes=,  # optional — The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio.
    fee_calculation_type="...",  # optional — How the Fee accrual amount is calculated. Supported values: &#39;FixedAnnual&#39; (a fixed annual amount, requires TotalAnnualAccrualAmount), &#39;FixedDaily&#39; (a fixed daily amount, requires DailyAccrualAmount), &#39;FixedPercentage&#39; (a fixed percentage of the CalculationBase, requires FeeRatePercentage), &#39;VariablePercentage&#39; (a percentage of the CalculationBase resolved from a rate source at each accrual date, requires VariablePercentageSource), &#39;Tiered&#39; (a single rate applied to the whole CalculationBase, chosen by the tier the base falls in, requires Tiers), &#39;Blended&#39; (each tier&#39;s rate applied to the portion of the CalculationBase within that tier, requires Tiers). Optional: when not provided it is inferred as &#39;FixedAnnual&#39; if TotalAnnualAccrualAmount is populated and &#39;FixedPercentage&#39; otherwise, so existing requests keep their behaviour; the new calculation types must be requested explicitly. Available values: FixedAnnual, FixedDaily, FixedPercentage, VariablePercentage, Tiered, Blended.
    daily_accrual_amount=0.0,  # optional — The fixed daily accrued amount for a &#39;FixedDaily&#39; Fee, in the fund currency. The amount accrues for each day of the accrual period with no annualisation or day-count proration; Treatment does not affect it.
    variable_percentage_source="...",  # optional — The source of the rate for a &#39;VariablePercentage&#39; Fee, in the form \&quot;scope/provider/instrumentIdType/instrumentId\&quot; identifying a Rate quote series in the quote store. At each accrual date the most recent rate at or before that date is used; if no rate can be found the valuation point calculation fails. The quote&#39;s normalised value (its value divided by any scale factor) is applied like FeeRatePercentage, as a multiplier of the CalculationBase: a rate of 5.2% must normalise to 0.052.
    variable_percentage_source_offset=0.0,  # optional — An optional adjustment added to the rate resolved from the VariablePercentageSource, expressed as a factor like FeeRatePercentage (e.g. 0.0025 adds 25 basis points).
    tiers=[],  # optional — The rate tiers for a &#39;Tiered&#39; or &#39;Blended&#39; Fee: between 2 and 10 tiers over the CalculationBase. Every tier except the last must have a Threshold, and thresholds must be positive and strictly increasing; a base equal to a Threshold falls in that tier, and the final tier covers the balance above the last threshold. A &#39;Tiered&#39; Fee applies the rate of the tier the whole base falls in; a &#39;Blended&#39; Fee applies each tier&#39;s rate to the portion of the base within that tier.
    fee_cap=0.0,  # optional — An optional annual cap on the accrued fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency and assessed period-to-date. Each day accrues only up to the amount left under the cap for the current fee year, which runs from one AnchorDate to the next; once the cap is reached nothing further accrues until the next AnchorDate.
    fee_floor=0.0  # optional — An optional annual floor on the calculated fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency. The annualised fee amount is raised to the floor before being prorated to each accrual day.
)
```

- [ResourceId](ResourceId.md)
- [DayMonth](DayMonth.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [FeeRateTier](FeeRateTier.md) — used in `tiers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

