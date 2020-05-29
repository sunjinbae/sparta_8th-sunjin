import requests # requests 라이브러리 설치 필요

#ajax 
#url, header, body
# get - url, type
# post -url, type, data

# headers = {
#     "Contents-Type" : "application/json"
# }

# data = {
#     "username" : "sunjin"
#     "password" : "123456"
# # }
# requests.get('url',headers={})
# requests.post('url',headers={}, data=data)

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json() # Json 데이터를 자동으로 Python Dictionary로 변환

realtime_city_air = rjson["RealtimeCityAir"]
rows = realtime_city_air["row"] # 리스트

for row in rows:
    gu_name = row["MSRSTE_NM"]
    mise_value = row["IDEX_MVL"]

    print(gu_name, mise_value)

if mise_value < 100:
    print(gu_name)