# ImageSummary

Represents the metadata of an image
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | Name of the image |
| **push_time** | **datetime** | Optional | The push time of the image |
| **pull_time** | **datetime** | Optional | The latest pull time of the image |
| **digest** | **str** | Optional | The digest of the image |
| **size** | **int** | Optional | The size of the image (in bytes) |
| **tags** | [List[Tag]](Tag.md) | Optional | The tags of the image |
| **scan_status** | **str** | Optional | The Scan Status of the stated image |
| **scan_summary** | [ScanSummary](ScanSummary.md) | Optional | *No description available.* |
| **link** | [Link](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.ImageSummary import ImageSummary

instance = ImageSummary(
    name="...",  # optional — Name of the image
    push_time=datetime.now(),  # optional — The push time of the image
    pull_time=datetime.now(),  # optional — The latest pull time of the image
    digest="...",  # optional — The digest of the image
    size=0,  # optional — The size of the image (in bytes)
    tags=[],  # optional — The tags of the image
    scan_status="...",  # optional — The Scan Status of the stated image
    scan_summary=ScanSummary(...),  # optional
    link=Link(...)  # optional
)
```

- [Tag](Tag.md) — used in `tags`
- [ScanSummary](ScanSummary.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

