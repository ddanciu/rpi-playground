import pygame
import math
from time import sleep

#Taken from https://www.pygame.org/docs/ref/joystick.html

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)


BUTTON_X = 1

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

    def __init__(self, queue, debug=False):
        pygame.init()

        self.queue = queue
         
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


        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        if joystick_count < 1:
            self.joystick = None
        else:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        self.direction = None
        self.magnitude = 0

        self.state()


    def listen(self):
        # -------- Main Program Loop -----------
        while self.done==False:


            self.action = None
            
            # EVENT PROCESSING STEP
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that we are done so we exit this loop
                
                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                if event.type == pygame.JOYAXISMOTION:
                    #print("Joystick AXIS motion.")
                    
                    x = self.joystick.get_axis( 0 )
                    y = self.joystick.get_axis( 1 )

                    self.direction = self.computeDirection(x, y)
                    self.magnitude = self.computeMagnitude(x, y)

                    self.action = (self.direction, self.magnitude)

                if event.type == pygame.JOYBALLMOTION:
                    print("Joystick BALL motion.")
                    
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick BUTTON pressed, quit: " + str(self.done))
                    self.done = self.done | (self.joystick.get_button( 1 ) == 1)
                    


                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick BUTTON released.")
                    
                    
                if event.type == pygame.JOYHATMOTION:
                    print("Joystick HAT motion.")
            


            if self.done: 
                self.action = ("Q", 0)

            if self.action:
                self.queue.put(self.action)


                
            # Limit to 20 frames per second
            self.clock.tick(20)
                
            if self.debug:
                self.state()        
        
        self.close()
        

    def computeMagnitude(self, x = 0, y = 0):
        if abs(x) < 0.2 and abs(y) < 0.2:
            return 0
        return math.sqrt(x*x + y*y)

    def computeDirection(self, x = 0, y = 0):

        if abs(x) < 0.2 and abs(y) < 0.2:
            return None

        alpha = math.atan2(-y, x)

        pi_per_8 = math.pi / 8
        
        if -pi_per_8 < alpha and alpha <= pi_per_8:
            _direction = "E"

        if pi_per_8 < alpha and alpha <= (3 * pi_per_8):
            _direction = "NE"
        
        if (3 * pi_per_8) < alpha and alpha <= (5 * pi_per_8):
            _direction = "N"
        
        if (5 * pi_per_8) < alpha and alpha <= (7 * pi_per_8):
            _direction = "NW"
        
        if (7 * pi_per_8) < alpha or alpha <= (-7 * pi_per_8):
            _direction = "W"
        
        if (-7 * pi_per_8) < alpha and alpha <= (-5 * pi_per_8):
            _direction = "SW"
        
        if (-5 * pi_per_8) < alpha and alpha <= (-3 * pi_per_8):
            _direction = "S"

        if (-3 * pi_per_8) < alpha and alpha <= -pi_per_8:
            _direction = "SE"

        return _direction

    def getArc(self, _dir):

        pi_per_8 = math.pi / 8

        arcs = {

            "E" : (-pi_per_8, pi_per_8),

            "NE" : (pi_per_8, (3 * pi_per_8)),
            
            "N" : ((3 * pi_per_8), (5 * pi_per_8)),
            
            "NW" : ((5 * pi_per_8), (7 * pi_per_8)),
            
            "W" : ((7 * pi_per_8), (-7 * pi_per_8)),
            
            "SW" : ((-7 * pi_per_8), (-5 * pi_per_8)),
            
            "S" : ((-5 * pi_per_8), (-3 * pi_per_8)),

            "SE" : ((-3 * pi_per_8), -pi_per_8)
        }

        return arcs[_dir]


    def drawCircleArc(self, screen,color,center,radius,startRad,endRad,thickness):
        (x,y) = center
        rect = (x-radius,y-radius,radius*2,radius*2)
       
        pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)

    def state(self):
        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill(WHITE)
        self.textPrint.reset()
    
        # Get the name from the OS for the controller/joystick
        name = self.joystick.get_name()
        self.textPrint.print(self.screen, "Joystick name: {}".format(name) )


        # Get the name from the OS for the controller/joystick
        self.textPrint.print(self.screen, "DIRECTION: {}, MAGNITUDE: {:>6.3f}".format(self.direction, self.magnitude) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = self.joystick.get_numaxes()
        self.textPrint.print(self.screen, "Number of axes: {}".format(axes) )
        self.textPrint.indent()
        
        for i in range( axes ):
            axis = self.joystick.get_axis( i )
            self.textPrint.print(self.screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        self.textPrint.unindent()
            
        buttons = self.joystick.get_numbuttons()
        self.textPrint.print(self.screen, "Number of buttons: {}".format(buttons) )
        self.textPrint.indent()

        for i in range( buttons ):
            button = self.joystick.get_button( i )
            self.textPrint.print(self.screen, "Button {:>2} value: {}".format(i,button) )
        self.textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = self.joystick.get_numhats()
        self.textPrint.print(self.screen, "Number of hats: {}".format(hats) )
        self.textPrint.indent()

        for i in range( hats ):
            hat = self.joystick.get_hat( i )
            self.textPrint.print(self.screen, "Hat {} value: {}".format(i, str(hat)) )
        self.textPrint.unindent()
        
        self.textPrint.unindent()


        pygame.draw.circle(self.screen, BLACK, (300, 500), 100, 2)
        if self.direction == None:
            pygame.draw.circle(self.screen, BLUE, (300, 500), 20, 0)
        else:
            arc = self.getArc(self.direction)
            mag = (int) (100 * min(self.magnitude, 0.99))
            self.drawCircleArc(self.screen, RED, (300, 500), mag, arc[0], arc[1], mag)
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    


    def close(self):
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit ()



