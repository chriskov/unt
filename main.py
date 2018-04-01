import telebot
import os
import random
import urllib.request as urllib2



token = "580226470:AAEcW2BUNdtnpdZpLNgGAId92rZOR0JSSlc"
bot = telebot.TeleBot(token)
# bot.send_message(197752486, 'привет')
# upd = bot.get_updates()
# print(upd)
# lastupd = upd[-1]
# messagefromuser = lastupd.message
# print(messagefromuser)

# @bot.message_handler(content_types=['commands'])
# def handle_command(message):
#  print("ogo hello")

print(bot.get_me())


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} . (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)


@bot.message_handler(commands={'start'})
def handle_text(message):
    usermarkup = telebot.types.ReplyKeyboardMarkup(True, False)
    usermarkup.row('/start', '/stop')
    usermarkup.row('Привет', 'photo')
    usermarkup.row('ТУТ ЧТО ТО БУДЕТ', 'НО ЭТО ')
    usermarkup.row('НЕ ТОЧНО')
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0}! Воспользуйся навигацией Помощь : /help Чтобы пообщаться просто напиши мне привет".format(
                         message.from_user.first_name), reply_markup=usermarkup)


@bot.message_handler(commands={'stop'})
def handle_text(message):
    hidemarkup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     " Мда {0} {0} ...".format(message.from_user.first_name), reply_markup=hidemarkup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "ну впринципе я могу тебе помочь но мне лень")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "чо тебя надо епта я вас не звал идите нахой!"
    if message.text == "photo":
       # directory = 'C:/Users/Christina/Pictures/picsfor'
       # all_files_in_directory = os.listdir(directory)
       # randomfile = random.choice(all_files_in_directory)
        url = 'https://goo.gl/yqqUci'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        #img = open(directory + '/' + randomfile, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "привет" or message.text == "Привет":
        answer = "ну здарова"
        log(message, answer)
        bot.send_message(message.chat.id, "ну здарова")
    elif message.text == "love" or message.text == "te amo":
        answer = "и я тебя лав"
        bot.send_message(message.chat.id, 'и я тебя лав')
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


# @bot.message_handler(content_types={'sticker'})
# def handle_sticker(message):
#    print('wow')


bot.polling(none_stop=True, interval=0)
