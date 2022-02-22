import pygame


class Playlist:
    """A class designed to manage the music playlist."""

    def __init__(self, path):
        """Initialize Playlist content."""

        # Create a list of songs.
        self.songs = [path + 'Factory-On-Mercury.ogg', path + 'Light-Years_v001.ogg', path + 'Steamtech-Mayhem.ogg']
        self.playlist_length = len(self.songs)
        self.current_song = 0

        # Define own event.
        self.next_song_event = pygame.USEREVENT + 1

    def set_next_song(self):
        """Set the next song from the playlist."""

        self.current_song = (self.current_song + 1) % self.playlist_length

    def set_song_end_event(self):
        """Set the song end event."""

        pygame.mixer.music.set_endevent(self.next_song_event)

    def load_song(self):
        """Load the song from the playlist."""

        pygame.mixer.music.load(self.songs[self.current_song])

    @staticmethod
    def play_song():
        """Play the current song from the playlist."""

        pygame.mixer.music.play()

    @staticmethod
    def pause_song():
        """Pause the current song from the playlist."""

        pygame.mixer.music.pause()

    @staticmethod
    def resume_song():
        """Resume the current song from the playlist."""

        pygame.mixer.music.unpause()

    @staticmethod
    def stop_song():
        """Stop playing the current song from the playlist."""

        pygame.mixer.music.stop()
