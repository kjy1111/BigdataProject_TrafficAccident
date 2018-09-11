from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request

SERVICE_KEY = 'lPho2AedT94HdWcuLEqLx%2FxutLFprTW4diIv6lp%2FylcbEtT0TFuMSfWdSiWip2LcqZ3fRfZ4tTKNyZiU%2BKUfAw%3D%3D'
EndPoint = 'http://apis.data.go.kr/B552061/trafficAccidentDeath/getRestTrafficAccidentDeath'


def trafficaccident_url(endpoint, **params):
    url = '%s?servicekey=%s&%s' % (endpoint, SERVICE_KEY, urlencode(params))
    return url


def trafficaccident_fetch_tad_info(searchYear, siDo, guGun):
    url = trafficaccident_url(EndPoint, searchYear=searchYear, siDo=siDo, guGun=guGun, _type='json')
    json_result = json_request(url=url)

    json_searchResult = json_result.get('searchResult')
    json_accidentDeath = json_searchResult.get('accidentDeath')

    return json_accidentDeath