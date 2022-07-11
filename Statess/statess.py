from aiogram.dispatcher.filters.state import State, StatesGroup

class From(StatesGroup):
	channelAdd = State()
	channelDelete = State()
	send_msg = State()
	forward_msg = State()
	clear_msg = State()

	Qissa_add = State()
	Qissa_name_btn = State()
	Qissa_file_btn = State()

	Q = State()