import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the diamention and properties of the button
        self.width, self.height = 200, 50
        self.button_color= (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #none attribute implies default font, 48 is the size

        # build the buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center =self.screen.center
        
        # the button message need to be prepped only once.
        # Pygame works with text by rendering the string you want to display as 
        # an image. we call _prep_msg() to handle this rendering.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """turn msg into a rendered image and center text on the button"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color) # boolean is for antialiasing , last parameter is the background
     
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center


    def draw_button(self):
        """draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
        

        

