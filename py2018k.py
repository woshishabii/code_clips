# by: RainStar
# 简单的实现了2018k.cn平台的一些接口

import requests

check_version_proto = ['update', 'force', 'not_recommend', 'url', 'version']

# 获取更新信息
# 参数: id->实例ID, current_version(可选)->当前版本号
check_version = lambda id, *current_version: dict(zip(check_version_proto, requests.get('http://api.2018k.cn/checkVersion', params={'id': id, "version": current_version}).text.split('|')))

# 获取实例信息
# 参数: id->实例ID, data->要获取哪些数据, 类型:list
get_example = lambda id, data : dict(zip(data, requests.get('http://api.2018k.cn/getExample', params={'id': id, 'data': '|'.join(data)}).text.split('|')))

class WebAuth:
    # 卡密相关
    
    # 获取卡密信息
    # 参数: id->卡密编号
    get_webauth_info = lambda id: requests.get('https://api.2018k.cn/webAuth/getWebAuthInfo', params={'id': id}).json()['data']
    # 根据实例ID查询卡密
    # 参数: private_key->实例ID, mac->机器码
    query_auth_byID = lambda private_key, mac : requests.get('https://api.2018k.cn/webAuth/authQueryById', params={'privateKey': private_key, 'mac': mac}).text == 'true'
    # 绑定卡密
    # 参数: id->卡密, instance_id->实例ID, mac->机器码
    register_auth_code = lambda id, instance_id, mac : requests.get('https://api.2018k.cn/webAuth/authCodeRegister', params={'id': id, 'privateKey': instance_id, 'mac': mac}).text == 'true'
    # 根据MAC查询卡密
    # 参数: id->实例ID, mac->机器码
    query_auth_byMAC = lambda id, mac: requests.get('https://api.2018k.cn/webAuth/getAuthByMacId', params={'id': id, 'mac': mac}).json()['data']
