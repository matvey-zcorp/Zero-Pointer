import pygame
import gui

def main():
	bookAntiqua_font = gui.Font("resources/fonts/BKANT.TTF", 24)
	window = gui.Window(640, 480, "Zero Pointer", None)
	test_text = gui.Text(window, window.get_width() / 2 - bookAntiqua_font.get_size(), window.get_height() / 2 - bookAntiqua_font.get_size(), bookAntiqua_font.get_font(), "TEST", False, pygame.Color("yellow"))
	while True:
		test_text.draw()
		window.update()
if __name__ == "__main__":
	main()