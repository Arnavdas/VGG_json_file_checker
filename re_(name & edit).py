import os, json, pathlib as pl, shutil, json, copy

pth_root = pl.Path('/home/arnav/Desktop/detectron2_trial')
pth_folder = pth_root.joinpath('sample_data')
pth_img = pth_folder.joinpath('rectified_img')
pth_json = pth_folder.joinpath('new_json_file.json')
pth_dest = pth_root.joinpath('final_img')

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file(): 
    
    print('Root path :',pth_root,', Folder path :',pth_folder,', json file path :',pth_json,'\n')
    all_json, wrong_tag, new_json = {}, ['apple','orange','joint','nut'], {}
    nam = 'fruit_' # for new name to new_json file
    edit_dict, edit_key, fname = {'aple':'apple', 'oranje':'orange'}, 'testing'+'_', 'example'+'_'
    json_file = json.load(pth_json.open())
    
    print('Total annotations in the json file :',len(json_file),'\n')
    
    for i in json_file:
        if len(json_file[i]['regions']) != 0:
            for k in json_file[i]['regions']:
                if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
                    print('annotated objects present but no annotations in :',j,'\n')
                else:
                    for s in k['region_attributes']:# sometimes key values are dictionary themselves like : {'apple':True}
                        if type(k['region_attributes'][s]) == dict:
                            pass
                        else:# sometimes there are strings only like : 'apple'
#                             print(k['region_attributes'][s])
                            if k['region_attributes'][s] in wrong_tag:# to remove particular tagged objects
                                remove.append(k)
                            if k['region_attributes'][s] in edit_dict.keys():# changes exact object tag(like cat, fish, apple)
                                k['region_attributes'][s] = edit_dict[k['region_attributes'][s]]
        if edit_key not in i:
            new_json[edit_key+i] = json_file[i]# modify this according to your needs
                                
    new_json_1 = copy.deepcopy(new_json)

    for i in new_json_1:
        if fname not in new_json[i]['filename']:
            new_json[i]['filename'] = fname+new_json[i]['filename']# use this if u have already renamed image files
        for k in new_json_1[i]['regions']:
            if k in remove:
                new_json[i]['regions'].remove(k)
                                    
    if pth_img.is_dir() and pth_dest.is_dir():# shifts images in the new json file: u have the option to exclude this operation
        for i in new_json:
            if new_json[i]['filename'] in os.listdir(pth_img):# shifts/copies/renames img files
                v = new_json[i]['filename']
#                 os.rename() # renames orignal files(can also shift as well if new file is preceded with a diff directory name)
#                 shutil.move() # moves original file from one directory to another
                shutil.copy2(str(pth_img)+'/'+v, str(pth_dest)+'/'+fname+v) # (safest of 3) copies file from one directory to another & as well renames the copy 
                new_json[i]['filename'] = fname+v
            elif new_json[i]['filename'] not in os.listdir(pth_dest):# if not available in both folders
                print(new_json[i]['filename'] ,'not in',pth_img,'or in',pth_dest)
            else:
                print(pth_dest,':',pth_dest.is_dir(),',',pth_img,':',pth_img.is_dir())
                        
                        
    print('Total annotations in the new json file :',len(new_json),'\n')
    if pth_dest.is_dir():
        print('total files in new dest :',len(os.listdir(pth_dest)),'\n')
        
    if len(new_json) != 0:
        # writes the above dictonary as a json file containing updated filenames and keys
        new_name = nam+'_all_final.json'# should end with .json
        pth_new_json = pth_root.joinpath('new_jsons')# setting the path for new corrected json file to be created
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
