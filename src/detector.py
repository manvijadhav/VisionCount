import cv2
from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_path="models/yolo11n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        return results


if __name__ == "__main__":
    video_path = "data/input/traffic.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise ValueError("Could not read the first frame.")

    detector = ObjectDetector()
    results = detector.detect(frame)

    result = results[0]

    # Draw YOLO detections on the frame
    annotated_frame = result.plot()

    # Display the result
    cv2.imshow("VisionCount - YOLO Detection", annotated_frame)

    print("YOLO detection completed successfully!")
    print(f"Total objects detected: {len(result.boxes)}")

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = result.names[class_id]

        print(
            f"Object: {class_name} | "
            f"Confidence: {confidence:.2f}"
        )

    print("\nPress any key in the image window to close it.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()