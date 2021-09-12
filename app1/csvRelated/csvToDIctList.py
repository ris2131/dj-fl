#급여대상,사료 종목,브랜드,이름,가격,용량,사료 형태,제조국,유기농여부,특이사항,칼로리(100g),특정종대상,동물크기,급여연령,Mainflavor,주원료,키블크기,금기대상,특정급여시기,질환,처방적용대상효능,수분,조단백질,조지방,조회분,조섬유,칼슘,인,탄수화물,오메가3,오메가6
import csv 
from . import filterDictList
#from app1 import csvRelated
def csvToDictList(flavorKey,algKey, healthKey):#algKey,flavorKey,healthKey
    data = [] #list
    #현재위치가 루트로 되어있는거 같더라.
    with open('./app1/csvRelated/kingFile.csv','r',encoding='utf-8-sig') as csvfile: #특정 파일을 읽어도록
        rdr = csv.DictReader(csvfile)

        for line in rdr:
            #print(line)
            dic_data = {#dict
                "pet": "",#급여대상
                "brand" : "",#브랜드
                "name" : "",#이름
                "food_shape" : "",#사료형태(건식)
                "size" : "",#급여가능 동물크기
                #"age" : [0,0],#급여연령 일단 안하기로 했대.
                "flavor" : [],#맛
                "alg" : [],#알레르기
                "health" : [],#건강개선
                "explain" : "",#사료해석

                
            }
            dic_data["pet"] = line["급여대상"]
            dic_data["brand"] = line["브랜드"]
            dic_data["name"] = line["이름"]
            dic_data["food_shape"] = line["사료 형태"] 
            dic_data["size"] = line["동물크기"]
                              
            dic_data["alg"] = [alg_data.strip() for alg_data in line["알레르기"].split(",")]
            
            
            dic_data["flavor"] = [flavor_data.strip() for flavor_data in line["Mainflavor"].split(",")] #BUG 제안 이것도 스페이스?
            dic_data["health"] = [dis_data.strip() for dis_data in line["건강 개선"].split(",")]
            dic_data["explain"] = line["사료 해석"]
            #print(dic_data)
            data.append(dic_data)
    
    #filterDictList.filter_flavor(data,flavorKey)
    #filterDictList.filter_alg(data,algKey)
    #filterDictList.filter_health(data,healthKey)
    print(data)
    return data


