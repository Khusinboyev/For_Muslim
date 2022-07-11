import pytz
import datetime
from handlaers.functions import *
from databas import *
from key import *
from buttons.mButtons import *

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
	user_id = message.chat.id
	sql.execute("""CREATE TABLE IF NOT EXISTS users ("user_id"  INTEGER,"date"  INTEGER, "lang" INTEGER);""")
	check = sql.execute(f"""SELECT user_id FROM users WHERE user_id = {user_id}""").fetchone()
	if check == None:
		sana = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
		sql.execute(f"""INSERT INTO users (user_id, date, lang) VALUES ('{user_id}', '{sana}', '{message.from_user.language_code}')""")
		db.commit()
	enter_btn1 = types.InlineKeyboardMarkup(row_width=1)
	enter_btn1.add(InlineKeyboardButton("🕋 Muslumon bo'lsangiz kiring 🕋", callback_data="enter1"))
	sql.execute("SELECT id FROM channels")
	rows = sql.fetchall()
	join_inline = types.InlineKeyboardMarkup(row_width=1)
	# try:
	title = 1
	for row in rows:
		all_details = await dp.bot.get_chat(chat_id=row[0])
		url = all_details['invite_link']
		join_inline.insert(InlineKeyboardButton(f"{title} - kanal", url=url))
		title+=1
	join_inline.add(InlineKeyboardButton("🔁 Tekshirish", callback_data='check'))

	if await functions.check_on_start(message.chat.id):
		await message.answer(f"""Assalomu alaykum <b>{message.from_user.first_name}</b>\n\n\nBot faqat muslummonlar uchun""", reply_markup=enter_btn1)
	else:
		await message.answer("Botimizdan foydalanish uchun kanalimizga azo bo'ling", reply_markup=join_inline)
	# except:
	# 	sql.execute("SELECT id FROM channels")
	# 	name = ""
	# 	for row in sql.fetchall():
	# 		id = row[0]
	# 		name += str(id)+" " + "\n"
	# 	admins = handlaers.admin_panel.Admin
	# 	for admin in admins:
	# 		await dp.bot.send_message(chat_id=admin, text=f"Botda muammo bor. Siz botga ulagan kanallarni tekshirib ko'ring, agar bot botga ulangan kanallarga admin bo'lmasa bot ishlamaydi\n\n\n\nBotga ulangan kanallar: \n{name}")
	# 	await message.reply("Muammo yuzasidan adminga murojaat qiling: @coder_admin_py")


@dp.callback_query_handler(text="check")
async def check(call: CallbackQuery):
	enter_btn1 = types.InlineKeyboardMarkup(row_width=1)
	enter_btn1.add(InlineKeyboardButton("🕋 Muslumon bo'lsangiz kiring 🕋", callback_data="enter1"))
	user_id = call.from_user.id
	print(user_id)
	if await functions.check_on_start(user_id):
		await call.answer()
		await call.message.edit_text(f"""Assalomu alaykum <b>{call.from_user.first_name}</b>\n\n\nBot faqat muslummonlar uchun""", reply_markup=enter_btn1)
	else:
		await call.answer(show_alert=True, text="Botimizdan foydalanish uchun kanalimizga azo bo'ling")

