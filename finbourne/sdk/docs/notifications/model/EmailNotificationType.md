# EmailNotificationType

The information required to create or update an Email notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of delivery mechanism for this notification |
| **subject** | **str** | Required | The subject of the email |
| **plain_text_body** | **str** | Required | The plain text body of the email |
| **html_body** | **str** | Optional | The HTML body of the email (if any) |
| **email_address_to** | **List[str]** | Required | &#39;To&#39; recipients of the email |
| **email_address_cc** | **List[str]** | Optional | &#39;Cc&#39; recipients of the email |
| **email_address_bcc** | **List[str]** | Optional | &#39;Bcc&#39; recipients of the email |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.EmailNotificationType import EmailNotificationType

instance = EmailNotificationType(
    type="...",  # required — The type of delivery mechanism for this notification
    subject="...",  # required — The subject of the email
    plain_text_body="...",  # required — The plain text body of the email
    html_body="...",  # optional — The HTML body of the email (if any)
    email_address_to=,  # required — &#39;To&#39; recipients of the email
    email_address_cc=,  # optional — &#39;Cc&#39; recipients of the email
    email_address_bcc=  # optional — &#39;Bcc&#39; recipients of the email
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

