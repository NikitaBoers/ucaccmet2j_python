import json
import csv

saving_precipation_all={}
all_stationsnamed={}

with open ('stations.csv') as file:#load in stations.csv
    stations=csv.DictReader(file)
    for row in stations:#for every dictionary entry
        location=(row['Location'])#add location to variable
        station=(row['Station'])#add station code to variable

        #keep in with loop to be able to do this for every station
        all_stations={}# this is the dictionary for entries within each station
        all_stations['station']=station
        all_stations['state']=row['State']
        filename='precipitation.json'
        # load file as dictionary
        with open(filename, encoding= 'utf8') as file:
            precipation_dict=json.load(file)
            #create variable for list of all with seattle
            all_seattle=[]
            #find code for Seattle in data and select vlue and date and save in dictionary
            for row in precipation_dict:
                if station in row['station']:
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
        #print(list_monthly_precipation)
        all_stations['TotalMonthlyPrecipation']=list_monthly_precipation#add to list for all answers

        # create and save in JSON for each station 
        with open ('MontlyPrecipation.json', 'w') as f: 
            json.dump ( list_monthly_precipation , f , indent =4 , sort_keys = True ) 
        

        #Part 2
        sum_precipation=sum(list_monthly_precipation)# Sum precipation over whole year
        

        #create list of 12 values of sum precipation
        list_percentual_precipation=[]
        for i in list_monthly_precipation:
            monthly_percentual=i/sum_precipation*100
            list_percentual_precipation.append(monthly_percentual)

        #print(list_percentual_precipation)
        all_stations['RelativeMonthlyPrecipation']=list_percentual_precipation
        all_stations['TotalYearlyPrecipation']=sum_precipation
        all_stationsnamed[location]=all_stations




#Part3
#rewritten code
#relative precipation over whole year compared to other stations
list_total_precipation_all=[]#make list for total precipation of all stations
for key in all_stationsnamed:#for loop for the dictionary with info about all stations
    row = all_stationsnamed[key]#make sure row stands for dictionary entry not just for the key
    totalprecipation=row['TotalYearlyPrecipation']#assign total precipation 
    list_total_precipation_all.append(totalprecipation)#add it to the list
total_precipation_all=sum(list_total_precipation_all)#sum list

list_relative_precipation_all=[]#make list to save all relative precipations
for key in all_stationsnamed:#for loop for the dictionary with info about all stations
    row = all_stationsnamed[key]#make sure row stands for dictionary entry not just for the key
    totalprecipation=row['TotalYearlyPrecipation']#assign total precipation to variable
    relative_precipation=totalprecipation/total_precipation_all*100#calculate relative precipation
    row['RelativeYearlyPrecipation']=relative_precipation#add to dictionary
    all_stationsnamed[key]= row
    '''
    dict_relative_precipation={}
    dict_relative_precipation[key]=relative_precipation
    list_relative_precipation_all.append(dict_relative_precipation)
    '''
print(all_stationsnamed)

#save answers in json file
with open ('PrecipationAssignment.json', 'w') as f: 
            json.dump ( all_stationsnamed , f , indent =4 , sort_keys = True )