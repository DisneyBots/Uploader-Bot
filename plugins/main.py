from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """

👋 Hᴇʟʟᴏ , {} ♡

Tʜɪꜱ ɪꜱ ᴘᴏᴡᴇʀꜰᴜʟ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ.

Pʀᴇꜱꜱ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ...

Pᴏᴡᴇʀᴇᴅ ʙʏ : [ᴅɪsɴᴇʏ ʙᴏᴛs](https://telegram.me/Disney_Bots)
"""
    HELP_TEXT = """
ʟɪɴᴋ ᴛᴏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ

➠ sᴇɴᴅ ᴀ ʟɪɴᴋ ғᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ /showthumb ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.

Pᴏᴡᴇʀᴇᴅ ʙʏ : [ᴅɪsɴᴇʏ ʙᴏᴛs](https://telegram.me/Disney_Bots)
 
"""
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ x ʙᴏᴛ](https://t.me/UploaderrXRobot)

**Cʜᴀɴɴᴇʟ** : [ᴅɪsɴᴇʏ ʙᴏᴛs](https://t.me/Disney_Bots)

**Vᴇʀꜱɪᴏɴ** : [2.0 ʙᴇᴛᴀ](https://t.me/UploaderrXRobot)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/tamilanbots)

**Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://heroku.com/)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.10.2](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 1.2.9](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** [𝙼𝚘𝚗𝚎𝚢𝙴𝚊𝚛𝚗𝚅𝙸𝙿](https://t.me/tamilanxbots)

**Pᴏᴡᴇʀᴇᴅ ʙʏ :** [@ᴅɪsɴᴇʏʜᴅʟɪɴᴋs](https://t.me/DisneyHDLinks)

"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ᴜᴘᴅᴀᴛᴇs', url='https://telegram.me/Disney_bots'),
        InlineKeyboardButton(' sᴜᴘᴘᴏʀᴛ', url='https://telegram.me/Disneybots_support')
        ],[
        InlineKeyboardButton(' ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton(' ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton(' ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton(' ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

    IFLONG_FILE_NAME = " ᴏɴʟʏ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs ᴄᴀɴ ʙᴇ ɴᴀᴍᴇᴅ . "
    RENAME_403_ERR = "sᴏʀʀʏ. ʏᴏᴜʀ ᴀʀᴇ ɴᴏᴛ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜɪs ғɪʟᴇ."
    ABS_TEXT = " ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʙᴇ sᴇʟғɪsʜ."
    UPGRADE_TEXT = "<b>ɴᴏ ᴘʀᴇᴍɪɴᴜᴍ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴏᴜʀ ʙᴏᴛ @Disney_Bots </b>  /help ғᴏʀ ᴅᴇᴛᴀɪʟs"
    FORMAT_SELECTION = "Nᴏᴡ ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ꜰᴏʀᴍᴀᴛ (ᴏʀ) ꜰɪʟᴇ ꜱɪᴢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = "📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ғɪʟᴇ "
    UPLOAD_FILE = " ᴜᴘʟᴏᴀᴅɪɴɢ 📤 \n\n To  transfer.sh "
    ANNO_UPLOAD = " ᴜᴘʟᴏᴀᴅɪɴɢ📤 \n\n To  anonfiles.com "
    BAY_UPLOAD = " ᴜᴘʟᴏᴀᴅɪɴɢ📤 \n\n To  bayfiles.com "
    GO_FILE_UPLOAD = " 📤ᴜᴘʟᴏᴀᴅɪɴɢ📤 \n\n To  gofile.io "
    DOWNLOAD_START = "📄 ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴜɴɪᴛs ɪᴛ's ᴄᴏᴍᴘʟᴇᴛᴇᴅ ⏳\n\n📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ sᴛᴀʀᴛᴇᴅ..."
    UPLOAD_START = "📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ..."
    RCHD_BOT_API_LIMIT = "sɪᴢᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ᴍᴀxɪᴍᴜᴍ ᴀʟʟᴏᴡᴇᴅ sɪᴢᴇ *500ᴍʙ). ɴᴇᴠᴇʀᴛʜʟᴇss, ᴛʀʏɪɴɢ ᴛᴏ ᴜᴘʟᴏᴀᴅ."
    RCHD_TG_API_LIMIT = "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\nᴅᴇᴛᴇᴄᴛᴇᴅ ғɪʟᴇ sɪᴢᴇ: {}\nᴅᴏʀʀʏ. ʙᴜᴛ, ɪ ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 2GB ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘɪ ʟɪᴍɪᴛᴀᴛɪᴏɴ."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " ᴊᴏɪɴ : https://t.me/Disney_Bots\nғᴏʀ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nᴛʜᴀɴᴋ ғᴏʀ ᴜsɪɴɢ ᴍᴇ\n\nᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs."
    NOT_AUTH_USER_TEXT = "ᴘʟᴇᴀsᴇ /upgrade ʏᴏᴜʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "ᴅᴇᴛᴇᴄᴛᴇᴅ ғɪʟᴇ sɪᴢᴇ: {}. ғʀᴇᴇ ᴜsᴇʀs ᴄᴀɴ ᴏɴʟʏ ᴜᴘʟᴏᴀᴅ: {}\nᴘʟᴇᴀsᴇ /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "✅ Tʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ ᴍᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " /n <b>ᴊᴏɪɴ : @Disney_Bots </b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "ɴᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ."
    NO_VOID_FORMAT_FOUND = "ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴜʀʟ"
    FILE_NOT_FOUND = "ᴇʀʀᴏʀ, ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʜɪɢʜ sᴘᴇᴇᴅ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ"
    REPLY_TO_DOC_FOR_C2V = "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ"
    REPLY_TO_DOC_FOR_SCSS = "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ sᴄʀᴇᴇɴsʜᴏᴛs"
    REPLY_TO_DOC_FOR_RENAME_FILE = "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛᴏ /ren ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ"
    AFTER_GET_LINK = " <b>ғɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n<b>ғɪʟᴇ sɪᴢᴇ :</b> {}\n\n<b>⚡ʟɪɴᴋ⚡ :</b> <code>{}</code>\n\nJoin : @Disney_bots_4u"
    AFTER_GET_DL_LINK = " <b>ғɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n<b>ғɪʟᴇ sɪᴢᴇ :</b> {}\n\n<b>⚡ʟɪɴᴋ⚡ :</b> <code>{}</code>\n\nValid for <b>14</b> days.\nJoin : @Disney_bots_4u"
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @Disney_Bots_4u \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>ғɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n<b>ғɪʟᴇ sɪᴢᴇ :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @Disney_Bots"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = " ᴘʀᴏᴄᴇss ᴄᴀɴᴄᴇʟʟᴇᴅ"
    ZIP_UPLOADED_STR = "ᴜᴘʟᴏᴀᴅᴇᴅ {} ғɪʟᴇs ɪɴ {} sᴇᴄᴏɴᴅs"
    FREE_USER_LIMIT_Q_SZE = """ᴄᴀɴɴᴏᴛ ᴘʀᴏᴄᴇss.
Fʀᴇᴇ ᴜsᴇʀs ᴏɴʟʏ 1 ʀᴇǫᴜᴇsᴛ ᴘʀᴇ 30 ᴍɪɴᴜᴛᴇs.
/upgrade or ᴛʀʏ 1800 sᴇᴄᴏɴᴅs ʟᴀᴛᴇʀ."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>sᴏʀʀʏ ᴅᴇᴀʀ ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ғᴏʀ ᴜsɪɴɢ ᴍᴇ 😌😉....</code>"
    BANNED_USER_TEXT = "<code>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ!</code>"
