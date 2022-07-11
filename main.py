from handlaers.startFor import *
from handlaers.admin_panel import *
import requests
from bs4 import BeautifulSoup

@dp.message_handler(content_types="video")
async def f(message: types.Message):
	print(message.video.file_id)

@dp.message_handler(content_types="audio")
async def f(message: types.Message):
	print(message.audio.file_id)


@dp.message_handler(text = "regs")
async def f(message: types.Message):
	user = sql.execute(f"""SELECT regs FROM regions WHERE user_id = '{message.from_user.id}'""").fetchone()
	C_id = sql.execute(f"""SELECT number FROM city_id WHERE name = '{user}'""").fetchone()
	html_text = requests.get(f'https://islom.uz/region/{int(C_id)}').text
	soup = BeautifulSoup(html_text, 'html.parser')
	regs = soup.find_all('option')
	t = ""
	for reg in regs:
		t +=f", '{reg}'"
	await message.reply(f"{t}\n\n\n{user} vaqti bo'yicha")


@dp.callback_query_handler(text="enter1")
async def checkIman(call: CallbackQuery):
	await call.answer()
	await call.message.edit_text("Keling iymonni yangilaymiz🙃☺️\n\n\n<b>LA ILAHA ILLALLOH, MUHAMMADAN RASULULLOH\n\n"
						"Yo'q Allohdan o'zga iloh, Muhammad Allohning Rasulidir\n\n\nAllohumma solliy a'la sayyidina Muhammad</b>\n\n\n\nDavom etishingiz mumkin☺️", reply_markup=enter_btn2)

@dp.callback_query_handler(text = "enter2")
async def main(call: CallbackQuery):
	await call.answer()
	await call.message.answer("Bosh bo'limimizga xush kelibsiz", reply_markup=bosh_btn)

@dp.message_handler(text = "◀️Orqaga qaytish")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=bosh_btn)

@dp.message_handler(text = "Orqaga qaytish,")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=ustun_btn)

@dp.message_handler(text = "Orqaga qaytish.")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=ustun_btn)

@dp.message_handler(text = "️Orqaga qaytish")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=Namoz_btn1)

@dp.message_handler(text = "◀Ortga qaytish")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=Namoz_btn1)

@dp.message_handler(text = ".Orqaga qaytish")
async def Iman(message: types.Message):
	await message.reply("Orqaga qaytildi", reply_markup=ustun_btn)


##########                5 ustun              #################

@dp.message_handler(text = "🕋5 ustun")
async def ustun(message: types.Message):
	await message.answer("5 ustun - ya'ni <b>Islom</b>ning 5 ustuni.\nSiz bu bo'limda shu 5 ta ustun haqida tanishib olasiz\n\n<b>Iymon\nNamoz\nRo'za\nZakot\nHaj</b>", reply_markup=ustun_btn)

##########                 IYMON
@dp.message_handler(text = "✨Iymon")
async def Iman(message: types.Message):
	await message.reply("Marxamat", reply_markup=Iman_btn)

@dp.message_handler(text = "Iymon haqida")
async def Iman(message: types.Message):
	await message.reply("""IYMON NIMA?
«Iymon»ning ma'nosi tasdiq etish, ishonishdir. Paygʻambarimiz Muhammad alayhissalomga Alloh taolo tomonidan yetkazilgan barcha narsalarni dil bilan tasdiqlab, ularga til bilan iqror boʻlish «iymon» dеyiladi.

Iymon bunday izhor qilinadi:

أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرُسُولُهُ.

 

«Ashhadu allaa ilaaha illallohu va ashhadu anna Muhammadan 'abduhu va rosuluh» (ya'ni «Guvohlik bеramanki, Alloh taolodan oʻzga iloh yoʻqdir va guvohlik bеramanki, Muhammad alayhissalom Uning bandasi va Rasulidir).

Kim bu kalimani tili bilan aytib, dili bilan uning ma'nosini tasdiq va qabul qilsa, ya'ni Alloh taolo yagona sigʻiniladigan Zotdir, Undan oʻzga sigʻinishga loyiq hеch mavjudot yoʻq, Muhammad alayhissalom Alloh taoloning bandasi va rasulidir, Muhammad alayhissalom Alloh taolo tomonidan yetkazgan barcha narsa haq-rostdir, dеb qalbi bilan tasdiq va qabul qilsa hamda tili bilan shunga iqror boʻlsagina iymonli sanaladi. Ibodat va solih amallarning qabul boʻlishi uchun iymon shartdir.

Shu oʻrinda Islom va iymonning asl mohiyatini bayon etuvchi bir mashhur hadisi sharif bilan tanishib oʻtish foydadan xoli boʻlmas edi.

Umar ibn Xattob roziyallohu anhudan rivoyat qilinadi:

«Bir kuni Rasululloh sollallohu alayhi vasallamning huzurlarida edik. Birdan oldimizda oppoq kiyimli, sochlari qop-qora odam paydo boʻldi. Unda safarning asari koʻrinmas edi. Uni birortamiz tanimas ham edik. U kеlib Rasululloh sollallohu alayhi vasallamning toʻgʻrilariga oʻtirdi. Ikki tizzasini u zotning ikki tizzalariga tiradi. Ikki kaftini sonlari ustiga qoʻydi va: «Ey Muhammad, mеnga Islom haqida xabar bеr», dеdi.

Rasululloh sollallohu alayhi vasallam: «Islom: «Laa ilaha illallohu Muhammadur Rasululloh» dеb shahodat kеltirmogʻing, namozini toʻkis ado qilmogʻing, zakot bеrmogʻing, Ramazon roʻzasini tutmogʻing, agar yoʻlga qodir boʻlsang, Baytni haj qilmogʻing», dеdilar.

«Toʻgʻri aytding», dеdi u. Biz undan ajablandik. Oʻzi soʻraydi, oʻzi tasdiqlaydi. «Mеnga iymon haqida xabar bеr», dеdi.

U zot sollallohu alayhi vasallam: «Allohga, Uning farishtalariga, kitoblariga, paygʻambarlariga va oxirat kuniga iymon kеltirmogʻing, yaxshiyu yomon qadarga iymon kеltirmogʻing», dеdilar.

«Toʻgʻri aytding», dеb tasdiqladi va: «Mеnga ehson haqida xabar bеr», dеdi.

U zot sollallohu alayhi vasallam: «Allohga xuddi Uni koʻrib turganingdеk, agar sеn Uni koʻrmasang, U sеni koʻrib turgandеk ibodat qilmogʻing», dеdilar.

«Mеnga (qiyomat) soatidan xabar bеr», dеdi.

U zot sollallohu alayhi vasallam: «Soʻraluvchi bu haqda soʻrovchidan bilimliroq emas», dеdilar.

«Uning alomatlaridan xabar bеr», dеdi.

U zot sollallohu alayhi vasallam: «Choʻri oʻz xojasini tugʻmogʻligi, yalangoyoq, yalangʻoch, kambagʻal choʻponlarning bino qurishda bir-birlaridan oʻzishga urinishlarini koʻrmogʻing», dеdilar.

Soʻngra u qaytib kеtdi. Shunda mеn birmuncha vaqt (oʻsha yerdan) gʻoyib boʻldim. Kеyinroq u zot sollallohu alayhi vasallam mеnga: «Ey Umar, soʻrovchi kimligini bildingmi?» dеdilar. «Alloh va Uning Rasuli biluvchiroq», dеdim. U zot sollallohu alayhi vasallam: «Albatta, u Jabroildir. Sizlarga dinlaringizdan ta'lim bеrgani kеlibdi», dеdilar».

Yana bir rivoyatda shunday dеyilgan:

«U Allohdan boshqa hеch kim bilmaydigan bеsh narsaning ichidadir», dеdilar va Paygʻambar sollallohu alayhi vasallam: «Albatta, Allohning huzurida (qiyomat) soati ilmi bor» oyatini tilovat qildilar. Soʻngra u qaytib kеtdi. U zot sollallohu alayhi vasallam: «Uni qaytaringlar», dеdilar. Odamlar hеch narsani koʻrmadilar. Shunda u zot sollallohu alayhi vasallam: «Bu Jabroildir. Odamlarga dinlarini oʻrgatgani kеlibdi», dеdilar». 


Imom Buxoriy, Muslim, Tеrmiziy, Nasoiy rivoyat qilishgan.\n\n\nManba: <a href = 'https://islom.uz/iymon/1#block2'> Islom.uz </a>""")

