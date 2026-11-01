import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

TOKEN = "9162299516:AAFLZ_fnGrGDT2pXKVl4tdMnZvpnw1HNqRY"

# ====== REZYUME MA'LUMOTLARI (ikki tilda) ======
TEXTS = {
    "uz": {
        "menu": "Bo'limni tanlang:",
        "about": (
            "👤 Nu'monjon Rustamjonov\n"
            "🎓 Universitet talabasi | Junior IT va raqamli mutaxassis\n"
            "📍 O'zbekiston\n\n"
            "📝 Qisqacha:\n"
            "Axborot xavfsizligi yo'nalishida o'qiyotgan universitet talabasiman. "
            "Dasturlash, axborot texnologiyalari va raqamli yechimlarga qiziqaman. "
            "Shaxsiy Telegram bot loyihalarini ishlab chiqish va kompyuter vositalari "
            "bilan ishlash bo'yicha amaliy tajribam bor.\n\n"
            "Yangi texnologiyalarni mustaqil o'rganaman, muammolarni hal qila olaman "
            "va individual vazifalar ustida ishlayman. Masofaviy, yarim kunlik "
            "(part-time) va boshlang'ich darajadagi imkoniyatlarga qiziqaman.\n\n"
            "🏫 Ta'lim:\n"
            "Namangan davlat texnika universiteti\n"
            "Yo'nalish: Axborot xavfsizligi\n"
            "Daraja: 2-kurs talabasi\n\n"
            "🌐 Tillar: O'zbek (ona tili)"
        ),
        "skills": (
            "🛠 Texnik ko'nikmalar\n\n"
            "🐍 Dasturlash: Python, C++ (o'rganish va amaliy ishlab chiqish)\n"
            "🔐 IT: axborot xavfsizligi va kompyuter tizimlari bo'yicha asosiy bilimlar\n"
            "🤖 Telegram botlar: shaxsiy botlarni yaratish va sozlash (aiogram)\n"
            "🗄 Ma'lumotlar bazasi: SQLite\n"
            "🧠 AI vositalari: tadqiqot, unumdorlik va raqamli kontent yaratishda"
        ),
        "projects": (
            "📂 Shaxsiy loyihalar\n\n"
            "🤖 Rezyuume: Telegram bot\n"
            "Demo: https://t.me/Rezyuume_bot\n"
            "• Shaxsiy Telegram bot loyihasi\n"
            "• Telegram bot ishlab chiqish bo'yicha amaliy tajribani ko'rsatadi\n"
            "• Mustaqil raqamli loyiha sifatida yaratilgan\n\n"
            "🤖 Telegram bot ishlab chiqish\n"
            "• Python va aiogram yordamida botlar yaratish\n"
            "• Bot bilan o'zaro aloqa tizimlari, ma'lumotlar bazasi integratsiyasi "
            "va avtomatik funksiyalar\n"
            "• Ma'lumotlarni saqlash uchun SQLite"
        ),
        "experience": (
            "💼 Amaliy ish tajribasi\n\n"
            "• Amaliy ishlar va texnik vazifalar bo'yicha tajriba\n"
            "• Avtomobillarni ta'mirlash va xizmat ko'rsatish tajribasi\n"
            "• Avtomobil tuzilishi va ishlash tamoyillarini tushunish\n"
            "• Ehtiyot qismlar va komponentlar bo'yicha amaliy bilim\n"
            "• Avtomobil qismlarini ajrata olish va vazifalarini bilish\n"
            "• Ta'mirlash va texnik xizmat jarayonlaridagi amaliy tajriba\n"
            "• Texnik muammolarni aniqlash va bartaraf etish jarayonlarini tushunish"
        ),
        "contact": (
            "📞 Aloqa\n\n"
            "📱 Telefon: +998907958507\n"
            "✉️ Email: rustamjonovnomonjon82@gmail.com\n"
            "💬 Telegram: @Rustamjonoff1\n\n"
            "Masofaviy, part-time va boshlang'ich lavozimlardagi takliflarga ochiqman."
        ),
        "btn_about": "👤 Men haqimda",
        "btn_skills": "🛠 Ko'nikmalar",
        "btn_projects": "📂 Loyihalar",
        "btn_experience": "💼 Tajriba",
        "btn_contact": "📞 Aloqa",
        "btn_back": "⬅️ Orqaga",
        "btn_lang": "🌐 Til / Language",
    },
    "en": {
        "menu": "Choose a section:",
        "about": (
            "👤 Nu'monjon Rustamjonov\n"
            "🎓 University Student | Junior IT & Digital Specialist\n"
            "📍 Uzbekistan\n\n"
            "📝 Professional Summary:\n"
            "A university student majoring in Information Security with an interest in "
            "programming, information technology, and digital solutions. I have practical "
            "experience developing personal Telegram bot projects and working with "
            "computer-based tools.\n\n"
            "I can learn new technologies independently, solve problems, and work on "
            "individual tasks. I'm interested in remote, part-time, and entry-level "
            "opportunities where I can apply my existing skills and keep growing "
            "professionally.\n\n"
            "🏫 Education:\n"
            "Namangan State Technical University\n"
            "Field of Study: Information Security\n"
            "Current Level: 2nd-year student\n\n"
            "🌐 Languages: Uzbek (native)"
        ),
        "skills": (
            "🛠 Technical Skills\n\n"
            "🐍 Programming: Python, C++ (learning and practical development)\n"
            "🔐 IT: basic knowledge of information security and computer systems\n"
            "🤖 Telegram Bots: personal bot development and configuration (aiogram)\n"
            "🗄 Database: SQLite\n"
            "🧠 AI Tools: for research, productivity, and digital content creation"
        ),
        "projects": (
            "📂 Personal Projects\n\n"
            "🤖 Rezyuume: Telegram Bot\n"
            "Demo: https://t.me/Rezyuume_bot\n"
            "• Personal Telegram bot project\n"
            "• Demonstrates practical experience with Telegram bot development\n"
            "• Created as an independent digital project\n\n"
            "🤖 Telegram Bot Development\n"
            "• Developing Telegram bots using Python and aiogram\n"
            "• Bot interaction systems, database integration, and automated functions\n"
            "• SQLite for data storage"
        ),
        "experience": (
            "💼 Practical Work Experience\n\n"
            "• Hands-on work and practical technical tasks\n"
            "• Automotive repair and maintenance\n"
            "• Understanding of vehicle structure and operating principles\n"
            "• Practical knowledge of automotive spare parts and components\n"
            "• Ability to identify vehicle parts and understand their functions\n"
            "• Practical experience in maintenance and repair processes\n"
            "• Understanding of how to diagnose and resolve technical issues"
        ),
        "contact": (
            "📞 Contact\n\n"
            "📱 Phone: +998907958507\n"
            "✉️ Email: rustamjonovnomonjon82@gmail.com\n"
            "💬 Telegram: @Rustamjonoff1\n\n"
            "Open to remote, part-time, and entry-level opportunities."
        ),
        "btn_about": "👤 About me",
        "btn_skills": "🛠 Skills",
        "btn_projects": "📂 Projects",
        "btn_experience": "💼 Experience",
        "btn_contact": "📞 Contact",
        "btn_back": "⬅️ Back",
        "btn_lang": "🌐 Til / Language",
    },
}
CHOOSE_LANG = "Tilni tanlang / Choose your language:"
# =================================================

