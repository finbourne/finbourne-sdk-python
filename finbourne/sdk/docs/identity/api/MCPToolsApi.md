# identity.MCPToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcp_tool**](MCPToolsApi.md#create_mcp_tool) | **POST** /identity/api/mcptools/{scope}/{code} | [EARLY ACCESS] CreateMcpTool: Create an MCP Tool
[**delete_mcp_tool**](MCPToolsApi.md#delete_mcp_tool) | **DELETE** /identity/api/mcptools/{scope}/{code} | [EARLY ACCESS] DeleteMcpTool: Delete an MCP Tool
[**get_mcp_tool**](MCPToolsApi.md#get_mcp_tool) | **GET** /identity/api/mcptools/{scope}/{code} | [EARLY ACCESS] GetMcpTool: Get an MCP Tool
[**list_mcp_tools**](MCPToolsApi.md#list_mcp_tools) | **GET** /identity/api/mcptools | [EARLY ACCESS] ListMcpTools: List all MCP Tools
[**update_mcp_tool**](MCPToolsApi.md#update_mcp_tool) | **PUT** /identity/api/mcptools/{scope}/{code} | [EARLY ACCESS] UpdateMcpTool: Update an MCP Tool


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.mcp_tools_api import MCPToolsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(MCPToolsApi)
```

---

# **create_mcp_tool**
> McpToolResponse createMcpTool = create_mcp_tool(scope, code, upsert_mcp_tool_request)

[EARLY ACCESS] CreateMcpTool: Create an MCP Tool

Creates a new MCP tool definition

### Example

```python
api_instance = api_client_factory.build(MCPToolsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_mcp_tool_request = UpsertMcpToolRequest()
api_response = api_instance.create_mcp_tool(scope, code, upsert_mcp_tool_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | [required] 
 **code** | **str**| The code of the MCP tool | [required] 
 **upsert_mcp_tool_request** | [**UpsertMcpToolRequest**](UpsertMcpToolRequest.md)| The MCP tool definition | [required] 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**409** | A tool with the same code or name already exists in this domain |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_mcp_tool**
> deleteMcpTool = delete_mcp_tool(scope, code)

[EARLY ACCESS] DeleteMcpTool: Delete an MCP Tool

Deletes an MCP tool (soft delete - closes the current version)

### Example

```python
api_instance = api_client_factory.build(MCPToolsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_instance.delete_mcp_tool(scope, code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | [required] 
 **code** | **str**| The code of the MCP tool | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_mcp_tool**
> McpToolResponse getMcpTool = get_mcp_tool(scope, code, version=version)

[EARLY ACCESS] GetMcpTool: Get an MCP Tool

Retrieves an MCP tool. If version is specified, retrieves that specific version for audit purposes. Otherwise, retrieves the current version.

### Example

```python
api_instance = api_client_factory.build(MCPToolsApi)
scope = 'scope_example' # str
code = 'code_example' # str
version = 56 # int (optional)
api_response = api_instance.get_mcp_tool(scope, code, version=version)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | [required] 
 **code** | **str**| The code of the MCP tool | [required] 
 **version** | **int**| Optional version number to retrieve. If not specified, returns the current version. | [optional] 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_mcp_tools**
> List[McpToolResponse] listMcpTools = list_mcp_tools()

[EARLY ACCESS] ListMcpTools: List all MCP Tools

Lists all current MCP tools for the domain

### Example

```python
api_instance = api_client_factory.build(MCPToolsApi)
api_response = api_instance.list_mcp_tools()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[McpToolResponse]**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List MCP Tools |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_mcp_tool**
> McpToolResponse updateMcpTool = update_mcp_tool(scope, code, upsert_mcp_tool_request)

[EARLY ACCESS] UpdateMcpTool: Update an MCP Tool

Updates an existing MCP tool, creating a new version

### Example

```python
api_instance = api_client_factory.build(MCPToolsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_mcp_tool_request = UpsertMcpToolRequest()
api_response = api_instance.update_mcp_tool(scope, code, upsert_mcp_tool_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | [required] 
 **code** | **str**| The code of the MCP tool | [required] 
 **upsert_mcp_tool_request** | [**UpsertMcpToolRequest**](UpsertMcpToolRequest.md)| The updated MCP tool definition | [required] 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**409** | Renaming this tool would conflict with an existing tool name in this domain |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

