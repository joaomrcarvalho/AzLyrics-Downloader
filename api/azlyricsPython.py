from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse, time


def getAndProcessArtistsPage(artists):
    for currentArtist in artists.split("*"):
        currentArtist = currentArtist.lower().replace(" ", "")
        firstLetter = currentArtist[:1]
        generate_url = 'http://azlyrics.com/' + firstLetter + '/' + currentArtist + ".html"
        alternativeProcessing(generate_url, currentArtist, save=True)


def generating(artist, title, save):
    artist = artist.lower().replace(" ", "")
    title = title.lower().replace(" ", "")
    generate_url = 'http://azlyrics.com/lyrics/' + artist + '/' + title + '.html'
    processSong(generate_url, artist, title, save)


def alternativeProcessing(generate_url, artist, save):
    print("generating url: " + generate_url)
    response = urllib.request.urlopen(generate_url)
    read_artist_page = response.read()
    soup = BeautifulSoup(read_artist_page).find_all("a")
    i = 0
    for x in soup:
        i = i + 1
        completeLink = x.extract()
        stringToCompare = '<a href="../lyrics/' + artist
        if completeLink.decode().startswith(stringToCompare):
            sep = '/'
            currentSongName = completeLink.decode().split(sep, 3)[3]
            sep = '.html'
            currentSongName = currentSongName.split(sep, 1)[0]
            print("processing " + artist + "'s song " + currentSongName + "...")
            generating(artist, currentSongName, save)


def processSong(generate_url, artist, title, save):
    response = urllib.request.urlopen(generate_url)
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics)
    lyrics = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [x.getText() for x in lyrics]
    printing(artist, title, save, lyrics)


def printing(artist, title, save, lyrics):
    for x in lyrics:
        print(x)
    if save:
        saving(artist, title, lyrics)
    else:
        pass


def saving(artist, title, lyrics):
    f = open(artist + '_' + title + '.txt', 'w')
    f.write("\n".join(lyrics).strip())
    f.close()
    time.sleep(15) #in order to avoid being disconnected from the server
