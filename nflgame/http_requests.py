import json
import requests

class NflRequest:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    timeout = 30
    url = None

    def __init__(self, **kwargs):
        """ Initialize the request object """
        if isinstance(kwargs.get("headers", None), dict):
            self.headers = kwargs.pop("headers")
        if isinstance(kwargs.get("user_agent", None), str):
            self.headers['User-Agent'] = kwargs.pop("user_agent")
        if type(kwargs.get("timeout", None)) in [int, float]:
            self.timeout = kwargs.pop("timeout")
        if isinstance(kwargs.get("url", None), str):
            self.url = kwargs.pop("url")

    def request(self, **kwargs):
        """ Preform the actual get request and return a normalized object """

        url = self.url
        #override the instance url if one is provided
        if isinstance(kwargs.get("url", None), str):
            url = kwargs.pop("url")
        if url is None:
            raise NflRequestNoUrl
        
        method = 'GET' if not isinstance(kwargs.get("method", None), str) else kwargs.pop("method")
        params = {} if not isinstance(kwargs.get("params", None), dict) else kwargs.pop("params")
        timeout = self.timeout if not type(kwargs.get("timeout", None)) in [int, float] else kwargs.pop("timeout")

        # Currently using the 'requests' library for http calls
        # https://requests.readthedocs.io/en/master/
        try:
            request_get = requests.request(method, url, headers=self.headers, params=params, timeout=timeout)
        except requests.exceptions.Timeout:
            raise NflRequestTimedOut
        except requests.exceptions.ConnectionError:
            raise NflRequestConnectionError
        except requests.exceptions.HTTPError:
            raise NflRequestHTTPError
        except Exception as e:
            raise
    
        return NflResponse(
            status_code=request_get.status_code,
            encoding=request_get.encoding,
            headers=request_get.headers,
            body=request_get.text,
            bytes=request_get.content
        )

    def get(self, **kwargs):
        """ Shortcut for a GET Request """
        kwargs["method"] = 'GET'
        return self.request(**kwargs)
    
    def head(self, **kwargs):
        """ Shortcut for a HEAD Request """
        kwargs["method"] = 'HEAD'
        return self.request(**kwargs)
    

class NflResponse:
    """ Wrapper for the http response data """
    status_code = -1
    encoding = None
    headers = None
    body = None
    bytes = None

    def __init__(self, **kwargs):
        """ Initialize an Response wrapper """
        if kwargs.get("status_code", None) is not None:
            self.status_code = kwargs.pop("status_code")
        if kwargs.get("encoding", None) is not None:
            self.encoding = kwargs.pop("encoding")
        if kwargs.get("headers", None) is not None:
            self.headers = kwargs.pop("headers")
        if kwargs.get("body", None) is not None:
            self.body = kwargs.pop("body")
        if kwargs.get("bytes", None) is not None:
            self.bytes = kwargs.pop("bytes")

    def json(self):
        """ Attempt to convet the repsonse body to json """
        if self.status_code == -1 or self.body is None:
            raise NflResponseUninitialized
        return json.loads(self.body)

    


# ###############
# Exceptions
# Exceptions for the classes above
# ###############

class NflRequestNoUrl(Exception):
    """ Raised if no url is defined for an NflRequest """
    message = "No url was specified for that nfl request"

class NflRequestTimedOut(Exception):
    """ Raised if an http request times out """
    message = "The request timed out"

class NflRequestConnectionError(Exception):
    """ Raised if there is an error with the connection """
    message = "There was an error in the connection for that request"

class NflRequestHTTPError(Exception):
    """ Raised if There is an http error """
    message = "There was an Http error with that request"




class NflResponseUninitialized(Exception):
    """ Raised if no url is defined for an NflRequest """
    message = "The response was never correctly initialized with data"