import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
import random
import time
import threading

bot = telebot.TeleBot("8163292020:AAHe1KEytagF7j2THuwxf0U5nJhCXhgMEtw", parse_mode="HTML")
user_state = {}

# --- زخارف عربية محسّنة عالية الجودة ---
def arabic_style_1(t):
    tashkeel = ['ً', 'ٌ', 'ٍ', 'ّ', 'ْ', 'َ', 'ُ', 'ِ']
    return ''.join(c + random.choice(tashkeel) if c.isalpha() else c for c in t)

def arabic_style_2(t):
    tashkeel = ['ً', 'ٌ', 'ٍ', 'ّ', 'ْ', 'َ', 'ُ', 'ِ']
    return ''.join(c + random.choice(tashkeel) + 'ـ' if c.isalpha() else c for c in t).strip('ـ')

def arabic_style_3(t):
    symbols = ['ۖ', 'ۗ', 'ۘ', 'ۙ', 'ۚ', 'ۛ']
    return ''.join(c + random.choice(symbols) if c.isalpha() else c for c in t)

def arabic_style_4(t):
    symbols = ['ہ', 'ہہ', 'ہہہ']
    return ''.join(c + random.choice(symbols) if c.isalpha() else c for c in t)

def arabic_style_5(t):
    hearts = ['❣']
    tashkeel = ['ً', 'ٌ', 'ٍ', 'ّ', 'ْ', 'َ', 'ُ', 'ِ']
    return ''.join(random.choice(hearts) + c + random.choice(tashkeel) + random.choice(hearts) + 'ـ' if c.isalpha() else c for c in t).strip('ـ')

arabic_styles = [arabic_style_1, arabic_style_2, arabic_style_3, arabic_style_4, arabic_style_5]

