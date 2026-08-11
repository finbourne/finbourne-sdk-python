# StorageObject

An object representation of a drive file or folder
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | File or folder identifier |
| **path** | **str** | Required | Path of the folder or file |
| **name** | **str** | Required | Name of the folder or file |
| **created_by** | **str** | Required | Identifier of the user who created the file or folder |
| **created_on** | **datetime** | Required | Date of file/folder creation |
| **updated_by** | **str** | Required | Identifier of the last user to modify the file or folder |
| **updated_on** | **datetime** | Required | Date of file/folder modification |
| **type** | **str** | Required | Type of storage object (file or folder) |
| **size** | **int** | Optional | Size of the file in bytes |
| **status** | **str** | Optional | File status corresponding to virus scan status. (Active, Available, Checking, MalwareDetected, Failed) |
| **status_detail** | **str** | Optional | Detailed description describing any negative terminal state of file |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.StorageObject import StorageObject

instance = StorageObject(
    id="...",  # required — File or folder identifier
    path="...",  # required — Path of the folder or file
    name="...",  # required — Name of the folder or file
    created_by="...",  # required — Identifier of the user who created the file or folder
    created_on=datetime.now(),  # required — Date of file/folder creation
    updated_by="...",  # required — Identifier of the last user to modify the file or folder
    updated_on=datetime.now(),  # required — Date of file/folder modification
    type="...",  # required — Type of storage object (file or folder)
    size=0,  # optional — Size of the file in bytes
    status="...",  # optional — File status corresponding to virus scan status. (Active, Available, Checking, MalwareDetected, Failed)
    status_detail="...",  # optional — Detailed description describing any negative terminal state of file
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

