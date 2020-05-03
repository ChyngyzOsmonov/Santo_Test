import telebot
import cfg
from telebot import types
from string import Template

bot = telebot.TeleBot(cfg.token)

user_dict = {}

main_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
test = types.KeyboardButton('/test')
test2 = types.KeyboardButton('/test2')
test3 = types.KeyboardButton('/test3')
main_button.add(test)
main_button.add(test2, test3)


class User:
    def __init__(self, fullname):
        self.fullname = fullname

        keys = ['phone', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

        for key in keys:
            self.key = None


class User2:
    def __init__(self, fullname):
        self.fullname = fullname

        keys = ['phone', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

        for key in keys:
            self.key = None


class User3:
    def __init__(self, fullname):
        self.fullname = fullname

        keys = ['phone', 'q1', 'q2', 'q3', 'q4', 'q5']

        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    bot.send_message(
        message.chat.id,
        '''Добро пожаловать
        ''',
        reply_markup=main_button)


#########################################################Test###################################################

@bot.message_handler(commands=["test"])
def user_reg(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, 'Введите Ф.И.О', reply_markup=markup)
    bot.register_next_step_handler(msg, process_fio_step)


def process_fio_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        Q1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Фуросемид')
        a2 = types.KeyboardButton('Торасемид')
        Q1.add(a1, a2)

        msg = bot.send_message(chat_id, 'Какой диуретик уменьшает развитие фиброза миокарда?', reply_markup=Q1)
        bot.register_next_step_handler(msg, process_q1_step)

    except Exception as e:
        print(e)


def process_q1_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q1 = message.text

        Q2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('10 мг, 5 мг')
        a2 = types.KeyboardButton('10 мг, 5 мг, 2,5 мг')
        Q2.add(a1, a2)

        msg = bot.send_message(chat_id, 'Сколько дозировок у Тригрима?', reply_markup=Q2)

        bot.register_next_step_handler(msg, process_q2_step)

    except Exception as e:
        print(e)


def process_q2_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q2 = message.text

        Q3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Отеки только сердечного генеза')
        a2 = types.KeyboardButton('Отеки любого генеза')
        Q3.add(a1, a2)

        msg = bot.send_message(chat_id, 'Показания к назначению Тригрима', reply_markup=Q3)

        bot.register_next_step_handler(msg, process_q3_step)

    except Exception as e:
        print(e)


def process_q3_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q3 = message.text

        Q4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('5 лет')
        a2 = types.KeyboardButton('3 года')
        Q4.add(a1, a2)

        msg = bot.send_message(chat_id, 'Срок годности Тригрима', reply_markup=Q4)
        bot.register_next_step_handler(msg, process_q4_step)

    except Exception as e:
        print(e)


def process_q4_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q4 = message.text

        Q5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Тромбо-Асс')
        a2 = types.KeyboardButton('Тромбопол')
        Q5.add(a1, a2)

        msg = bot.send_message(chat_id, 'Дозировки 75 мг и 150 мг  характерны для', reply_markup=Q5)
        bot.register_next_step_handler(msg, process_q5_step)

    except Exception as e:
        print(e)


def process_q5_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q5 = message.text

        Q6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Анальгетик')
        a2 = types.KeyboardButton('Антиагрегант')
        Q6.add(a1, a2)

        msg = bot.send_message(chat_id, 'Фармацевтическая группа Тромбопола', reply_markup=Q6)
        bot.register_next_step_handler(msg, process_q6_step)

    except Exception as e:
        print(e)


def process_q6_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q6 = message.text

        Q7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Кардиомагнила')
        a2 = types.KeyboardButton('Тромбопола')
        Q7.add(a1, a2)

        msg = bot.send_message(chat_id, 'Кишечнорастворимая оболочка у', reply_markup=Q7)
        bot.register_next_step_handler(msg, process_q7_step)

    except Exception as e:
        print(e)


def process_q7_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q7 = message.text

        Q8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Тромбо-Асс')
        a2 = types.KeyboardButton('Тромбопол')
        Q8.add(a1, a2)

        msg = bot.send_message(chat_id, 'Чей слоган: Твое сердце бьется не только для тебя!', reply_markup=Q8)
        bot.register_next_step_handler(msg, process_q8_step)

    except Exception as e:
        print(e)


def process_q8_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.q8 = message.text

        markup = types.ReplyKeyboardRemove(selective=False)

        bot.send_message(chat_id, getRegData(user, 'Вы закончили тест\nВаши ответы', message.from_user.first_name,
                                             getResult(user)),
                         parse_mode="Markdown", reply_markup=markup)
        bot.send_message(cfg.chat_id, getRegData(user, 'Тест сдали на ', bot.get_me().username, getResult(user)),
                         parse_mode="Markdown")

        bot.send_message(chat_id, '<b>Правильные ответы к тесту №1</b>\n\n'
                                  'Какой диуретик уменьшает развитие фиброза миокарда? \n<b>-Торасемид</b>\n'
                                  'Сколько дозировок у Тригрима? \n<b>-10 мг, 5 мг, 2,5 мг</b>\n'
                                  'Показания к назначению Тригрима: \n<b>-Отеки любого генеза</b>\n'
                                  'Срок годности Тригрима: \n<b>-5 лет</b>\n'
                                  'Дозировки 75 мг и 150 мг характерны для \n<b>-Тромбопол</b>\n'
                                  'Фармацевтическая группа Тромбопола: \n<b>-Антиагрегант</b>\n'
                                  'Кишечнорастворимая оболочка у \n<b>-Тромбопола</b>\n'
                                  'Чей слоган: Твое сердце бьется не только для тебя! \n<b>-Тромбопол</b>',
                         reply_markup=main_button,
                         parse_mode='HTML')
        bot.send_photo(chat_id, sendPhoto(user))

    except Exception as e:
        print(e)


def getRegData(user, title, name, get_result):
    t = Template('$title *$name* \nФИО: *$fullname* '
                 '\nВопрос №1: *$q1* '
                 '\nВопрос №2: *$q2*'
                 '\nВопрос №3: *$q3*'
                 '\nВопрос №4: *$q4*'
                 '\nВопрос №5: *$q5*'
                 '\nВопрос №6: *$q6*'
                 '\nВопрос №7: *$q7*'
                 '\nВопрос №8: *$q8*'
                 '\n*$get_result*')

    return t.substitute({
        'get_result': get_result,
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'q1': user.q1,
        'q2': user.q2,
        'q3': user.q3,
        'q4': user.q4,
        'q5': user.q5,
        'q6': user.q6,
        'q7': user.q7,
        'q8': user.q8,
    })


def getResult(user):
    true_count = 0
    if user.q1 == 'Торасемид':
        true_count += 1
    if user.q2 == '10 мг, 5 мг, 2,5 мг':
        true_count += 1
    if user.q3 == 'Отеки любого генеза':
        true_count += 1
    if user.q4 == '5 лет':
        true_count += 1
    if user.q5 == 'Тромбопол':
        true_count += 1
    if user.q6 == 'Антиагрегант':
        true_count += 1
    if user.q7 == 'Тромбопола':
        true_count += 1
    if user.q8 == 'Тромбопол':
        true_count += 1

    if true_count >= 7:
        return f'\nСупер! У вас отличные знания!\nПравильных ответов всего: {true_count}'
    elif true_count <= 7:
        return f'\nНеплохо!\nПравильных ответов всего: {true_count}'


def sendPhoto(user):
    true_count = 0
    if user.q1 == 'Торасемид':
        true_count += 1
    if user.q2 == '10 мг, 5 мг, 2,5 мг':
        true_count += 1
    if user.q3 == 'Отеки любого генеза':
        true_count += 1
    if user.q4 == '5 лет':
        true_count += 1
    if user.q5 == 'Тромбопол':
        true_count += 1
    if user.q6 == 'Антиагрегант':
        true_count += 1
    if user.q7 == 'Тромбопола':
        true_count += 1
    if user.q8 == 'Тромбопол':
        true_count += 1

    if true_count >= 7:
        return open('/home/test/Santo_Test/images/super.jpg', 'rb')


############################################test2##################################################################

@bot.message_handler(commands=["test2"])
def user_reg_test2(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, 'Введите Ф.И.О', reply_markup=markup)
    bot.register_next_step_handler(msg, process_fio_step_test2)


def process_fio_step_test2(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User2(message.text)

        Q1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Нитраты')
        a2 = types.KeyboardButton('Ацетисалициловую кислоту')
        Q1.add(a1, a2)

        msg = bot.send_message(chat_id, 'Для профилактики инфаркта и инсульта назначают', reply_markup=Q1)
        bot.register_next_step_handler(msg, process_q1_step_test2)

    except Exception as e:
        print(e)


def process_q1_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q1 = message.text

        Q2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Лизинопри')
        a2 = types.KeyboardButton('Периндоприл')
        a3 = types.KeyboardButton('Эналаприл')
        Q2.add(a1, a2)
        Q2.add(a3)

        msg = bot.send_message(chat_id, 'Самый высокий уровень липофильности у', reply_markup=Q2)
        bot.register_next_step_handler(msg, process_q2_step_test2)

    except Exception as e:
        print(e)


def process_q2_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q2 = message.text

        Q3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Периндоприла')
        a2 = types.KeyboardButton('Рамиприла')
        Q3.add(a1, a2)

        msg = bot.send_message(chat_id, 'В наименьшей степени среди всех ин.АПФ  гипотония первой дозы развивается  у',
                               reply_markup=Q3)
        bot.register_next_step_handler(msg, process_q3_step_test2)

    except Exception as e:
        print(e)


def process_q3_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q3 = message.text

        Q4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Эналаприл')
        a2 = types.KeyboardButton('Лизиноприл')
        a3 = types.KeyboardButton('Периндоприл')
        Q4.add(a1, a2)
        Q4.add(a3)

        msg = bot.send_message(chat_id, 'Самая большая доказательная база у', reply_markup=Q4)
        bot.register_next_step_handler(msg, process_q4_step_test2)

    except Exception as e:
        print(e)


def process_q4_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q4 = message.text

        Q5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Рамиприла')
        a2 = types.KeyboardButton('Периндоприла')
        a3 = types.KeyboardButton('Лизиноприла')
        Q5.add(a1, a2)
        Q5.add(a3)

        msg = bot.send_message(chat_id, 'Для пациентов, перенесших мозговой инсульт наибольшая эффективность '
                                        '(класс I, уровень А) доказана у', reply_markup=Q5)
        bot.register_next_step_handler(msg, process_q5_step_test2)

    except Exception as e:
        print(e)


def process_q5_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q5 = message.text

        Q6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Лизиноприл')
        a2 = types.KeyboardButton('Периндоприл')
        a3 = types.KeyboardButton('Рамиприл')
        Q6.add(a1, a2)
        Q6.add()

        msg = bot.send_message(chat_id, 'Уменьшает риск развития ХСН  на  39%, риск ОИМ на  24%',
                               reply_markup=Q6)
        bot.register_next_step_handler(msg, process_q6_step_test2)

    except Exception as e:
        print(e)


def process_q6_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q6 = message.text

        Q7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Индапамид SR')
        a2 = types.KeyboardButton('Индап')
        Q7.add(a1, a2)

        msg = bot.send_message(chat_id, 'Тиазидоподобный диуретик с пролонгированным механизмом действия',
                               reply_markup=Q7)
        bot.register_next_step_handler(msg, process_q7_step_test2)

    except Exception as e:
        print(e)


def process_q7_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q7 = message.text

        Q8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('2,5 мг')
        a2 = types.KeyboardButton('1,5 мг')
        Q8.add(a1, a2)

        msg = bot.send_message(chat_id, 'Доза активного вещества в Индапамиде SR', reply_markup=Q8)
        bot.register_next_step_handler(msg, process_q8_step_test2)

    except Exception as e:
        print(e)


def process_q8_step_test2(message):
    try:
        chat_id = message.chat.id
        user2 = user_dict[chat_id]
        user2.q8 = message.text

        markup = types.ReplyKeyboardRemove(selective=False)

        bot.send_message(chat_id,
                         getRegData_test2(user2, 'Вы закончили тест\nВаши ответы', message.from_user.first_name,
                                          getResult_test2(user2)),
                         parse_mode="Markdown", reply_markup=markup)
        bot.send_message(cfg.chat_id,
                         getRegData_test2(user2, 'Закончили тест на ', bot.get_me().username,
                                          getResult_test2(user2)),
                         parse_mode="Markdown")
        bot.send_message(chat_id, '<b>Правильные ответы к тесту №2</b>\n\n'
                                  'Для профилактики инфаркта и инсульта назначают :\n<b>-Ацетисалициловую кислоту</b>\n'
                                  'Самый высокий уровень липофильности у \n<b>-Периндоприл</b>\n'
                                  'В наименьшей степени среди всех иАПФ  гипотония первой дозы развивается у '
                                  '\n<b>-Периндоприла</b>\n'
                                  'Самая большая доказательная база у \n<b>-Периндоприл</b>\n'
                                  'Для пациентов, перенесших мозговой инсульт наибольшая эффективность'
                                  ' (класс I, уровень А) доказана у \n<b>-Периндоприла</b>\n'
                                  'Уменьшает риск развития ХСН  на  39%, риск ОИМ на  24%: \n<b>-Периндоприл</b>\n'
                                  'Тиазидоподобный диуретик с пролонгированным механизмом действия: \n'
                                  '<b>-Индапамид SR</b>\n'
                                  'Доза активного вещества в Индапамиде SR: \n<b>-1,5 мг</b>', reply_markup=main_button,
                         parse_mode='HTML')
        bot.send_photo(chat_id, sendPhoto_test2(user2))

    except Exception as e:
        print(e)


def getRegData_test2(user2, title, name, get_result_2):
    t = Template('$title *$name* \n\nФИО: *$fullname* '
                 '\nВопрос №1: *$q1* '
                 '\nВопрос №2: *$q2*'
                 '\nВопрос №3: *$q3*'
                 '\nВопрос №4: *$q4*'
                 '\nВопрос №5: *$q5*'
                 '\nВопрос №6: *$q6*'
                 '\nВопрос №7: *$q7*'
                 '\nВопрос №8: *$q8*'
                 '\n*$get_result_2*')

    return t.substitute({
        'get_result_2': get_result_2,
        'title': title,
        'name': name,
        'fullname': user2.fullname,
        'q1': user2.q1,
        'q2': user2.q2,
        'q3': user2.q3,
        'q4': user2.q4,
        'q5': user2.q5,
        'q6': user2.q6,
        'q7': user2.q7,
        'q8': user2.q8,
    })


def getResult_test2(user2):
    true_count_2 = 0
    if user2.q1 == 'Ацетисалициловую кислоту':
        true_count_2 += 1
    if user2.q2 == 'Периндоприл':
        true_count_2 += 1
    if user2.q3 == 'Периндоприла':
        true_count_2 += 1
    if user2.q4 == 'Периндоприл':
        true_count_2 += 1
    if user2.q5 == 'Периндоприла':
        true_count_2 += 1
    if user2.q6 == 'Периндоприл':
        true_count_2 += 1
    if user2.q7 == 'Индапамид SR':
        true_count_2 += 1
    if user2.q8 == '1,5 мг':
        true_count_2 += 1

    if true_count_2 >= 7:
        return f'\nСупер! У вас отличные знания!\nПравильных ответов всего: {true_count_2}'
    elif true_count_2 <= 7:
        return f'\nНеплохо!\nПравильных ответов всего: {true_count_2}'


def sendPhoto_test2(user2):
    true_count_2 = 0
    if user2.q1 == 'Ацетисалициловую кислоту':
        true_count_2 += 1
    if user2.q2 == 'Периндоприл':
        true_count_2 += 1
    if user2.q3 == 'Периндоприла':
        true_count_2 += 1
    if user2.q4 == 'Периндоприл':
        true_count_2 += 1
    if user2.q5 == 'Периндоприла':
        true_count_2 += 1
    if user2.q6 == 'Периндоприл':
        true_count_2 += 1
    if user2.q7 == 'Индапамид SR':
        true_count_2 += 1
    if user2.q8 == '1,5 мг':
        true_count_2 += 1

    if true_count_2 >= 7:
        return open('/home/test/Santo_Test/images/super.jpg', 'rb')


#############################################test3############################################################

@bot.message_handler(commands=["test3"])
def user_reg_test3(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, 'Введите Ф.И.О', reply_markup=markup)
    bot.register_next_step_handler(msg, process_fio_step_test3)


def process_fio_step_test3(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User3(message.text)

        Q1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Бисептол')
        a2 = types.KeyboardButton('Цефтриаксон')
        Q1.add(a1, a2)

        msg = bot.send_message(chat_id, 'Выражение :Надежный ход в борьбе с инфекцией , подходит больше для',
                               reply_markup=Q1)
        bot.register_next_step_handler(msg, process_q1_step_test3)

    except Exception as e:
        print(e)


def process_q1_step_test3(message):
    try:
        chat_id = message.chat.id
        user3 = user_dict[chat_id]
        user3.q1 = message.text

        Q2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Азитромицин')
        a2 = types.KeyboardButton('Цефтриаксон')
        Q2.add(a1, a2)

        msg = bot.send_message(chat_id, 'Бета-лактамный антибактериальный препарат широкого спектра действия – это',
                               reply_markup=Q2)
        bot.register_next_step_handler(msg, process_q2_step_test3)

    except Exception as e:
        print(e)


def process_q2_step_test3(message):
    try:
        chat_id = message.chat.id
        user3 = user_dict[chat_id]
        user3.q2 = message.text

        Q3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Увеличивает концентрацию антибиотиков в мокроте и бронхиальном секрете')
        a2 = types.KeyboardButton('Действие начинается через 30 мин')
        a3 = types.KeyboardButton('Все выше перечисленное')
        Q3.add(a2)
        Q3.add(a1)
        Q3.add(a3)

        msg = bot.send_message(chat_id, 'Амбро- эффект с первых часов применения, за счет чего',
                               reply_markup=Q3)
        bot.register_next_step_handler(msg, process_q3_step_test3)

    except Exception as e:
        print(e)


def process_q3_step_test3(message):
    try:
        chat_id = message.chat.id
        user3 = user_dict[chat_id]
        user3.q3 = message.text

        Q4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Обладает противовоспалительным эффектом')
        a2 = types.KeyboardButton('Разжижает мокроту и выводит из лёгких ')
        a3 = types.KeyboardButton('Все выше перечисленное')
        Q4.add(a1)
        Q4.add(a2)
        Q4.add(a3)

        msg = bot.send_message(chat_id, 'Механизм действия Амбро:', reply_markup=Q4)
        bot.register_next_step_handler(msg, process_q4_step_test3)

    except Exception as e:
        print(e)


def process_q4_step_test3(message):
    try:
        chat_id = message.chat.id
        user3 = user_dict[chat_id]
        user3.q4 = message.text

        Q5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton('Таблетки')
        a2 = types.KeyboardButton('Сироп')
        a3 = types.KeyboardButton('Все выше перечисленное')
        Q5.add(a1, a2)
        Q5.add(a3)

        msg = bot.send_message(chat_id, 'Какие формы выпуска есть у Амбро', reply_markup=Q5)
        bot.register_next_step_handler(msg, process_q5_step_test3)

    except Exception as e:
        # bot.reply_to(message, 'Повторите попытку')
        print(e)


def process_q5_step_test3(message):
    try:
        chat_id = message.chat.id
        user3 = user_dict[chat_id]
        user3.q5 = message.text

        markup = types.ReplyKeyboardRemove(selective=False)

        bot.send_message(chat_id,
                         getRegData_test3(user3, 'Вы закончили тест\nВаши ответы ', message.from_user.first_name,
                                          getResult_test3(user3)),
                         parse_mode="Markdown", reply_markup=markup)
        bot.send_message(cfg.chat_id,
                         getRegData_test3(user3, 'Тест закончили на ', bot.get_me().username,
                                          getResult_test3(user3)),
                         parse_mode="Markdown")
        bot.send_message(chat_id, '<b>Правильные ответы к тесту №3</b>\n\n'
                                  'Выражение: Надежный ход в борьбе с инфекцией , '
                                  'подходит больше для :\n<b>-Цефтриаксон</b>\n'
                                  'Бета-лактамный антибактериальный препарат '
                                  'широкого спектра действия – это \n<b>-Цефтриаксон</b>\n'
                                  'Амбро- эффект с первых часов применения, за счет чего: \n'
                                  '<b>-Все выше перечисленное</b>\n'
                                  'Механизм действия Амбро: \n<b>-Все выше перечисленное</b>\n'
                                  'Какие формы выпуска есть у Амбро: \n<b>-Все выше перечисленное</b>',
                         reply_markup=main_button,
                         parse_mode='HTML')

        bot.send_photo(chat_id, sendPhoto_test3(user3))

    except Exception as e:
        print(e)


def getRegData_test3(user3, title, name, get_result_3):
    t = Template('$title *$name*\n\nФИО: *$fullname* '
                 '\nВопрос №1: *$q1* '
                 '\nВопрос №2: *$q2*'
                 '\nВопрос №3: *$q3*'
                 '\nВопрос №4: *$q4*'
                 '\nВопрос №5: *$q5*'
                 '\n*$get_result_3*')

    return t.substitute({
        'get_result_3': get_result_3,
        'title': title,
        'name': name,
        'fullname': user3.fullname,
        'q1': user3.q1,
        'q2': user3.q2,
        'q3': user3.q3,
        'q4': user3.q4,
        'q5': user3.q5,
    })


def getResult_test3(user3):
    true_count_3 = 0
    if user3.q1 == 'Цефтриаксон':
        true_count_3 += 1
    if user3.q2 == 'Цефтриаксон':
        true_count_3 += 1
    if user3.q3 == 'Все выше перечисленное':
        true_count_3 += 1
    if user3.q4 == 'Все выше перечисленное':
        true_count_3 += 1
    if user3.q5 == 'Все выше перечисленное':
        true_count_3 += 1

    if true_count_3 >= 4:
        return f'\nСупер! У вас отличные знания!\nПравильных ответов всего: {true_count_3}'
    elif true_count_3 <= 4:
        return f'\nНеплохо!\nПравильных ответов всего: {true_count_3}'


def sendPhoto_test3(user3):
    true_count_3 = 0
    if user3.q1 == 'Цефтриаксон':
        true_count_3 += 1
    if user3.q2 == 'Цефтриаксон':
        true_count_3 += 1
    if user3.q3 == 'Все выше перечисленное':
        true_count_3 += 1
    if user3.q4 == 'Все выше перечисленное':
        true_count_3 += 1
    if user3.q5 == 'Все выше перечисленное':
        true_count_3 += 1

    if true_count_3 >= 4:
        return open('/home/test/Santo_Test/images/super.jpg', 'rb')


try:
    bot.polling(none_stop=True, interval=0, timeout=30)
except Exception as E:
    print(E)
