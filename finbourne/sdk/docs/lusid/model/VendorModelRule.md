# VendorModelRule

A rule that identifies the set of preferences to be used for a given library, model and instrument type.  There can be many such rules, though only the first found for a given combination would be used.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **supplier** | **str** | Required | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc |
| **model_name** | **str** | Required | The vendor library model name |
| **instrument_type** | **str** | Required | The vendor library instrument type |
| **parameters** | **str** | Optional | THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood. |
| **model_options** | [ModelOptions](ModelOptions.md) | Optional | *No description available.* |
| **instrument_id** | **str** | Optional | This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general. |
| **address_key_filters** | [List[AddressKeyFilter]](AddressKeyFilter.md) | Optional | Condition for model selection. If a condition is satisfied the default model for valuation is overridden (for that instrument). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VendorModelRule import VendorModelRule

instance = VendorModelRule(
    supplier="...",  # required — The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc
    model_name="...",  # required — The vendor library model name
    instrument_type="...",  # required — The vendor library instrument type
    parameters="...",  # optional — THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.
    model_options=ModelOptions(...),  # optional
    instrument_id="...",  # optional — This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general.
    address_key_filters=[]  # optional — Condition for model selection. If a condition is satisfied the default model for valuation is overridden (for that instrument).
)
```

- [ModelOptions](ModelOptions.md)
- [AddressKeyFilter](AddressKeyFilter.md) — used in `address_key_filters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

