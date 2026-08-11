# TransactionEntity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Required | The link to the transaction entity. |
| **entity_unique_id** | **str** | Required | The unique id of the transaction, combining the portfolio and transaction identifiers. |
| **as_at_version_number** | **int** | Optional | The version number of the transaction entity at the requested asAt. |
| **status** | **str** | Required | The status of the transaction entity. &#39;Prevailing&#39; when the transaction exists — including a cancelled transaction, whose cancellation is reflected in its own status rather than here; &#39;Deleted&#39; when the transaction&#39;s portfolio has been deleted; &#39;DoesNotExist&#39; when the transaction does not yet exist (e.g. staged creation preview). Available values: Prevailing, Deleted, DoesNotExist. |
| **as_at_deleted** | **datetime** | Optional | The asAt datetime at which the portfolio (and by extension, the transaction) was deleted. |
| **user_id_deleted** | **str** | Optional | The unique id of the user who deleted the portfolio. |
| **request_id_deleted** | **str** | Optional | The unique request id of the command that deleted the portfolio. |
| **prevailing_portfolio** | [PortfolioWithoutHref](PortfolioWithoutHref.md) | Optional | *No description available.* |
| **prevailing_input_transaction** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **deleted_portfolio** | [PortfolioWithoutHref](PortfolioWithoutHref.md) | Optional | *No description available.* |
| **deleted_input_transaction** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **previewed_status** | **str** | Optional | The status of the transaction after the staged modification is applied. Always &#39;Prevailing&#39; for transaction previews. Available values: Prevailing, Deleted, DoesNotExist. |
| **previewed_portfolio** | [PortfolioWithoutHref](PortfolioWithoutHref.md) | Optional | *No description available.* |
| **previewed_input_transaction** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionEntity import TransactionEntity

instance = TransactionEntity(
    href="...",  # required — The link to the transaction entity.
    entity_unique_id="...",  # required — The unique id of the transaction, combining the portfolio and transaction identifiers.
    as_at_version_number=0,  # optional — The version number of the transaction entity at the requested asAt.
    status="...",  # required — The status of the transaction entity. &#39;Prevailing&#39; when the transaction exists — including a cancelled transaction, whose cancellation is reflected in its own status rather than here; &#39;Deleted&#39; when the transaction&#39;s portfolio has been deleted; &#39;DoesNotExist&#39; when the transaction does not yet exist (e.g. staged creation preview). Available values: Prevailing, Deleted, DoesNotExist.
    as_at_deleted=datetime.now(),  # optional — The asAt datetime at which the portfolio (and by extension, the transaction) was deleted.
    user_id_deleted="...",  # optional — The unique id of the user who deleted the portfolio.
    request_id_deleted="...",  # optional — The unique request id of the command that deleted the portfolio.
    prevailing_portfolio=PortfolioWithoutHref(...),  # optional
    prevailing_input_transaction=Transaction(...),  # optional
    deleted_portfolio=PortfolioWithoutHref(...),  # optional
    deleted_input_transaction=Transaction(...),  # optional
    previewed_status="...",  # optional — The status of the transaction after the staged modification is applied. Always &#39;Prevailing&#39; for transaction previews. Available values: Prevailing, Deleted, DoesNotExist.
    previewed_portfolio=PortfolioWithoutHref(...),  # optional
    previewed_input_transaction=Transaction(...),  # optional
    links=[]  # optional
)
```

- [PortfolioWithoutHref](PortfolioWithoutHref.md)
- [Transaction](Transaction.md)
- [PortfolioWithoutHref](PortfolioWithoutHref.md)
- [Transaction](Transaction.md)
- [PortfolioWithoutHref](PortfolioWithoutHref.md)
- [Transaction](Transaction.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

