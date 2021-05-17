import numpy as np
import os, json, cv2
import matplotlib.pyplot as plt

def asset(x_pts, y_pts, tag):
    return {"shape_attributes":{"name":"polygon","all_points_x":x_pts,"all_points_y":y_pts}, "region_attributes":{"object":str(tag)}}    

def border_only(coord, i):
    bin_dest, bin_nam = '/home/phiai/Desktop/arnavDas/Tower asset detection/binary masks/', i+'_bin_mask.png'
    plt.imsave(bin_dest+bin_nam, coord)
    im = cv2.imread(bin_dest+bin_nam)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours[0].T[0], contours[0].T[1]

# end with '/' all below directory paths
pth = ''# , path of all images
pth_new_json = ''# pth where the newly created json file will be stored
pic_dest = ''# new destination for images
all_json = {}# json obj
nam = 'new'# name for new json file to be created
obj_json = []# if any particular list of object(s) u wish to make vgg json files of

for j in os.listdir(pth):
    if j.endswith('.JPG') or j.endswith('.jpg'):
        file_name = j#or can be tower_name+'_'+(any number).jpg, should always end with .jpg/.png/.jpeg 
#         os.rename(pth+j, pic_dest+file_name)# renames this img to new img name file_name
#         shutil.copy2(pth+j, pic_dest+file_name)# copies this img to a new destination with new name file_name
        file_size = os.stat(pth+j).st_size
        json_obj = {"filename":file_name,"size":file_size,'regions':[],"file_attributes":{}}
# for Below line note that u can prepend anything to file_name+str(file_size) but do not change anything in between file_name and str(file_size)
        json_key = file_name+str(file_size)
        pred = predictor_1(cv2.imread(pth+j))# predictor_1 is the model which gives the output in the format of a detectron2 Mask-RCNN model

        for i in range(len(pred['instances'])):
            try:# used try bcz if there's no contours in current image skip the process
                coord = pred['instances'].pred_masks[i]
                x_pt, y_pt = border_only(coord.cpu(), str(i))
                tag = CLASS_NAMES[pred['instances'].pred_classes[i]]
                if tag in obj_json:
                    json_obj['regions'].append(asset(x_pt.tolist()[0], y_pt.tolist()[0], tag))
            except:
                pass
        
        all_json[json_key] = json_obj
    # break
        
print('Total annotations in the new json file :',len(all_json),'\n')
if os.path.isdir(pth_dest):
    print('total files in new dest :',len(os.listdir(pth_dest)),'\n')

if len(all_json) != 0:
    # writes the above dictonary as a json file containing updated filenames and keys
    new_name = nam+'_all_final.json'# should end with .json
    p = 1

    if new_name in os.listdir(pth_new_json):
        print(new_name,'already exists in',pth_new_json,'\t')
        p = int(input('if u proceed(enter 1) it will be overwritten, else enter 0 :'))

    if p:
        if os.path.isfile(pth_new_json):
            os.remove(str(pth_new_json)+'/'+new_name)  
        with open(str(pth_new_json)+'/'+new_name,'w') as write_file:# creates new json file in the same directory or rewrites it
            json.dump(all_json, write_file)
            print(new_name,'created in',pth_new_json,':',os.path.isfile(pth_new_json+'/'+new_name),'\n')
    else:
        print('no new json file created in :',pth_new_json,'\n') 
