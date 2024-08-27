from functools import reduce
import humanize
from datetime import timedelta
import random
class MP3_Playlist:
    
    def __init__(self):
        
        # Stores playlist in an array of tuples
        # Data is organised in the form [(trackName(string), duration(int))]
        self.array_tuple_playlist = []
        self.playlist_name = 'default name'
        self.is_playlist_empty = isPlaylistEmpty(self.array_tuple_playlist)
         

     
    def name_of_playlist(self):
        """
        Returns name of playlist
        """ 
        return self.playlist_name + " " + "Playlist"
    
    
    def load_playlist(self, path_to_file):
        '''
        takes @path_to_file and returns an array tuple of the playlist 
        '''
        # self.playlist_name = input("Give your playlist a name: ")
        try:
            with open(f'{path_to_file}', 'r') as file:
                playlist = file.read()
            
            
            playlist = playlist.split('\n')
            for track in playlist:
                track = track.split(',')
                self.array_tuple_playlist.append(tuple(track)) 
                
            # assert playlist is not not empty 
            self.is_playlist_empty = False
            
            return self.array_tuple_playlist
        
        except FileNotFoundError:
            print("The file was not found.")
        except IOError:
            print("An I/O error occurred.")

    
    def display_tracks(self):
        if self.is_playlist_empty:
            return f"You do not have any playlist yet"
        print(f"{self.playlist_name} playlist")
        counter = 0
        for track in self.array_tuple_playlist:
            trackName, duration = track
            # TODO: work on optimizing convert_seconds fucntion
            duration = int(duration)
            hours, minutes, seconds = convert_seconds(duration)
            counter += 1
            print(f"{counter}. {trackName} -> {minutes:02}:{seconds:02}")
        
        
    # TODO: work on this method of tracks to take multiple tracks at a time
    def add_track_to_playlist(self, *tracks):
        # track_name = input("Enter track name: ")
        for track in tracks: 
            self.array_tuple_playlist.append((track, get_track_duration()))
            
        print(f"{tracks} has been added to playlist\n")
    
    def remove_track_from_playlist(self, track_name):
        # track_name = input("Enter name of track you want to remove from playlist: ")
        
        self.array_tuple_playlist = [track for track in self.array_tuple_playlist if track[0].lower() != track_name.lower()]
        print(f"{track_name} has been removed to playlist\n")
        
    
    def find_track(self):
        pass
    
    def total_tracks_in_playlist(self):
        '''
        Returns the total number of tracks in the playlist
        '''
        if self.is_playlist_empty:
        # if len(self.add_track_to_playlist) == 0:
            return f"{self.playlist_name} playlist is empty"
        return f'{self.playlist_name} playlist has {len(self.array_tuple_playlist)} tracks'
    
    def total_duration_of_playlist(self):
        '''
        Returns the total duration of the playlist
        '''
        if self.is_playlist_empty:
        # if len(self.add_track_to_playlist) == 0:
            return f"{self.playlist_name} playlist is empty"
        
        # Use reduce to sum up the durations
        duration = reduce(lambda total_duration, item: total_duration + int(item[1]), self.array_tuple_playlist, 0)
        hours, minutes, seconds = convert_seconds(duration)
        return f'Total duration of {self.playlist_name} playlist is {hours:02}:{minutes:02}:{seconds:02}'
    
    def create_playlist(self):
        pass
    
    def clear_playlist(self):
        if self.is_playlist_empty and self.playlist_name == 'default name':
            return 'You do not have any playlist yet'
        elif self.is_playlist_empty:
            return f"{self.playlist_name} playlist is empty"
        
        self.array_tuple_playlist.clear()
        return "Playlist is cleared"
    

def isPlaylistEmpty(playlist):
    '''
    Takes the playlist as an arguement and retuns <b>True</b> if playlist is empty
    <br/>
    Else returns <b>False</b>
    '''
    return True if len(playlist) == 0 else False
    
def get_duration(track):
    return track[1]

def convert_seconds(seconds):
    delta = timedelta(seconds=seconds)
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return delta.days * 24 + hours, minutes, seconds

def humanize_duration(seconds):
    return humanize.naturaldelta(timedelta(seconds=seconds))

def get_track_duration():
    return random.randint(150, 250)