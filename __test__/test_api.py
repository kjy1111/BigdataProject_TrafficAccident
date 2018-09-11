import collect.api as ca
import collect.crawler as cc

# url = ca.trafficaccident_url(
#     'http://apis.data.go.kr/B552061/frequentzoneOldman/getRestFrequentzoneOldman',
#     searchYearCd='2015048',
#     siDo='11',
#     guGun='',
#     _type='json',
#     pageNo=1)
# print(url)

item = ca.trafficaccident_fetch_tad_info('2014', '1100', '')
result = []
b = {}
for a in item:
    b = cc.preprocess_tad(a)
    result.append(b)
print(result)