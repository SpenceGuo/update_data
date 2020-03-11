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
    with open('by_area.json','r',encoding='utf8') as load_f:
        tmp = json.load(load_f)
    hubei_dic = {"confirmedCount":0,"deadCount":0,"curedCount":0,"insickCount":0,"time":""}
    feihubei_dic = {"confirmedCount":0,"deadCount":0,"curedCount":0,"insickCount":0,"time":""}
    for i in range(len(tmp)-1,-1,-1):
        if tmp[i]["name"] != "全国" and tmp[i]["name"] != "非湖北":
            text = get_information(tmp[i]['provinceName'])
            tmp[i]["lastUpdate"] = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(text["results"][0]["updateTime"]/1000))
            
            new_inf = {}
            last_inf = tmp[i]["records"][-1]
            new_inf["confirmedIncreased"] = text["results"][0]["confirmedCount"]-last_inf["confirmedCount"]
            new_inf["deadIncreased"] = text["results"][0]["deadCount"]-last_inf["deadCount"]
            new_inf["curedIncreased"] = text["results"][0]["curedCount"]-last_inf["curedCount"]
            new_inf["confirmedCount"] = text["results"][0]["confirmedCount"]
            new_inf["deadCount"] = text["results"][0]["deadCount"]
            new_inf["curedCount"] = text["results"][0]["curedCount"]
            new_inf["insickCount"] = text["results"][0]["currentConfirmedCount"]
            new_inf["updateTime"] = str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)
            if feihubei_dic["time"] < tmp[i]["lastUpdate"]:
                feihubei_dic["time"] = tmp[i]["lastUpdate"]
            if tmp[i]["name"] !="湖北省":
                feihubei_dic["confirmedCount"] += new_inf["confirmedCount"]
                feihubei_dic["deadCount"] += new_inf["deadCount"]
                feihubei_dic["curedCount"] += new_inf["curedCount"]
                feihubei_dic["insickCount"] += new_inf["insickCount"]
            else:
                hubei_dic["confirmedCount"] = new_inf["confirmedCount"]
                hubei_dic["deadCount"] = new_inf["deadCount"]
                hubei_dic["curedCount"] = new_inf["curedCount"]
                hubei_dic["insickCount"] = new_inf["insickCount"]
                hubei_dic["time"] = tmp[i]["lastUpdate"]
            tmp[i]["records"].append(new_inf)
        elif tmp[i]["name"] =="非湖北":
            tmp[i]["lastUpdate"] = feihubei_dic["time"]
            new_inf = {}
            last_inf = tmp[i]["records"][-1]
            new_inf["confirmedIncreased"] = feihubei_dic["confirmedCount"]-last_inf["confirmedCount"]
            new_inf["deadIncreased"] = feihubei_dic["deadCount"]-last_inf["deadCount"]
            new_inf["curedIncreased"] = feihubei_dic["curedCount"]-last_inf["curedCount"]
            new_inf["confirmedCount"] = feihubei_dic["confirmedCount"]
            new_inf["deadCount"] = feihubei_dic["deadCount"]
            new_inf["curedCount"] = feihubei_dic["curedCount"]
            new_inf["insickCount"] = feihubei_dic["insickCount"]
            new_inf["updateTime"] = str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)
            tmp[i]["records"].append(new_inf)
        else:
            tmp[i]["lastUpdate"] = max(feihubei_dic["time"],hubei_dic["time"])
            new_inf = {}
            last_inf = tmp[i]["records"][-1]
            new_inf["confirmedIncreased"] = feihubei_dic["confirmedCount"]+hubei_dic["confirmedCount"]-last_inf["confirmedCount"]
            new_inf["deadIncreased"] = feihubei_dic["deadCount"]+hubei_dic["deadCount"]-last_inf["deadCount"]
            new_inf["curedIncreased"] = feihubei_dic["curedCount"]+hubei_dic["curedCount"]-last_inf["curedCount"]
            new_inf["confirmedCount"] = feihubei_dic["confirmedCount"]+hubei_dic["confirmedCount"]
            new_inf["deadCount"] = feihubei_dic["deadCount"]+hubei_dic["deadCount"]
            new_inf["curedCount"] = feihubei_dic["curedCount"] +hubei_dic["curedCount"]
            new_inf["insickCount"] = feihubei_dic["insickCount"] + hubei_dic["insickCount"]
            new_inf["updateTime"] = str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)
            tmp[i]["records"].append(new_inf)
            
    with open('by_area.json','w',encoding='utf8') as dump_f:
        json.dump(tmp,dump_f,ensure_ascii=False,indent = 2)       





   
            
            
            