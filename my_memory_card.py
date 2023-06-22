#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QButtonGroup, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer 
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Hачиональная xижина якутов', 'Урасa', 'Opта', 'Mглу', 'Xатa'))

app = QApplication([])

'''Интерфейс приложение Memory Card'''
window = QWidget()
window.setWindowTitle('Memo Card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году был основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox  = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
AnsGroupBox.setLayout(layout_res)

ResultGroupBox = QGroupBox('Резльтат тестирования')
lb_Result_test = QLabel('')
layout_res_test = QVBoxLayout()
layout_res_test.addWidget(lb_Result_test, alignment=Qt.AlignCenter)
ResultGroupBox.setLayout(layout_res_test)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(ResultGroupBox)
AnsGroupBox.hide()
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий Вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    '''функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кно
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - Неверн
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ
    show_question() # показываем панель вопросов

def show_correct(res):
    '''показать результат - установим переданный текст в надпись ''результат'' и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        window.points += 1
        window.questions += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            window.questions +=1
            show_correct('Неверно!')

def next_question():
    '''задает следующий вопрос из списка'''
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        btn_OK.setText('Завершить Тест') # если список вопросов закончился идем сначал
        lb_Question.setText('Тест завершен')
    else:
        q = questions_list[window.cur_question] # взяли вопрос
        ask(q) # cnpocunu

def result_test():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResultGroupBox.show()
    lb_Result_test.setText('Вы набрали: '+ str(window.points)+ ' из '+ str(window.questions))


def test():
    '''временная фунция, которая позволяет нажатием на кнопку'''
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Завершить Тест':
        result_test()
    else:
        next_question()




window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.cur_question = -1
window.points = 0
window.questions = 0

btn_OK.clicked.connect(test)


next_question()
window.resize(400, 300)
window.setLayout(layout_card)
window.show()
app.exec()