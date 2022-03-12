import configparser


cfg = configparser.ConfigParser()
cfg.read('./environment.ini')

ML = cfg["ml"]
MODEL_PATH = ML['model_path']
LABLE_PATH = ML['label_path']

NMS_THRESHOLD = float(ML['mns_threshold'])
SCORE_THRESHOLD = float(ML['score_threshold'])
NUMBER_CLASSES = int(ML['num_classes'])
MAX_CLASS_OUT = int(ML['max_class_out'])