import json
from glob import glob
import cv2
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("--input_folder", help="input_path_to_your_data (Absolute path is better)",
                    type=str)
parser.add_argument("--output_folder", help="output_folder",
                    type=str)

args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder
json_labels = glob(path.join(input_folder, "*.json"))
for label_path in json_labels:
    img_path = label_path.replace("json", "jpg")
    img_mat = cv2.imread(img_path)
    with open(label_path) as f:
        data = json.load(f)
        shapes = data['shapes']
        for shape in shapes:
            label = shape['label']
            points = shape['points']
            [x1, y1], [x2, y2] = points
            roi = img_mat[int(y1):int(y2), int(x1):int(x2)]
            cv2.imwrite(path.join(output_folder, label + ".jpg"), roi)