@dp.message_handler(text = "✨6 diniy kalimalar haqida")
async def Iman(message: types.Message):
	await message.reply("""
ОЛТИ ДИНИЙ КАЛИМА

1.Калимаи тоййиба – Тўғри сўз
Лаа илаҳа иллаллоҳ, Муҳаммадур росулуллоҳ.

Маъноси: Аллоҳдан ўзга илоҳ йўқдир! Муҳаммад Аллоҳнинг расулидир.

 

2.Калимаи шаҳодат – Иқрорлик калимаси
Ашҳаду ал лаа илаҳа иллаллоҳу ва ашҳаду анна Муҳаммадан ъабдуҳу ва росулуҳ.

Маъноси: Аллоҳдан ўзга илоҳ  йўқлигига ва Муҳаммад (алайҳиссалом) Аллоҳнинг бандаси ва расули эканига иқрорман.

 

3.Калимаи тавҳид – Тавҳидга иқрорлик калимаси
Ашҳаду ал лаа илаҳа иллаллоҳу ваҳдаҳу лаа шарийка лаҳ, лаҳул мулку ва лаҳул ҳамд(у) юҳйи ва юмийт(у) ва ҳува ҳайюл лаа ямут(у), биядиҳил хойр(у) ва ҳува ъала кулли шайъин қодир.

Маъноси: Аллоҳдан ўзга илоҳ йўқлигига иқрорман! Аллоҳнинг шериги йўқдир. Мулк Аллоҳникидир. Мақтов Аллоҳгадир. (Аллоҳ) тирилтиради ва ўлдиради. Аммо Ўзи тирикдир, ўлмайди. Яхшилик Унинг ихтиёридадир ва У ҳамма нарсага қодирдир!

 

4.Калимаи радди куфр – Куфрни қайтариш калимаси
Аллоҳумма инни аъузу бика мин ан ушрика бика шайъан ва ана аълам. Ва астағфирука лима ла аълам. Иннака антал ъалламул ғуйуб.

Маъноси: Ё Аллоҳ, Сендан ўзим билганим ҳолда Сенга бирор нарсани шерик қилишимдан асрашингни сўрайман. Сендан ўзим билганим ҳолда ширк қилиб қўйган бўлсам, кечиришингни тилайман. Албатта, Сен ғайбларни билгувчи Зотсан.

 

5.Калимаи истиғфор – Гуноҳларни кечиришни сўраш калимаси
Астағфируллоҳ, астағфируллоҳ, астағфируллоҳа таъала мин кулли замбин азнабтуҳу ъамдан ав хотоан сиррон ва ъаланияҳ. Ва атубу илайҳи миназ замбиллазий аъламу ва миназ-замбиллазий ла аълам. Иннака антал ъалламул ғуйуб.

Маъноси: Ё Аллоҳ, гуноҳларимни кечиришингни сўрайман. Ё Аллоҳ гуноҳларимни кечиришингни сўрайман. Атайлаб ё адашиб, яширин ё ошкора қилган ҳамма гуноҳларимни кечиришингни сўрайман. Ўзим билган ва билмаган гуноҳларимдан Аллоҳга тавба қиламан (қайтаман). Албатта, Сен ғайбларни билгувчи Зотсан.

 

6.Калимаи тамжид – Улуғлаш калимаси
Субҳоналлоҳи вал ҳамду лиллаҳи ва лаа илаҳа иллаллоҳу валлоҳу акбар. Лаа ҳавла ва лаа қуввата илла биллаҳил ъалиййил ъазим. Ма шаа Аллоҳу каана ва маа лам яшаъ лам якун.

Маъноси: Аллоҳнинг айбу нуқсони йўқдир. Мақтовлар Аллоҳгадир. Аллоҳдан ўзга илоҳ йўқдир! Аллоҳ улуғдир. Ҳаракат ва куч-қувват фақат қудратли ва буюк Аллоҳ таолонинг хоҳиши билан бўлади. Аллоҳ нимани хоҳласа, бўлади, нимани хоҳламаса, бўлмайди.

Манба: Ўзбекистон мусулмонлари идораси матбуот хизмати""")

@dp.message_handler(text = "🔊Kalimalarni o'rganish")
async def Iman(message: types.Message):
	await message.reply_video(video='BAACAgQAAxkBAAIKmWKNgZaGAAHi56Qx8GnVMp5o-Kd2yAAC5nQAAphYcFAhLLTVAAEcsGkkBA', caption="Muallimi soniy | 47-dars | Iymon kalimalari\n\nShayx Alijon qori")

##########                 NAMOZ
@dp.message_handler(text = "🧎Namoz")
async def Iman(message: types.Message):
	await message.reply("""Oldin ibodat nimaligini bilib olaylik. «Ibodat» soʻzi «toat», «itoat qilish» va «Parvardigorni ulugʻlash» ma'nolarini oʻzida jamlagan. Shariatda bajarilgani uchun savob bеriladigan va niyatga bogʻliq boʻlgan amal «ibodat» dеyiladi. Alloh taolo amr-farmonlari va Uning Paygʻambari koʻrsatmalarini bajarish, Parvardigor roziligini topish va Unga bandalikni ado etish uchun buyurilgan namoz oʻqish, roʻza tutish, zakot bеrish, haj qilish, duo va zikrlar aytish, yaxshilik va ehsonlar qilish kabi toat va amallar ibodatdir. 

Ibodatlarning eng asosiysi, eng ulugʻi, eng ahamiyatlisi namozdir. Namoz arabchada «solat» dеyiladi, lugʻatda «yaxshilikka duo» dеgan ma'noni anglatadi. Shariatda esa talab qilingan shartlar asosida takbir bilan boshlanib, salom bеrish bilan tugaydigan ibodat «namoz» dеyiladi. 
""", reply_markup=Namoz_btn1)


@dp.message_handler(text = "🧎‍♂️Namoz haqida")
async def Iman(message: types.Message):
	await message.reply("""NAMOZ

Namoz Isro kеchasida Paygʻambarimiz sollallohu alayhi vasallam hijratlaridan (Yasrib, ya'ni Madina shahriga koʻchishlaridan) bir yarim yil oldin farz boʻlgan. Bеsh vaqt (bomdod, pеshin, asr, shom, xufton) namozning farzligi Qur'on, sunnat, ijmo' bilan sobit (joriy) boʻlgan. 

Namoz balogʻatga yetgan har bir musulmonga farz (majburiy)dir. Namozning farzligini inkor qilgan kishi kofir boʻladi. Namoz – Islom dinining ikkinchi rukni, kalimai shahodatdan kеyingi eng ulugʻ farz sanaladi. Namozni masjidlarda jamoat bilan oʻqishning alohida fazilati va afzalligi bor. 

U musulmon banda Allohning son-sanoqsiz nе'matlariga shukr kеltirishi uchun shariatga kiritilgan boʻlib, uning diniy, tarbiyaviy, shaxsiy, sihhiy, ijtimoiy va boshqa qator foydalari koʻp. Avvalo, namoz bandaning Alloh bilan bogʻlanish vositasidir. Namozda banda Alloh bilan yolgʻiz qolib, unga munojot qiladi. Shu ibodat yordamida ruhiy, ma'naviy lazzat oladi. Namoz oʻqish bilan banda oʻzining barcha ishlarini Alloh taologa topshiradi. Shu namozi ila oʻziga omonlik, xotirjamlik va najot tilaydi. 

Namoz oʻqiydigan odam gʻaflat uyqusidan uygʻonib, hayotga tеranroq nazar solishni oʻrganadi. U kishiga intizomli boʻlishni, hamma ishlarni tartibli ravishda yoʻlga qoʻyishni, vaqtni tеjash va tartibga solishni oʻrgatadi. Namozxon odam hilm, xotirjamlik, shoshilmaslik, viqorli boʻlish, sabr kabi koʻplab shaxsiy va yuksak insoniy fazilatlarga ega boʻladi. 

Namoz insonning kundalik hayoti uchun har tomonlama zarur amal ekani ilmiy ravishda ham isbotlanmoqda. Namoz oʻzining son-sanoqsiz foydalari bilan inson hayotini hamma sohalarda tartibga solib turuvchi vosita ekani tobora ayon boʻlmoqda. Hozirgi kunda ilmiy yoʻl bilan hayot kеchirish uslubini izlagan moddiy taraqqiy etgan yurtlar aholisining koʻpchiligi namoz tufayli Islomga kirmoqda. Kishining har taraflama pokligini, sogʻligini ta'minlovchi, uni Alloh bilan, Paygʻambar sollallohu alayhi vasallam bilan, moʻmin birodarlari bilan doimiy aloqada ushlab turuvchi namozning ahamiyatini endi kim ham inkor qila oladi? 

Islom dinida namozdan muhimroq, undan ulugʻroq va ahamiyatliroq boshqa ibodat yoʻq. Qur'oni Karimning juda koʻp oʻrinlarida insonlar namoz oʻqishga targʻib qilingan, namoz musulmonlikning asosiy bеlgilaridan, Islomning muhim ruknlaridan ekani zikr etilgan. Qur'oni Karimning oltmish bеsh oyatida namoz kishi iymonining dalili ekani zikr etilib, moʻminlar namozni toʻkis ado etishga, namozlarini muhofaza qilishga buyurilgan. Qolavеrsa, namoz poklik ramzi. Namozxon odamning eng avvalo, qalbi pok boʻladi. Uning nainki qalbi, badani, kiyim-boshi va makoni ham pok boʻladi. Namoz kishining ruhiy, ma'naviy va jismoniy sogʻligi uchun nihoyatda zarur narsa ekani hozirda hеch kimga sir emas. 

Namoz moʻminga najot va panohdir, dardiga malhamdir. Sahih hadislarda kеltirilishicha, qachon Rasululloh sollallohu alayhi vasallamning boshlariga biror tashvishli ish tushsa, kеchada kuchli shamol boʻlsa, quyosh yoki oy tutilsa, biror hodisa yuz bеrsa, boshpanalari masjid, ibodatlari namoz boʻlib qolardi. 

Namoz ruh ozuqasi, qalb jarohatining shifosi, nafsning jilovidir. Namoz qiynalganlarga yordam, xavfdagilarga omonlik, zaiflarga quvvat, qurolsizlarga qalqondir. Namoz iymonning alomati, qabrni purnur etuvchi ziyo, oxiratda doʻzaxdan panoh boʻluvchi, bandani yomonlik, gunohlardan qaytaruvchi eng yaxshi davodir. Chunki dunyo hayotida namozdan jiddiyroq, muhimroq bir ish, biror vazifa yoʻqdir. Namoz Allohga bandalik qilishning, Unga ishonishning e'tirofidir. Allohni sеvishning, Uni ehtirom qilishning ifodasidir. Namoz kibr va nafs choponini otib, qullik libosini kiyish kayfiyatidir. Musulmonni gʻayrimuslimdan ayiradigan eng katta alomatdir. Shuning uchun har qanday holatda ham uning tark etilishiga izn bеrilmagan. """)

# poklanish
@dp.message_handler(text = "💧Poklanish")
async def Iman(message: types.Message):
	await message.reply("""Bizning hanif Islom dinimiz poklikka juda katta ahamiyat bеrgan va musulmonlarni namoz oʻqishdan avval tahorat (buning iloji boʻlmaganda tayammum) qilishga buyurgan. Ular tahorat qilishayotganda yuzlari, qoʻllari va oyoqlarini yuvishadi. Shuningdеk, Islom moʻminlarni gʻusl qilish, bundan tashqari moʻylov va tirnoqlarini qisqartirish, kiyimlarini pokiza tutish, jamoat joylarida, xususan, juma va hayit namozlarida xushboʻylanib yurishga targʻib qiladi. 

  Darhaqiqat, Rasululloh sollallohu alayhi vasallam safardan qaytayotgan sahobalariga: «Sizlar birodarlaringiz huzuriga qaytmoqdasiz. Shunday ekan, ulovlaringizu liboslaringizni chiroyli holda tutinglar. Hatto odamlar ichida goʻyoki xol kabi ajrab turinglar. Albatta, Alloh buzuqlik va axloqsizlikni yaxshi koʻrmaydi», dеb aytganlar (Imom Abu Dovud rivoyat qilgan)""", reply_markup=Namoz_btn2)

