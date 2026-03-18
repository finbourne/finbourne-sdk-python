import json
import os
from typing import Dict, TextIO, Protocol, Union, Iterable, Optional, Tuple, Any
import logging
from finbourne.sdk.extensions.proxy_config import ProxyConfig
from finbourne.sdk.configuration import Configuration  # Changed import
from finbourne.sdk.extensions.file_access_token import FileAccessToken
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.extensions.socket_keep_alive import keep_alive_socket_options
from finbourne.sdk.extensions.api_configuration import ApiConfiguration


logger = logging.getLogger(__name__)

ENVIRONMENT_CONFIG_KEYS = {
    "token_url": "FBN_TOKEN_URL",
    "api_url": "FBN_BASE_URL",
    "username": "FBN_USERNAME",
    "password": "FBN_PASSWORD",
    "client_id": "FBN_CLIENT_ID",
    "client_secret": "FBN_CLIENT_SECRET",
    "app_name": "FBN_APP_NAME",
    "certificate_filename": "FBN_CLIENT_CERTIFICATE",
    "fbn_profile":"FBN_PROFILE",
    "proxy_address": "FBN_PROXY_ADDRESS",
    "proxy_username": "FBN_PROXY_USERNAME",
    "proxy_password": "FBN_PROXY_PASSWORD",
    "access_token": "FBN_ACCESS_TOKEN",
    "total_timeout_ms": "FBN_TOTAL_TIMEOUT_MS",
    "connect_timeout_ms": "FBN_CONNECT_TIMEOUT_MS",
    "read_timeout_ms": "FBN_READ_TIMEOUT_MS",
    "rate_limit_retries": "FBN_RATE_LIMIT_RETRIES"
}

SECRETS_FILE_CONFIG_KEYS = {
    "token_url": "tokenUrl",
    "api_url": "baseUrl",
    "username": "username",
    "password": "password",
    "client_id": "clientId",
    "client_secret": "clientSecret",
    "app_name": "applicationName",
    "certificate_filename": "clientCertificate",
    "proxy_address": "address",
    "proxy_username": "username",
    "proxy_password": "password",
    "access_token": "accessToken",
    "total_timeout_ms": "totalTimeoutMs",
    "connect_timeout_ms": "connectTimeoutMs",
    "read_timeout_ms": "readTimeoutMs",
    "rate_limit_retries": "rateLimitRetries",
    "profile_name":"profileName"
}


class ConfigurationLoader(Protocol):
    def load_config(self) -> Dict[str, object]:
        pass


class SecretsFileConfigurationLoader:
    def __init__(
        self,
        api_secrets_file: Union[TextIO, str],
        profile_name: str
    ):
        self._api_secrets_file = api_secrets_file or ""
        self._profile_name = profile_name

    def load_config(self) -> Dict[str, object]:
        logger.debug(f"loading config from secrets file: {self._api_secrets_file}")
        profiles_config_key = "profiles"
        default_profile = self._profile_name
        proxy_config_key = "proxy"
        try:
            try:
                config = json.load(self._api_secrets_file)
            except AttributeError:
                with open(self._api_secrets_file) as api_secrets_file:
                    config = json.load(api_secrets_file)
        except OSError:
            logger.warning(f"Unable to open secrets file {self._api_secrets_file}")
            return {}
        except json.JSONDecodeError:
            logger.warning("unable to deserialise contents of secrets file to json")
            return {}

        profiles_config_section = config.get(profiles_config_key, {})
        profile_section = profiles_config_section.get(default_profile, {})
        populated_api_config_values = {
            key: profile_section.get(value)
            for key, value in SECRETS_FILE_CONFIG_KEYS.items()
            if "proxy" not in key
        }
        proxy_config_section = profiles_config_section.get(proxy_config_key, {})
        populated_proxy_values = {
            key: proxy_config_section.get(value)
            for key, value in SECRETS_FILE_CONFIG_KEYS.items()
            if "proxy" in key
        }
        populated_config_dict = {
            **populated_api_config_values,
            **populated_proxy_values,
        }
        filtered_config = {k: v for k, v in populated_config_dict.items() if v is not None}
        return filtered_config


class EnvironmentVariablesConfigurationLoader:
    def __init__(self, environment_variables: Optional[Dict[str, str]] = None):
        """
        Initialize the EnvironmentVariablesConfigurationLoader.

        Parameters
        ----------
        environment_variables : Optional[Dict[str, str]]
            Optional dictionary of environment variables to use for configuration.
            If not provided, will use os.environ by default.
        """
        self._environment_variables = environment_variables

    def load_config(self) -> Dict[str, object]:
        logger.debug("loading config from environment variables")
        environment_variables = os.environ if self._environment_variables is None else self._environment_variables
        populated_api_config_values = {
            key: environment_variables.get(value)
            for key, value in ENVIRONMENT_CONFIG_KEYS.items()
            if "proxy" not in key
        }
        if not populated_api_config_values["api_url"]:
            raise ValueError("api_url must be set in environment variables")
        for key in ["total_timeout_ms", "connect_timeout_ms", "read_timeout_ms", "rate_limit_retries"]:
            if populated_api_config_values[key]:
                try:
                    populated_api_config_values[key] = int(populated_api_config_values[key])
                except ValueError as e:
                    raise ValueError(f"invalid value for '{key}' - value must be an integer if set")
        populated_proxy_values = {
            key: os.environ.get(value)
            for key, value in ENVIRONMENT_CONFIG_KEYS.items()
            if "proxy" in key
        }
        populated_config_dict = {
            **populated_api_config_values,
            **populated_proxy_values,
        }
        filtered_config = {k: v for k, v in populated_config_dict.items() if v is not None}
        return filtered_config


