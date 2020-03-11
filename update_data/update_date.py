import json
import requests
import datetime
import time
import copy


def get_information(pname):
    
    url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province='+pname
    while 1:
        try:
            res = requests.get(url)
            t = json.loads(res.text)
      
            if isinstance(t,dict) and t["success"] == True:
                return t
            else: continue
        except:
            continue


if __name__ == "__main__":
    with open('by_date.json','r',encoding='utf8') as load_f:
        tmp = json.load(load_f)
        
    template = copy.deepcopy(tmp[-1]) 
    template['day']=str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)
    for province in template['records']:
        text = get_information(province['provinceName'])
        

        new_time = time.strftime("%Y-%m-%dT%H:%M:%S."+str(text["results"][0]["updateTime"]%1000)+"Z",time.localtime(text["results"][0]["updateTime"]/1000))
        province["confirmedIncreased"] = text["results"][0]["confirmedCount"]-province["confirmedCount"]
        province["curedIncreased"] = text["results"][0]["curedCount"]-province["curedCount"]
        province["deadIncreased"] = text["results"][0]["deadCount"]-province["deadCount"]
        province["confirmedCount"] = text["results"][0]["confirmedCount"]
        province["curedCount"] = text["results"][0]["curedCount"]
        province["deadCount"] = text["results"][0]["deadCount"]
        province["updateTime"] = template["day"]
        province["lastUpdate"] = new_time
        province["suspectedCount"] = text["results"][0]["suspectedCount"]
        province["insickCount"] = text["results"][0]["currentConfirmedCount"]
        
        for city in province["cityList"]:
            for new_city in text["results"][0]["cities"]:
                if city["name"]==new_city["cityName"]:
                    city["confirmedIncreased"] = new_city["confirmedCount"]-city["confirmedCount"]
                    city["curedIncreased"] = new_city["curedCount"]-city["curedCount"]
                    city["deadIncreased"] = new_city["deadCount"]-city["deadCount"]
                    city["confirmedCount"] = new_city["confirmedCount"]
                    city["curedCount"] = new_city["curedCount"]
                    city["deadCount"] = new_city["deadCount"]
                    city["updateTime"] = template["day"]
                    city["lastUpdate"] = new_time
                    city["suspectedCount"] = new_city["suspectedCount"]
                    city["insickCount"] = new_city["currentConfirmedCount"]
                    break
    tmp.append(template)
    with open('by_date.json','w',encoding='utf8') as dump_f:
        json.dump(tmp,dump_f,ensure_ascii=False,indent = 2)             
    
            
            
            