import telebot

bot = telebot.TeleBot('7537254260:AAEyyW44XsGzBi5M4dTJ3UL00g7NeQ0k_8g')
    
@bot.message_handler(commands = ['start'])
def send_start_message(message):
    bot.send_message(message.chat.id, 'Привет!, я бот который поможет тебе узнать о загрязнении окружающей среды!')
    bot.send_message(message.chat.id, 'У меня есть такие команды как: /pollution_info, /items, /trash_cans, /creative_solution.')
    
@bot.message_handler(commands = ['pollution_info'])
def infa(message):
    bot.reply_to(message, 'Загрязнение негативно влияет на всю окружающую среду. Нетрудно заметить замедление роста деревьев, исчезание редких растений, более чувствительных к загрязнению, нарушения в процессе фотосинтеза, прогрессирующее загрязнение вод и почв, изменение климата и ландшафта.')
    with open('pollute.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
        
@bot.message_handler(commands = ['items'])
def items(message):
    bot.reply_to(message, 'Всего 7 видов предметов, которые нельзя выбрасывать в мусороное ведро:Стеклянные градусники(Градусник содержит до 500 мг ртути), Медикаменты, Аэрозольные флаконы, Целлофановые пакеты, Компьютеры, электроника, Бытовая химия,  Люминесцентные лампы')

@bot.message_handler(commands = ['trash_cans'])
def trash(message):
    bot.reply_to(message, 'Если видишь такие мусорные ведра, то можешь смело выбрасывать в них любой мусор!')
    with open('cans.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
        
@bot.message_handler(commands = ['creative_solution'])
def creation(message):
    bot.reply_to(message, 'А если ты хочешь подойти к мусору креативно, то можешь сделать такую поделку!')
    with open('podelka.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)


bot.infinity_polling()