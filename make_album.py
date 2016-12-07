def make_album(artist_name, album_title, number_tracks = ''):
    if number_tracks:
        album = {'artist_name':artist_name, 'album_title':album_title, 'number_tracks':number_tracks}
    else:
        album = {'artist_name':artist_name, 'album_title':album_title}
    return album

while True:
    artist_name = input("Enter artist name: ")
    if artist_name == 'q':
        break
    album_name = input("Enter album name: ")
    if album_name == 'q':
        break
    album = make_album(artist_name, album_name)
    print(album)
