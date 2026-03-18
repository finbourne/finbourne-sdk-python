# UploadImageInstructions


## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **docker_login_command** | **str** | Required | *No description available.* |
| **build_versioned_docker_image_command** | **str** | Required | *No description available.* |
| **tag_versioned_docker_image_command** | **str** | Required | *No description available.* |
| **push_versioned_docker_image_command** | **str** | Required | *No description available.* |
| **tag_latest_docker_image_command** | **str** | Optional | *No description available.* |
| **push_latest_docker_image_command** | **str** | Optional | *No description available.* |
| **expiry_time** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.UploadImageInstructions import UploadImageInstructions

instance = UploadImageInstructions(
    docker_login_command="...",  # required
    build_versioned_docker_image_command="...",  # required
    tag_versioned_docker_image_command="...",  # required
    push_versioned_docker_image_command="...",  # required
    tag_latest_docker_image_command="...",  # optional
    push_latest_docker_image_command="...",  # optional
    expiry_time=datetime.now()  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

