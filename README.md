# VGG_json_file_operations


These set of scripts are for performing different operations on json annotation files, iff you are using VGG image annotator(https://www.robots.ox.ac.uk/~vgg/software/via/), while uploading this script worked for VGG 2.1.0 and have selected 'polygon region shape' as the annotation shape to annotate the objects.

Put this up here because I use these scripts while annotating extensively.

* Faults_&_Counts.py : Counts the annotated assets and also picks out the objects where there are some mistakes(like the area is specified but not tagged or if the annotation file exits but it's empty)

* re_(move & create).py : removes objects from annotation files if they have 0 region attributes or have 0 regions and recreates new corrected json file(s)

* combine_&_shift.py : combines different json files to create a single json file as well as shifts all the files(images) mentioned in the json file

PS : there are some indentation errors in above scripts while running in some text editors but otherwise seems fine in jupyter notebook
