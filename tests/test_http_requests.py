import unittest
import json
from nflgame.http_requests import *

class NflRequestTest(unittest.TestCase):
    """ 
        Basic test orchestrator for nflgame.http_requests.NflRequest cases 
        This class includes 'Nfl' in the name but realistically its just a request wrapper
        As such, the tests are gamcenter-agnostic but uture test urls *could* be official nfl urls
    """

    #Basic URL For testing
    URL_BASIC = "https://gist.githubusercontent.com/xabrickx/7a3085ecdcf6f6467128436463e59fd9/raw/c5261e779f38cb3ae73f29c2ca258a932ec71120/2019122300.json"
    # Official nfl.com url for testing
    URL_NFL = "http://www.nfl.com/player/joethomas/2507162/profile"
    TIMEOUT_BASIC = 7 
    TIMEOUT_BARE = 7777

    def test_bare_init(self):
        """ Test creation of the base class and that it contains defaults needed for bare functionality"""
        request_test = NflRequest()
        self.assertEqual(request_test.url, None)
        self.assertTrue(hasattr(request_test, "timeout"))

    def test_bare_request(self):
        """ Test the base classes ability initalize with a full set of kwargs """
        HEAD_HOST = "nflrequest.test.test"
        HEADERS = {
            "User-Agent": "If this user agent appears, The Override in 'HEAD_UA' did not work",
            "Host" : HEAD_HOST
        }        
        HEAD_UA = "This user agent is 'The Override'.  For this test it should appear in place of any default"
        URL = "https://nflrequest.test.test"

        request_test = NflRequest(
            headers=HEADERS,
            user_agent=HEAD_UA,
            timeout=self.TIMEOUT_BARE,
            url=URL
        )

        self.assertEqual(request_test.url, URL)
        self.assertEqual(request_test.timeout, self.TIMEOUT_BARE)
        self.assertEqual(request_test.headers["Host"], HEAD_HOST)
        self.assertEqual(request_test.headers["User-Agent"], HEAD_UA)

    def test_basic_request(self):
        """ 
            Test a simple http request
            The content does not matter, we just want to know that we can make a simple GET
        """
        request_test = NflRequest(
            method="GET",
            timeout=self.TIMEOUT_BASIC,
            url=self.URL_BASIC
        )
        self.assertEqual(request_test.url, self.URL_BASIC) # Test duplication?
        
        expected_response = request_test.request()
        self.assertTrue(hasattr(expected_response, "status_code"))
        self.assertEqual(expected_response.status_code, 200)
    
    def test_request_vanity_get(self):
        """ 
            Test the vanity 'GET' request  which should force the get method
        """
        request_test = NflRequest(
            timeout=self.TIMEOUT_BASIC,
            url=self.URL_BASIC
        )
        expected_response = request_test.get()
        self.assertTrue(hasattr(expected_response, "status_code"))
        self.assertEqual(expected_response.status_code, 200)
    
    def test_request_vanity_head(self):
        """ 
            Test the vanity 'HEAD' request  which should force the HEAD method
        """
        request_test = NflRequest(
            timeout=self.TIMEOUT_BASIC,
            url=self.URL_BASIC
        )
        expected_response = request_test.head()
        self.assertTrue(hasattr(expected_response, "status_code"))
        self.assertEqual(expected_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