class ArgsConfigurationLoader:
    def __init__(self,
        token_url:Optional[str]=None,
        api_url:Optional[str]=None,
        username:Optional[str]=None,
        password:Optional[str]=None,
        client_id:Optional[str]=None,
        client_secret:Optional[str]=None,
        app_name:Optional[str]=None,
        certificate_filename:Optional[str]=None,
        proxy_address:Optional[str]=None,
        proxy_username:Optional[str]=None,
        proxy_password:Optional[str]=None,
        access_token:Optional[str]=None,
        total_timeout_ms:Optional[int]=None,
        connect_timeout_ms:Optional[int]=None,
        read_timeout_ms:Optional[int]=None,
        rate_limit_retries:Optional[int]=None,
        ):
        self.__token_url = token_url
        self.__api_url = api_url
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__app_name = app_name
        self.__certificate_filename = certificate_filename
        self.__proxy_address = proxy_address
        self.__proxy_username = proxy_username
        self.__proxy_password = proxy_password
        self.__access_token = access_token
        self.__total_timeout_ms = total_timeout_ms
        self.__connect_timeout_ms = connect_timeout_ms
        self.__read_timeout_ms = read_timeout_ms
        self.__rate_limit_retries = rate_limit_retries

    def load_config(self) -> Dict[str, object]:
        logger.debug("loading config from arguments passed to ArgsConfigurationLoader")
        return {
            "token_url" : self.__token_url, 
            "api_url" : self.__api_url, 
            "username" : self.__username, 
            "password" : self.__password, 
            "client_id" : self.__client_id, 
            "client_secret" : self.__client_secret, 
            "app_name" : self.__app_name, 
            "certificate_filename" : self.__certificate_filename, 
            "proxy_address" : self.__proxy_address, 
            "proxy_username" : self.__proxy_username, 
            "proxy_password" : self.__proxy_password, 
            "access_token" : self.__access_token,
            "total_timeout_ms" : self.__total_timeout_ms,
            "connect_timeout_ms" : self.__connect_timeout_ms,
            "read_timeout_ms" : self.__read_timeout_ms,
            "rate_limit_retries" : self.__rate_limit_retries,
        }


class FileTokenConfigurationLoader:
    def __init__(
        self, access_token_location: str = os.getenv("FBN_ACCESS_TOKEN_FILE", "")
    ):
        self.access_token = None
        if access_token_location is not None and access_token_location != "":
            self.access_token = FileAccessToken(access_token_location)

    def load_config(self) -> Dict[str, Union[FileAccessToken, None]]:
        return {"access_token": self.access_token}

def get_api_configuration(
    secrets_path: Optional[str] = None, 
    profile_name: str = "default", 
    environment_variables: Optional[Dict[str, str]] = None,
    socket_options: Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]] = keep_alive_socket_options(),
    tcp_keep_alive: bool = True,
) -> Configuration:
    """
    Read configuration from config loaders.
    Update config with values from each loader in order (last write wins).
    Initially looks at relative path 'secrets.json' for secrets file,
    but can be overridden by passing a secrets_path argument. Then checks environment variables for configuration.
    Lastly checks for FileTokenConfigurationLoader. Will throw an exception if all of these fail.

    Parameters
    ----------
    secrets_path: Optional[str]
        Optional path to a secrets file to load configuration from. Defaults to 'secrets.json'.
    profile_name: str
        The name of the profile to use when loading configuration from the secrets file. 
        Defaults to 'default', but can be overridden by FBN_PROFILE environment variable.
    environment_variables: Optional[Dict[str,str]]
        Optional dictionary of environment variables to use for configuration. 
        If not provided, will use os.environ by default.

    Returns
    -------
    Configuration
        Configuration that can be passed to an ApiClient, RefreshingToken, etc.
        
    Raises
    ------
    ValueError
        If no configuration is found from any loader or if api_url is not set.
    """
    # Set defaults
    secrets_path = secrets_path or "secrets.json"
    profile_name = os.getenv("FBN_PROFILE", profile_name)
    
    # Try loading configuration from each source in order
    loaders = [
        SecretsFileConfigurationLoader(api_secrets_file=secrets_path, profile_name=profile_name),
        EnvironmentVariablesConfigurationLoader(environment_variables=environment_variables),
        FileTokenConfigurationLoader()
    ]
    
    loaded_config = None
    for loader in loaders:
        try:
            loaded_config = loader.load_config()
            if loaded_config and len(loaded_config) > 0:
                break
        except Exception:
            # Continue to next loader if this one fails
            continue
    
    if not loaded_config:
        raise ValueError(
            "No configuration found. Please provide a secrets file, environment variables, or a file token."
        )
    
    # Start with loaded config
    config = loaded_config.copy()
    
    # Handle proxy configuration
    proxy_address = config.pop("proxy_address", None)
    if proxy_address is not None:
        proxy_username = config.pop("proxy_username", None)
        proxy_password = config.pop("proxy_password", None)
        config["proxy_config"] = ProxyConfig(
            address=proxy_address, 
            username=proxy_username, 
            password=proxy_password
        )
    else:
        config["proxy_config"] = None
    
    # Validate required configuration
    api_url = config.get("api_url")
    if not api_url:
        raise ValueError("api_url must be set in configuration")
    
    api_config = ApiConfiguration(**config)
    return api_config.build_api_client_config(
        tcp_keep_alive=tcp_keep_alive,
        socket_options=socket_options
    )
