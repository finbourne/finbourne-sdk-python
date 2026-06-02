from urllib3 import make_headers
from urllib.parse import urlsplit, urlunsplit
from typing import Dict


class ProxyConfig:
    """
    This class is used to hold the proxy configuration details
    """

    def __init__(self, address, username=None, password=None):
        """
        :param str address: The address of the proxy including the port e.g. https://myproxy.com:8080
        :param str username: The username for the proxy
        :param str password: The password for the proxy
        """
        self.address = address
        self.__username = username
        self.__password = password

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if "http://" not in address and "https://" not in address:
            raise ValueError(
                f"The provided proxy address of {address} does not contain a protocol, please specify in the full format e.g. http://myproxy.com:8080"
            )

        self.__address = address

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def _masked_address(self):
        parts = urlsplit(self.__address)
        netloc = parts.netloc
        if "@" in netloc:
            host = netloc.rsplit("@", 1)[1]
            netloc = f"****@{host}"
        return urlunsplit(parts._replace(netloc=netloc))

    def __repr__(self):
        return f"ProxyConfig(address={self._masked_address()!r}, username={self.__username!r}, password='****')"

    def format_proxy_schema(self):
        """
        Takes the proxy details and converts them into a dictionary format to be used with other libraries e.g. requests

        :return: dict: A dictionary with the http and https proxy details including username and password
        """

        proxy_url = self.address

        # Only run if there is a username and password
        if self.username is not None and self.password is not None:
            index = self.address.index("://")

            proxy_url = f"{self.address[0:index + 3]}{self.username}:{self.password}@{self.address[index + 3:]}"

        return {"http": proxy_url, "https": proxy_url}

    @property
    def headers(self) -> Dict[str, str]:
        """Return Proxy auth headers

        Returns
        -------
        Any
            Proxy auth headers
        """
        if self.__username is not None and self.__password is not None:
            return make_headers(
                proxy_basic_auth=f"{self.__username}:{self.__password}"
            )
        else:
            return {}
