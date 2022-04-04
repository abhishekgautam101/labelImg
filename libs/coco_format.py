import glob
import json


def fromVOCtoCOCO(createML_annotation_folder):
    # reading json files
    for file_name in glob.glob(createML_annotation_folder+'/*.xml'):
        print(file_name)