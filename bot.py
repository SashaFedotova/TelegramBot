from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_API_URL, TG_TOKEN

#sms используется при отправке команды start
def sms(bot, update):
    print('Кто-то отправил команду /start, что мне делать? ')
    bot.message.reply_text('Здравствуйте, я бот! '.format(bot.message.chat.first_name))

#отвечает тем же сообщенеим, которое ему написали
def parrot(bot, update):
    print(bot.message.text)#печатаем сообщение пользователя
    bot.message.reply_text(bot.message.text)#отправляем сообщение пользователя обратно




def main():
    #Создадим переменную my_bot, с помощью которой будем взаимодействовать с ботом
    my_bot = Updater(TG_TOKEN, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))#dispatcher принимает от платформы сообщение add_handler и передает в обработчик CommandHandler

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))#обработчик текстового сообщения

    my_bot.start_polling()# проверяем наличие сообщений от платформы Telegram
    my_bot.idle() #бот будет работать, пока его не остановят


main()
