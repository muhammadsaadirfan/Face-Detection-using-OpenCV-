# import cv2
# import os

# class VideoStream:
#     def __init__(self, source=0):
#         """Initialize video stream."""
#         self.camera = cv2.VideoCapture(0)
#         self.source = source
#         self.cap = None
#         self.video_running = False

#     def start_camera(self):
#         """Start camera stream."""
#         self.cap = cv2.VideoCapture(self.source)
#         if not self.cap.isOpened():
#             raise Exception("Failed to initialize camera/video stream!")

#     def start_video(self, video_path):
#         """Start a video file stream."""
#         if not os.path.exists(video_path):
#             raise FileNotFoundError(f"Video file not found: {video_path}")
#         self.cap = cv2.VideoCapture(video_path)
#         if not self.cap.isOpened():
#             raise Exception("Failed to open video file!")


#     def convert_to_rgb(self, frame):
#         """Convert a BGR frame to RGB."""
#         return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


#     def is_opened(self):
#         """Check if the stream is open."""
#         return self.cap and self.cap.isOpened()
    



#     def get_frame(self):
#         """Get the current frame from the stream (camera or video file)."""
#         if self.cap and self.cap.isOpened():  # If a video source (camera or file) is open
#             ret, frame = self.cap.read()
#             if ret:
#                 return frame
#         elif self.camera and self.camera.isOpened():  # If camera is initialized
#             ret, frame = self.camera.read()
#             if not ret:
#                 raise Exception("Unable to capture video from camera.")
#             return frame
#         return None


#     def show_frame(self):
#         while True:
#             frame = self.get_frame()
#             cv2.imshow("Camera Feed", frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         self.release()  # Ensure the camera is released after exiting the loop
#         cv2.destroyAllWindows()


#     def release(self):
#         self.camera.release()
#         if self.cap:
#             self.cap.release()
#             self.cap = None

# if __name__ == "__main__":
#     stream = VideoStream()
#     stream.show_frame()