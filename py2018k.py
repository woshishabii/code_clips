# by: RainStar
# 简单的实现了2018k.cn平台的一些接口

import requests

check_version_proto = ['update', 'force', 'not_recommend', 'url', 'version']

check_version = lambda id, *current_version: dict(zip(check_version_proto, requests.get('http://api.2018k.cn/checkVersion', params={'id': id, "version": current_version}).text.split('|')))

get_example = lambda id, data : dict(zip(data, requests.get('http://api.2018k.cn/getExample', params={'id': id, 'data': '|'.join(data)}).text.split('|')))

class WebAuth:
    get_webauth_info = lambda id: requests.get('https://api.2018k.cn/webAuth/getWebAuthInfo', params={'id': id}).json()['data']
    query_auth_byID = lambda private_key, mac : requests.get('https://api.2018k.cn/webAuth/authQueryById', params={'privateKey': private_key, 'mac': mac}).text == 'true'
    register_auth_code = lambda id, instance_id, mac : requests.get('https://api.2018k.cn/webAuth/authCodeRegister', params={'id': id, 'privateKey': instance_id, 'mac': mac}).text == 'true'
    query_auth_byMAC = lambda id, mac: requests.get('https://api.2018k.cn/webAuth/getAuthByMacId', params={'id': id, 'mac': mac}).json()['data']
