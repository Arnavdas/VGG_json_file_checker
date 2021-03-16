import os, json, pathlib as pl

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Desktop/detectron2_trial')
pth_folder = pth_root.joinpath('sample_data_2')

# FOR ONE JSON FILE :

pth_json = pth_folder.joinpath('imperfect_again_json.json')# place the json file to be operated on 

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():

	print('Root path :',pth_root,', Folder path :',pth_folder,', Json file path :',pth_json)
    json_dict = json.load(pth_json.open())
    print('images in ',pth_json.name,':',len(json_dict))
    dict_relevant, no_region, dict_final = {}, {}, {}
    
    # FOR SELECTING RELEVANT(ANNOTATED REGIONS) AND EXCLUDING NON ANNOTATED PARTS FROM ONE JSON FILE:
    for j in json_dict:
        if len(json_dict[j]['regions']) > 0:# or len(json_dict[j]['region']) > 0:
            dict_relevant[j] = json_dict[j]
        else:
            no_region[j] = json_dict[j]

    print('Total of relevant & non-relevant regions : ',len(dict_relevant),',',len(no_region))
    
    # REMOVES REGIONS WITH 0 REGION ATTRIBUTES(That have no tags) FOR ONE JSON FILE:
    for j in dict_relevant:
        to_remove = []
        for k in dict_relevant[j]['regions']:
            if len(k['region_attributes']) == 0:
                to_remove.append(k)
        for m in to_remove:
            dict_relevant[j]['regions'].remove(m)
    
    # After the above step maybe some regions will have 0 annotated regions, we need to remove them again
    for j in dict_relevant:
        if len(dict_relevant[j]['regions']) > 0:# or len(json_dict[j]['region']) > 0:
            dict_final[j] = dict_relevant[j]
        else:
            print('non tagged regions in',j,":",len(dict_relevant[j]['regions']))
            no_region[j] = dict_relevant[j]
    
    print('Total of relevant & non-relevant regions :',len(dict_final),',',len(no_region))
    
    print('Final annotations in corrected json_dict :',len(dict_final))
    
    # writes the above dictonary as a json file containing updated filenames and keys
    new_name = 'imperfect_rectified_again.json'# should end with .json
    pth_new_json = pth_folder#setting the path for new corrected json file to be created
    with open(str(pth_new_json)+'/'+new_name,'w') as write_file:# creates new json file in the same directory 
        json.dump(dict_final, write_file)
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir(),',',pth_json,':',pth_json.is_file())


# FOR MULTPLE JSON FILES AT ONCE :

# if pth_root.is_dir() and pth_folder.is_dir():
	# print('Root path :',pth_root,', Folder path :',pth_folder)
#     json_all = {}

#     for i in os.listdir(pth_folder):
#         if i.endswith('.json'):
#             pth_json = pth_folder.joinpath(i)
#             json_all[i] = json.load(pth_json.open())
#             print(i,':',len(json_all[i]),'images')
            
#     print('total json files captured : ',len(json_all),'\n')
    
#     for t,i in enumerate(json_all):
#         json_dict = json_all[i]
#         print(i,' JSON FILE :')
#         dict_relevant, no_region, dict_final = {}, {}, {}
    
#         # FOR SELECTING RELEVANT(ANNOTATED REGIONS) AND EXCLUDING NON ANNOTATED PARTS FROM ONE JSON FILE:
#         for j in json_dict:
#             if len(json_dict[j]['regions']) > 0:# or len(json_dict[j]['region']) > 0:
#                 dict_relevant[j] = json_dict[j]
#             else:
#                 no_region[j] = json_dict[j]

#         print('Total of relevant & non-relevant regions : ',len(dict_relevant),',',len(no_region))

#         # REMOVES REGIONS WITH 0 REGION ATTRIBUTES(That have no tags) FOR ONE JSON FILE:
#         for j in dict_relevant:
#             to_remove = []
#             for k in dict_relevant[j]['regions']:
#                 if len(k['region_attributes']) == 0:
#                     to_remove.append(k)
#             for m in to_remove:
#                 dict_relevant[j]['regions'].remove(m)

#         # After the above step maybe some regions will have 0 annotated regions, we need to remove them again
#         for j in dict_relevant:
#             if len(dict_relevant[j]['regions']) > 0:# or len(json_dict[j]['region']) > 0:
#                 dict_final[j] = dict_relevant[j]
#             else:
#                 print('non tagged regions in',j,":",len(dict_relevant[j]['regions']))
#                 no_region[j] = dict_relevant[j]

#         print('Total of relevant & non-relevant regions :',len(dict_final),',',len(no_region))

#         print('Final annotations in corrected json_dict :',len(dict_final),'\n')
        
#         # writes the above dictonary as a json file containing updated filenames and keys
#         new_name = 'new_json_files.json'# should end with .json
#         pth_new_json = pth_folder.joinpath('new_jsons')#setting the path for new corrected json file to be created
#         with open(str(pth_new_json)+'/'+str(t)+'_'+new_name,'w') as write_file:# creates new json file in the same directory 
#             json.dump(dict_final, write_file)
        
# else: 
#     print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir())
