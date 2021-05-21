import os, pathlib as pl, json

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Downloads/')
pth_folder = pth_root#.joinpath('finall_all')# Desktop
pth_json = pth_fold.joinpath('all_final.json')

nam = 'xyz_only'
pth_new_json = pth_fold#storage dir of new json file 

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():
   
    print('Root path :',pth_root,', Folder path :',pth_folder,', json file path :',pth_json,'\n')
    json_file = json.load(pth_json.open())
    print('Total annotations in the json file :',len(json_file),'\n')
    ann, dup_img, new_json = 0, [], None
    
    for i in json_file:
        assets_set, assets_list, assets_region = set({}), [], []
        if len(json_file[i]['regions']) != 0:
            for ind, k in enumerate(json_file[i]['regions']):
                if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
                    print('annotated objects present but no annotations in :',j,'\n')
                else:# below line collects all x_coordinates and y_coordinates of assets in an image json file
                    assets_set = assets_set.union({tuple(k['shape_attributes']['all_points_x']), tuple(k['shape_attributes']['all_points_y'])})
                    assets_list.append((k['shape_attributes']['all_points_x'], k['shape_attributes']['all_points_y']))
                    assets_region.append(k)
        
        if len(assets_set) < 2*len(assets_list):
        	
            print('duplicates present in ',i)
            new_json = json_file.copy()
            dup_img.append(i)
            ann+= 2*len(assets_list) - len(assets_set)

            for coord in assets_list:
                if assets_list.count(coord) > 1:
                    for j in range(1, assets_list.count(coord)):
                        for kk in assets_region:
#                             print(kk)
                            if coord == (kk['shape_attributes']['all_points_x'], kk['shape_attributes']['all_points_y']):
                                try:# if already removed it will throw an error
                                    new_json[i]['regions'].remove(kk)
                                    break
                                except:
                                    pass

    print('total duplicate coordinates present in images : ',len(dup_img))
    print('total duplicate x, y coordinates present : ',ann)
    
    if new_json!=None:
        # writes the above dictonary as a json file containing updated filenames and keys
        new_name = nam+'_dup_del.json'# should end with .json
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