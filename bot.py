from pyrogram import Client, filters
import yt_dlp
import os

API_ID = 26661512
API_HASH = "f6b739531fb66ec7e18af2a4e50c3811"
BOT_TOKEN = "7897450086:AAH7ehLzvte3mldWfnCmnbtqu9JudsFNg6g"

bot = Client("video_downloader_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    await message.reply_text(
        "আসসালামু আলাইকুম!

আমি একটি ভিডিও ডাউনলোডার বট।

YouTube / TikTok / Instagram ভিডিওর লিংক পাঠান, আমি ভিডিওটি ডাউনলোড করে দিব।"
    )

@bot.on_message(filters.text & ~filters.command("start"))
async def download_handler(_, message):
    url = message.text
    await message.reply_text("ডাউনলোড শুরু হচ্ছে, দয়া করে অপেক্ষা করুন...")

    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await message.reply_video(video=filename, caption="এই নিন আপনার ভিডিও!")
        os.remove(filename)

    except Exception as e:
        await message.reply_text(f"দুঃখিত! একটি সমস্যা হয়েছে:

{e}")

bot.run()