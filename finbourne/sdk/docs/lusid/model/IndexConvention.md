# IndexConvention

A set of conventions that describe the conventions for calculation of payments made on rates interbank lending and similar.  Based on ISDA 2006 conventions and similar documentation. Please see the knowledge base for further documentation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fixing_reference** | **str** | Required | The reference rate name for fixings. |
| **publication_day_lag** | **int** | Required | Number of days between spot and publication of the rate. |
| **payment_tenor** | **str** | Required | The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) |
| **day_count_convention** | **str** | Required | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365]. |
| **currency** | **str** | Required | Currency of the index convention. |
| **index_name** | **str** | Optional | The name of the index for which this represents the conventions of.  For instance, \&quot;SOFR\&quot;, \&quot;LIBOR\&quot;, \&quot;EURIBOR\&quot;, etc.  Defaults to \&quot;INDEX\&quot; if not specified. |
| **scope** | **str** | Optional | The scope used when updating or inserting the convention. |
| **code** | **str** | Optional | The code of the convention. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IndexConvention import IndexConvention

instance = IndexConvention(
    fixing_reference="...",  # required — The reference rate name for fixings.
    publication_day_lag=0,  # required — Number of days between spot and publication of the rate.
    payment_tenor="...",  # required — The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097)
    day_count_convention="...",  # required — when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365].
    currency="...",  # required — Currency of the index convention.
    index_name="...",  # optional — The name of the index for which this represents the conventions of.  For instance, \&quot;SOFR\&quot;, \&quot;LIBOR\&quot;, \&quot;EURIBOR\&quot;, etc.  Defaults to \&quot;INDEX\&quot; if not specified.
    scope="...",  # optional — The scope used when updating or inserting the convention.
    code="..."  # optional — The code of the convention.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

