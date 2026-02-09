#1
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = person("Aydyn",18)
print(p1)

#2
class playlist():
    def __init__(self,name):
        self.name = name
        self.songs = []

    def addsong(self,song):
        self.songs.append(song)
        return f"Added: {song}"

    def removesong(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def showsongs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f" - {song}")

mylist = playlist("Fovourits")
mylist.addsong("Bohemian Rhapsody")
mylist.addsong("Stairway to Heaven")
mylist.showsongs()

#3
class person2():
    def __init__(self,name):
        self.name = name
    def grt(self):
        print(f"Hello {self.name}, how are you today?")
p2 = person2("Aydyn")
del person2.grt()
p2.grt() # will be error
