import face_recognition
from video_stream import VideoStream
import numpy as np

class FaceEncoder:
    def __init__(self):
        self.video_stream = VideoStream()

    def get_face_encodings(self):
        frame = self.video_stream.get_frame()
        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            return None
        encodings = face_recognition.face_encodings(frame, face_locations)
        return encodings

    def release(self):
        self.video_stream.release()

if __name__ == "__main__":

    encoder = FaceEncoder()
    np.list1=encoder.get_face_encodings()
    print(np.list1)
    