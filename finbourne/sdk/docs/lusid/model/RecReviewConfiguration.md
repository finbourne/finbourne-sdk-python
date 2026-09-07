# RecReviewConfiguration

How the results of a rec definition's runs are reviewed and approved: what needs reviewing, when the  reviewer may submit, and who has to approve the submission.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **open_exceptions** | [RecReviewRequirementRule](RecReviewRequirementRule.md) | Optional | *No description available.* |
| **closed_exceptions** | [RecReviewRequirementRule](RecReviewRequirementRule.md) | Optional | *No description available.* |
| **matches** | [RecReviewRequirementRule](RecReviewRequirementRule.md) | Optional | *No description available.* |
| **review_submission** | [RecReviewSubmission](RecReviewSubmission.md) | Optional | *No description available.* |
| **required_approvals** | [List[RecReviewRequiredApproval]](RecReviewRequiredApproval.md) | Optional | The approvals a submitted review has to collect. All are required and may be given in any order, and no user may give more than one of them. Empty means no approvals are required and the reviewer self-approves on submission. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecReviewConfiguration import RecReviewConfiguration

instance = RecReviewConfiguration(
    open_exceptions=RecReviewRequirementRule(...),  # optional
    closed_exceptions=RecReviewRequirementRule(...),  # optional
    matches=RecReviewRequirementRule(...),  # optional
    review_submission=RecReviewSubmission(...),  # optional
    required_approvals=[]  # optional — The approvals a submitted review has to collect. All are required and may be given in any order, and no user may give more than one of them. Empty means no approvals are required and the reviewer self-approves on submission.
)
```


## Related Models

- [RecReviewRequirementRule](RecReviewRequirementRule.md)
- [RecReviewRequirementRule](RecReviewRequirementRule.md)
- [RecReviewRequirementRule](RecReviewRequirementRule.md)
- [RecReviewSubmission](RecReviewSubmission.md)
- [RecReviewRequiredApproval](RecReviewRequiredApproval.md) — used in `required_approvals`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

