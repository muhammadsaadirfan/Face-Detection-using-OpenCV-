import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import platform
import os

# Import the VideoStream class
from video_stream import VideoStream

class LockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Security System")
        self.root.geometry("1920x1080")

        if platform.system() == "Windows":
            self.root.state('zoomed')
        else:
            self.root.attributes('-zoomed', True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Canvas for Video
        self.canvas = tk.Canvas(self.root, width=1920, height=1080, bg="black")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        # Buttons
        self.play_video_button = tk.Button(self.root, text="Play Video", command=self.play_video, bg="green", fg="white")
        self.play_video_button.place(relx=0.4, rely=0.9, anchor="center")

        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings, bg="gray", fg="white")
        self.settings_button.place(relx=0.6, rely=0.9, anchor="center")

        # Video Stream Object
        self.video_stream = VideoStream()
        self.photo_image = None

    def play_video(self):
        """Play a video file on the canvas."""
        video_path = "/home/muhammad/Books/3rd_semester/CP_Manuals/project/gui/video/l.mp4"  # Replace with your video path
        try:
            self.video_stream.start_video(video_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.video_stream.video_running = True
        self.update_video_frame()

    def update_video_frame(self):
        """Fetch and display the next video frame."""
        if self.video_stream.video_running and self.video_stream.is_opened():
            frame = self.video_stream.get_frame()
            if frame is not None:
                rgb_frame = self.video_stream.convert_to_rgb(frame)
                image = Image.fromarray(rgb_frame)
                image = image.resize((1920, 1080), Image.Resampling.LANCZOS)
                self.photo_image = ImageTk.PhotoImage(image=image)
                self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
                self.root.after(10, self.update_video_frame)
            else:
                # End of video
                self.video_stream.video_running = False
                self.video_stream.release()
                messagebox.showinfo("Info", "Video playback finished.")

    def open_settings(self):
        """Open password-protected settings."""
        password = simpledialog.askstring("Password", "Enter password:", show='*')
        if password == "admin123":
            self.open_access_manager()
        else:
            messagebox.showerror("Access Denied", "Incorrect password!")

    def open_access_manager(self):
        """Manage user access."""
        access_window = tk.Toplevel(self.root)
        access_window.title("Manage Access")
        access_window.geometry("400x300")

        add_button = tk.Button(access_window, text="Add Access", command=self.add_access, bg="green", fg="white")
        add_button.pack(pady=20)

        remove_button = tk.Button(access_window, text="Remove Access", command=self.remove_access, bg="red", fg="white")
        remove_button.pack(pady=20)

    def add_access(self):
        """Add user access by capturing an image."""
        user_name = simpledialog.askstring("Add User", "Enter user name:")
        if user_name:
            save_path = f"/home/muhammad/Books/3rd_semester/CP_Manuals/project/authorized_faces/{user_name}.png"
            try:
                self.video_stream.start_camera()
                frame = self.video_stream.get_frame()
                if frame is not None:
                    rgb_frame = self.video_stream.convert_to_rgb(frame)
                    image = Image.fromarray(rgb_frame)
                    image.save(save_path)
                    messagebox.showinfo("Success", f"Image saved as '{user_name}.png'")
                else:
                    messagebox.showerror("Error", "Failed to capture image from camera!")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                self.video_stream.release()

    def remove_access(self):
        """Remove user access by deleting a file."""
        user_name = simpledialog.askstring("Remove User", "Enter user name to remove:")
        if user_name:
            file_path = f"/home/muhammad/Books/3rd_semester/CP_Manuals/project/authorized_faces/{user_name}.png"
            if os.path.exists(file_path):
                os.remove(file_path)
                messagebox.showinfo("Success", f"User '{user_name}' removed successfully!")
            else:
                messagebox.showerror("Error", f"User '{user_name}' not found!")

    def on_close(self):
        """Handle window close event."""
        self.video_stream.release()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = LockGUI(root)
    root.mainloop()
