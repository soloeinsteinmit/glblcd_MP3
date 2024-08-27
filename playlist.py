from MP3_Playlist import MP3_Playlist

# prompt = input("""
# Do you want to Create or Load a playlist
# Press 'l' to load playlist from file or
# Press 'c' to creat a new playlist
# -> """)
prompt = 'l'
if prompt.lower() == 'l':
    playlist_path = 'playlists/playlist2.txt'
    playlist1 = MP3_Playlist()

    playlist1.load_playlist(path_to_file=playlist_path)
    
    # print(playlist1.total_tracks_in_playlist())
    playlist1.display_tracks()
    print("\n\n")
   
    
    playlist1.add_track_to_playlist("Tokyo Moonlight", "Boston Nights", "My Califonia Days", "Not by Might")
    playlist1.display_tracks()
    
    # print(playlist1.total_duration_of_playlist())
elif prompt.lower() == 'c':
    pass
else:
    print("Invalid command")
