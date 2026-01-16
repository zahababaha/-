from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

app = QApplication([])

# Главное окно
mw = QWidget()
mw.setWindowTitle('Тест Руфье')
mw.resize(400, 300)

# Экран 1: Описание правил
s1 = QWidget()
l1 = QVBoxLayout()

trs = QLabel('Добро пожаловать в программу по определению состояния здоровья!\n\nДанное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний. \nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд, а потом - за последние 15 секунд первой минуты периода восстановления. \nВажно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
bs = QPushButton('Начать')

l1.addWidget(trs, alignment=Qt.AlignCenter)
l1.addWidget(bs, alignment=Qt.AlignCenter)
s1.setLayout(l1)

# Экран 2: Ввод результатов
s2 = QWidget()
l2 = QVBoxLayout()

text_instruction = QLabel('Введите результаты измерений:')
lH1 = QHBoxLayout()
lH2 = QHBoxLayout()
lH3 = QHBoxLayout()

lp1 = QLabel('Пульс в покое (P1):')
ip1 = QLineEdit()
lH1.addWidget(lp1, alignment=Qt.AlignCenter)
lH1.addWidget(ip1, alignment=Qt.AlignCenter)

lp2 = QLabel('Пульс после нагрузки (P2):')
ip2 = QLineEdit()
lH2.addWidget(lp2, alignment=Qt.AlignCenter)
lH2.addWidget(ip2, alignment=Qt.AlignCenter)

lp3 = QLabel('Пульс после отдыха (P3):')
ip3 = QLineEdit()
lH3.addWidget(lp3, alignment=Qt.AlignCenter)
lH3.addWidget(ip3, alignment=Qt.AlignCenter)

bc = QPushButton('Рассчитать результат')

l2.addWidget(text_instruction, alignment=Qt.AlignCenter)
l2.addLayout(lH1)
l2.addLayout(lH2)
l2.addLayout(lH3)
l2.addWidget(bc, alignment=Qt.AlignCenter)
s2.setLayout(l2)

# Экран 3: Результаты
s3 = QWidget()
l3 = QVBoxLayout()

tr = QLabel('Результат теста:')
li = QLabel('Индекс Руфье: ')
lv = QLabel('Оценка: ')

l3.addWidget(tr, alignment=Qt.AlignCenter)
l3.addWidget(li, alignment=Qt.AlignCenter)
l3.addWidget(lv, alignment=Qt.AlignCenter)
s3.setLayout(l3)

# Функции переключения экранов
def show_screen2():
    mw.layout().setCurrentIndex(1)

def show_screen3():
    # Расчет индекса Руфье
    try:
        p1 = int(ip1.text())
        p2 = int(ip2.text())
        p3 = int(ip3.text())
        index = (4 * (p1 + p2 + p3) - 200) / 10

        # Простая оценка результата
        if index < 3:
            v = "Отлично"
        elif index < 6:
            v = "Хорошо"
        elif index < 9:
            v = "Удовлетворительно"
        else:
            v = "Слабо"

        li.setText(f'Индекс Руфье: {index:.1f}')
        lv.setText(f'Оценка: {v}')
        mw.layout().setCurrentIndex(2)
    except:
        li.setText('Ошибка ввода данных')
        lv.setText('Проверьте правильность ввода')
        mw.layout().setCurrentIndex(2)

# Настройка главного окна с stacked layout
from PyQt5.QtWidgets import QStackedLayout
sl = QStackedLayout()
sl.addWidget(s1)
sl.addWidget(s2)
sl.addWidget(s3)
mw.setLayout(sl)

# Подключение обработчиков событий
bs.clicked.connect(show_screen2)
bc.clicked.connect(show_screen3)

mw.show()
app.exec_()