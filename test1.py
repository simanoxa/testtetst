import random
import time
def ugadayslovo():
    #выбор слова
    def get_word():
        lst_word = ['','актер', 'тупик', 'завод', 'банан', 'совет', 'белка', 'весть', 'тесть', 'сапер', 'мираж', 'гараж', 'багаж', 'муляж', 'жизнь', 'жрица', 'фобия', 'магия', 'почка', 'порча', 'сахар', 'вазон', 'газон', 'лодка', 'горка', 'порка', 'дождь', 'ласка', 'пасха', 'шорох', 'хохот', 'топот', 'порох', 'горох', 'топор', 'ропот', 'вопль', 'доска', 'каска', 'басня', 'башня', 'тоска', 'соска', 'кокос', 'закат', 'ворот', 'товар', 'олово', 'филин', 'дятел', 'весна', 'осень', 'секта', 'песок', 'пинок', 'пират', 'школа', 'гроза', 'базар', 'забор', 'замок', 'выдра', 'кусок', 'роман', 'тропа', 'трава', 'гогот', 'навес', 'сезон', 'кокон', 'палец', 'цапля', 'кость', 'горло', 'крыша', 'крыса', 'пирог', 'земля', 'талон', 'фасон', 'номер', 'халва', 'ларек', 'акула', 'мидия', 'ферзь', 'театр', 'огонь', 'ветка', 'вечер', 'шатер', 'шалаш', 'шторм', 'зефир', 'ферма', 'проза', 'валет', 'карта', 'книга', 'видео', 'плечо', 'почта', 'червь', 'визит', 'зебра', 'месть', 'треск', 'конец', 'цыган', 'крест', 'пресс', 'ссора', 'балет', 'петух', 'курок', 'кубок', 'искра', 'исток', 'скала', 'палка', 'тазик', 'фильм', 'песня', 'сопля', 'посох', 'жираф', 'финал', 'забег', 'побег', 'стена', 'водка', 'рюмка', 'миска', 'ложка', 'вилка', 'спорт', 'кабан', 'кофта', 'ворон', 'гость', 'факел', 'добро', 'сосна', 'жетон', 'зевок', 'засор', 'мусор', 'грязь', 'труба', 'канал', 'ванна', 'ретро', 'чехол', 'блюдо', 'пакет', 'океан', 'бомба', 'бочка', 'качок', 'крупа', 'колье', 'каток', 'круиз', 'кубик', 'кисть', 'пятно', 'баран', 'кобра', 'досуг', 'белье', 'сцена', 'сюжет', 'химия', 'танец', 'ковер', 'кулак', 'кефир', 'озеро', 'бутик', 'кухня', 'плита', 'копье', 'арбуз', 'астра', 'олень', 'лавка', 'лимон', 'лемур', 'зверь', 'слово', 'буква', 'форма', 'плата', 'слуга', 'мешок', 'мечта', 'мазок', 'мачта', 'штора', 'масть', 'носок']
        rnd = random.randint(1,201)
        return lst_word[rnd]
    def print_word(word_, list_):
        for c in word_:
            if c in list_:
                print(c, end=' ')
            else:
                print('_', end=' ')
        print()

    #стадии человечка
    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
        return stages[tries]
    #тело
    def go(word):
        word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
        guessed = False                    # сигнальная метка
        guessed_letters = []               # список уже названных букв
        guessed_words = []                 # список уже названных слов
        tries = 6                          # количество попыток
        print('Привет, давайте сыграем? Я загадаю слово из 5 букв, а ваша задача его отгадать!')
        print((display_hangman(tries)))
        print(word_completion)
        while True:
            print('Введите букву. Если догадываешься, введи слово')
            word_input = input().upper()
            if not word_input.isalpha():
                print('Вы допустили ошибку')
                continue
            if len(word) > 1:
                if word_input == word:
                    print('Поздравляю, вы отгадали слово! Вы победили!') 
                    break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                print(f'Не правильно, осталось {tries} попыток')
                if word_input in guessed_words or word_input in guessed_letters:
                    print('Уже было')
                    tries += 1
                if tries == 0:
                    print(f'Увы, вы проиграли!:( Слово:{word}')
                    break
                continue
            if word_input in word:
                guessed_letters.append(word_input)
                for c in word:
                    if c  in guessed_letters:
                        print('Угадали букву')
                        print_word(word, guessed_letters)
                        guessed = False
                        break
                    guessed = True
                if guessed:    
                    print_word(word, guessed_letters)
                    print('Поздравляю, вы угадали слово! Вы победили!')
                    break
            else:
                guessed_letters.append(word_input)
                tries -= 1
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                print(f'Не верно, осталось попыток {tries}')
            if tries == 0:
                print(f'Вы не смогли угадать слово: {word}')
                break

    go(get_word().upper())
    print('Возвращаю в главное меню!')
    time.sleep(3)
    nachalo()
