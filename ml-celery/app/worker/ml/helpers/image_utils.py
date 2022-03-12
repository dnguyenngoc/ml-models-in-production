
import cv2
import requests
import numpy as np
from PIL import Image
from io import BytesIO

# import from file
from settings import ml_config


def read_image_from_path_to_numpy(path):
    image = Image.open(path)
    image = image.convert('RGB')
    return np.asarray(image)


def read_image_file(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image


def read_image_from_dir(path) -> Image.Image:
    image = Image.open(path)
    return image


def read_bytes_image_from_url(url):
    response = requests.get(url)
    image_bytes = BytesIO(response.content)
    return image_bytes.read()


def read_image_from_url(url):
    im = Image.open(requests.get(url, stream=True).raw)
    return im


def io_bytes_to_numpy(io_bytes):
    image = Image.open(BytesIO(io_bytes))
    image = image.convert('RGB')
    return  np.asarray(image)



def crop_and_recog_to_bytes(boxes, image):
    crop = []
    def crop_bytes(ymin, xmin, ymax, xmax):
        crop_image = image[ymin:ymax, xmin:xmax]
        pil_im = Image.fromarray(crop_image)
        b = BytesIO()
        pil_im.save(b, 'jpeg')
        im_bytes = b.getvalue()
        return im_bytes
    if len(boxes) == 1:
        ymin, xmin, ymax, xmax = int(boxes[0][0]), int(boxes[0][1]), int(boxes[0][2]), int(boxes[0][3])
        crop.append(crop_bytes(ymin, xmin, ymax, xmax))
    else:
        for box in boxes:
            ymin, xmin, ymax, xmax = int(box[0]), int(box[1]), int(box[2]), int(box[3])
            crop.append(crop_bytes(ymin, xmin, ymax, xmax))
    return crop


def get_center_point(coordinate_dict: dict):
    di = dict()
    for key in coordinate_dict.keys():
        xmin, ymin, xmax, ymax = coordinate_dict[key]
        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        di[key] = (x_center, y_center)
    return di


def sort_result_detection_follow_class_id(detection_boxes, detection_scores, detection_classes, num_class):              
    detection_boxes = np.array(detection_boxes)
    detection_classes= np.array(detection_classes)
    detection_scores = np.array(detection_scores)
    end_boxes = []
    end_score = []
    end_class = []
    for i in range(num_class):
        class_id = i + 1
        score = np.array(detection_scores[detection_classes == class_id])
        boxes = np.array(detection_boxes[detection_classes == class_id])
        end_boxes.append(boxes)
        end_score.append(score)
        end_class.append(class_id)
    return end_boxes, end_score, end_class