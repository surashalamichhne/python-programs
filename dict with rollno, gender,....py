Dict={'roll no':[1,2,3,4],'name':['ram','hari','adi','elisha'],'marks':[70.0,80.0,60.0,40,0],'gender':['male','male','female','female']}
for i in range(len(Dict['roll no'])):
    if Dict['gender'][i]=='male':
        print(Dict['marks'][i])
        print(Dict['name'][i])
        print(Dict['gender'][i])