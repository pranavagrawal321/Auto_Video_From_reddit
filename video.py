import subprocess
import random
from mutagen.mp3 import MP3

video_file = 'videos/video.mp4'
question_mp3 = 'Voiceovers/Questions/1e7i3ig.mp3'
answer_mp3 = 'Voiceovers/Answers/1e7i3ig_le0f5at.mp3'

question_length = MP3(question_mp3).info.length
answer_length = MP3(answer_mp3).info.length
total_length = question_length + answer_length

video_info = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
original_video_duration = float(video_info.stdout.strip())

max_start_time = original_video_duration - total_length
if max_start_time < 0:
    raise ValueError("Combined length of MP3 files exceeds the duration of the original video.")

start_time = random.uniform(0, max_start_time)

speed_factor = 1.25

frame_width = 1280
frame_height = 720

ffmpeg_cmd = [
    'ffmpeg',
    '-ss', str(start_time),
    '-i', video_file,
    '-t', str(total_length),
    '-filter:v', f'setpts={1/speed_factor}*PTS,scale={frame_width}:{frame_height}',
    '-c:v', 'libx264',
    '-crf', '23',
    '-preset', 'fast',
    '-movflags', '+faststart',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-threads', '0',
    '-strict', 'experimental',
    'trimmed_video.mp4'
]

subprocess.run(ffmpeg_cmd)

print(f"Video trimmed starting from {start_time} seconds for {total_length} seconds at {speed_factor}x speed and resized to {frame_width}x{frame_height}")