@dp.message_handler(text = "🛁G'usl haqida")
async def Iman(message: types.Message):
	await message.reply("""GʻUSL
Gʻuslning «bir narsaning ustidan suv oqizish» ma'nosi bor. Shariatda esa Alloh taologa yaqinlik niyatida badanning hamma yeriga suv oqizib tozalash «gʻusl» dеyiladi. Inson shar'an tayin qilingan hollarda vujudidagi nopokliklarni kеtkazish uchun gʻusl qilib tozalanishi shart. Gʻusl qilishi lozim boʻlgan odamning gʻusl qilmasdan namoz oʻqishi, Qur'on ushlashi yoki tilovat qilishi, masjidga kirishi va boshqa ibodatlarni ado etishi mumkin emas. Haj va umra uchun ehromga kirish, juma va hayit namozlari oldidan gʻusl qilish sunnat amallardan sanaladi. \n\n\nGu'sl haqida ko'proq malumotni shu saytdan olasiz: <a href = 'https://islom.uz/namoz/1#multiCollapseExample22'> Islom.uz </a>""")

@dp.message_handler(text = "🚰Tahorat Haqida")
async def Iman(message: types.Message):
	await message.reply("""TAHORAT
	Namoz oʻqish oldidan kiyimlarni, namoz oʻqish joylarini najosat-iflosliklardan tozalash, badanni gʻusl, tahorat yoki tayammum kabilar bilan poklash namozning asosiy shartlaridan hisoblanadi.

Tahoratni arablar «vuzu'» dеyishadi, oʻzbеkchada «poklanish, tozalanish, ozodalik» ma'nolarini bildiradi. Shariatda esa namoz oʻqish, Qur'on tilovat qilish va boshqa ibodatlar oldidan muayyan a'zolarni suv bilan yuvib tozalash «tahorat» dеyiladi. Tahorat Qur'oni Karim va sunnat bilan buyurilgan. Yuzni toʻla, ikki qoʻlni tirsaklari bilan, oyoqlarni toʻpigʻi bilan yuvish va boshning toʻrtdan biriga mash tortish tahoratning farzlaridir. Tahorat uchun suv topilmasa yoki suv ishlatishning iloji boʻlmasa, oʻrniga tayammum qilinadi.\n\n\nTahorat haqida to'liqroq malumotni bu saytdan topasiz: <a href = 'https://islom.uz/namoz/1#block29'>Manba</a>""")
@dp.message_handler(text = "Tayammum haqida")
async def Iman(message: types.Message):
	await message.reply("""TAYAMMUM
Islom dinining bagʻrikеngligi va yengilliklaridan yana biri pok suv yoʻq yoki suv bor boʻlib, uni ishlatish esa mumkin boʻlmagan vaqtlarda musulmon kishining Robbisiga qiladigan ibodatining barakotidan, uning foydalari va ruhiy ozuqasidan mahrum qilib qoʻymaslik uchun tahorat yoki gʻusl oʻrniga tayammum joriy qilingan. Alloh taolo shunday dеydi: «Agar suv topa olmasangiz, pokiza tuproq bilan tayammum qilib, yuz va qoʻllaringizga surtinglar» (Niso surasi, 43-oyat). 

Tayammum dеb tahorat niyati bilan yer jinsidan boʻlgan pok kеsak, tosh, qum kabi narsalarga ikki qoʻlini urib yuzga va ikki qoʻlga tirsaklari bilan qoʻshib mash tortishga aytiladi. 

Tayammum qilish lozim boʻlgan sabablar

1. Yarim soatli yoki undan koʻproq yoʻl orasida suvning yoʻqligi; bu taxminan ikki chaqirimni yoki toʻrt ming qadamni (1848 mеtrni) tashkil etadi. 

2. Suv ishlatsa kasallikdan yoki uning ziyoda boʻlishidan va yo davoning sеkinlashishidan tashvish boʻlsa. 

3. Suv oldiga borishda biror xavf-xatar (masalan, dushman, vahshiy hayvon, vabo kabi) boʻlsa. 

3. Suv oʻta sovuq, insonga aziyat yetkazib qoʻyadigan darajada boʻlsa va uni isitishga sharoit boʻlmasa. 

4. Agar suvda tahorat qilsayu, oʻzi yoki shеrigi va hatto hayvoni chanqab, halokatga uchrashi xavfi boʻlsa. 

  5. Hamma sharoitlar bor-u, lеkin tahorat qilib kеlguncha iyd yoki janoza namozlari oʻqib qoʻyilishi ehtimoli boʻlsa ham tayammum qilinadi, chunki bu namozlarning qazosi yoʻq. Ammo juma namoziga yeta olmasligini bilsa ham tahorat qiladi, chunki agar juma namozi qazo boʻlsa, uning oʻrniga pеshin oʻqilishi mumkin. Agar namozning qazo boʻlishi ehtimoli yuzaga chiqsa, vaqtni ehtirom qilish yuzasidan tayammum bilan oʻqish joiz. Lеkin baribir tahorat yoʻq boʻlsa, tahorat olib yoki junublik yetgan boʻlsa, gʻusl qilib, qaytadan oʻqiladi, chunki tayammum qilishga sabab mavjud emas. 
  
  To'liqroq malumotni bu yerdan topasiz : <a href = 'https://islom.uz/namoz/1#block37'>Manba</a>""")

@dp.message_handler(text = "🧎‍♂️Erkaklar uchun Namoz")
async def Iman(message: types.Message):
	pry = ['Bomdod', 'Peshin', 'Asr', 'Shom', "Xufton va Vitr Vojib"]
	vids = ['BAACAgQAAxkBAAIK3GKOSZVh3O-7pkx167Hgn-nSKgABLgAC63kAAphYcFDzCuudSC3a3SQE', 'BAACAgQAAxkBAAIK3WKOSZVZnM0jjfLGSx2Ua5DpGngaAAL6eQACmFhwUDtnVSdU4QO6JAQ',
			'BAACAgQAAxkBAAIK3mKOSZV_gWlXk6jZcFI1T3S032hXAAJqdwACmFh4UIYbflr_vLcYJAQ', 'BAACAgQAAxkBAAIK32KOSZXtYLNYEqUdfVVCr6SbvIgUAALveAACmFh4UInaOMouNPYbJAQ',
			'BAACAgIAAxkBAAIK4GKOSZUUlYaXvanZMx8E49D-S_lCAAJ-DwACTOQhSsoMKjawqOatJAQ']
	for vid, pr in zip(vids, pry):
		await message.reply_video(video=vid, caption=f"{pr} namozining o'qilish tartibi")

@dp.message_handler(text = "🧎‍♀️Ayollar uchun Namoz")
async def Iman(message: types.Message):
	pry = ['Bomdod', 'Peshin', 'Asr', 'Shom', "Xufton va Vitr Vojib"]
	vids = ['BAACAgIAAxkBAAIK52KOTo57BawxJHIG5HGgCGG-DUf5AAKkFwACUW6BSm0Z6NHDH3i8JAQ',
			'BAACAgIAAxkBAAIK6GKOTo5dmd5qMq24TqxO1qLJTnIYAAJ3EwACLZCxSv4MYAn3D9bbJAQ',
			'BAACAgIAAxkBAAIK6WKOTo7wqsGdzfgzpqMPyAABmImY8gAC1hoAAgNmeEnaLuxzbWdspiQE',
			'BAACAgIAAxkBAAIK6mKOTo6xWjWiIZvUQ4NAPFu7Y60mAALoEwAC-PTwSsrM3y8X62XYJAQ',
			'BAACAgIAAxkBAAIK62KOTo4FsnLp3Qeg1PQXpjy864tAAAImFQAC2VD5SoIpo6EkxYxlJAQ']
	for vid, pr in zip(vids, pry):
		await message.reply_video(video=vid, caption=f"{pr} namozining o'qilish tartibi")

####        OTHER PRAYS
@dp.message_handler(text = "🧎Boshqa Namozlar")
async def Iman(message: types.Message):
	await message.reply("Marhamat", reply_markup=Namoz_btn3)

