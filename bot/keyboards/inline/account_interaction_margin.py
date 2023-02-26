from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.inline.callback_data.callback_data import acc_inter_cb_data


def account_interaction_buttons_margin(acc_name: dict) -> InlineKeyboardMarkup:
	interactions = InlineKeyboardMarkup(row_width=2)

	balance = InlineKeyboardButton("Balance", callback_data=acc_inter_cb_data.new(
		acc_name=acc_name, id="balance"
	))
	stability = InlineKeyboardButton("Stability", callback_data=acc_inter_cb_data.new(
		acc_name=acc_name, id="stability"
	))
	yield_period = InlineKeyboardButton("Yield", callback_data=acc_inter_cb_data.new(
		acc_name=acc_name, id="yield"
	))
	cancel_orders = InlineKeyboardButton("Cancel Orders", callback_data=acc_inter_cb_data.new(
		acc_name=acc_name, id="cancel"
	))
	back = InlineKeyboardButton("« Back to Accounts List", callback_data=acc_inter_cb_data.new(
		acc_name=acc_name, id="back"
	))

	interactions.insert(balance)
	interactions.insert(stability)
	interactions.insert(yield_period)
	interactions.insert(cancel_orders)
	interactions.insert(back)

	return interactions