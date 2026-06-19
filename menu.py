import gui

def init(window, font, play_command):
	global background
	global name
	global play_button

	background = gui.Image("resources/images/menu.png")
	name = gui.Text(window, window.get_width() - font.get_size() - 128 - 64, font.get_size(), font.get_font(), "Zero Pointer", True, gui.get_color("red"))
	play_button = gui.Button(window, gui.Image("resources/images/play_button.png").get_image(), gui.Image("resources/images/play_button_highlight.png").get_image(), window.get_width() / 4 / 2, 128, play_command)

def draw_background(window):
	global background

	window.draw(obj=background.get_image(), x=0, y=0, rect=None)

def draw_name():
	global name

	name.draw()

def draw_play():
	global play_button

	play_button.draw()

def update_play():
	global play_button

	play_button.update()