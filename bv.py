import telebot;
bot = telebot.TeleBot('6078117071:AAH08U95CnQbrdlp01Z0rQQn-Do0mJXM4cA');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        name = message.from_user.username
        bot.send_message(message.from_user.id, "*📍 Приветствую!* Я Бот-Помощник по Мафии."
    "\n👀 Если вы впервые в Мафии-Баку, воспользуйтесь командой *.нью*"
    '\n🔎 Если вы уже играли в Мафию-Баку, воспользуйтесь командой *.инф*', parse_mode='Markdown')
    elif message.text == '.нью' or message.text == '.Нью'or message.text == '.рег':
        bot.send_message(message.from_user.id, "👁 Добро пожаловать в ряды Мафиозников!"
    '\nДля дальнейшего обучения нужно *Присоединиться к игре*. '
    '\nЕсли в данный момент проводится регистрация в игру, то смс с регистрацией'
    ' закреплено в том чате, в котором вы узнали обо мне :)'
    '\nЕсли в данный момент в чате нет закрепленной регистрации, вероятнее всего в чате уже проходит игра. '
    '\nДождитесь ее окончания и присоединяйтесь.'
    '\nКак только вы присоединитесь к регистрации, воспользуйтесь командой *.игра*'
    '\nЕсли вы уже находитесь в регистрации, вам нужно подождать начала игры.', parse_mode='Markdown')
bot.polling(none_stop=True, interval=0)