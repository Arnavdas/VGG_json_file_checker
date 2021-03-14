# VGG_json_file_operations


These set of scripts are for performing different operations on json annotation files, iff you are using VGG image annotator(https://www.robots.ox.ac.uk/~vgg/software/via/) and have selected 'polygon region shape' as the annotation shape to annotate the objects.

Put this up here because I use these scripts while annotating extensively.

* Faults_&_Counts.py : Counts the annotated assets and also picks out the objects where there are some mistakes(like the area is specified but not tagged or if the annotation file exits but it's empty)

* re_(move & create).py : removes objects from annotation files if they have 0 region attributes or have 0 regions and recreates new corrected json file(s)
