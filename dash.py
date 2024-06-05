# Importing all the required Libraries
from ultralytics import YOLO
import supervision as sv
import numpy as np

np.bool = np.bool_


class Dash:
    def __init__(self, path):
        self.path = path
        self.video_info = sv.VideoInfo.from_video_path(self.path)
        self.model = YOLO("yolov8n.pt")  # loading the model
        self.selected_classes = [0, 1, 2, 3, 5, 7]  # classes to be predicted
        # 0: person, 1:bicycle , 2:car, 3:motorcycle, 5:bus, 7:truck
        x = [sv.Color(r=255, g=0, b=0), sv.Color(r=255, g=255, b=0), sv.Color(r=0, g=255, b=0), sv.Color(r=0, g=0, b=225), sv.Color(r=0, g=0, b=225)]
        scale = 3  # scale for matching the video resolution
        self.polygons = [
            scale * np.array([
                [460, 450],
                [740, 450],
                [900, 550],
                [300, 550]
            ], np.int32),
            scale * np.array([
                [530, 373],
                [670, 373],
                [740, 447],
                [460, 447]
            ], np.int32),
            scale * np.array([
                [570, 330],
                [630, 330],
                [670, 370],
                [530, 370]
            ], np.int32),
            scale * np.array([
                [670, 373],
                [905, 373],
                [1200, 550],
                [905, 550]
            ], np.int32),
            scale * np.array([
                [295, 373],
                [530, 373],
                [295, 550],
                [0, 550]
            ], np.int32)
        ]
        self.zones = [
            sv.PolygonZone(
                polygon=polygon,
                frame_resolution_wh=self.video_info.resolution_wh
            )
            for polygon
            in self.polygons
        ]
        self.zone_annotators = [
            sv.PolygonZoneAnnotator(
                zone=zone,
                color=x[index],
                thickness=2,
                text_thickness=2,
                text_scale=2,
                text_padding=0
            )
            for index, zone
            in enumerate(self.zones)
        ]
        self.box_annotators = [
            sv.BoxAnnotator(
                color=x[index],
                thickness=2,
                text_thickness=2,
                text_scale=1,
                text_padding=0

            )
            for index
            in range(len(self.polygons))
        ]

    def dash_detect(self, frame):
        results = self.model(frame, imgsz=1280)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = detections[np.isin(detections.class_id, self.selected_classes)]
        detections = detections[detections.confidence > 0.5]

        level = 0
        close = False
        mod = False
        far = False
        for i in range(len(self.polygons)):
            mask = self.zones[i].trigger(detections=detections)
            detections_filtered = detections[mask]
            labels = []
            for detection in detections_filtered:
                _, _, confidence, class_id, _, _ = detection
                class_name = self.model.names[class_id]
                label = f"{class_name} {confidence:0.2f}"
                labels.append(label)
            if len(labels):
                if i == 0:
                    close = True
                if i == 1:
                    mod = True
                if i == 2:
                    far = True

            frame = self.box_annotators[i].annotate(scene=frame, detections=detections_filtered, labels=labels)
            frame = self.zone_annotators[i].annotate(scene=frame)

        return frame, close, mod, far
