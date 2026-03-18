# CertificateState

Information held about the minting / revoking of a certificate. It does *not* contain the certificate itself
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Optional | The \&quot;key\&quot; to which this belongs in the dictionary, basically the CN without any version information |
| **version** | **int** | Optional | The version of this certificate |
| **common_name** | **str** | Optional | The common Name of the Certificate |
| **type** | [CertificateType](CertificateType.md) | Optional | *No description available.* |
| **creation_status** | [CertificateStatus](CertificateStatus.md) | Optional | *No description available.* |
| **revocation_status** | [CertificateStatus](CertificateStatus.md) | Optional | *No description available.* |
| **validity_start** | **datetime** | Optional | The earliest point at which a certificate can be used |
| **validity_end** | **datetime** | Optional | The latest point at which a certificate can be used |
| **revoked_at** | **datetime** | Optional | The point at which this was revoked, if any |
| **revoked_by** | **str** | Optional | The user which revoked this, if any |
| **created_at** | **datetime** | Optional | The point at which this was created |
| **permissions_set_at** | **datetime** | Optional | The point at which permissions were adjusted by the system |
| **created_by** | **str** | Optional | The user which created this |
| **serial_number** | **str** | Optional | The Vault-issued serial number of the certificate, if any - used for revocation |
| **links** | [List[Link]](Link.md) | Optional | The location within Configuration Store that this is saved to |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CertificateState import CertificateState

instance = CertificateState(
    key="...",  # optional — The \&quot;key\&quot; to which this belongs in the dictionary, basically the CN without any version information
    version=0,  # optional — The version of this certificate
    common_name="...",  # optional — The common Name of the Certificate
    type=CertificateType(...),  # optional
    creation_status=CertificateStatus(...),  # optional
    revocation_status=CertificateStatus(...),  # optional
    validity_start=datetime.now(),  # optional — The earliest point at which a certificate can be used
    validity_end=datetime.now(),  # optional — The latest point at which a certificate can be used
    revoked_at=datetime.now(),  # optional — The point at which this was revoked, if any
    revoked_by="...",  # optional — The user which revoked this, if any
    created_at=datetime.now(),  # optional — The point at which this was created
    permissions_set_at=datetime.now(),  # optional — The point at which permissions were adjusted by the system
    created_by="...",  # optional — The user which created this
    serial_number="...",  # optional — The Vault-issued serial number of the certificate, if any - used for revocation
    links=[]  # optional — The location within Configuration Store that this is saved to
)
```

- [CertificateType](CertificateType.md)
- [CertificateStatus](CertificateStatus.md)
- [CertificateStatus](CertificateStatus.md)
- [Link](Link.md) — used in `links`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

