import cv2


def open_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    return cap


def get_video_info(cap):
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = frame_count / fps if fps > 0 else 0

    return {
        "fps": fps,
        "frame_count": frame_count,
        "width": width,
        "height": height,
        "duration": duration,
    }


if __name__ == "__main__":
    video_path = "data/input/traffic.mp4"

    cap = open_video(video_path)
    info = get_video_info(cap)

    print("Video opened successfully!")
    print(f"Resolution: {info['width']} x {info['height']}")
    print(f"FPS: {info['fps']:.2f}")
    print(f"Total frames: {info['frame_count']}")
    print(f"Duration: {info['duration']:.2f} seconds")

    ret, frame = cap.read()

    if ret:
        print("First frame read successfully!")
        print(f"Frame shape: {frame.shape}")
    else:
        print("Could not read the first frame.")

    cap.release()