
import cv2
from pathlib import Path
from ultralytics import YOLO

# Project folders
BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "videos"
OUTPUT_DIR = BASE_DIR / "output"

VIDEO_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Load the YOLO object detection model
model = YOLO("yolo11n.pt")


def main():
    print("\n=== OBJECT DETECTION AND TRACKING ===")
    print("1. Use webcam")
    print("2. Use a recorded video")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        source = 0

    elif choice == "2":
        filename = input(
            "Enter the video filename inside the videos folder: "
        ).strip()

        video_path = VIDEO_DIR / filename

        if not video_path.is_file():
            print(f"Video not found: {video_path}")
            return

        source = str(video_path)

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Could not open the webcam or video.")
        return

    writer = None
    output_path = OUTPUT_DIR / "tracked_output.mp4"
    frames_processed = 0

    print("\nDetection and tracking started!")
    print("Press Q in the video window to stop.")

    try:
        while True:
            success, frame = cap.read()

            if not success:
                break

            results = model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                conf=0.35,
                device="cpu",
                verbose=False
            )

            annotated_frame = results[0].plot()

            # Create the output video when the first frame is available
            if writer is None:
                height, width = annotated_frame.shape[:2]

                fps = cap.get(cv2.CAP_PROP_FPS)

                if fps <= 0 or fps > 120:
                    fps = 25.0

                fourcc = cv2.VideoWriter_fourcc(*"mp4v")

                writer = cv2.VideoWriter(
                    str(output_path),
                    fourcc,
                    fps,
                    (width, height)
                )

                if not writer.isOpened():
                    print("Error: Could not create the output video.")
                    writer.release()
                    writer = None
                    break

            writer.write(annotated_frame)
            frames_processed += 1

            cv2.imshow(
                "CodeAlpha - Object Detection and Tracking",
                annotated_frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()

        if writer is not None:
            writer.release()

        cv2.destroyAllWindows()

    if frames_processed > 0:
        print(f"\nFrames processed: {frames_processed}")
        print(f"Processed video saved to: {output_path}")
    else:
        print("No video frames were processed.")

    print("Project stopped.")


if __name__ == "__main__":
    main()