dp = Dispatcher()


def lang_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="menu:uz"),
                InlineKeyboardButton(text="🇬🇧 English", callback_data="menu:en"),
            ]
        ]
    )


def main_menu(lang: str) -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=t["btn_about"], callback_data=f"sec:{lang}:about")],
            [InlineKeyboardButton(text=t["btn_skills"], callback_data=f"sec:{lang}:skills")],
            [InlineKeyboardButton(text=t["btn_projects"], callback_data=f"sec:{lang}:projects")],
            [InlineKeyboardButton(text=t["btn_experience"], callback_data=f"sec:{lang}:experience")],
            [InlineKeyboardButton(text=t["btn_contact"], callback_data=f"sec:{lang}:contact")],
            [InlineKeyboardButton(text=t["btn_lang"], callback_data="lang")],
        ]
    )


def back_button(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=TEXTS[lang]["btn_back"], callback_data=f"menu:{lang}")]
        ]
    )


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(CHOOSE_LANG, reply_markup=lang_menu())


@dp.callback_query(F.data == "lang")
async def choose_lang(call: CallbackQuery):
    await call.message.edit_text(CHOOSE_LANG, reply_markup=lang_menu())
    await call.answer()


@dp.callback_query(F.data.startswith("menu:"))
async def show_menu(call: CallbackQuery):
    lang = call.data.split(":")[1]
    if lang in TEXTS:
        await call.message.edit_text(TEXTS[lang]["menu"], reply_markup=main_menu(lang))
    await call.answer()


@dp.callback_query(F.data.startswith("sec:"))
async def show_section(call: CallbackQuery):
    _, lang, section = call.data.split(":")
    if lang in TEXTS and section in TEXTS[lang]:
        await call.message.edit_text(TEXTS[lang][section], reply_markup=back_button(lang))
    await call.answer()


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
