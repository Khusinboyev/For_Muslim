from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton



main_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_btn.add("📊Statistika", "🔧Kanallar", "📤Reklama", "♻️ Tozalash")

channel_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
channel_btn.add("➕Kanal qo'shish", "❌Kanalni olib tashlash")
channel_btn.add("📋 Kanallar ro'yxati", "🔙Orqaga qaytish")

reklama_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
reklama_btn.add("📨Forward xabar yuborish", "📬Oddiy xabar yuborish", "🔙Orqaga qaytish")


############    Enter manu

enter_btn1 = InlineKeyboardMarkup(row_width=1)
enter_btn1.add(InlineKeyboardButton("🕋 Muslumon bo'lsangiz kiring 🕋", callback_data="enter1"))


###########     Davom etish

enter_btn2 = InlineKeyboardMarkup()
enter_btn2.add(InlineKeyboardButton("Davom etish", callback_data="enter2"))


##########      Bosh menu

bosh_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bosh_btn.add("🕋5 ustun", "📖Qur'on", "Payg'ambarimiz haqida", "🗞Payg'ambarlar qissalari", "Allohning go'zal ismlari", "📖Qur'ondagi qissalar",
             "⏳Namoz vaqtlari")


##########      5 ustun

ustun_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
ustun_btn.add("✨Iymon", "🧎Namoz", "🤲Ro'za", "💳Zakot", "🕋Haj", "◀️Orqaga qaytish")

Iman_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Iman_btn.add("Iymon haqida", "✨6 diniy kalimalar haqida", "🔊Kalimalarni o'rganish", "Orqaga qaytish,")

Namoz_btn1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Namoz_btn1.add("🧎‍♂️Namoz haqida", "💧Poklanish", "🧎‍♂️Erkaklar uchun Namoz", "🧎‍♀️Ayollar uchun Namoz", "🧎Boshqa Namozlar",
              "🔎Namozdagi bazi holatlar", "📿Namozdan keyingi zikr va duolar", "Orqaga qaytish.")

Namoz_btn2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Namoz_btn2.add("🛁G'usl haqida", "🚰Tahorat Haqida", "Tayammum haqida", "️Orqaga qaytish")

Namoz_btn3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Namoz_btn3.add("🧎Qazo namozlari", "Qolganlari tez orada", "◀Ortga qaytish")

Haj_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
Haj_btn.add("🕋Haj haqida", "🕋Hajning tartibi🧮", ".Orqaga qaytish")



###########            QUR'AN MENU

Quran_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Quran_btn.add("📖Quro'ni karim haqida batafsil", "📖Qur'on kitobi", "Qorilarning qiroatlari🔊", "Nashidalar🔊", "◀️Orqaga qaytish")

Qiroat_btn= InlineKeyboardMarkup(row_width=2)
names =['Mishariy Roshid Al- Afasy', 'Muhammad Minshaviy', 'Abdulbosit Abdussomad', 'Abdurrahmon As-Sudaysiy', 'Mahmud Xolid Xusoriy', 'Xasan va Xusan qorilar', 'Абдуллоҳ qori', 'Абдулбосит Абдуссомад']
for name in names:
    Qiroat_btn.insert(InlineKeyboardButton(text=name, callback_data=name))

Juz_btn= InlineKeyboardMarkup(row_width=2)
w = 0
names =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114']
for name in names:
    w+=1
    Juz_btn.insert(InlineKeyboardButton(text=str(int(name)+1), callback_data=name))
    if w==57:
        break
Juz_btn.add(InlineKeyboardButton(text="◀️", callback_data="◀️"))
Juz_btn.insert(InlineKeyboardButton(text="▶️", callback_data="▶️"))
Juz_btn.insert(InlineKeyboardButton(text="❌", callback_data="❌"))

###########            PAYG'AMBARIMIZ HAQIDA

Habibim_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Habibim_btn.add("Nuriddin hoji domla🔊", 'Abdulloh domla maruzasi🔊', "🎞Teleseriali", "◀️Orqaga qaytish")




###########              Payg'ambarlar qissalari

