import random as rm, copy
import os, pathlib as pl, json

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Downloads/')
pth_folder = pth_root#.joinpath('finall_all')# Desktop
pth_json = pth_fold.joinpath('final_json_again.json')

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():
   
    print('Root path :',pth_root,', Folder path :',pth_folder,', json file path :',pth_json,'\n')
    wrong_tag, new_json = ['apple'], {}
    nam = 'trial_delete' # for new name to new_json file
    json_file = json.load(pth_json.open())
    print('Total annotations in the json file :',len(json_file),'\n')
    ann = 2000# no of assets to be cut off : should be lesser than or equal to total number of assets in the wrong_tag
       
    while ann > 0:
        remove = []
       
        for i in rm.sample(json_file.keys(), 1):
            if len(json_file[i]['regions']) != 0:
                for k in json_file[i]['regions']:
                    if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
                        print('annotated objects present but no annotations in :',j,'\n')
                    else:
                        for s in k['region_attributes']:# sometimes key values are dictionary themselves like : {'apple':True}
                            if type(s) == dict:
                                pass
                            else:# sometimes there are strings only like : 'apple'
                                if k['region_attributes'][s] in wrong_tag:# to remove particular tagged objects
#                                     print( k['region_attributes'][s])
                                    remove.append(k)
   
        new_json_1 = copy.deepcopy(json_file)

        for i in new_json_1:
            for k in new_json_1[i]['regions']:
                if k in remove:
                    json_file[i]['regions'].remove(k)
                    ann-=1
#                     print(ann)
                   
    new_json = json_file.copy()
    if len(new_json) != 0:
        # writes the above dictonary as a json file containing updated filenames and keys
        new_name = nam+'_all_final.json'# should end with .json
        pth_new_json = pth_root#.joinpath('new_jsons')# setting the path for new corrected json file to be created
        p = 1

        if pth_new_json.is_dir():
            if new_name in os.listdir(pth_new_json):
                print(new_name,'already exists in',pth_new_json,'\t')
                p = int(input('if u proceed(enter 1) it will be overwritten, else enter 0 :'))

        if p:
            if pth_new_json.is_file():
                os.remove(str(pth_new_json)+'/'+new_name)    
            with open(str(pth_new_json)+'/'+new_name,'w') as write_file:# creates new json file in the same directory or rewrites it
                json.dump(new_json, write_file)
                print(new_name,'created in',pth_new_json,':',pth_new_json.joinpath(new_name).is_file())
        else:
            print('no new json file created in :',pth_new_json)
else:
	print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir(),',',pth_json,':',pth_json.is_file())