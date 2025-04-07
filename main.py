
from bot.handlers import *

TOKEN = "7553550247:AAFuY-BOnO8S1p0kbhv5aFOH59_YMM_ZCTY"

async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

    #
    # @dp.message()
    # async def echo_handler(message: Message) -> None:
    #     try:
    #
    #         await message.send_copy(chat_id=message.chat.id)
    #     except TypeError:
    #
    #         await message.answer("Nice try!")