# --- زخارف إنجليزية حرفية ---
def fancy1(t): return ''.join(["𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy2(t): return ''.join(["αв¢∂єƒgнιנкℓмησρqяѕтυνωχуz"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy3(t): return ''.join(["ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy4(t): return ''.join(["𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘷𝘄𝘅𝘆𝘇"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy5(t): return ''.join(["𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy6(t): return ''.join(["ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy7(t): return ''.join(["🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy8(t): return ''.join(["🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy9(t): return ''.join(["🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy10(t): return ''.join(["𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy11(t): return ''.join(["🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy12(t): return ''.join(["ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"[ord(c.upper())-65] if c.isalpha() else c for c in t])
def fancy13(t): return ''.join(["₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱ɊⱤ₴₮ɄV₩ӾɎⱫ"[ord(c.upper())-65] if c.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else c for c in t])
def fancy14(t): return ''.join(["𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"[ord(c.lower())-97] if c.isalpha() else c for c in t])
def fancy15(t): return ''.join(["ʍɨʐɨռɢ" if c == 'z' else c for c in t])

english_styles = [fancy1, fancy2, fancy3, fancy4, fancy5, fancy6, fancy7, fancy8, fancy9, fancy10, fancy11, fancy12, fancy13, fancy14, fancy15]

# --- زخارف عربية كاملة ---
zakhrafa_ar = [
    lambda t: f"★彡 {t} 彡★",
    lambda t: f"『 {t} 』",
    lambda t: f"°• {t} •°",
    lambda t: f"♚ {t} ♚",
    lambda t: f"𓆩 {t} 𓆪",
    lambda t: f"↫ {t} ↬",
    lambda t: f"꧁༺ {t} ༻꧂",
    lambda t: f"⎯━⊰ {t} ⊱━⎯",
    lambda t: f"✿ {t} ✿",
    lambda t: f"｡◕‿◕｡ {t} ｡◕‿◕｡",
    lambda t: f"❖ {t} ❖",
    lambda t: f"✸ {t} ✸",
    lambda t: f"۞ {t} ۞",
    lambda t: f"༒ {t} ༒",
    lambda t: f"☬ {t} ☬"
]

# رموز زخرفية للنسخ (زر الرموز)
symbols_list = [
    "★", "☆", "✦", "✧", "✩", "✪", "✫", "✬", "✭", "✮", "✯", "✰",
    "♠", "♣", "♥", "♦",
    "♤", "♧", "♡", "♢",
    "☀", "☁", "☂", "☃", "☄", "☾", "☼", "☽", "☿",
    "⚡", "☠", "☢", "☣", "☯", "☮", "☸", "☭", "✞", "✟", "✠",
    "✈", "✉", "✎", "✏", "✐", "✑", "✒", "✔", "✖", "✗", "✘", "✙", "✚", "✛", "✜", "✝",
    "♬", "♩", "♪", "♫", "♭", "♮", "♯",
    "─", "━", "│", "┃", "┄", "┅", "┆", "┇", "┈", "┉", "┊", "┋",
    "╭", "╮", "╯", "╰", "╱", "╲", "╳", "╴", "╵", "╶", "╷", "╸", "╹", "╺", "╻", "╼", "╽", "╾", "╿",
    "╔", "╗", "╝", "╚", "╦", "╩", "╠", "╣", "╬", "═", "║",
    "╒", "╓", "╔", "╕", "╖", "╗", "╘", "╙", "╚", "╛", "╜", "╝", "╞", "╟", "╠", "╡", "╢", "╣", "╤", "╥", "╦", "╧", "╨", "╩", "╪", "╫", "╬",
    "◇", "◆", "○", "●", "◌", "◎", "◉", "◍", "◐", "◑", "◒", "◓", "◔", "◕", "◖", "◗", "◘", "◙", "◚", "◛", "◜", "◝", "◞", "◟", "◠", "◡", "◢", "◣", "◤", "◥", "◦", "◨", "◩", "◪", "◫", "◬", "◭", "◮", "◯",
    "⬤", "⬥", "⬦", "⬧", "⬨", "⬩", "⬪", "⬫", "⬬",
    "⬰", "⬱", "⬲", "⬳", "⬴", "⬵", "⬶", "⬷", "⬸", "⬹", "⬺", "⬻",
    "⬼", "⬽", "⬾", "⬿",
    "∴", "∵", "∶", "∷", "∸", "∹", "∺", "∻", "∼", "∽", "∾", "∿", "≀", "≁", "≂", "≃", "≄", "≅", "≆", "≇", "≈", "≉", "≊", "≋", "≌", "≍",
    "←", "↑", "→", "↓", "↔", "↕", "↖", "↗", "↘", "↙", "↚", "↛", "↜", "↝", "↞", "↟", "↠", "↡", "↢", "↣", "↤", "↥", "↦", "↧", "↨", "↩", "↪", "↫", "↬", "↭", "↮", "↯",
    "∀", "∁", "∂", "∃", "∄", "∅", "∆", "∇", "∈", "∉", "∊", "∋", "∌", "∍", "∎", "∏", "∐", "∑", "−", "∓", "∔", "∕", "∖", "∗", "∘", "∙", "√", "∝", "∞", "∟", "∠", "∡", "∢",
    "⊂", "⊃", "⊄", "⊅", "⊆", "⊇", "⊈", "⊉", "⊊", "⊋", "⊏", "⊐", "⊑", "⊒", "⊓", "⊔", "⊕", "⊖", "⊗", "⊘", "⊙", "⊚", "⊛", "⊜", "⊝", "⊞", "⊟", "⊠", "⊡", "⊢", "⊣", "⊤", "⊥", "⊦", "⊧", "⊨", "⊩", "⊪", "⊫", "⊬", "⊭", "⊮", "⊯",
    "‖", "‗", "‘", "’", "‚", "“", "”", "„", "†", "‡", "•", "…", "‰", "′", "″", "‹", "›", "※", "⁂", "⁅", "⁆", "⁇", "⁈", "⁉", "⁊", "⁋", "⁌", "⁍", "⁎", "⁏", "⁐", "⁑", "⁒", "⁓", "⁔", "⁕", "⁖", "⁗", "⁘", "⁙", "⁚", "⁛", "⁜", "⁝", "⁞",
    "⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "⁺", "⁻", "⁼", "⁽", "⁾", "ⁿ", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎", "₏",
    "ₐ", "ₑ", "ₒ", "ₓ", "ₔ", "ₕ", "ₖ", "ₗ", "ₘ", "ₙ", "ₚ", "ₛ", "ₜ",
    "⟨", "⟩", "⟪", "⟫", "⟬", "⟭", "⟮", "⟯",
    "⌈", "⌉", "⌊", "⌋", "⌌", "⌍", "⌎", "⌏", "⌐", "⌑", "⌒", "⌓", "⌔", "⌕", "⌖", "⌗", "⌘", "⌙", "⌚", "⌛", "⌜", "⌝", "⌞", "⌟", "⌠", "⌡", "⌢", "⌣", "⌤", "⌥", "⌦", "⌧", "⌨",
    "❖", "❘", "❙", "❚", "❯", "❰", "❱", "❲", "❳", "❨", "❩", "❪", "❫", "❬", "❭", "❮", "❯", "❰", "❱", "❲", "❳", "❴", "❵",
    "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾", "❿",
    "✁", "✂", "✃", "✄", "✆", "✇", "✈", "✉", "✊", "✋", "✌", "✍", "✎", "✏", "✐", "✑", "✒", "✓", "✔", "✕", "✖", "✗", "✘", "✙", "✚", "✛", "✜", "✝", "✞", "✟", "✠", "✡", "✢", "✣", "✤", "✥", "✦", "✧",
    "⚀", "⚁", "⚂", "⚃", "⚄", "⚅",
    "♔", "♕", "♖", "♗", "♘", "♙", "♚", "♛", "♜", "♝", "♞", "♟",
    "⟀", "⟁", "⟂", "⟃", "⟄", "⟅", "⟆", "⟇", "⟈", "⟉", "⟊", "⟋", "⟌", "⟍", "⟎", "⟏",
    "⟐", "⟑", "⟒", "⟓", "⟔", "⟕", "⟖", "⟗", "⟘", "⟙", "⟚", "⟛", "⟜", "⟝", "⟞", "⟟", "⟠", "⟡", "⟢", "⟣", "⟤", "⟥", "⟦", "⟧", "⟨", "⟩", "⟪", "⟫",
    "⊀", "⊁", "⊂", "⊃", "⊄", "⊅", "⊆", "⊇", "⊈", "⊉", "⊊", "⊋", "⊌", "⊍", "⊎", "⊏", "⊐", "⊑", "⊒", "⊓", "⊔", "⊕", "⊖", "⊗", "⊘", "⊙", "⊚", "⊛", "⊜", "⊝", "⊞", "⊟", "⊠", "⊡", "⊢", "⊣", "⊤", "⊥",
    "⋀", "⋁", "⋂", "⋃", "⋄", "⋅", "⋆", "⋇", "⋈", "⋉", "⋊", "⋋", "⋌", "⋍", "⋎", "⋏",
    "∘", "⨀", "⨁", "⨂", "⨃", "⨄", "⨅", "⨆", "⨇", "⨈", "⨉", "⨊", "⨋", "⨌", "⨍", "⨎", "⨏"
]
# --- حذف رسالة بعد وقت ---
def delete_message_later(chat_id, message_id, delay=5):
    time.sleep(delay)
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass

# --- قائمة رئيسية ---
def get_main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🎨 زخرفة عربية", callback_data="z_ar"),
        InlineKeyboardButton("🅰️ زخرفة إنجليزية", callback_data="z_en"),
        InlineKeyboardButton("🎲 زخرفة عشوائية", callback_data="z_rand"),
        InlineKeyboardButton("🔣 الرموز", callback_data="symbols"),
        InlineKeyboardButton("🛠 الدعم الفني", url="https://t.me/oli17")
    )
    return kb

@bot.message_handler(commands=["start"])
def start(msg):
    uid = msg.chat.id
    user_state[uid] = {"state": None, "message_id": None, "last_notification": None}
    kb = get_main_menu()
    sent_msg = bot.send_message(uid, """
<b>👋 مرحبًا بك في بوت الزخرفة المتكامل</b>

🖋️ يدعم زخرفة عربية متقدمة، زخرفة إنجليزية، زخرفة عشوائية، وزِر للرموز كلها.

اختر ما يناسبك من الأزرار أدناه:
""", reply_markup=kb)
    user_state[uid]["message_id"] = sent_msg.message_id

@bot.callback_query_handler(func=lambda c: True)
def handle_callback(call):
    uid = call.message.chat.id
    user_state[uid]["state"] = call.data
    kb = InlineKeyboardMarkup(row_width=2)

    if call.data == "back":
        kb = get_main_menu()
        bot.edit_message_text(
            chat_id=uid,
            message_id=user_state[uid]["message_id"],
            text="""
<b>👋 مرحبًا بك في بوت الزخرفة المتكامل</b>

🖋️ يدعم زخرفة عربية متقدمة، زخرفة إنجليزية، زخرفة عشوائية، وزِر للرموز كلها.

اختر ما يناسبك من الأزرار أدناه:
""",
            reply_markup=kb
        )
        return

    if call.data == "symbols":
        bot.edit_message_text(
            chat_id=uid,
            message_id=user_state[uid]["message_id"],
            text=f"<b>🔣 الرموز الزخرفية بالكامل:</b>\n<code>{symbols_list}</code>",
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("↩️ رجوع", callback_data="back"))
        )
        return

    prompts = {
        "z_ar": "✍️ أرسل لي النص <b>بالعربية</b> لتطبيق الزخارف:",
        "z_en": "✍️ Send me text <b>in English</b> for decoration:",
        "z_rand": "✍️ أرسل أي نص للحصول على زخرفة عشوائية:"
    }

    bot.edit_message_text(
        chat_id=uid,
        message_id=user_state[uid]["message_id"],
        text=prompts.get(call.data, "") + "\n\n<i>اضغط 'رجوع' للعودة إلى القائمة الرئيسية</i>",
        reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("↩️ رجوع", callback_data="back"))
    )

@bot.message_handler(func=lambda m: m.chat.id in user_state and user_state[m.chat.id]["state"])
def handle_text(msg):
    uid = msg.chat.id
    txt = msg.text.strip()

    try:
        bot.delete_message(uid, msg.message_id)
    except:
        pass

    notification = bot.send_message(uid, "⏳ جارٍ معالجة النص...")
    user_state[uid]["last_notification"] = notification.message_id

    time.sleep(2)

    try:
        bot.delete_message(uid, notification.message_id)
    except:
        pass

    if not txt or len(txt) > 50:
        warn = bot.send_message(uid, "⚠️ الرجاء إرسال نص بين 1 و50 حرف فقط.")
        threading.Thread(target=delete_message_later, args=(uid, warn.message_id)).start()
        return

    mode = user_state[uid]["state"]
    user_state[uid]["state"] = None

    if mode == "z_ar":
        styles = arabic_styles + zakhrafa_ar
    elif mode == "z_en":
        styles = english_styles
    elif mode == "z_rand":
        styles = [random.choice(arabic_styles + zakhrafa_ar + english_styles)]
    else:
        styles = []

    response = "<b>✨ هنا بعض الزخارف:</b>\n\n"
    for i, fn in enumerate(styles, 1):
        try:
            response += f"{i}- <code>{fn(txt)}</code>\n"
        except:
            pass

    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("↩️ رجوع", callback_data="back"))

    bot.edit_message_text(
        chat_id=uid,
        message_id=user_state[uid]["message_id"],
        text=response,
        reply_markup=kb
    )

@bot.inline_handler(lambda q: len(q.query.strip()) > 0)
def inline_zakhrafa(query):
    text = query.query.strip()
    all_styles = arabic_styles + zakhrafa_ar + english_styles
    random.shuffle(all_styles)
    results = []
    for i, fn in enumerate(all_styles[:10]):
        try:
            styled = fn(text)
            results.append(InlineQueryResultArticle(
                id=str(i),
                title=f"زخرفة {i+1}",
                description=styled,
                input_message_content=InputTextMessageContent(
                    message_text=f"<code>{styled}</code>",
                    parse_mode="HTML"
                ),
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("📋 نسخ", switch_inline_query=styled)
                )
            ))
        except:
            pass
    bot.answer_inline_query(query.id, results, cache_time=1)

if __name__ == "__main__":
    print("✅ البوت يعمل الآن بكامل الميزات!")
    bot.infinity_polling()