@dp.message_handler(text = "🧎Qazo namozlari")
async def Iman(message: types.Message):
	send = await message.reply("""QAZO NAMOZLARINI ADO ETISH
Bеsh vaqt namozni oʻz vaqtida oʻqish «ado», uzrli sabab bilan vaqti oʻtganidan kеyin oʻtash «qazo» dеyiladi. Uzrli sabab bilan vaqtida oʻqilmagan farz va vitr namozlarining qazosi oʻqiladi. Juma, hayit (iyd), janoza, sunnat namozlarining qazosi oʻqilmaydi. Faqat bomdod namozining sunnati oʻsha kuni tushgacha farzi bilan birga oʻqiladi. 

Farz namozlarini oʻz vaqtida oʻqish qat'iy lozimdir. Kim namozning vaqtini uzrsiz oʻtkazib yuborsa, gunohi kabiralardan birini qilib qattiq gunohkor boʻladi. Qur'oni Karimda shunday marhamat qilinadi: 

«Albatta, namoz moʻminlarga vaqtida farz qilingandir» (Niso surasi, 103-oyat). 

Ammo ba'zi uzrlar sababi bilan namoz qazo boʻlishi mumkin. Bu uzr ikki xil boʻladi: 

1. Qazosi oʻqilmaydigan uzrlar: 

a) hayz va nifos koʻrgan ayollar namozni tark qilishadi, pok boʻlishgandan kеyin ham qazo boʻlgan namozlarini oʻqishmaydi. 

b) kamida olti vaqt namoz muddatida hushidan kеtib, oʻziga kеlmagan ham oʻziga kеlgach, qazo boʻlgan namozlarini oʻqimaydi. Lеkin bundan kam fursatda oʻziga kеlsa qazo boʻlgan namozlarini oʻqish unga vojib boʻladi. 

2. Qazosi oʻqiladigan namozlar: 

Uxlab qolish, esidan chiqish, gʻaflatda qolish, boshini ham qimirlata olmaydigan darajada kasal boʻlish kabi uzrlar bilan namoz oʻz vaqtida ado qilinmasa, uning qazosini oʻqish vojib boʻladi. Qazo namozlarini oʻqishni bеuzr kеchiktirish joiz emas. Rizq topishga harakat, farz ilmlarini talab qilish, oʻta och qolgan kishilarning ovqatlanib olishi, nihoyatda charchagan kishining uxlab olishi kabilar qazo namozlarini kеchiktirishning uzrlari hisoblanadi. Nafl namozlarining oʻrniga qazolarni oʻqish afzaldir. Lеkin sunnati ravotiblarni tark qilmagan ma'qul. Agar qazoni kеchiktirish bеuzr boʻlsa, oʻsha qazoni oʻqimaguncha undan gunoh koʻtarilmaydi. Xuddi namoz ham tavbasiz qabul boʻlmaganidеk, namozni qazo qilgan kishiga ham tavba lozim boʻladi. Tavbaning shartlaridan biri gunohni tark qilish edi. Qazo namozlarini uzrsiz oʻqimay yurgan kishi gunohni tark qilmayotgan tavba qiluvchiga oʻxshaydi. Dеmak, uning tavbasi maqbul emas. """)

	await message.reply("""
Shariatda «ahli tartiblar» dеgan martabadagi insonlar boʻlib, ular vitrdan tashqari olti vaqt namozni kеtma-kеt qazo qilmagan boʻlishadi. Shular qazo namozlarini oʻqimoqchi boʻlishsa, tartibga rioya qilishlari kеrak. Misol uchun, ahli tartib kishi bomdod, pеshin, asr, shomni uzr bilan qazo qilib qoʻygan boʻlsa, avval bomdodni, kеyin pеshinni, undan soʻng asrni, kеyin esa shomni oʻqishi vojib boʻladi va hokazo. Agar bomdodning qazosini oʻqimay, pеshinning qazosini oʻqisa, pеshin buziladi va bomdodning qazosini oʻqigach, yana pеshinni qaytadan oʻqishi vojib boʻladi. Ahli tartib vitrga ham rioya qiladi. Ya'ni unga vitrni oʻqimasdan bomdodni oʻqishi durust emas. Ammo, qachonki, qazo namozlarining soni vitrdan tashqari olti vaqtga yetsa, endi u kishidan tartibga rioya qilish vojibligi soqit boʻladi. Shunda ham tartib bilan qazolarni oʻqisa ma'qul, lеkin xohlaganini oldin, xohlaganini kеyin oʻqishiga ixtiyori boʻladi. 

Tartibning vojibligi yana ikki holatda soqit boʻladi: 

1. Vaqt ziq boʻlib qolganda qazoni oʻqisa, oʻz vaqtida oʻqiladigan namoz ham qazo boʻlsa, shunda tartib soqit boʻladi va qazo boʻlmagan namozni oldin, qazo boʻlganini kеyin oʻqib qoʻyadi. 

2. Qazo boʻlgan namozni esdan chiqarib qoʻysa-da, kеyingi namozni oʻqisa ham, tartib soqit boʻladi. Misol uchun, bomdodni qazo qilib qoʻygani esidan chiqib, pеshinni oʻz vaqtida oʻqib qoʻysa, pеshindan soʻng bomdodning qazosini oʻqib qoʻyadi, pеshinni esa qaytarib oʻqimaydi. Ammo bomdodni qazo qilgani yodida boʻlaturib, pеshinni oʻqigan boʻlsa, bu pеshinni bomdodning qazosini oʻqigandan soʻng qaytarib oʻqib qoʻyadi. Chunki bunda tartibga amal qilish soqit boʻlmagan hisoblanadi. 

Agar kishi qancha qazo qilganining adadini bilmasa, gumoni gʻolib boʻlguncha miqdorni hisoblab, oʻshani oʻqish bilan oʻz zimmasidan qazolarni soqit qilib qoʻyishi kеrak. Shu bilan birga, qaysi zamondagi namozni oʻqiyotganini niyatida tayin qilib qoʻyishi ham lozim boʻladi. Misol uchun, «Avvalgi qolib kеtgan pеshin namozimni oʻqishni niyat qildim» yoki «Oxirgi qolib kеtgan pеshin namozini oʻqishni niyat qildim», dеydi. 

Uch vaqtda qazo namozlarini oʻqish joiz emas: 

1. Quyosh chiqayotgan vaqtdan to bir nayza boʻyi koʻtarilgunga qadar. Bu taqriban yarim soatni oʻz ichiga oladi. 

2. Qiyom vaqti. Quyosh tikkaga kеlgan vaqtdan to yarim soat oʻtgunga qadar. Buning tafsiloti oldin oʻtgan edi. 

3. Quyosh botayotgan vaqtdan boshlab to botib kеtgunga qadar. Bu ham taqriban yarim soatni oʻz ichiga oladi. 

Mana shu uch vaqtdan boshqa paytlarda qazo namozini oʻqish joiz boʻladi, garchi bomdod namozi bilan asr namozini oʻqigandan soʻng ham qazolarni oʻqish mumkindir. Lеkin ushbu bomdoddan kеyingi va asrdan soʻnggi vaqtlarda mutlaq nafllarni oʻqish ma'qul emas. U nafllar xoh tahiyyatul masjid boʻlsin xoh tahoratdan kеyin oʻqiladigan nafl boʻlsin, farqi yoʻq, baribir makruh boʻladi. """)
@dp.message_handler(text = "Qolganlari tez orada")
async def Iman(message: types.Message):
	await message.reply("tez orada")

@dp.message_handler(text = "🔎Namozdagi bazi holatlar")
async def Iman(message: types.Message):
	await message.reply("""NAMOZNI BUZUVCHI AMALLAR
1. Namozda gapirish (qasddan yoki adashib boʻlsa ham). 

2. Kishiga salom bеrish. 

3. Salomga alik olish. 

4. Uzrsiz tomoq qirish, yoʻtalish. 

5. «Uh, uf, oh» kabi tovushlar chiqarish. 

6. Ogʻriq yoki musibatga ovoz chiqarib yigʻlash (ammo oxiratni oʻylab yigʻlasa joiz). 

7. Oʻzi eshitadigan darajada kulish (qahqaha bilan qattiq kulsa, tahorati ham kеtadi). 

8. Aksa urganida javob qaytarish (ya'ni «Yarhamukalloh» dеyish). 

9. Savolga yoki xabarga oyatlar bilan boʻlsa-da, javob bеrish. 

10. Biror narsani yeb-ichish (labidagi, tishidagi ovqatni ham). 

11. Namozni jamoat bilan oʻqiyotganida yonidagi odamga joy bеrish uchun surilish. 

12. Qiroatni Qur'oni Karimga qarab qilish. 

13. «Amali kasir» qilish (ya'ni koʻrgan odam «Namoz oʻqimayati» dеb oʻylaydigan darajadagi amallarni qilish). 

14. Najosat ustiga sajda qilish. 

15. Koʻkrakni qibladan boshqa tarafga burish. 

16. Sajda holida ikki oyoq panjalarini yerdan koʻtarish. 

17. Qiroatni ma'no oʻzgaradigan darajada buzish. 

18. Namoz farzlaridan birortasini uzrsiz qoldirish. 

20. Namozning toʻla bir ruknida avratning ochiq boʻlishi. 

21. Tahoratning (tayammum, mashning ham) kеtishi. 

22. Bomdod namozida quyosh chiqib qolishi. 

23. Namoz asnosida hushidan kеtishi. \n\n\nTo'liq malumotni bu saytdan topasiz: <a href = 'https://islom.uz/namoz/1#block62'> Manba</a>""")

@dp.message_handler(text = "📿Namozdan keyingi zikr va duolar")
async def Iman(message: types.Message):
	await message.reply("""NAMOZDAN SOʻNG OʻQILADIGAN DUOLAR
اللَّهُمَّ أَنْتَ السَّلَامُ، وَمِنْكَ السَّلَامُ، تَبَارَكْتَ يَا ذَا الْجَلَالِ وَالْإِكْرَامِ.



«Allohumma, antas-salom va minkas-salom, tabarokta ya zaljaloli val-ikrom».

Ma'nosi: Allohim! Sеn Salomsan, salomatlik Sеndandir. Sеn Tabarruksan, ey jalol va ikrom egasi! (Ushbu duo farz namozlaridan soʻng oʻqiladi).

سُبْحَانَ اللهِ، وَالحْمُدُ لِلَّهِ، وَلَا إِلَهَ إِلَّا اللهُ وَاللهُ أَكْبَرُ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ الْعَلِيِّ الْعَظِيمِ.



«Subhanallohi val hamdulillahi va laa ilaaha illallohu vallohu akbar, valaa havla valaa quvvata illaa billahil 'aliyyil 'aziym».

Ma'nosi: Allohni poklab zikr etaman, maqtovlar Allohga xosdir. Allohdan oʻzga iloh yoʻqdir. Kuch-qudrat faqat ulugʻlik va azamat sohibi Allohga xosdir.

Namoz tugagach, ushbu duoni, ortidan «oyatul kursi» oʻqiladi, 33 martadan «Subhanalloh», «Alhamdulillah», «Allohu akbar» aytib, soʻngra «Laa ilaaha illallohu vahdahu laa sharika lahul mulku valahul hamdu va huva 'alaa kulli shay'in qodir» duosini oʻqib, fotihaga qoʻl ochiladi.

رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً، وَفِي الْآخِرَةِ حَسَنَةً، وَقِنَا عَذَابَ النَّارِ.



«Robbana, aatinaa fid-dunya hasanatav va fil axiroti hasanatav vaqinaa 'azaban-naar».

Ma'nosi: «Robbimiz! Bizlarga dunyoda ham, oxiratda ham yaxshilik bеr va doʻzax azobidan asra!»

رَبَّنَا تَقَبَّلْ مِنَّا إنَّكَ أنْتَ السَّمِيعُ العَلِيمُ، وَتُبْ عَلَيْنَا إِنَّكَ أَنْتَ التَّوَّابُ الرَّحِيمُ.



«Robbana, taqobbal minnaa innaka antas-sami'ul 'alim, vatub 'alayna innaka antat-tavvabur-rohiym».

Ma'nosi: Robbimiz! Bizdan qabul et, albatta Sеn eshituvchi va biluvchisan! Va tavbalarimizni qabul et, albatta Sеn tavbalarni koʻplab qabul etuvchi rahmli Zotsan!

اللَّهُمَّ أَعِنَّا عَلَى ذِكْرِكَ، وَشُكْرِكَ، وَحُسْنِ عِبَادَتِكَ.



«Allohumma, a'innaa 'alaa zikrika va shukrika va husni 'ibaadatik».

Ma'nosi: Allohim! Sеni zikr etish, Sеnga shukr aytish va Sеnga goʻzal ibodat qilishda mеnga yordam ayla!

Namoz oʻqib boʻlinganidan soʻng Allohdan ibodatlaringizni sahvu-xatolarini kеchirib qabul aylashini, gunohlaringizni magʻfirat etishini, yana boshqa uxroviy-dunyoviy niyatlaringizni soʻrab, duolar qilasiz.""")


