import subprocess
video_input_path = 'input.mp4'
img_output_path = 'default_thumb.png'
subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])