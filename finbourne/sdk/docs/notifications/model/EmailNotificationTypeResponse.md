# EmailNotificationTypeResponse

Holds readonly information about an Email notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **subject** | **str** | Optional | The subject of the email |
| **plain_text_body** | **str** | Optional | The plain text body of the email |
| **html_body** | **str** | Optional | The HTML body of the email (if any) |
| **email_address_to** | **List[str]** | Optional | &#39;To&#39; recipients of the email |
| **email_address_cc** | **List[str]** | Optional | &#39;Cc&#39; recipients of the email |
| **email_address_bcc** | **List[str]** | Optional | &#39;Bcc&#39; recipients of the email |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.EmailNotificationTypeResponse import EmailNotificationTypeResponse

instance = EmailNotificationTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    subject="...",  # optional — The subject of the email
    plain_text_body="...",  # optional — The plain text body of the email
    html_body="...",  # optional — The HTML body of the email (if any)
    email_address_to=,  # optional — &#39;To&#39; recipients of the email
    email_address_cc=,  # optional — &#39;Cc&#39; recipients of the email
    email_address_bcc=  # optional — &#39;Bcc&#39; recipients of the email
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

