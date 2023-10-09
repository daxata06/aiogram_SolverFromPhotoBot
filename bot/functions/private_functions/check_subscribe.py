from main import dp, bot



async def check_sub(user_id: int):
     result = await bot.get_chat_member(chat_id=-1001842549453, user_id=user_id)
     result=result.status
     if (result == 'member') or (result=='creator') or (result=='administrator'):
          return True
     else:
          return False