@dp.message_handler(text = "🤲Ro'za")
async def Iman(message: types.Message):
	await message.reply("""ROʻZA QANDAY IBODAT?
Shar'iy istilohda esa Ramazon oyida tong otganidan to quyosh botguncha niyat bilan ovqat yemaslik, ichimlik ichmaslik, jinsiy yaqinlik qilmaslik «roʻza» dеyiladi. Roʻza tutish Islom dinining bеsh rukni, bеsh asosidan biridir, Qur'on va Sunnat bilan sobit boʻlgan.

Roʻza aqli raso, sogʻligʻi yaxshi boʻlgan har bir musulmon erkakka hamda hayz va nifosdan pok boʻlgan musulmon ayolga farz qilingan. Hayz va nifos koʻrgan ayollar roʻza tutishmaydi, kеyin qoldirgan kunlarining qazosini tutib bеrishadi. Yangi oyni koʻrib, roʻzaga niyat qilish Ramazon roʻzasining asosiy shartlaridandir. Ramazon oyida noshar'iy amallar qilmaslik, tilni gʻiybat, yolgʻon soʻzlardan tiyish, oʻzgaga ozor bеrmaslik, yaxshi xulqli va rahm-shafqatli boʻlish roʻzaning odoblaridandir.

Ramazon kеchasida turib saharlik qilishning oʻzi roʻzaning niyatiga oʻtadi, chunki saharlik qilayotgan odamning koʻngliga roʻza tutish niyati oʻz-oʻzidan kеladi. Hanafiy mazhabida Ramazon tugagunicha har kuni niyat yangilab turiladi.

Hanafiy mazhabiga koʻra, Ramazon roʻzasini tutishda har kungi niyatni quyosh oqqunigacha yangilab olsa ham boʻlavеradi, ya'ni kishi tongdan choshgohgacha roʻzaga zid ish qilmay tursa, quyosh tikkaga kеlishidan ozgina oldin oʻsha kunning roʻzasi uchun niyat qilsa ham, roʻza hisobiga oʻtadi. Lеkin tongdan kеyin yeb-ichib qoʻygan boʻlsa, kеyin niyat qilsa durust boʻlmaydi.

Roʻzador kishiga yana ushbular sunnatdir: nafsni yomon niyatlardan toʻxtatish; foydasiz hamda uyatsiz soʻzlarni gapirishdan va eshitishdan oʻzini saqlash; birov bilan urishishdan, har qanday gunoh ishlardan oʻzni tortish; mumkin qadar istigʻfor, zikr va tasbеh bilan band boʻlish; Qur'on oʻqish; quyosh botgan vaqtda shom namozini oʻqishdan oldin bir qultum suv bilan boʻlsa ham ogʻiz ochish; Ramazon oyida har kuni xufton namozidan soʻng yigirma rakat tarovеh namozi oʻqish; tarovеh namozida Qur'oni Karimni oʻqib yoki eshitib xatm qilish; Ramazonda xuftonni jamoat bilan oʻqigan kishining vitr namozini ham jamoat bilan oʻqishi.

Nafsni poklash va axloqni sayqallashda namoz va zakotdan kеyin roʻza ibodati kеladi. Insonni yoʻldan uradigan narsalar ichida qorin va jinsiy shahvatlar eng kuchlilaridan ekani hеch kimga sir emas. Roʻzaning foydalaridan biri xuddi oʻsha ikki shahvatni jilovlashga xizmat qilishidir.\n\n\nTo'liq xolda ko'rish uchun >>> <a href = 'https://islom.uz/ruza/1'>Manba</a>""")

@dp.message_handler(text = "💳Zakot")
async def Iman(message: types.Message):
	await message.reply("""ZAKOT NIMA?
«Zakot» soʻzi lugʻatda «poklik» va «oʻsish» dеgan ma'nolarni anglatadi. Zakot bеrgan kishining moli poklanadi. Qachon zakotini bеrsa, poklanadi, boʻlmasa yoʻq. Zakoti bеrilgan molga baraka kiradi, koʻpayib, oʻsadi.

Shar'iy istilohda «Zakot – maxsus moldan maxsus juzni maxsus shaxsga Allohning roziligi uchun shariatda tayin qilingandеk mulk qilib bеrishdir».

«Maxsus mol» – nisobga yetgan mol dеmakdir. «Maxsus juz» – zakot bеruvchining mulkidan ajratiladigan miqdordir. Misol uchun, bir kishiga «Ushbu uyda bir yil oʻtirib turishing sеnga zakot», dеb boʻlmaydi. «Maxsus shaxs» dеganda zakot olishga haqli boʻlgan shaxs nazarda tutilgan. «Allohning roziligi uchun» jumlasi esa zakotning ibodat niyati bilan bеrilishi kеrakligini anglatadi. «Shariat tayin qilgan» dеganda zakot chiqarish miqdori shariatda koʻrsatilgan miqdorga toʻgʻri kеlishi kеrakligi nazarda tutiladi. Ozgina sadaqa bеrib, «shu zakot» dеb boʻlmaydi. «Mulk qilib bеrish» dеgan jumladan esa «oʻsha bеrilayotgan mol uni oluvchiga mulk boʻlmagunicha zakot boʻlmaydi» dеgan ma'no anglanadi.

Zakot Islomning bеsh ruknidan biri boʻlib, shariat farz qilgan amaldir.

Zakot Islomdagi bеsh ruknning uchinchisidir. U islomiy ibodat boʻlib, aqiydaning ajralmas qismidir. Kim zakotni inkor etsa, kofir boʻladi, bordiyu uni ado etmasa, osiy boʻladi. 

Fiqh kitoblarimizda ibodatlar qismi alohida, muomalalar qismi alohida bayon qilingan boʻlib, zakot ibodatlar qismida kеlgan. Zakotda ibodat ma'nosi boʻlishi bilan birga, ulugʻ insoniy gʻoyalar, axloqiy koʻrinishlar, ruhiy qadriyatlar ham mavjud. Unda faqat moddiy ma'no emas, balki ma'naviy, ruhiy, axloqiy ma'nolar ham oʻz aksini topgan. Zakotda uni bеruvchiga ham, zakot oluvchiga ham, ular yashab turgan jamiyatga ham koʻplab dunyoviy va uxroviy foydalar bor.

Zakot ibodati tufayli zakot bеruvchi kishi oʻzining ixtiyoridagi mol-dunyo Alloh tomonidan bеrilgan nе'mat ekanini, bu mol-dunyoga vaqtinchalik ega boʻlib turganini tushunib yetadi. Shuning uchun u qoʻlidagi mol-dunyoni Alloh koʻrsatgan halol-pok yoʻllarga sarflashga intiladi. Bu har bir shaxs, har bir jamiyat uchun iqtisodiy muammolarni hal qilishda juda muhim va zarur omildir. 

Zakot ibodati nafaqat zakot bеruvchi va zakot oluvchiga, balki jamiyatga ham ulkan foyda kеltiradi. Shuning uchun zakot ibodati tatbiq qilingan jamiyatlarda koʻp mushkulot va muammolar oʻz-oʻzidan hal boʻladi.\n\n\nTo'liq holda ko'rish uchun >>> <a href = 'https://islom.uz/zakot/1'>Manba</a>""")

@dp.message_handler(text = "🕋Haj")
async def Iman(message: types.Message):
	await message.reply("Haj 5 ustunning biridir\n\nAgar borishlikka imkoniyat bo'lsa albatta borish kerak", reply_markup=Haj_btn)

@dp.message_handler(text = "🕋Haj haqida")
async def Iman(message: types.Message):
	await message.reply("""HAJ QANDAY IBODAT?
Haj ibodatining boshqa ibodatlardan bir farqi shuki, u hammaga ham bir paytning oʻzida farz boʻlavermaydi, balki ayrim shartlariga muvofiq kelgan musulmonlargagina farzdir. Qodir boʻlgan odamlarga Alloh uchun Baytni haj qilish farz. Ulamolar kishiga haj farz boʻlishi uchun quyidagi shartlar mavjud boʻlishi kerakligini ta'kidlashgan:

1) musulmon boʻlishi;

2) balogʻatga etgan boʻlishi;

3) oqil boʻlishi;

4) hajga qodir boʻlishi;

5) sogʻ-salomat boʻlishi;

6) hukumat man qilmagan boʻlishi;

7) yoʻlda omonlik boʻlishi;

8) ayol kishiga mahrami boʻlishi;

Kimda ushbu shartlardan birortasi boʻlmasa, unga haj farz boʻlmaydi.

Haj – Islomning bеsh arkonidan biri boʻlgan ulugʻ rukn, Allohga mahbub ibodatdir. Bu ibodat Alloh taologa yuzlanish, U Zotning tajalliysi, nurining markazi boʻlgan maskanda ado etiladi. Hadisi shariflarda kеlishicha, Baytullohi sharif shunday makonga joylashganki, uning ayni ustida, yettinchi osmonda Baytul Ma'mur, uning ustida esa Alloh taoloning Arshi joylashgan. Alloh taoloning tavajjuhi, nuri va tajalliyoti dastlab Ka'batullohga nozil boʻlib, kеyin butun olamga tarqaladi. Shu sababli bu yerga kеlish baxtiga musharraf boʻlgan musulmonlar uchun ulkan saodat bor.

Haj oshiqona ibodat boʻlib, u yerga borish faqat hazrati Ibrohim alayhissalomning haj e'loniga «labbay» dеb javob bеrgan kishilargagina nasib etadi. U nеcha marotaba labbay dеgan boʻlsa, Ka'batullohni oʻshancha marta tavof qilish sharafiga muyassar boʻladi. Shuningdеk, u yerga borib, haj ibodatini ado etish yana bir saodatga sababdir.

Haj ibodatida ulkan hikmatlar boʻlib, bu hikmatlarning barchasini insonning ojiz aqli toʻla anglab olishi qiyin. Shunday boʻlsa ham ulamolar ijtihod qilganlar.

Hajda islomiy birlik yorqin namoyon boʻladi. Haj chogʻida musulmonlarning his-tuygʻulari, ibodatlari va hatto suvratlari bir xil boʻladi. Bu erda irqchilik, mahalliychilik, tabaqachilik kabi salbiy holatlarga oʻrin qolmaydi. Hamma bir Allohga iymon kеltirib, bir Baytullohni tavof qiladi. Tinchlik Islomning shiori ekani hajda yana bir bor namoyon boʻladi. Hamma tinch, yurt tinch, ibodat tinch, xalq tinch boʻladi.

Haj ulkan islomiy anjuman boʻlib, har bir musulmon dunyoning turli burchaklaridan kelgan din qardoshlari bilan uchrashadi, turli masalalarni muhokama qiladi. Islom va iymon rishtalari mustahkamlanadi.

Hajda musulmon banda omonlik yurti boʻlmish Makkai mukarramaga safar qiladi. Makka – ulugʻ, muqaddas shahar. Alloh taolo Qur'oni Karimda uning nomi bilan qasam ichgan. Oʻzining uyi boʻlmish Ka'baning shu shaharda qaror topishini iroda qilgan.

Haj ulugʻ ruhiy ozuqa beradigan ibodat boʻlib, unda musulmon bandaning vujudi Alloh taologa taqvo bilan, Unga toat qilishga azmu qaror bilan, gunohlariga nadomat bilan toʻladi. Bu safarda musulmon kishining Allohga, Uning Rasuliga va moʻmin-musulmonlarga boʻlgan muhabbati ziyoda boʻladi. Dunyoning hamma taraflaridagi din qardoshlariga nisbatan doʻstlik tuygʻulari uygʻonib, mustahkamlanadi.\n\n\nTo'liq holda ko'rish uchun >>> <a href = 'https://islom.uz/haj/1#block1'>Manba</a>""")

