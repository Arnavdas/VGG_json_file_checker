import os, pathlib as pl, json

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Desktop/detectron2_trial')# set the root path( dir where u have stored your data)
pth_fold = pth_root.joinpath('sample_data')# set the path to folder you annotation file is in 

# FOR SINGLE JSON FILE :

pth_json = pth_fold.joinpath('10_sample_json.json')# set the json file name present inside the folder

print('Root path :',pth_root,', Folder path :',pth_fold,', Json file path :',pth_json)

if pth_root.is_dir() and pth_fold.is_dir() and pth_json.is_file() :# check if all the directories and files exist
    
    count_obj, json_file = {}, json.load(open(pth_json))
    tag = 'object'# change to region attribute value you had entered in vgg image annotator
    # tag = []# if u have multiple tags/region attribute values in the json file

    print('total images inside the json file :',len(json_file))

    for j in json_file:
        if len(json_file[j]['regions']) != 0:
            for k in json_file[j]['regions']:
                if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
                    print('annotated objects present but no annotations in :',j)
                else:
                    if type(tag) != list:
                        if type(k['region_attributes'][tag]) != dict:
                            try:
                                count_obj[k['region_attributes'][tag]]+= 1
                            except:
                                count_obj[k['region_attributes'][tag]] = 1
                        else:
                            for p in k['region_attributes'][tag]:
                                try:
                                    count_obj[p]+= 1
                                except:
                                    count_obj[p] = 1

                    else:#for multiple tag values
                        for t in tag:
                            while True:
                                try:
                                    tag_type = type(k['region_attributes'][tag])
                                    break
                                except:
                                    pass
                            if tag_type != dict:
                                try:
                                    count_obj[k['region_attributes'][tag]]+= 1
                                except:
                                    count_obj[k['region_attributes'][tag]] = 1
                            else:
                                pass
                                for p in tag_type:
                                    try:
                                        count_obj[p]+= 1
                                    except:
                                        count_obj[p] = 1

        else:
            print('NO annotated objects at all in :',j)

    print(count_obj)
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_fold,':',pth_fold.is_dir(),',',pth_json,':',pth_json.is_file())

# FOR MULTIPLE JSON FILES

# if pth_root.is_dir() and pth_fold.is_dir():

#     print('Root path :',pth_root,', Folder path :',pth_fold)

#     json_file, count_obj, tot = {}, {}, 0

#     for i in pth_fold.iterdir():
#         if i.name.lower().endswith('json'):
#             json_file[i] = json.load(i.open())
#             print(i.name,'json file :',len(json_file[i]),' images')
#             tot+=len(json_file[i])
        
#     print('total images inside the multiple json files :',tot)

#     tag = 'object'# change to region attribute value you had entered in vgg image annotator
#     # tag = []# if u have multiple tags/region attribute values in the json file

#     for i in json_file:
#         for j in json_file[i]:
#             if len(json_file[i][j]['regions']) != 0:
#                 for k in json_file[i][j]['regions']:
#                     if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
#                         print('annotated objects present but no annotations in :',i,',',j)
#                     else:
#                         if type(tag) != list:# for single tag values
#                             if type(k['region_attributes'][tag]) != dict:
#                                 try:
#                                     count_obj[k['region_attributes'][tag]]+=1
#                                 except:
#                                     count_obj[k['region_attributes'][tag]] = 1
#                             else:
#                                 for p in k['region_attributes'][tag]:
#                                     try:
#                                         count_obj[p]+=1
#                                     except:
#                                         count_obj[p] = 1
#                         else:
#                             #for multiple tag values 
#                             for t in tag:
#                                 while True:
#                                     try:
#                                         tag_type = type(k['region_attributes'][tag])
#                                         break
#                                     except:
#                                         pass
#                                 if tag_type != dict:
#                                     try:
#                                         count_obj[k['region_attributes'][tag]]+= 1
#                                     except:
#                                         count_obj[k['region_attributes'][tag]] = 1
#                                 else:
#                                     for p in tag_type:
#                                         try:
#                                             count_obj[p]+= 1
#                                         except:
#                                             count_obj[p] = 1
#             else:
#                 print('NO annotated objects at all in :',i,',',j)

#     print(count_obj)
# else:
#     print(pth_root,':',pth_root.is_dir(),',',pth_fold,':',pth_fold.is_dir())
