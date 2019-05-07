from appJar import gui
import webbrowser

app = gui()
app.addLabel("title", "Yeet")
app.setLabelBg("title", "pink")
app.setFullscreen("title")
destBut = "---Destiny---"
auraBut = "---Aura---"


def press(button):
    auraurl = "https://www.youtube.com/channel/UCBC-H182liKJyjet_2NeMsQ/videos"
    desturl = "https://www.youtube.com/user/destiny/videos"
    if button == destBut:
        webbrowser.open(desturl, 0)
    if button == auraBut:
        webbrowser.open(auraurl, 0)
    app.stop()


app.addButtons([auraBut, destBut], press)
app.go()
