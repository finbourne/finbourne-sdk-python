# Fee

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **fee_code** | **str** | Optional | The code of the Fee. |
| **fee_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the Fee. |
| **description** | **str** | Optional | A description for the Fee. |
| **origin** | **str** | Optional | The origin or source of the Fee accrual. |
| **calculation_base** | **str** | Optional | The calculation base for a Fee that is calculated using a percentage (TotalAnnualAccrualAmount and CalculationBase cannot both be present). When the Fee is a ShareClass Fee (i.e: when ShareClasses contains at least one value), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;ShareClass.GAV\&quot;, \&quot;ShareClass.GAV - ShareClass.Fees[ShareClassFeeCode1].Amount\&quot;, \&quot;ShareClass.Fees[ShareClassFeeCode1].CalculationBase\&quot;. When the Fee is a NonShareClassSpecific Fee (i.e: when ShareClasses contains no values), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;GAV\&quot;, \&quot;GAV - Fees[NonClassSpecificFeeCode1].Amount\&quot;, \&quot;Fees[NonClassSpecificFeeCode1].CalculationBase\&quot;.  |
| **accrual_currency** | **str** | Required | The accrual currency. |
| **treatment** | **str** | Required | The accrual period of the Fee; &#39;Monthly&#39; or &#39;Daily&#39;. |
| **total_annual_accrual_amount** | **float** | Optional | The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) |
| **fee_rate_percentage** | **float** | Optional | The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount) |
| **payable_frequency** | **str** | Required | The payable frequency for the Fee; &#39;Annually&#39;, &#39;Quarterly&#39; or &#39;Monthly&#39;. |
| **business_day_convention** | **str** | Required | The business day convention to use for Fee calculations on weekends or holidays. Supported string values are: [Previous, P, Following, F, None]. |
| **start_date** | **datetime** | Required | The start date of the Fee. |
| **end_date** | **datetime** | Optional | The end date of the Fee. |
| **anchor_date** | [DayMonth](DayMonth.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Fee properties. These will be from the &#39;Fee&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **share_classes** | **List[str]** | Optional | The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio. |
| **nav_type_code** | **str** | Optional | When provided runs against the specified NAV Type, otherwise the Primary NAV Type will be used. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Fee import Fee

instance = Fee(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    fee_code="...",  # optional — The code of the Fee.
    fee_type_id=ResourceId(...),  # required
    display_name="...",  # required — The name of the Fee.
    description="...",  # optional — A description for the Fee.
    origin="...",  # optional — The origin or source of the Fee accrual.
    calculation_base="...",  # optional — The calculation base for a Fee that is calculated using a percentage (TotalAnnualAccrualAmount and CalculationBase cannot both be present). When the Fee is a ShareClass Fee (i.e: when ShareClasses contains at least one value), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;ShareClass.GAV\&quot;, \&quot;ShareClass.GAV - ShareClass.Fees[ShareClassFeeCode1].Amount\&quot;, \&quot;ShareClass.Fees[ShareClassFeeCode1].CalculationBase\&quot;. When the Fee is a NonShareClassSpecific Fee (i.e: when ShareClasses contains no values), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;GAV\&quot;, \&quot;GAV - Fees[NonClassSpecificFeeCode1].Amount\&quot;, \&quot;Fees[NonClassSpecificFeeCode1].CalculationBase\&quot;. 
    accrual_currency="...",  # required — The accrual currency.
    treatment="...",  # required — The accrual period of the Fee; &#39;Monthly&#39; or &#39;Daily&#39;.
    total_annual_accrual_amount=0.0,  # optional — The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)
    fee_rate_percentage=0.0,  # optional — The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount)
    payable_frequency="...",  # required — The payable frequency for the Fee; &#39;Annually&#39;, &#39;Quarterly&#39; or &#39;Monthly&#39;.
    business_day_convention="...",  # required — The business day convention to use for Fee calculations on weekends or holidays. Supported string values are: [Previous, P, Following, F, None].
    start_date=datetime.now(),  # required — The start date of the Fee.
    end_date=datetime.now(),  # optional — The end date of the Fee.
    anchor_date=DayMonth(...),  # optional
    properties=ModelProperty(...),  # optional — The Fee properties. These will be from the &#39;Fee&#39; domain.
    version=Version(...),  # optional
    portfolio_id=ResourceId(...),  # optional
    share_classes=,  # optional — The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio.
    nav_type_code="...",  # optional — When provided runs against the specified NAV Type, otherwise the Primary NAV Type will be used.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [DayMonth](DayMonth.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

