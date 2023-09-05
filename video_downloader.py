from pytube import YouTube


# the function takes the video url as an argument
def video_downloader(video_url):
    # passing the url to the YouTube object
    my_video = YouTube(video_url)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title


# the try statement will run if there are no errors
# try:
#     # getting the url from the user
#     youtube_link = input('Enter the YouTube link:')
#     print(f'Downloading your Video, please wait.......')
#     # passing the url to the function
#     video = video_downloader(youtube_link)
#     # printing the video title
#     print(f'"{video}" downloaded successfully!!')
# #the except will catch ValueError, URLError, RegexMatchError and simalar
# except:
#     print(f'Failed to download video\nThe '\
#           'following might be the causes\n->No internet '\
#           'connection\n->Invalid video link')





