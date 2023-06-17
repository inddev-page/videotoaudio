import moviepy.editor

video = moviepy.editor.VideoFileClip('idcf - Slowed (Remix).mp4')
audio = video.audio

audio.write_audiofile("audio.mp3")