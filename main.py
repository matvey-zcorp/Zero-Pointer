import menu
import gui

scene = "menu"

def main():
	global scene

	def change_scene_to_level_selector():
		global scene

		scene = "level-selector"

	window = gui.Window(640, 480, "Zero Pointer", None)

	bookAntiqua_font = gui.Font("resources/fonts/BKANT.TTF", 32)

	menu.init(window, bookAntiqua_font, change_scene_to_level_selector)

	while True:
		if scene == "menu":
			menu.draw_background(window)
			menu.draw_name()
			menu.draw_play()
			menu.update_play()
		window.update()

if __name__ == "__main__":
	main()