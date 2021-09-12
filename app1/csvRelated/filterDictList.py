def filter_flavor(filter_data, key):
    filtered_data = []
    
    for data in filter_data:
        cnt = 0
        for flavor_data in data["flavor"]:
            if flavor_data in key:
                cnt+=1
        if cnt>0 or key[0] == [""]:
            data["cnt"] = cnt
            filtered_data.append(data)
    return filtered_data

def filter_health(filter_data, key):
    filtered_data = []

    for data in filter : 
        flag = False
        for key_data in key:
            if key_data in data["health"]:
                flag = True
        if flag == True:
            filtered_data.append(data)
    return data


def filter_alg(filter_data, key):
    filtered_data = []
    for data in filter_data:
        flag = True
        for alg_data in data["alg"]:
            if alg_data in key:
                flag = False
                break
        if flag == True:
            filtered_data.append(data)
    
    return filtered_data

