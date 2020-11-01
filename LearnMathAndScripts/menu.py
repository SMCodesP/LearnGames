import pygame_menu
import os.path as path


class Menu:

    def __init__(self):
        engine = pygame_menu.sound.Sound()
        __audiodir__ = path.join(path.dirname(path.abspath(__file__)), 'resources', 'audio', '{0}')
        engine.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, '/home/smcodes/PycharmProjects/LearnGames/LearnMathAndScripts/resources/audio/vgmenuselect.ogg')
        fontMenu = pygame_menu.font.FONT_NEVIS
        __fontdir__ = path.join(path.dirname(path.abspath(__file__)), 'resources', 'fonts', '{0}')
        minecrafter = __fontdir__.format('Minecrafter.otf')
        __imagedir__ = path.join(path.dirname(path.abspath(__file__)), 'resources', 'images', '{0}')
        theme = pygame_menu.themes.Theme(
            background_color=pygame_menu.baseimage.BaseImage(image_path=__imagedir__.format("wallpaper.jpg")),
            menubar_close_button=False,
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
            widget_font=fontMenu,
            widget_selection_effect=pygame_menu.widgets.HighlightSelection(border_width=5, margin_x=25, margin_y=0),
            title_background_color=(224, 32, 65),
            title_font_color=(51, 51, 51),
            title_font=fontMenu,
            title_font_size=35,
            title_offset=(5, 0),
            title_shadow=True,
            title_shadow_color=(65, 65, 65),
            title_shadow_offset=1,
            widget_margin=(-15, 25),
            widget_offset=(0, 15),
            widget_alignment=pygame_menu.locals.ALIGN_RIGHT,
            widget_font_color=(255, 255, 255)
        )
        self.menu_template = pygame_menu.Menu(720, 1280, title="Nomad warrior - Olympus prison", theme=theme)
        self.menu_template.add_text_input('Nome » ', default='SMCodes')

        def start_the_game():
            self.menu_template.disable()
            pass

        self.menu_template.add_button('Jogar', start_the_game)
        self.menu_template.add_selector(
            'Dificuldade » ',
            [('Dificil', 1), ('Medio', 2), ('Facil', 3)])
        self.menu_template.add_button('Sair', pygame_menu.events.EXIT)
        self.menu_template.set_sound(engine, recursive=True)

    def render(self, screen):
        self.menu_template.mainloop(screen)
