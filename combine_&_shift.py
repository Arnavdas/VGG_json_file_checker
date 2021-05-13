import os, libpath as lib, shutil, json 

print('current directory : ',os.getcwd())

# set the root path and folder path(in which json file(s) is/are present)
pth_root = pl.Path('/home/arnav/Desktop/detectron2_trial/sample_data_2')# set the root path( dir where u have stored your data)
pth_folder = pth_root.joinpath('new_jsons')# set the path to folder you annotation file is in
new_name = 'all_json_files_new_2.json'# new json file name (should end with .json)
pth_new_json = pth_folder# setting the path for new corrected json file to be created

# BELOW CODE READS ALL JSON FILES AND COMBINES THEM

if pth_root.is_dir() and pth_folder.is_dir(): 
    
    print('Root path :',pth_root,', Folder path :',pth_folder,'\n')
    all_json, t, p = {}, 1, 1

    for i in pth_folder.iterdir():
        if str(i).endswith('.json'):
            json_now = json.load(i.open())
            print('len of ',i,':',len(json_now),'\n')
            for j in json_now:
                if j in all_json:# if a key repeats itself you can rename to include it or ignore it
#                     pass #  ignore  this item & move to next item, else :
                    jj = j +'_'+str(t)
                    print(j,'already exists in the json_all, so will be renaming this key to',jj,'include it \n')
                    all_json[jj] =  json_now[j]
                    t+=1
                else:
                    all_json[j] =  json_now[j]

    print('final len of combined dict : ', len(all_json),'\n')

    # writes the above dictonary as a json file containing updated filenames and keys
    if new_name in os.listdir(pth_new_json):
        print(new_name,'already exists in',pth_new_json,'\t')
        p = int(input('if u proceed(enter 1), it will be overwritten else enter 0 :'))
    
    if t*p:    
        with open(str(pth_new_json)+'/'+new_name,'w') as write_file:# creates new json file in the same directory or rewrites it
            json.dump(all_json, write_file)
            print(new_name,'json file created in ',pth_new_json,'\n')
    else:
        print('no new json file created in ',pth_new_json,'\n')
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir())


# BELOW CODE READS ALL JSON FILES AND SHIFTS/COPIES THE IMG FILES FROM ONE FOLDER TO ANOTHER

if pth_root.is_dir() and pth_folder.is_dir() and pth_json.is_file():
    
    print('Root path :',pth_root,', Folder path :',pth_folder,', Json file path :',pth_json)
    json_dict = json.load(pth_json.open())
    print('images in ',pth_json.name,':',len(json_dict),'\n')
    file_names = [json_dict[i]['filename'] for i in json_dict]
    
#     print(file_names)
    
    source, dest = pth_root.joinpath('sample_data_2'), pth_folder # set the path the json file to be read
    
    if source.is_dir() and dest.is_dir():
        print('source path, dest path :',source,',',dest,'\n')
        
        for f in file_names:
            if f not in os.listdir(source):
                print(f,"doesn't exist in :",source,'\n')
            elif f in os.listdir(dest):
                print(f,"already exists in :",dest,'\n')
                print('note that if u rename it here u need to rename it in the json file as well \n')
            else:
                shutil.copy2(str(source)+'/'+f, dest)# to copy image from source to destination
                print(f,'copied from',source,'to',dest,'\n')
#                 shutil.move(str(source)+'/'+f, dest)# to move image from source to destination
#                 print(f,'shifted from',source,'to',dest,'\n')
    else:
        print(source,':',source.is_dir(),',',dest,':',dest.is_dir())
else:
    print(pth_root,':',pth_root.is_dir(),',',pth_folder,':',pth_folder.is_dir(),',',pth_json,':',pth_json.is_file())
