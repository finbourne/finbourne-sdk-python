# PostCloseActivity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of the entity, possible values are: * &#x60;PortfolioTransaction&#x60;, * &#x60;Instrument&#x60;, * &#x60;InstrumentEvent&#x60;, * &#x60;InstrumentEventInstruction&#x60;, * &#x60;PortfolioSettlementInstruction&#x60;, and, * &#x60;Quote&#x60;. |
| **entity_unique_id** | **str** | Required | The entity unique ID. The expected format for each entity is: | entityType                       | entityUniqueId                                    | |----------------------------------|---------------------------------------------------| | &#x60;PortfolioTransaction&#x60;           | &#x60;portfolioUniqueId_transactionId&#x60;                 | | &#x60;Instrument&#x60;                     | &#x60;instrumentUniqueId&#x60;                              | | &#x60;InstrumentEvent&#x60;                | &#x60;corporateActionSourceUniqueId_instrumentEventId&#x60; | | &#x60;InstrumentEventInstruction&#x60;     | &#x60;portfolioUniqueId_instructionId&#x60;                 | | &#x60;PortfolioSettlementInstruction&#x60; | &#x60;portfolioUniqueId_settlementInstructionId&#x60;       | | &#x60;Quote&#x60;                          | &#x60;quoteSeriesUniqueId_quoteSeriesInstrumentId&#x60;     | |
| **as_at** | **datetime** | Required | The &#x60;AsAt&#x60; time of the event that needs to be added to the closed period. |
| **effective_at** | **str** | Optional | The &#x60;EffectiveAt&#x60; time of the event that need to be added to the closed period. This can be a date or cut label. Only applicable for &#x60;Quote&#x60; post-close activities. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostCloseActivity import PostCloseActivity

instance = PostCloseActivity(
    entity_type="...",  # required — The type of the entity, possible values are: * &#x60;PortfolioTransaction&#x60;, * &#x60;Instrument&#x60;, * &#x60;InstrumentEvent&#x60;, * &#x60;InstrumentEventInstruction&#x60;, * &#x60;PortfolioSettlementInstruction&#x60;, and, * &#x60;Quote&#x60;.
    entity_unique_id="...",  # required — The entity unique ID. The expected format for each entity is: | entityType                       | entityUniqueId                                    | |----------------------------------|---------------------------------------------------| | &#x60;PortfolioTransaction&#x60;           | &#x60;portfolioUniqueId_transactionId&#x60;                 | | &#x60;Instrument&#x60;                     | &#x60;instrumentUniqueId&#x60;                              | | &#x60;InstrumentEvent&#x60;                | &#x60;corporateActionSourceUniqueId_instrumentEventId&#x60; | | &#x60;InstrumentEventInstruction&#x60;     | &#x60;portfolioUniqueId_instructionId&#x60;                 | | &#x60;PortfolioSettlementInstruction&#x60; | &#x60;portfolioUniqueId_settlementInstructionId&#x60;       | | &#x60;Quote&#x60;                          | &#x60;quoteSeriesUniqueId_quoteSeriesInstrumentId&#x60;     |
    as_at=datetime.now(),  # required — The &#x60;AsAt&#x60; time of the event that needs to be added to the closed period.
    effective_at="..."  # optional — The &#x60;EffectiveAt&#x60; time of the event that need to be added to the closed period. This can be a date or cut label. Only applicable for &#x60;Quote&#x60; post-close activities.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

