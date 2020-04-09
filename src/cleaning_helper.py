def lacounty_daily_text_2_table(text_list):
    # pipeline function for LAC date from mar 30
    out_lst = []
    temp = list(filter(lambda x: "City" in x, text_list))
    if temp:
        string = temp[0]
        str_lst2 = string.split("\t  ")
        string2 = str_lst2[0][:str_lst2[0].find("\t(\t")]

        for i in str_lst2:
            string2 = i[:i.find("\t(\t")]
            tem_lst = string2.replace("\t",",").strip().split(",")
            out_lst.append(tem_lst[0:2])
    return out_lst


def lacounty_daily_text_2_table2(text_list):
    # pipeline function for LAC date of mar 22 - mar 29
    out_lst = []
    temp = list(filter(lambda x: "City" in x, text_list))
    if temp:
        string = temp[0]
        str_lst2 = string.split("\t")
        for i in range(len(str_lst2) - 1):
            temp_lst = []
            temp_lst.append (str_lst2[i].split("  ", 1)[1])
            temp_lst.append (str_lst2[i + 1].split("  ", 1)[0])
            out_lst.append(temp_lst)
    return out_lst

def find_LB_or_PD(raw_data, city):
    # Get case information of Long Beach and Pasadena which are reported seperately
    out_list = []
    for item in out:
        temp_lst = [item[1].split("\r\n\t")[1]]
        if len(item[2]) > 0:
            out_lst = []
            text_list = item[2]
            temp = list(filter(lambda x: city in x, text_list))
            if temp:
                temp_lst.append(temp[0].replace("-","").split(city)[1].split()[0])    
        if len(temp_lst) == 2:
        
            out_list.append(temp_lst)
        
        if len(out_list)>1 and out_list[-1][0] == out_list[-2][0]:
            out_list.pop(-1)
    return out_list

# helper function to fix city names
def aka_name(city_name):
    new_name = ""
    if city_name[:7] == "City of":
        new_name += city_name[-(len(city_name) - 8) : ]
    elif city_name[:14] == 'Unincorporated':
        new_name += city_name[-(len(city_name) - 17) : ]
    elif city_name[:14] == 'Los Angeles - ':
        new_name += city_name[-(len(city_name) - 14) : ]
    else:
        new_name += city_name
    return new_name