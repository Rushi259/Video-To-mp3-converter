import tkinter as tk
from tkinter import filedialog, messagebox
import moviepy.editor as mp
import os

def upload_file():
    global video_file, video_folder
    video_file = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    if video_file:
        video_folder = os.path.dirname(video_file)
        file_label.config(text=os.path.basename(video_file))

def convert_to_mp3():
    if video_file:
        try:
            video = mp.VideoFileClip(video_file)
            audio = video.audio
            
            # Construct the output file path in the same folder
            mp3_filename = os.path.splitext(os.path.basename(video_file))[0] + ".mp3"
            save_path = os.path.join(video_folder, mp3_filename)
            
            audio.write_audiofile(save_path)
            messagebox.showinfo("Success", f"Conversion Completed! Saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("No File", "Please upload a video file first.")

# Initialize the main window
root = tk.Tk()
root.title("Video to MP3 Converter")

# Set the window size
root.geometry("400x200")
root.configure(bg='black')

# Initialize video file and folder variables
video_file = None
video_folder = None

# Create an upload button
upload_button = tk.Button(root, text="Upload Video", command=upload_file)
upload_button.pack(pady=20)

# Label to show the selected file
file_label = tk.Label(root, text="No file selected", bg='black', fg='white')
file_label.pack()

# Create a convert button
convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack(pady=20)

# Run the application
root.mainloop()
