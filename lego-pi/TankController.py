import pygame

#Taken from https://www.pygame.org/docs/ref/joystick.html

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

class Controller:

    def __init__(self, debug=False):
        pygame.init()
         
        # Set the width and height of the screen [width,height]
        self.screen = pygame.display.set_mode([500, 700])

        pygame.display.set_caption("Lego Tank Controller")

        #Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Initialize the joysticks
        pygame.joystick.init()
            
        # Get ready to print
        self.textPrint = TextPrint()

        # If DEBUG is enabled print the status of the controller.
        self.debug = debug


    def listen(self):
        # -------- Main Program Loop -----------
        while self.done==False:
            
            # EVENT PROCESSING STEP
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that we are done so we exit this loop
                
                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                if event.type == pygame.JOYAXISMOTION:
                    print("Joystick AXIS motion.")

                if event.type == pygame.JOYBALLMOTION:
                    print("Joystick BALL motion.")
                    
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick BUTTON pressed.")
                    
                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick BUTTON released.")
                    
                if event.type == pygame.JOYHATMOTION:
                    print("Joystick HAT motion.")
            
            if self.debug:
                self.state()        
        
        self.close()


    def state(self):
        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill(WHITE)
        self.textPrint.reset()

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        self.textPrint.print(self.screen, "Number of joysticks: {}".format(joystick_count) )
        self.textPrint.indent()
        
        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
        
            self.textPrint.print(self.screen, "Joystick {}".format(i) )
            self.textPrint.indent()
        
            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()
            self.textPrint.print(self.screen, "Joystick name: {}".format(name) )
            
            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            self.textPrint.print(self.screen, "Number of axes: {}".format(axes) )
            self.textPrint.indent()
            
            for i in range( axes ):
                axis = joystick.get_axis( i )
                self.textPrint.print(self.screen, "Axis {} value: {:>6.3f}".format(i, axis) )
            self.textPrint.unindent()
                
            buttons = joystick.get_numbuttons()
            self.textPrint.print(self.screen, "Number of buttons: {}".format(buttons) )
            self.textPrint.indent()

            for i in range( buttons ):
                button = joystick.get_button( i )
                self.textPrint.print(self.screen, "Button {:>2} value: {}".format(i,button) )
            self.textPrint.unindent()
                
            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in an array.
            hats = joystick.get_numhats()
            self.textPrint.print(self.screen, "Number of hats: {}".format(hats) )
            self.textPrint.indent()

            for i in range( hats ):
                hat = joystick.get_hat( i )
                self.textPrint.print(self.screen, "Hat {} value: {}".format(i, str(hat)) )
            self.textPrint.unindent()
            
            self.textPrint.unindent()

        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second
        self.clock.tick(10)
    
    def close(self):
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit ()


if __name__ == "__main__":
    ds4 = Controller(debug=True)
    ds4.listen()
