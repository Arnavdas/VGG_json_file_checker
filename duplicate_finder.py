import os, pathlib as pl, json

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Downloads/')
pth_folder = pth_root#.joinpath('finall_all')# Desktop
pth_json = pth_fold.joinpath('final_json_again.json')

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():
   
    print('Root path :',pth_root,', Folder path :',pth_folder,', json file path :',pth_json,'\n')
    json_file = json.load(pth_json.open())
    print('Total annotations in the json file :',len(json_file),'\n')
    ann, dup_img = 0, []
       
    for i in json_file:
        assets_set, assets_list = set({}), []
        if len(json_file[i]['regions']) != 0:
            for ind, k in enumerate(json_file[i]['regions']):
                if len(k['shape_attributes']) == 0 or len(k['region_attributes']) == 0:
                    print('annotated objects present but no annotations in :',j,'\n')
                else:# below line collects all x_coordinates and y_coordinates of assets in an image json file
                    assets_set = assets_set.union({tuple(k['shape_attributes']['all_points_x']), tuple(k['shape_attributes']['all_points_y'])})
                    assets_list.append((k['shape_attributes']['all_points_x'], k['shape_attributes']['all_points_y']))
#         print(i,':',len(assets_set),len(assets_list))
        if len(assets_set) < 2*len(assets_list):   
            dup_img.append(i)
            ann+= 2*len(assets_list) - len(assets_set)

    print('total duplicate coordinates present in images : ',len(dup_img))
    print('total duplicate x, y coordinates present : ',ann)
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir(),',',pth_json,':',pth_json.is_file())