@dp.message_handler(text = "🕋Hajning tartibi🧮")
async def Iman(message: types.Message):
	await message.reply("""HAJNING FAPZ, VOJIB VA SUNNATLAPI
Haj ibodatining fapzlapi ychta:

1. Ehrom.

2. Apafotda typish.

3. Tavofyl ifoza (ifoza tavofi) qilish.

Fapz amallapdan bipontaci – yo ehrom, yo Apafotda typish va yo ifoza tavofi ado etilmay qolca, haj va ympa byziladi. Bynga koʻshimcha, ifoza tavofidan avval ayoliga yaqinlik qilish ham haj va ympani buzadi.

Hajning vojiblapi qyyidagilapdip:

1. Cafo va Mapva tepaliklapi opacida ca'y qilish.

2. Myzdalifada typish.

3. Tosh otish.

4. Sochni oldirish yoki qisqartirish.

5. Tavofyl vido kilish.

6. Qypbonlik coʻyish (qipon va tamatty' hajini niyat qilganlapga).

Endi by hykmlapga bip oz kengpoq tyshyncha bepaylik.

1. Cafo va Mapva tepaliklapi opacida ca'y qilish. Hanafiy mazhabi boʻyicha, bu amal hajning vojib amallapidan hicoblanadi. By ibodat tavofdan keyin bajariladi. Sa'yda ikki tepalik (togʻcha) opacida etti mapta bopib-kеlinadi. Yupishni Cafo tеpaligidan boshlash shapt. Yettinchi ca'y Mapvada tygaydi. Ikki tepalikning oʻptalapida yashil chipoqlap oʻpnatilgan ikkita yashil yctyn bop, shylapning opacida tezlab yupish kepak.

2. Myzdalifada typish. Apafotdan qaytgandan keyin Muzdalifada bir muddat typish kepak. Hanafiy mazhabiga binoan, oʻninchi zylhijjaning tongi otgandan coʻng bip lahza boʻlca-da, typish kеrak.

3. Tosh otish. Hayitning bipinchi kyni tosh Aqoba deb nomlangan joyda otiladi. Otiladigan toshlapning coni etti dona boʻladi. Tosh otadigan vaqt hayitning bipinchi kuni bomdoddan kеyin kipadi, qyyosh chiqib, to zavol vaqti kipgyncha otca yaxshi boʻladi. Qyyosh botgyncha otca ham pyxcat. Lekin kechaci otca makpyh boʻladi. Hayitning ikkinchi kyni ych joyda ettitadan tosh otiladi. By kyni tosh otish vaqti – zavoldan to qyyosh botgyncha. Uchinchi kyni ham xyddi shunday. Hoji toʻptinchi kynga ham Minoda qolca, u kyni ham shynday qiladi. Bugungi kunda Haj mavsumiga kеladigan ziyoratchilarning soni kеskin ortgani sababli hojilarning xavfsizligini ta'minlash va izdihomlarning oldini olish maqsadida Saudiya Arabistoni hukumati tomonidan tosh otish amali uchun har bir davlatga alohida vaqtlar tayin etilgan. Shunga koʻra, hojilarning ushbu jadvalga amal qilishlari maqsadga muvofiq hisoblanadi.

4. Cochni oldipish yoki qicqaptipish. By amal hayit kyni tosh otib, qypbonlik coʻyib boʻlingandan coʻnggina bajapiladi. Cochni toʻla olish qisqartirishdan afzal. Chynki Paygʻambapimiz collallohy alayhi vacallam cochini oldipganlapga pahmat va magʻfipat coʻpab ych mapta dyo qilganlap, qicqaptipganlapga bip mapta. Cochni qicqaptipganda y ep-by epidan qipqib qoʻyish kifoya qilmaydi, balki kamida boshning toʻrtdan bir qismidan barmoqning bir boʻgʻimi miqdoricha kaltalatiladi. Agar soch barmoqning bir boʻgʻimidan qisqa boʻlsa, hammasini oldirish vojib boʻladi.

5. Qipon yoki tamatty' haj qilganlapning bip hapakat bilan ikki ibodatni ado etganlapi shykponaciga qypbonlik qilishlapi vojibdip. Qypbonlik vaqti hayit kyni Aqobada tosh otib kelingandan coʻng boshlanadi. Oʻsha kyni va keyingi ikki kyn shomga qadar qiron va tamattu' qypbonliklapini coʻyish vaqtidip. Makon jihatidan eca Minoda boʻlishi afzal. Hapamdan tashqapida qypbonlik qilish mymkin emac.

6. Tavofyl vido. By tavof «Tavofyc-sodp» ham deb ataladi. Mazkyp tavof yuptga qaytishdan oldin Ka'bai myazzama bilan vidolashish ychyn qilinadi. Undan keyin hech napcaga mashgʻyl boʻlmay, tеzda yuptga joʻnab ketish kepak.

Hajning cynnatlapi quyidagilardir:

1) Ehromga kipish ychyn gʻycl qilish.

2) ehromga kipish paytida xyshboʻylik cyptish;

3) labbayka aytish;

4) tavofyl-qudum qilish;

5) tavof chogʻida etti mapta yzlykciz aylanish;

6) ca'yning etti mapta bopib-kelishini ketma-ket qilish;

7) ca'yda tahopatli boʻlish;

8) Apafa kechaci Minoda yotib qolish;

9) bipinchi tosh otgandan keyin qypbonlik coʻyish;

10) tosh otishni kechaciga qoldipmaclik;

11) tashpiq kechalapi Minoda yotish.\n\n\nTo'liq holda ko'rish uchun >>> <a href = 'https://islom.uz/haj/1#block6' > Manba</a>""")


###########            QUR'AN MENU                      ###########################

@dp.message_handler(text = "📖Qur'on")
async def Iman(message: types.Message):
	await message.reply("Xush kelibsiz", reply_markup=Quran_btn)

@dp.message_handler(text = "📖Quro'ni karim haqida batafsil")
async def Iman(message: types.Message):
	await message.reply("""Bismillahir Rohmanir Rohiym.
Alloh taologa bitmas-tuganmas hamdu sanolar boʻlsin.
Paygʻambarimizga mukammal va batamom salavotu durudlar boʻlsin.

«Qur'on» soʻzi lugʻatda «qiroat» ma'nosidagi masdardir.

Usulul fiqh ulamolari uning Mushaf, Tanzil, Furqon va Zikr kabi turli nomlari boʻlishiga qaramasdan «Kitob» ismini ishlatishga odatlanganlar va boshqalardan oʻzgacha ta'riflaydilar:
«Qur'on – Allohning Rasululloh sollallohu alayhi vasallamga arab tilida, eng qisqa surasi ham ojiz qoldiruvchi etib nozil qilgan kalomidir. Mushaflarda yozilgandir, tavotur ila naql qilingandir, tilovati ibodatdir, «Fotiha» surasi bilan boshlanib, «Naas» surasi bilan tugagandir».
Usulul fiqh ilmi mutaxassislarining ushbu ta'rifidan Qur'oni Karimning bir qancha xususiyatlari ayon boʻladi.

1. Qur'on nazmi va ma'nosi ila insonning toqatidan tashqari yuqori darajaga koʻtarilgan balogʻat ila ojiz qoldirishlik darajasidagi Allohning kalomidir. Shunday ekan, U dalolat qilgan hukmlarni bajarishlik vojibdir. Chunki, u itoati vojib boʻlgan Zotdan sodir boʻlgandir.
«Qur'on Allohning kalomi» dеyishlik bilan Allohning kalomidan boshqa narsalar, agar qudsiy yoki oddiy hadis boʻlsa ham, Qur'on dеyilmasligi ayon boʻladi. Chunki, hadislarning ma'nolari Allohdan boʻlishi bilan, uning jumlalarining tuzilishi va lafzlari Rasululloh sollallohu alayhi vasallamdandir. Agar hadis Allohga izofa qilinsa, ya'ni, unda soʻz Alloh taoloning nomidan kеtsa, qudsiy hadis hisoblanadi. Lеkin hadis hujjatlikda Qur'on martabasida boʻlmaydi. Uni namozlarda oʻqish durust emas va ibodati tilovat hisoblanmaydi.

2. Qur'onning hammasi arab tilida boʻlib, unda ajamlar tilida biron narsa ham yoʻq. Bas, uning tafsiri va boshqa har qanday tilga qilingan tarjimasi, agarda uning tafsirida oyatlarining dalolatiga har qancha e'tibor qilinsa yoki tarjimasida ma'nolariga har qancha e'tibor qilinsa ham, Qur'on boʻlmaydi. Chunki, Qur'on nazmi va ma'nosi arab tilida Allohdan nozil qilingan xos narsadir.

3. Qur'on Allohning Rasululloh sollallohu alayhi vasallamga tushirgan kalomiligini ta'kidlash bilan Alloh taoloning Muhammad alayhissalomdan boshqa Nabiylariga tushirgan kalomi ham Qur'on boʻlmasligi ayon boʻladi. Misol uchun Dovud alayhissalomga tushirgan kitobi «Zabur», Muso alayhissalomga tushirgan kitobi «Tavrot» va Iyso alayhissalomga tushirgan kitobi «Injil» dеyiladi.

4. Qur'on avloddan avlodga tavotur ila naql qilingandir. Ya'ni, Rasululloh sollallohu alayhi vasallamdan bir jamoa insonlar yodlab, kеyingilariga yetkazish vositasi bilan avloddan avlodga oʻtib kеlgan.
«Tavotur ila naql qilingan», dеgan iboradan, tavotir ila naql qilinmagan kalom Qur'oni Karim boʻla olmasligi kеlib chiqadi. Tavotir ila naql qilingan, dеgani esa, kalomning yolgʻonchiga chiqarib boʻlmaydigan darajada koʻp sondagi kishilar tomonidan naql qilinishiga aytiladi. Ularning hammalari ishonchli odamlar boʻlib, biror ogʻiz yolgʻonga yaqinlashmagan, koʻpliklari jihatidan yolgʻonga kеlishib olish imkonlari ham yoʻq boʻladi.
Qur'oni Karimning birinchi kalimasidan boshlab, oxirgi kalimasigacha aynan xuddi ana shu tariyqada naql qilingandir. Qur'oni Karimni Alloh taolodan vahiyning amiyni – ishonchli sohibi boʻlmish Jabroil alayhissalom Muhammad sollallohu alayhi vasallamga naql qilganlar.\n\n\nTo'liq malumot uchun >>> <a href = 'https://islom.uz/maqola/3308'>Manba</a>""")

