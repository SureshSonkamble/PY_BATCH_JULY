from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=x1ke0XViWcA&list=PL0zysOflRCemMnjIOHivEpZGDXFYyINnO')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
print(playlist.owner)

for video in playlist.videos:
    video.streams.first().download()

'''from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=x1ke0XViWcA&list=PL0zysOflRCemMnjIOHivEpZGDXFYyINnO')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
playlist.download_all()'''


