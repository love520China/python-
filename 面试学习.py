import re

import requests

url = "https://jw1.hustwenhua.net/jwglxt/cjcx/cjcx_cxXsgrcj.html?doType=query&gnmkdm=N305005"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "Cookie":"JSESSIONID=FDAC1D64D75AE4A92B257B55AD5D331A; route=ec9f1523782f6fc8f64960f81492aa8e"

}

my_data = {
    "xnm":2025,
    "xqm":"",
    "sfzgcj":"",
    "kcbj":"",
    "pkey":"",
    "_search":"false",
    "nd":"1775043211161",
    "queryModel.showCount":"15",
    "queryModel.currentPage":1,
    "queryModel.sortName":"",
    "queryModel.sortOrder":"asc",
    "time":0
}

resp = requests.post(url,data=my_data,headers=header)

obj = re.compile(r'"bfzcj".*?"cj":"(?P<fenshu>.*?).*?"jd":"(?P<jd>.*?)".*?"kcmc":"(?P<kemu>.*?)".*?',re.S)
result = obj.finditer(resp.text)
for item in result:
    print("科目"+item.group("kemu"))
    print("分数"+item.group("fenshu"))
    print("绩点"+item.group("jd"))
    print("\n")