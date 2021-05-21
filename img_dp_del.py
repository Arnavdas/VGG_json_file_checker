import os, pathlib as pl, json, copy

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Downloads/')
pth_folder = pth_root#.joinpath('finall_all')# Desktop
pth_json = pth_fold.joinpath('6_final_json_again.json')

nam = 'only_7'
pth_new_json = pth_fold #storage dir of new json file 

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():
   
    print('Root path :',pth_root,', Folder path :',pth_folder,', json file path :',pth_json,'\n')
    json_file = json.load(pth_json.open())
    print('Total annotations in the json file :',len(json_file),'\n')
    key_nam, file_nam = [i for i in json_file], [json_file[i]['filename'] for i in json_file]
    print(len(key_nam), len(set(file_nam)))
#     print(json_file)
    new_json, dict_file = json_file.copy(), {}

    if len(key_nam) != len(set(file_nam)):
        for i in json_file:
            try:
                dict_file[json_file[i]['filename']].append(i)
            except:
                dict_file[json_file[i]['filename']] = [i]

        for j in dict_file:
            if len(dict_file[j]) > 1:
                one_key = dict_file[j][0]# makes the first key found as the only key to absorb all other same image annotations
                for d in range(1, len(dict_file[j])):
                    new_json[one_key]['regions'].extend(json_file[dict_file[j][d]]['regions'])
                    new_json.pop(dict_file[j][d])
        
        
        if len(new_json) != 0:
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
        print('same no of filenames and keys')
            
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir(),',',pth_json,':',pth_json.is_file())