@dp.message_handler(text = "📖Qur'on kitobi")
async def Iman(message: types.Message):
	await message.reply_document(document="BQACAgIAAxkBAAILlWKOettSjjnXBsdL1uRRb3GrfD7aAAJsHQACX-54SAzHFty2OFKTJAQ", caption="Qur'oni karimning PDF shakli")

@dp.message_handler(text = "Qorilarning qiroatlari🔊")
async def Iman(message: types.Message):
	sql.execute(
		"""CREATE TABLE IF NOT EXISTS qiroat_tanla ("user_id"  INTEGER, "name"  INTEGER, "face" INTEGER);""")
	check = sql.execute(f"""SELECT face FROM qiroat_tanla WHERE user_id = {message.from_user.id}""").fetchone()
	if check == None:
		sql.execute(
			f"""INSERT INTO qiroat_tanla (user_id, face) VALUES ('{message.from_user.id}', '0')""")
		db.commit()
	await message.answer("O'zingiz yoqtirgan qorini tanlang", reply_markup=Qiroat_btn)

@dp.callback_query_handler(text = ['Mishariy Roshid Al- Afasy', 'Muhammad Minshaviy', 'Abdulbosit Abdussomad', 'Abdurrahmon As-Sudaysiy', 'Mahmud Xolid Xusoriy', 'Xasan va Xusan qorilar', 'Абдуллоҳ qori', 'Абдулбосит Абдуссомад'])
async def d(call: CallbackQuery):
	if call.data == 'Абдуллоҳ qori':
		sql.execute(f"""UPDATE qiroat_tanla SET name =  'ИСМИ НОМАЪЛУМ ҚОРИ АБДУЛЛОҲ ДЕСАК ҲАМ БЎЛАВЕРАДИ (Абдуллоҳ Аллоҳнинг қули )' WHERE user_id = '{call.from_user.id}'""")
		db.commit()
	else:
		sql.execute(
			f"""UPDATE qiroat_tanla SET name =  '{call.data}' WHERE user_id = '{call.from_user.id}'""")
		db.commit()
	await call.message.edit_text("O'zingizga kerakli Surani tanlang", reply_markup=Juz_btn)

@dp.callback_query_handler(text = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114'])
async def d(call: CallbackQuery):
	await call.answer()
	name = sql.execute(f"""SELECT name FROM qiroat_tanla  WHERE user_id = '{call.from_user.id}'""").fetchone()
	mus_ids = sql.execute(f"""SELECT file_id FROM qiroat  WHERE name = '{name[0]}'""").fetchall()
	mus_id = mus_ids[int(call.data)][0]
	await call.message.reply_audio(audio=mus_id, caption=f"{name[0]} qiroati\n\n{int(call.data)+1}-sura")

@dp.callback_query_handler(text = "◀️")
async def d(call: CallbackQuery):
	try:
		ww = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
		 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
		 '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57']
		Juz_btn = InlineKeyboardMarkup(row_width=2)
		for name in ww:
			Juz_btn.insert(InlineKeyboardButton(text=str(int(name)+1), callback_data=name))

		Juz_btn.add(InlineKeyboardButton(text="◀️", callback_data="◀️"))
		Juz_btn.insert(InlineKeyboardButton(text="▶️", callback_data="▶️"))
		Juz_btn.insert(InlineKeyboardButton(text="❌", callback_data="❌"))
		await call.message.edit_text("O'zingizga kerakli Surani tanlang", reply_markup=Juz_btn)
	except:
		await call.answer("Xato")

@dp.callback_query_handler(text = "❌")
async def d(call: CallbackQuery):
	sql.execute(f"""UPDATE qiroat_tanla SET name =  '{call.data}' WHERE user_id = '{call.from_user.id}'""")
	db.commit()
	await call.message.edit_text("O'zingiz yoqtirgan qorini tanlang", reply_markup=Qiroat_btn)

@dp.callback_query_handler(text = "▶️")
async def d(call: CallbackQuery):
	try:
		qq = ['57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
		 '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96',
		 '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113']
		Juz_btn = InlineKeyboardMarkup(row_width=2)
		for name in qq:
			Juz_btn.insert(InlineKeyboardButton(text=str(int(name)+1), callback_data=name))

		Juz_btn.add(InlineKeyboardButton(text="◀️", callback_data="◀️"))
		Juz_btn.insert(InlineKeyboardButton(text="▶️", callback_data="▶️"))
		Juz_btn.insert(InlineKeyboardButton(text="❌", callback_data="❌"))

		await call.message.edit_text("O'zingiz yoqtirgan qorini tanlang", reply_markup=Juz_btn)
	except:
		await call.answer("Xato")

@dp.message_handler(text = "Nashidalar🔊")
async def Iman(message: types.Message):
	audios = ['CQACAgIAAxkBAAILd2KOdXSN9jKQB67bYaJSgqFWps6mAAI9DAACwmDJSAN4R4R-HrW0JAQ', 'CQACAgQAAxkBAAILeGKOdXSl8AABb8DMdlnAmrKmbgTDRAACWy4AAleosVDvQ2SRZro1ySQE',
			'CQACAgIAAxkBAAILeWKOdXQVqRjfKJFeHtlhndkp3IWvAAJndgACHIOYCkZG5GV_aw9nJAQ', 'CQACAgIAAxkBAAILemKOdXQklHHRMSLf-WYanBEC3HDoAAKsCwAClE6wSdskpM4AAbeGSyQE',''
			'CQACAgQAAxkBAAILe2KOdXT-aEJYZBmWKoqsT2HLNru_AAKJCAAC7IVQUfDTB6-AD8P9JAQ', 'CQACAgIAAxkBAAILfGKOdXQK7zPdtsZp_XFlrpOJxhmwAAJvFAACLsIwSMt_Larvhz21JAQ',
			  'CQACAgQAAxkBAAILfWKOdXSCgBDR3xkZFU5Gd7jtdk0AA78IAAL3dBlSrs-YWo5ocWgkBA', 'CQACAgQAAxkBAAILfmKOdXSRdEs1weYYSEUFwRF7qIo3AAK3BwAC0TfYUm-HuvqunXtbJAQ',
			  'CQACAgIAAxkBAAILf2KOdXTtYKAMWDiFfw9OgA14HGTXAALvqREAAfMKIQdjsnfW90_7ISQE', 'CQACAgIAAxkBAAILgGKOdXR2r8Mc0JTHqL5G2MRPNb8WAAKVFwACZjlYSD79jEkpGd3UJAQ',
			  'CQACAgIAAxkBAAILgmKOdeX4kvqcvbXPZUjLJaxsHz51AAJkBQACC8TJSdFsjIEqLK24JAQ']
	for audio in audios:
		await message.reply_audio(audio=audio, caption=f"Biz bilan qoling")



###########            PAYG'AMBARIMIZ HAQIDA             ####################

@dp.message_handler(text = "Payg'ambarimiz haqida")
async def Iman(message: types.Message):
	await message.reply("Marhamat", reply_markup=Habibim_btn)

@dp.message_handler(text = "Nuriddin hoji domla🔊")
async def Iman(message: types.Message):
	await message.reply_audio(audio="CQACAgIAAxkBAAIMMGKPVOCScYKhIrmWuhLVChaa_IQPAAJHEwACdrMQSt8DJLgIJjepJAQ", caption="Payg'ambarimiz Muhammad ﷺ Siyratlari Nuriddin hoji domla")

@dp.message_handler(text = "Abdulloh domla maruzasi🔊")
async def Iman(message: types.Message):
	await message.reply_audio(audio="CQACAgIAAxkBAAIMKWKPRuXp5EujAAF9TL--jy2ySKq52wAC2hEAAqtoKEphoBQPSj0fNiQE", caption="Payg'ambarimiz Muhammad Mustafo sollollohi alayhi vasallamning hayot yo'llari, siyrati\n\n\nAbdulloh domla maruzasi")

@dp.message_handler(text = "🎞Teleseriali")
async def Iman(message: types.Message):
	await message.reply_video(video="BAACAgIAAxkBAAIMLWKPUhEJX6BqaIRFYAHcbEnuBqLDAAIFFgACbxeIS6kGUw5GezVbJAQ", caption=""""Муҳаммад (соллаллоҳу алайҳи ва саллам) Аллоҳнинг элчиси" фильм""")

@dp.message_handler(text = "📺Multiseriali")
async def Iman(message: types.Message):
	await message.reply("tez orada")



##############              PAYG'AMBARLAR QISSALARI              ##############

@dp.message_handler(text = "🗞Payg'ambarlar qissalari")
async def Iman(message: types.Message):
	await message.reply("tez orada", reply_markup=P_qissasi_btn)

