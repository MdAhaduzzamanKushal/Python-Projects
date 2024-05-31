from pytube import YouTube
import webbrowser

# Input the YouTube video URL
video_url = "https://www.youtube.com/watch?v=8iwkiyuN93M"

# Create a YouTube object
yt = YouTube(video_url)

# Get the video title and thumbnail URL
video_title = yt.title
thumbnail_url = yt.thumbnail_url

# Open the video in a web browser
webbrowser.open(yt.streams.first().url)

# Display the video details
print("Playing YouTube video:")
print("Title:", video_title)
print("Thumbnail URL:", thumbnail_url)
