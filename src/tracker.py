import cv2
from ultralytics import YOLO


class ObjectTracker:
    def __init__(self, model_path="models/yolo11n.pt"):
        self.model = YOLO(model_path)

    def track(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )

        return results


if __name__ == "__main__":
    video_path = "data/input/traffic.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    tracker = ObjectTracker()

    print("Starting object tracking...")
    print("Press Q to stop the tracking window.")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = tracker.track(frame)

        annotated_frame = results[0].plot()

        cv2.imshow("VisionCount - Object Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Object tracking completed successfully!")