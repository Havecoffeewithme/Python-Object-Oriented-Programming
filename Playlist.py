
class Playlist:
    def __init__(self, name):
        self.name = name 
        self.songs = []

    def add_songs(self, song):
        self.songs.append(song)
        print(f"added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed:{song}")

    def show_songs(self):
        print(f"Playlist '{self.name}")
        for song in self.songs:
            print(f"- {song}")

    def __add__(self, other):
        return self.name + other.name 
    
    def __len__(self):
        return len(self.songs)

    def __eq__(self, other):
        return self.name == other.name or self.songs == other.songs
        




p1 = Playlist("Momo")
p1.add_songs("dakalo")
p1.add_songs("Morena")
p1.add_songs("lerato")
p1.add_songs("mai mai")
p1.add_songs("Bothata")

p2 = Playlist("momo")
p2.add_songs("dakalo")
p2.add_songs("Morena")
p2.add_songs("lerato")
p2.add_songs("mai mai")

print(p1 == p2)
print(p1 + p2)

print(len(p1))
print(len(p2))


