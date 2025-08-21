import face_recognition
import os

def load_authorized_encodings():
    encodings = []
    authorized_faces_folder = r"/home/muhammad/Books/3rd_semester/CP_Manuals/project/authorized_faces"

    # Check if the folder exists
    if not os.path.exists(authorized_faces_folder):
        os.makedirs(authorized_faces_folder)

    # Loop through all images in the authorized_faces folder
    for filename in os.listdir(authorized_faces_folder):
        image_path = os.path.join(authorized_faces_folder, filename)

        # Skip non-image files
        if not filename.endswith(('.jpg', '.jpeg', '.png')):
            continue

        try:
            # Load image and convert to RGB (necessary for face_recognition)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            # If no faces are found, skip this image
            if len(face_encodings) == 0:
                print(f"No faces detected in {filename}")
                continue

            # Add the first face encoding to the list
            encodings.append(face_encodings[0])
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    return encodings

if __name__ == "__main__":
    encoding = load_authorized_encodings()
    print(encoding)
