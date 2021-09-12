#급여대상,사료 종목,브랜드,이름,가격,용량,사료 형태,제조국,유기농여부,특이사항,칼로리(100g),특정종대상,동물크기,급여연령,Mainflavor,주원료,키블크기,금기대상,특정급여시기,질환,처방적용대상효능,수분,조단백질,조지방,조회분,조섬유,칼슘,인,탄수화물,오메가3,오메가6
import csv
def csvToDictList():
    data = [] #list
    with open('KingFile.csv', encoding='utf-8-sig') as csvfile: #특정 파일을 읽어도록
        rdr = csv.DictReader(csvfile)
        
        for line in rdr:
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

                #"food_type" : "",#영양제,밥
                #"price": 0,
                #"amount" : 0,
                #"contry" : "",
                #"organic" : "",
                #"etc" : "",
                #"kcal": 0,
                #"breed": "",
                #"kibble" : "",
                #"not_when" : [],
                #"when" : [],
                #"disease" : [],
                #"main_eff" : [],
                #"nutr" : [0,0,0,0,0,0,0,0,0,0],     #0: 수분 / 1: 조단백 / 2: 조지방 / 3: 조회분 / 
                                                    #4: 조섬유 / 5: 칼슘 / 6. 인 / 7. 탄수화물
                                                    #8. 오메가3 / 9. 오메가6
            }

            dic_data["pet"] = line["급여대상"]
            #dic_data["food_type"] = line["사료 종목"]
            dic_data["brand"] = line["브랜드"]
            dic_data["name"] = line["이름"]
            #dic_data["price"] = int(line["가격"])
            #dic_data["amount"] = int(line["용량"])
            dic_data["food_shape"] = line["사료 형태"]
            #dic_data["country"] = line["제조국"]
            #dic_data["organic"] = True if line["유기농여부"] == "Y" else False
            #dic_data["etc"] = line["특이사항"]
            #dic_data["kcal"] = float(line["칼로리(100g)"])
            #dic_data["breed"] = line["특정종대상"]
            dic_data["size"] = line["동물크기"]
            #dic_data["nutr"][0] = float(line["수분"])
            #dic_data["nutr"][1] = float(line["조단백질"])
            #dic_data["nutr"][2] = float(line["조지방"])
            #dic_data["nutr"][3] = float(line["조회분"])
            #dic_data["nutr"][4] = float(line["조섬유"])
            #dic_data["nutr"][5] = float(line["칼슘"])
            #dic_data["nutr"][6] = float(line["인"])
            #dic_data["nutr"][7] = float(line["탄수화물"])
            #dic_data["nutr"][8] = float(line["오메가3"])
            #dic_data["nutr"][9] = float(line["오메가6"])
            #alg, disease, main_eff, kibble 얘네들 입력받아야함!!!
            dic_data["alg"] = [alg_data.strip() for alg_data in line["Allergy"].split(",")]
            
            #dic_data["age"] = line["급여연령"].split("~")
            #dic_data["age"][0] = float(dic_data["age"][0])
            #if dic_data["age"][1] == 'max':
            #    dic_data["age"][1] = 99999
            #else:
            #    dic_data["age"][1] = float(dic_data["age"][1])
            dic_data["flavor"] = [flavor_data.strip() for flavor_data in line["Mainflavor"].split(",")]
            

            #dic_data["age"] = list(map(float,dic_data["age"] ))
            #dic_data["when"] = line["특정급여시기"].split(",")
            #dic_data["not_when"] = line["금기대상"].split(",")

            data.append(dic_data)
    return data