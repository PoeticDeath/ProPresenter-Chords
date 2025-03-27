import os
import json
import tkinter as tk
import urllib.request
from time import sleep
import tkinter.font as ft

x = 3840
y = 1150
maxsize = size = 300
fontf = "Futura Condensed Medium"

root = tk.Tk()
root.config(bg = "systemTransparent")
root.wm_attributes("-transparent", 1)
root.overrideredirect(1)
root.wm_attributes("-topmost", 1)

font = ft.Font(font = (fontf, size))

T = tk.Text(root)
T.config(bg = "systemTransparent", fg = "white", font = (fontf, size), borderwidth = 0, highlightthickness = 0, wrap = "none", state = "disabled")
T.pack()
T.place(x = 0, y = 0, width = x, height = y)
T.tag_config("Just", justify = "left")

root.geometry(f"{x}x{y}+1920+0")

class KeyChords:
    def __init__(self, Key, Chord):
        self.Key = Key
        self.Chord = int(Chord)
    def add(self):
        match self.Key:
            case "C":
                match self.Chord:
                    case 0:
                        return "C"
                    case 1:
                        return "Dm"
                    case 2:
                        return "Em"
                    case 3:
                        return "F"
                    case 4:
                        return "G"
                    case 5:
                        return "Am"
                    case 6:
                        return "B" + chr(176)
            case "C#":
                match self.Chord:
                    case 0:
                        return "C#"
                    case 1:
                        return "D#m"
                    case 2:
                        return "E#m"
                    case 3:
                        return "F#"
                    case 4:
                        return "G#"
                    case 5:
                        return "A#m"
                    case 6:
                        return "B#" + chr(176)
            case "Db":
                match self.Chord:
                    case 0:
                        return "D" + chr(254)
                    case 1:
                        return "E" + chr(254) + "m"
                    case 2:
                        return "Fm"
                    case 3:
                        return "G" + chr(254)
                    case 4:
                        return "A" + chr(254)
                    case 5:
                        return "B" + chr(254) + "m"
                    case 6:
                        return "C" + chr(176)
            case "D":
                match self.Chord:
                    case 0:
                        return "D"
                    case 1:
                        return "Em"
                    case 2:
                        return "F#m"
                    case 3:
                        return "G"
                    case 4:
                        return "A"
                    case 5:
                        return "Bm"
                    case 6:
                        return "C#" + chr(176)
            case "Eb":
                match self.Chord:
                    case 0:
                        return "E" + chr(254)
                    case 1:
                        return "Fm"
                    case 2:
                        return "Gm"
                    case 3:
                        return "A" + chr(254)
                    case 4:
                        return "B" + chr(254)
                    case 5:
                        return "Cm"
                    case 6:
                        return "D" + chr(176)
            case "E":
                match self.Chord:
                    case 0:
                        return "E"
                    case 1:
                        return "F#m"
                    case 2:
                        return "G#m"
                    case 3:
                        return "A"
                    case 4:
                        return "B"
                    case 5:
                        return "C#m"
                    case 6:
                        return "D#" + chr(176)
            case "F":
                match self.Chord:
                    case 0:
                        return "F"
                    case 1:
                        return "Gm"
                    case 2:
                        return "Am"
                    case 3:
                        return "B" + chr(254)
                    case 4:
                        return "C"
                    case 5:
                        return "Dm"
                    case 6:
                        return "E" + chr(176)
            case "F#":
                match self.Chord:
                    case 0:
                        return "F#"
                    case 1:
                        return "G#m"
                    case 2:
                        return "A#m"
                    case 3:
                        return "B"
                    case 4:
                        return "C#"
                    case 5:
                        return "D#m"
                    case 6:
                        return "E#" + chr(176)
            case "Gb":
                match self.Chord:
                    case 0:
                        return "G" + chr(254)
                    case 1:
                        return "A" + chr(254) + "m"
                    case 2:
                        return "B" + chr(254) + "m"
                    case 3:
                        return "C" + chr(254)
                    case 4:
                        return "D" + chr(254)
                    case 5:
                        return "E" + chr(254) + "m"
                    case 6:
                        return "F" + chr(176)
            case "G":
                match self.Chord:
                    case 0:
                        return "G"
                    case 1:
                        return "Am"
                    case 2:
                        return "Bm"
                    case 3:
                        return "C"
                    case 4:
                        return "D"
                    case 5:
                        return "Em"
                    case 6:
                        return "F#" + chr(176)
            case "Ab":
                match self.Chord:
                    case 0:
                        return "A" + chr(254)
                    case 1:
                        return "B" + chr(254) + "m"
                    case 2:
                        return "Cm"
                    case 3:
                        return "D" + chr(254)
                    case 4:
                        return "E" + chr(254)
                    case 5:
                        return "Fm"
                    case 6:
                        return "G" + chr(176)
            case "A":
                match self.Chord:
                    case 0:
                        return "A"
                    case 1:
                        return "Bm"
                    case 2:
                        return "C#m"
                    case 3:
                        return "D"
                    case 4:
                        return "E"
                    case 5:
                        return "F#m"
                    case 6:
                        return "G#" + chr(176)
            case "Bb":
                match self.Chord:
                    case 0:
                        return "B" + chr(254)
                    case 1:
                        return "Cm"
                    case 2:
                        return "Dm"
                    case 3:
                        return "E" + chr(254)
                    case 4:
                        return "F"
                    case 5:
                        return "Gm"
                    case 6:
                        return "A" + chr(176)
            case "B":
                match self.Chord:
                    case 0:
                        return "B"
                    case 1:
                        return "C#m"
                    case 2:
                        return "D#m"
                    case 3:
                        return "E"
                    case 4:
                        return "F#"
                    case 5:
                        return "G#m"
                    case 6:
                        return "A#" + chr(176)
    def __str__(self):
        return self.add() + "-" + str(self.Chord + 1)

