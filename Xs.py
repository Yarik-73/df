from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QRadioButton, QMessageBox

app = QApplication([])
win = QWidget()

win.setWindowTitle('')
win.resize(400, 200)
win.move(100, 100)

question = QLabel(win)
question.setText('В якому році канал отримав золоту кнопку від YouTube?')
question.move(50, 10)

btn_ans1=QRadioButton(win)
btn_ans1.setText('2005')
btn_ans1.move(100, 60)
btn_ans2 = QRadioButton(win)
btn_ans2.setText('2010')
btn_ans2.move(200, 60)
btn_ans3 = QRadioButton(win)
btn_ans3.setText('2015')
btn_ans3.move(100, 120)
btn_ans4 = QRadioButton(win)
btn_ans4.setText('2020')
btn_ans4.move(200, 120)
def show_win():
    box = QMessageBox()
    box.setText('Правильно!')
    box.exec_()
def show_lose():
    box = QMessageBox()
    box.setText('Неправильно!')
    box.exec_()
btn_ans3.clicked.connect(show_win)
btn_ans1.clicked.connect(show_lose)
btn_ans2.clicked.connect(show_lose)
btn_ans4.clicked.connect(show_lose)
win.show()
app.exec()
