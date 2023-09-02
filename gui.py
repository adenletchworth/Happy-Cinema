import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import web_scraper
import language_processing

class CustomGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Happy Cinema')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Do you want to base your recommendation on a current movie?')
        self.layout.addWidget(self.label)

        self.button_yes = QPushButton('Yes')
        self.button_yes.clicked.connect(self.on_yes_clicked)
        self.layout.addWidget(self.button_yes)

        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.on_no_clicked)
        self.layout.addWidget(self.button_no)

        self.setLayout(self.layout)

    def on_yes_clicked(self):
        self.label.setText('Search for a current movie using exact title:')
        self.layout.removeWidget(self.button_yes)
        self.layout.removeWidget(self.button_no)
        self.button_yes.deleteLater()
        self.button_no.deleteLater()

        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.button_submit = QPushButton('Submit')
        self.button_submit.clicked.connect(self.on_submit_clicked)
        self.layout.addWidget(self.button_submit)

    def on_no_clicked(self):
        self.label.setText('Enter Description and Genre for your desired movie:')
        self.layout.removeWidget(self.button_yes)
        self.layout.removeWidget(self.button_no)
        self.button_yes.deleteLater()
        self.button_no.deleteLater()

        self.textbox1 = QLineEdit()
        self.layout.addWidget(self.textbox1)

        self.textbox2 = QLineEdit()
        self.layout.addWidget(self.textbox2)

        self.button_submit = QPushButton('Submit')
        self.button_submit.clicked.connect(self.on_submit_no_clicked)
        self.layout.addWidget(self.button_submit)

    def on_submit_clicked(self):
        user_text = self.textbox.text()
        guess_title = web_scraper.UrlPredictor(user_text)
        movie_finder = web_scraper.MovieScraper(guess_title)
        movie_finder.find_movie_attributes()
    
        if movie_finder.movie_attributes == {}:
            self.label.setText('Movie Not Found, Try Again (Try using Movie Year i.e Oppenheimer 2023)')
        else:      
            recommendations = language_processing.processInput(
            movie_finder.movie_attributes['Description'],
            movie_finder.movie_attributes['Genre']
            )


            while self.layout.count():
                item = self.layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()


            labels = ['Title', 'Description','Genre']
            count = 0
            for recommendation in recommendations:
                label = labels[count]
                count+=1
                recommendation_label = QLabel(f'{label}: {recommendation}')
                recommendation_label.setWordWrap(True)
                self.layout.addWidget(recommendation_label)

            self.setLayout(self.layout)


    def on_submit_no_clicked(self):
        user_text1 = self.textbox1.text()
        user_text2 = self.textbox2.text()

        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        recommendations = language_processing.processInput(user_text1,user_text2)
        labels = ['Title', 'Description','Genre']
        count = 0
        for recommendation in recommendations:
            label = labels[count]
            count+=1
            recommendation_label = QLabel(f'{label}: {recommendation}')
            recommendation_label.setWordWrap(True)
            self.layout.addWidget(recommendation_label)
        self.textbox1.deleteLater()
        self.textbox2.deleteLater()
        self.button_submit.deleteLater()

def main():
    app = QApplication(sys.argv)
    gui = CustomGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