while True:
    try:
        laststring = ""
        while True:
            size = maxsize
            font = ft.Font(font = (fontf, size))
            contents = json.loads(urllib.request.urlopen("http://127.0.0.1:1025/v1/presentation/active").read())
            slides = []
            SongName = contents["presentation"]["presentation_path"].split("/")[-1][:-4]
            ChordsPath = "/Users/harvestcommunitychurch/Documents/Chords/"
            Songs = os.listdir(ChordsPath)
            empty = True
            for i in Songs:
                if i.startswith(SongName):
                    empty = False
                    Song = i
            if empty:
                laststring = string = ""
                root.wm_attributes("-transparent", 0)
                T.config(state = "normal")
                T.delete("1.0", tk.END)
                T.config(state = "disabled")
                T.config(bg = "systemTransparent")
                root.wm_attributes("-transparent", 1)
                root.update()
                sleep(0.1)
                continue
            for i in contents["presentation"]["groups"]:
                for p in i["slides"]:
                    slides += [p["text"]]
            slideindex = json.loads(urllib.request.urlopen("http://127.0.0.1:1025/v1/presentation/slide_index").read())
            string = slides[slideindex["presentation_index"]["index"]].replace("\n", " \n")
            if string == laststring:
                root.update()
                sleep(0.1)
                continue
            laststring = string
            while font.measure(sorted(string.split("\n"), key=len)[-1]) > x:
                size -= 1
                font = ft.Font(font = (fontf, size))
            root.wm_attributes("-transparent", 0)
            T.config(state = "normal")
            T.delete("1.0", tk.END)
            ostring = string.split("\n")
            nstring = []
            Key = Song.split(" ")[-1][:-4]
            Chords = [i.split(",") for i in open(ChordsPath + Song, "r").read().split("\n")[2 * slideindex["presentation_index"]["index"]:]]
            for i in enumerate(ostring):
                tstring = ""
                line = i[1].split(" ")
                for o in enumerate(Chords[i[0]]):
                    oldlen = len(tstring)
                    if o[1] != "":
                        tstring += str(KeyChords(Key, o[1]))
                    try:
                        while font.measure(tstring[oldlen:]) < font.measure(line[o[0]] + " "):
                            tstring += " "
                    except IndexError:
                        tstring += " "
                nstring += [tstring]
                nstring += [i[1]]
            while y / font.metrics("linespace") < len(nstring):
                size -= 1
                font = ft.Font(font = (fontf, size))
            T.config(font = (fontf, size))
            T.insert(tk.END, "\n".join(nstring), "Just")
            T.config(state = "disabled")
            T.config(bg = "black")
            sleep(0.1)
    except Exception as E:
        print(E)