P_qissasi_btn = InlineKeyboardMarkup(row_width = 2)
paygambarlar = ["Odam alayhissalom", "Nuh alayhissalom", 'Hud alayhissalom', 'Solih alayhissalom', 'Ibrohim alayhissalom',
                'Lut alayhissalom', 'Yusuf alayhissalom', 'Ayyub alayhissalom', 'Yunus alayhissalom', 'Muso alayhissalom',
                'Yusha ibn Nun alayhissalom', 'Dovud va Sulaymon alayhissalomlar', 'Zakariyo va Yahyo alayhissalomlar', 'Iso alayhissalom']
for P_name in paygambarlar:
    P_qissasi_btn.insert(InlineKeyboardButton(text=P_name, callback_data=P_name))



###########              Allohning ismlari

Great_name_btn= InlineKeyboardMarkup(row_width=2)
names =[' 1 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50', '51 - 60', '61 - 70', '71 - 80', '81 - 90', '91 - 99']
for name in names:
    Great_name_btn.insert(InlineKeyboardButton(text=name, callback_data=name))



############            qissalar

Qissalar_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Qissalar_btn.add("👳‍♂️Insonlar qissasi", "🧕Ayollar qissasi", "🤩Ajoyibotlar qissasi", "🐫Jonzotlar qissasi", "◀️Orqaga qaytish")



##########               Namoz vaqtlari

P_T_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
P_T_btn.add("⏳Bugungi namoz vaqti", "⏳Kunlik duolar", "🏙Shaharni tanlash", "◀️Orqaga qaytish")


choos_city_btn = InlineKeyboardMarkup(row_width=2)
regs = ['Ангрен', 'Андижон', 'Арнасой', 'Ашхабод', 'Бекобод', 'Бишкек', 'Бойсун', 'Булоқбоши', 'Бурчмулла', 'Бухоро',
        'Газли', 'Гулистон', 'Денов', 'Деҳқонобод', 'Дўстлик', 'Душанбе', 'Жалолобод', 'Жамбул', 'Жиззах', 'Жомбой',
        'Зарафшон', 'Зомин', 'Каттақўрғон', 'Конибодом', 'Конимех', 'Косон', 'Косонсой', 'Марғилон', 'Мингбулоқ',
        'Муборак', 'Мўйноқ', 'Навоий', 'Наманган', 'Нукус', 'Нурота', 'Олмаота', 'Олот', 'Олтиариқ', 'Олтинкўл',
        'Пахтаобод', 'Поп', 'Риштон', 'Сайрам', 'Самарқанд', 'Таллимаржон']
for regff in regs:
    choos_city_btn.insert(InlineKeyboardButton(text=regff, callback_data=regff))
choos_city_btn.add(InlineKeyboardButton(text="⬅️", callback_data="⬅️"))
choos_city_btn.insert(InlineKeyboardButton(text="➡️", callback_data="➡️"))

choos_city_btn1 = InlineKeyboardMarkup(row_width=2)
regs = ['Тахтакўпир', 'Термиз', 'Томди', 'Тошкент', 'Тошҳовуз', 'Туркистон', 'Туркманобод', 'Тўрткўл', 'Узунқудуқ', 'Урганч', 'Ургут', 'Ўсмат', 'Учтепа', 'Учқудуқ', 'Учқўрғон', 'Ўш', 'Ўғиз', 'Фарғона', 'Хазорасп', 'Хива', 'Хонобод', 'Хонқа', 'Хўжанд', 'Хўжаобод', 'Чимбой', 'Чимкент', 'Чортоқ', 'Чуст', 'Шаҳрихон', 'Шеробод', 'Шовот', 'Шуманай', 'Янгибозор', 'Ғаллаорол', 'Ғузор', 'Қарши', 'Қарши', 'Қизилтепа', 'Қоракўл', 'Қоровулбозор', 'Қува', 'Қумқўрғон', 'Қўнғирот', 'Қўрғонтепа', 'Қўқон']
for regff in regs:
    choos_city_btn1.insert(InlineKeyboardButton(text=regff, callback_data=regff))
choos_city_btn1.add(InlineKeyboardButton(text="⬅️", callback_data="⬅️"))
choos_city_btn1.insert(InlineKeyboardButton(text="➡️", callback_data="➡️"))