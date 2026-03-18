# CreateApplicationRequest

A request to create an application for authenticating the source of token requests
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The Display Name of the application |
| **client_id** | **str** | Required | The OpenID Connect ClientId of the application |
| **type** | **str** | Required | The Type of the application. This must be either Native or Web |
| **redirect_uris** | **List[str]** | Optional | A web application&#39;s acceptable list of post-login redirect URIs |
| **post_logout_redirect_uris** | **List[str]** | Optional | A web application&#39;s acceptable list of post-logout redirect URIs |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateApplicationRequest import CreateApplicationRequest

instance = CreateApplicationRequest(
    display_name="...",  # required — The Display Name of the application
    client_id="...",  # required — The OpenID Connect ClientId of the application
    type="...",  # required — The Type of the application. This must be either Native or Web
    redirect_uris=,  # optional — A web application&#39;s acceptable list of post-login redirect URIs
    post_logout_redirect_uris=  # optional — A web application&#39;s acceptable list of post-logout redirect URIs
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