@dp.callback_query_handler(text = ["Odam alayhissalom", "Nuh alayhissalom", 'Hud alayhissalom', 'Solih alayhissalom', 'Ibrohim alayhissalom','Lut alayhissalom', 'Yusuf alayhissalom', 'Ayyub alayhissalom', 'Yunus alayhissalom', 'Muso alayhissalom', 'Yusha ibn Nun alayhissalom', 'Dovud va Sulaymon alayhissalomlar', 'Zakariyo va Yahyo alayhissalomlar', 'Iso alayhissalom'])
async def  P(call: CallbackQuery):
	await call.answer()
	ids = sql.execute(f"""SELECT file_id FROM Nabiy WHERE name = '{call.data}'""").fetchall()
	captions = sql.execute(f"""SELECT caption FROM Nabiy WHERE name = '{call.data}'""").fetchall()
	name = sql.execute(f"""SELECT name FROM Nabiy WHERE name = '{call.data}'""").fetchone()
	for id, caption in zip(ids, captions):
		await call.message.reply_audio(audio=id[0], caption=f"{name[0]}\n\n\n{caption[0]}")



#############                ALLOHNING ISMLARI                       ###################

@dp.message_handler(text = "Allohning go'zal ismlari")
async def Iman(message: types.Message):
	await message.answer("Allohning go'zal ismlari bordir, va ularni kim yod olsa jannatga kiradi", reply_markup=Great_name_btn)

@dp.callback_query_handler(text = [' 1 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50', '51 - 60', '61 - 70', '71 - 80', '81 - 90', '91 - 99'])
async def d(call: CallbackQuery):
	await call.answer()
	idss = sql.execute(f"""SELECT file_id FROM photos""").fetchall()[int(call.data[5:])-10:int(call.data[5:])]
	for ids in idss:
		await call.message.reply_photo(photo=ids[0])


##############               QISSALAR									#################

@dp.message_handler(text = "📖Qur'ondagi qissalar")
async def Iman(message: types.Message):
	await message.answer("Bu yerda siz Qur'oni karimda kelgan go'zal qissalar haqida bilib olasiz. InshaAlloh", reply_markup=Qissalar_btn)

@dp.message_handler(text = "👳‍♂️Insonlar qissasi")
async def Iman(message: types.Message):
	await message.answer("https://t.me/Qurondagi_qissalar/31")

@dp.message_handler(text = "🧕Ayollar qissasi")
async def Iman(message: types.Message):
	await message.answer("https://t.me/Qurondagi_qissalar/95")

@dp.message_handler(text = "🤩Ajoyibotlar qissasi")
async def Iman(message: types.Message):
	await message.answer("https://t.me/Qurondagi_qissalar/158")

@dp.message_handler(text = "🐫Jonzotlar qissasi")
async def Iman(message: types.Message):
	await message.answer("https://t.me/Qurondagi_qissalar/252")



##############                NAMOZ VAQTLARI             #################

@dp.message_handler(text = "⏳Namoz vaqtlari")
async def Iman(message: types.Message):
	await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=P_T_btn)

@dp.message_handler(text = "⏳Bugungi namoz vaqti")
async def Iman(message: types.Message):
	user = sql.execute(f"""SELECT regs FROM regions WHERE user_id = '{message.from_user.id}'""").fetchone()
	C_id = sql.execute(f"""SELECT number FROM city_id WHERE name = '{user[0]}'""").fetchone()
	html_text = requests.get(f'https://islom.uz/region/{int(C_id[0])}').text
	soup = BeautifulSoup(html_text, 'html.parser')
	matn = ''
	d = 0
	for m in ['Tong', 'Quyosh', 'Peshin', 'Asr', 'Shom', 'Xufton']:
		d += 1
		times = soup.find('div', id=f'tc{d}').text
		matn += f"<b>{m}</b> : {times}\n"

	await message.answer(f"Bugungi namoz vaqtlari👇👇\n\n{matn}\n\n<b>{user[0]}</b> vaqti bo'yicha")

@dp.message_handler(text = "⏳Kunlik duolar")
async def Iman(message: types.Message):
	# html_text = requests.get('https://islom.uz/').text
	# soup = BeautifulSoup(html_text, 'html.parser')

	await message.answer("""Бисмиллаҳир Роҳманир Роҳийм.
Аллоҳ таолога битмас-туганмас ҳамду санолар бўлсин.
Пайғамбаримизга мукаммал ва батамом салавоту дурудлар бўлсин.

Мўминнинг ҳар куни, бутун ҳаёти Аллоҳга ибодат қилишдан иборатдир. Кундалик ибодатлар бомдод намозига уйғонган дақиқалардан бошлаб кун бўйи давом этади. Аллоҳ таолонинг раҳмати, баракоти ва ҳимоясига сазовор бўлишимиз учун Унинг номи билан бошлаган ҳар бир ишимиз ибодатдир. Уйдан чиқишдан тонгда мусулмон киши томонидан айтиладиган дуолар:

Уйқудан уйғонганда. Маъноси: «Бизларни ўлдириб қайта тирилтирган Аллоҳга ҳамду-санолар бўлсин».

«Аллоҳим, Сенинг номинг ила тонг оттирдик, Сенинг номинг ила кеч киргиздик. Сенинг номинг ила тириламиз ва Сенинг номинг ила ўламиз. Ва Сенга қайтажакмиз».

Ҳожатхонага кираётганда ушбу дуо ўқилади. Маъноси: «Эй Роббим, эркак ва аёл шайтоннинг ёмонлигидан паноҳ сўрайман».

Ҳожатхонадан чиқаётганда ўқиладиган дуо. Маъноси: «Сенинг мағфиратингни сўрайман».

Таҳорат қилаётганда ўқиладиган дуо. Маъноси: «Илоҳим, мени ўз тарафингга юзланувчи покиза инсонлар сафига сол».

Кун давомида Аллоҳнинг паноҳида бўлмоқлик учун. Қайси бир одам бомдод ва шом намозларидан кейин уч марта: (маъноси) «Шундай Аллоҳнинг исми билан бошлайманки, Унинг исми туфайли еру осмонда бирор нарса зарар бера олмайди. У эшитувчи ва билувчи Зотдир», – деб айтса, унга бирор нарса зарар бермайди.

Овқат ейишдан олдин. «Аллоҳ исми билан». Агар аввалида Аллоҳ исмини зикр этишни унутса: «Овқатнинг аввали ва охирига Аллоҳнинг исми билан». «Аллоҳим, буни бизларга баракали қил, бунданда яхшиси билан ризқлантир».

Овқат еб бўлганда. «Бизларни овқатлантириб, бизларни суғориб ҳамда бизларни мусулмон қилиб қўйган Аллоҳга ҳамд бўлсин».

Кийинишда ўқиладиган дуо. «Менга кийимни насиб қилган ва кийинтир Аллоҳга ҳамд бўлсин. Менда куч ҳам қувват ҳам йўқ».

Уйдан чиқаётганда. Эй Раббим, адашиш ва адаштирилишдан, тойилиш ва тойилтирилишдан, зулм қилиш ва зулм кўришдан, жоҳиллик қилиш ва менга нисбатан жоҳиллик қилинишидан Сендан паноҳ сўрайман».""")

@dp.message_handler(text = "🏙Shaharni tanlash")
async def Iman(message: types.Message):
	check = sql.execute(f"""SELECT face FROM regions WHERE user_id = {message.from_user.id}""").fetchone()
	if check == None:
		sql.execute(
			f"""INSERT INTO regions (user_id, face) VALUES ('{message.from_user.id}', '{message.from_user.id}')""")
		db.commit()
	else:
		pass
	await message.answer("O'z shaharingizni tanlang👇👇👇", reply_markup=choos_city_btn)



@dp.callback_query_handler(text = ['Ангрен', 'Андижон', 'Арнасой', 'Ашхабод', 'Бекобод', 'Бишкек', 'Бойсун', 'Булоқбоши', 'Бурчмулла', 'Бухоро',
        'Газли', 'Гулистон', 'Денов', 'Деҳқонобод', 'Дўстлик', 'Душанбе', 'Жалолобод', 'Жамбул', 'Жиззах', 'Жомбой',
        'Зарафшон', 'Зомин', 'Каттақўрғон', 'Конибодом', 'Конимех', 'Косон', 'Косонсой', 'Марғилон', 'Мингбулоқ',
        'Муборак', 'Мўйноқ', 'Навоий', 'Наманган', 'Нукус', 'Нурота', 'Олмаота', 'Олот', 'Олтиариқ', 'Олтинкўл',
        'Пахтаобод', 'Поп', 'Риштон', 'Сайрам', 'Самарқанд', 'Таллимаржон', 'Тахтакўпир', 'Термиз', 'Томди', 'Тошкент', 'Тошҳовуз', 'Туркистон', 'Туркманобод', 'Тўрткўл', 'Узунқудуқ', 'Урганч', 'Ургут', 'Ўсмат', 'Учтепа', 'Учқудуқ', 'Учқўрғон', 'Ўш', 'Ўғиз', 'Фарғона', 'Хазорасп', 'Хива', 'Хонобод', 'Хонқа', 'Хўжанд', 'Хўжаобод', 'Чимбой', 'Чимкент', 'Чортоқ', 'Чуст', 'Шаҳрихон', 'Шеробод', 'Шовот', 'Шуманай', 'Янгибозор', 'Ғаллаорол', 'Ғузор', 'Қарши', 'Қарши', 'Қизилтепа', 'Қоракўл', 'Қоровулбозор', 'Қува', 'Қумқўрғон', 'Қўнғирот', 'Қўрғонтепа', 'Қўқон'])
async def reglar(call: CallbackQuery):
	await call.answer("Shaharingiz tanlandi")
	sql.execute(f"""UPDATE regions SET regs =  '{call.data}' WHERE user_id = '{call.from_user.id}'""")
	db.commit()


@dp.callback_query_handler(text = ['⬅️', '➡️'])
async def reglar(call: CallbackQuery):
	await call.answer()
	if call.data == '⬅️':
		await call.message.edit_text("O'z shaharingizni tanlang👇👇👇", reply_markup=choos_city_btn)
	else:
		await call.message.edit_text("O'z shaharingizni tanlang👇👇👇", reply_markup=choos_city_btn1)


if __name__=="__main__":
	executor.start_polling(dp)