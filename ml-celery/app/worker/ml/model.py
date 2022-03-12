"""
    @Author by Duy Nguyen Ngoc 
    @email: duynguyenngoc@hotmail.com
    @Date: 2021-09-15
    @Update-1: 2022-02-10 add non_max_suppression
"""


import numpy as np
import tensorflow.compat.v2 as tf
from worker.ml.helpers import load_label_map
from settings import ml_config


class DetectorTF2(object):
    """Load model with tensorflow version from >= 2.0.0 
        @Param: path_to_model=path to your folder contains tensorflow models
        @Param: path_to_lables=path to file label_map.pbtxt
        @Param: score_threshold=min score of predict
        @param: nms_threshold=iou
        @Param: num_classes=number class of models
        @Param: max_classes_out=max number of box out
        @Response: {load_model} load tensorflow to backgroud system
        @Response: {predict} dict of [num_detections, detection_classes, score_detections] and category_index
    """ 
    
    def __init__(
        self, 
        path_to_model,
        path_to_labels, 
        nms_threshold, 
        score_threshold,
        num_classes,
        max_classes_out,
    ):
        self.path_to_model = path_to_model
        self.path_to_labels = path_to_labels
        self.nms_threshold = nms_threshold
        self.score_threshold = score_threshold
        self.num_classes = num_classes
        self.max_classes_out = max_classes_out
        self.category_index = load_label_map.create_category_index_from_labelmap(
            path_to_labels, use_display_name=True)
        self.path_to_saved_model = self.path_to_model + "/saved_model"
        self.detect_fn = self.load_model()
    
    def load_model(self):
        detect_fn = tf.saved_model.load(self.path_to_saved_model)
        return detect_fn
    
    def predict(self, image):
        # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image_expanded = np.expand_dims(image_rgb, axis=0)

        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis, ...]

        # input_tensor = np.expand_dims(image_np, 0)
        detections = self.detect_fn(input_tensor)

        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                       for key, value in detections.items()}
        detections['num_detections'] = num_detections
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
        
        detection_boxes = detections['detection_boxes']
        detection_classes = detections['detection_classes']
        detection_scores = detections['detection_scores']
        
         # iou, score_min condition
        selected_indices = tf.image.non_max_suppression(
            detection_boxes, 
            detection_scores, 
            max_output_size=self.max_classes_out, 
            iou_threshold=self.nms_threshold, 
            score_threshold=self.score_threshold)
        
        selected_boxes = tf.gather(detection_boxes, selected_indices)
        selected_scores = tf.gather(detection_scores, selected_indices)
        selected_classes = tf.gather(detection_classes, selected_indices)
        
        # make new detection result
        detection_boxes = np.array(selected_boxes)
        detection_classes = np.array(selected_classes)
        detection_scores = np.array(selected_scores)
        detections_new = {}
        detections_new['detection_boxes'] = detection_boxes
        detections_new['detection_classes'] = detection_classes
        detections_new['detection_scores'] = detection_scores
        
        return detections_new, self.category_index



class CompletedModel(object):
    """[summary]
        Complete model object detection with tensorflow >= 2.0
    Args:
        @param: _load_model: load model from tensorflow train
        @param: _detect: put image(np.array) return detection(boxes, score, class), and scategory_index for cover class_id to class_name
    """
    def __init__(self):
        self.model = self._load_model()
        
    @staticmethod
    def _load_model():
        return DetectorTF2(
            path_to_model=ml_config.MODEL_PATH,
            path_to_labels=ml_config.LABLE_PATH,
            nms_threshold=ml_config.NMS_THRESHOLD, 
            score_threshold=ml_config.SCORE_THRESHOLD,
            num_classes=ml_config.NUMBER_CLASSES,
            max_classes_out=ml_config.MAX_CLASS_OUT
        )
    
    def detect(self, image):
        detections, category_index = self.model.predict(image)
        return detections, category_index
