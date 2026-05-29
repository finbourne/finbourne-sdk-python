# ReplayTransactionsRequest

Request to replay one or more transactions through a TPF instance. The instance ID is specified in the route path.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_ids** | **List[str]** | Required | List of transaction IDs to replay. |
| **mode** | **str** | Required | Replay mode - DryRun (preview only) or Committed (real send). |
| **destinations** | **List[str]** | Optional | Target destinations for Committed mode. Required for Committed, forbidden for DryRun. Valid values: Drive, Sftp, S3, Local |
| **options** | [ReplayOptions](ReplayOptions.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ReplayTransactionsRequest import ReplayTransactionsRequest

instance = ReplayTransactionsRequest(
    transaction_ids=,  # required — List of transaction IDs to replay.
    mode="...",  # required — Replay mode - DryRun (preview only) or Committed (real send).
    destinations=,  # optional — Target destinations for Committed mode. Required for Committed, forbidden for DryRun. Valid values: Drive, Sftp, S3, Local
    options=ReplayOptions(...)  # optional
)
```

- [ReplayOptions](ReplayOptions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

