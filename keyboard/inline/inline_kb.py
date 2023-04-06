from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="text", url='https://youtu.be/2Il_Ab-s0W8'),
                                        InlineKeyboardButton(text="text", callback_data='text')
                                    ]
                                ])