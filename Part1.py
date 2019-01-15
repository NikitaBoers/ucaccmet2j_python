import json
import csv
filename='precipitation.json'
# load file as dictionary
with open(filename, encoding= 'utf8') as file:
    precipation_dict=json.load(file)
    #create variable for list of all with seattle
    all_seattle=[]
    #find code for Seattle in data and select vlue and date and save in dictionary
    for row in precipation_dict:
        if 'GHCND:US1WAKG0038' in row['station']:
            dict_value_date={}
            dict_value_date['date']=row['date']
            dict_value_date['value']=row['value']
            #add dictionary to list
            all_seattle.append(dict_value_date)

dict_monthly_precipation={}
#sort by dates
for i in all_seattle:#get each dict with date and value
    i['year'], i['month'], i['day']=i['date'].split('-')#create new dictionary entry for seperated dates
    if i['month'] in dict_monthly_precipation:#if month is already in dict then add the value to it
        dict_monthly_precipation[i['month']]+= i['value']
    else:#otherwise create new dict entry
        dict_monthly_precipation[i['month']]=i['value']
list_monthly_precipation=list(dict_monthly_precipation.values())#make list from dict values
print(list_monthly_precipation)

# create and save in JSON
with open ('MontlyPrecipation.json', 'w') as f: 
    json.dump ( list_monthly_precipation , f , indent =4 , sort_keys = True ) 