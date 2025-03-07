import random
import sys
import os

from PyQt5.QtCore import QTimer, Qt, QTime, QUrl
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

#idk what this does mr ai said put  this in for troubleshooting with pysinstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.player = QMediaPlayer()  # mp3 player
        self.normal_geometry = None
        self.current_quote = ""
        self.displayed_text = ""
        self.typing_index = 0
        self.typing_timer = QTimer(self)
        self.initUI()

    def initUI(self):
        halo_quotes = [
            "No, I think we're just getting started.",
            "That's Not Going To Happen.",
            "We'll Make It.",
            "I Need A Weapon.",
            "Sir, Finishing This Fight.",
            "Wake Me When You Need Me.",
            "Our Duty As Soldiers Is To Protect Humanity, Whatever The Cost."
        ]

        # random quote setter
        self.current_quote = random.choice(halo_quotes)
        self.setWindowTitle("")  # Start with empty title
        self.typing_timer.timeout.connect(self.update_title)
        self.typing_timer.start(200)  # every 200ms text updates 1 character.
        self.setWindowIcon(QIcon(resource_path('halo-icon-36667.ico')))
        self.setGeometry(500, 300, 500, 500)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 200px; color: green;")
        self.setStyleSheet("background-color: black;") #i wanted a picture but it didn't work rip

        font_path = resource_path('Halo.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 150)
        self.time_label.setFont(font)

        self.update_time()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.adjustSize()

        audio_path = resource_path('Halo4OST.mp3')
        url = QUrl.fromLocalFile(audio_path)
        self.player.setMedia(QMediaContent(url))
        self.player.setPosition(3500)  # start mp3 from 3.5 sec
        self.player.play()

#this section actually the best since it makes it kinda feel like an actually screensaver with usage i guess
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            if self.isFullScreen():
                self.showNormal()
                if self.normal_geometry:
                    self.setGeometry(self.normal_geometry)
            else:
                self.normal_geometry = self.geometry()
                self.showFullScreen()
        elif event.key() == Qt.Key_R:  # R Key music cancel
            self.player.stop()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

    def update_title(self):
        if self.typing_index < len(self.current_quote):
            self.displayed_text += self.current_quote[self.typing_index]
            self.setWindowTitle(self.displayed_text)
            self.typing_index += 1
        else:
            self.typing_timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon_path = resource_path('halo-icon-36667.ico')
    icon = QIcon(icon_path)
    if icon.isNull():
        print("Icon doesn't work.")
    else:
        print("Icon works.")
        app.setWindowIcon(icon)
        clock = DigitalClock()
        clock.show()
        clock.setWindowIcon(icon)
    sys.exit(app.exec())