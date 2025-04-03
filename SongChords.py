from bs4 import BeautifulSoup
import urllib.request
import ssl

class KeyChords:
    def __init__(self, Key, Chord):
        self.Key = Key
        self.Chord = Chord
    def num(self):
        match self.Key:
            case "C":
                return ["C", "Dm", "Em", "F", "G", "Am", "B" + chr(176)].index(self.Chord)
            case "C#":
                return ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#" + chr(176)].index(self.Chord)
            case "Db":
                return ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C" + chr(176)].index(self.Chord)
            case "D":
                return ["D", "Em", "F#m", "G", "A", "Bm", "C#" + chr(176)].index(self.Chord)
            case "Eb":
                return ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "D" + chr(176)].index(self.Chord)
            case "E":
                return ["E", "F#m", "G#m", "A", "B", "C#m", "D#" + chr(176)].index(self.Chord)
            case "F":
                return ["F", "Gm", "Am", "Bb", "C", "Dm", "E" + chr(176)].index(self.Chord)
            case "F#":
                return ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#" + chr(176)].index(self.Chord)
            case "Gb":
                return ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "F" + chr(176)].index(self.Chord)
            case "G":
                return ["G", "Am", "Bm", "C", "D", "Em", "F#" + chr(176)].index(self.Chord)
            case "Ab":
                return ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "G" + chr(176)].index(self.Chord)
            case "A":
                return ["A", "Bm", "C#m", "D", "E", "F#m", "G#" + chr(176)].index(self.Chord)
            case "Bb":
                return ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "A" + chr(176)].index(self.Chord)
            case "B":
                return ["B", "C#m", "D#m", "E", "F#", "G#m", "A#" + chr(176)].index(self.Chord)
    def __str__(self):
        return str(self.num())

context = ssl._create_unverified_context()
song = input("Part Song URL: ")
page = urllib.request.urlopen(f"https://www.worshiptogether.com/songs/{song}/#SongChords", context=context)
p = BeautifulSoup(page.read(), features="html.parser")
key = p.head.find("meta", attrs={"property":"cludo:originalKey"})["content"]
music = p.body.find("div", {"class":"chord-pro-disp"}).find_all(lambda tag: tag.name == "div" and tag.has_attr("class"))
lyrics = []
for i in enumerate(music):
    if "\n" not in i[1].text:
        lyrics += [i[1].text]
lyrics = "\n".join(lyrics).replace("\xa0", "").split("\n")
chords = {"verse":[], "verse 1":[], "verse 2":[], "verse 3":[], "verse 4":[], "chorus":[], "chorus 1":[], "chorus 2":[], "chorus 3":[], "chorus 4":[], "bridge":[], "tag":[], "garbage":[]}
s = ""
for i in lyrics:
    if i == "":
        continue
    if i.strip().lower() in chords:
        s = i.strip().lower()
        continue
    if "repeat" in i.lower() or i.strip().lower() == "intro" or "(" in i:
        s = "garbage"
        continue
    chords[s] += [i]
del chords["garbage"]
ch = {}
for i in chords:
    ch[i] = ""
    spaces = 0
    for o in chords[i]:
        try:
            for l in range(10):
                o = o.replace(str(l), "")
            k = KeyChords(key, o.replace(" ", "/").split("/")[0])
            ch[i] += "," * spaces + str(k) + ","
            spaces = -1
        except ValueError:
            while "  " in o:
                o = o.replace("  ", " ")
            spaces += o.count(" ")
for i in ch:
    print(i + ":", ch[i])
