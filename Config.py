import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def configure_session():
    session = requests.Session()
    session.keep_alive = False
    retries = Retry(total=10, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    return session
