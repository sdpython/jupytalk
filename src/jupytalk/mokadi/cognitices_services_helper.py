"""
@file
@brief Call to Cognitive services
"""

import http.client
import urllib.request
import urllib.parse
import urllib.error
import json
from .mokadi_exceptions import CognitiveException


def bytes2python(answer):
    """
    Converts JSON bytes into a dictionary.

    @param      answer      bytes
    @return                 any type
    """
    string = answer.decode('utf-8')
    json_obj = json.loads(string)
    return json_obj


def call_api_news(subscription_key, query, market="fr-FR", count=10, offset=0):
    """
    Retrieve resuls for news

    @param      subscription_key
    @param      query               query
    @param      market              market
    @param      count               number of results
    @param      offset              skip results
    @return                         results
    """
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q': query,
        'count': "{0}".format(count),
        'offset': "{0}".format(offset),
        'mkt': market,
        'safeSearch': 'Moderate',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/news/search?%s" %
                     params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return bytes2python(data)
    except Exception as e:
        raise CognitiveException("[Errno {0}] {1}".format(e.errno, e.strerror))


def call_api_speech_reco(subkey, lang="fr-FR", filename=None, memwav=None,
                         url="https://speech.platform.bing.com/recognize"):
    """
    Implemented in module
    `ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/py-modindex.html>`_.
    Only available on Windows for the time being (relies on C# code).

    @param      subkey      subscription key
    @param      lang        language
    @param      filename    wav file
    @param      memwav      wav memory stream
    @param      url         url of the service
    @return                 dictionary wih the results

    Either filename or memwav must be specified.
    """
    from ensae_teaching_cs.pythonnet import vocal_recognition
    return vocal_recognition(subkey, lang=lang, filename=filename, memwav=memwav, url=url)