def ugaday():
    def start():
        print('Введи первое число')
        num_1 = int(input())
        print('Введи второе число')
        num_2 = int(input())
        if num_1 > num_2:
            num_1, num_2 = num_2, num_1
        rnd = random.randint(num_1, num_2)
        print(f'Я загадал число от {num_1} до {num_2}, теперь попробуй его отгадать!')
        otvet = int(input())
        flag = False
        count = 1
        while flag == False:
            if otvet == rnd:
                print('Отлично! Ты отгадал с', count, 'попытки! Поздравляю!')
                flag = True
                break
            elif otvet > rnd and otvet - rnd > 10:
                print('Слишком много, попробуй меньше')
                count += 1
            elif otvet > rnd and 5 < otvet - rnd < 10:
                print('Уже близко, попробуй чуть меньше')
                count += 1
            elif otvet > rnd and   otvet - rnd < 5:
                print('Совсем рядом, нужно меньше')
                count += 1
            elif otvet < rnd and rnd - otvet > 10:
                print('Слишком мало, попробуй больше')
                count += 1
            elif otvet < rnd and 5 < rnd - otvet < 10:
                print('Уже близко, попробуй чуть больше')
                count += 1
            elif otvet < rnd and   rnd - otvet < 5:
                print('Совсем рядом, нужно больше')
                count += 1
            otvet = int(input())
    print('Привет! Давай сыграем в игру? Готов начать? Введи "да" или "нет" и нажми Enter')
    sogl = input()
    if sogl.lower() == 'нет':
            print('Очень жаль! Возвращайся, как захочешь поиграть! Возвращаю в главное меню')
            nachalo()
    while sogl != 'нет':
        if sogl.lower() == 'да':
            print('Отлично! Начинаем!')
            time.sleep(3)
            print('Тебе нужно ввести два числа, я выберу случайное число в этом диапазоне')
            time.sleep(3)
            print('Твоя задача будет угадать число которое я загадал')
            time.sleep(3)
            print('Не переживай, я буду тебе подсказывать')
            time.sleep(3)
            start()
            print('Сыграем еще раз?')
            sogl = input()
            if sogl.lower() == 'нет':
                print('Правильно, на сегодня достаточно, возвращаю в главное меню')
                nachalo()
def shar():
    print('Привет, я магический шар, задай мне вопрос про будущее, а я предскажу тебе судьбу')
    time.sleep(3)
    def shar_8():
        print('Напиши свой вопрос и нажми Enter')
        vopros = input()
        lst = ['','Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', '	Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова','Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', '	Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']	
        rnd = random.randrange(1, 21)
        time.sleep(1)
        print('Думаю...')
        time.sleep(3)
        print(lst[rnd])
    shar_8()
    time.sleep(3)
    print('До скорых встреч! Возвращаю в главное меню')
    time.sleep(2)
    nachalo()
def generator():
    cif = '0123456789'
    mal = 'abcdefghijklmnopqrstuvwxyz'
    bol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    zn = '!#$%&*+-=?@^_'
    simv = ''
    print('Привет, я генератор надежных паролей')
    time.sleep(1)
    print('Сколько паролей тебе нужно сгенерировать?')
    n = int(input())
    print('Сколько символов должно быть в твоем пароле?')
    l = int(input())
    print('Пароль должен включить цифры? "да" или "нет"')
    add_cif = input('')
    print('Пароль должен содержать строчные буквы? "да" или "нет"')
    add_mal = input()
    print('Пароль должен содержать прописные буквы? "да" или "нет"')
    add_bol = input()
    print('Пароль должен Включить символы, такие как !#$%&*+-=?@^_?? "да" или "нет"')
    add_zn = input()
    time.sleep(2)
    if add_cif.lower() == 'да':
        simv += cif
    if add_mal.lower() == 'да':
        simv += mal
    if add_bol.lower() == 'да':
        simv += bol
    if add_zn.lower() == 'да':
        simv += zn
    def generate_password(l, simv):
        password = ''
        for i in range(l):
            password += random.choice(simv)
        print('Твой пароль:', password, sep='')
    for _ in range(n):
        generate_password(l, simv)
    time.sleep(2)
    print('Возвращаю в главное меню')
    time.sleep(2)
    nachalo()
def nachalo():
    print('Выбери из данных вариантов, что тебе интересно!')
    time.sleep(1)
    print('1. Игра "угадай число"')
    time.sleep(1)
    print('2. Шар с предсказаниями')
    time.sleep(1)
    print('3. Генератор паролей')
    time.sleep(1)
    print('4. Виселица')
    time.sleep(1)
    print('Введи номер интересующего пункта и нажми Enter')
    nomer = int(input())
    if nomer == 1:
        ugaday()
    if nomer == 2:
        shar()
    if nomer == 3:
        generator()
    if nomer == 4:
        ugadayslovo()
nachalo()