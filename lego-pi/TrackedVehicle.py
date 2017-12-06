import multiprocessing
import time
from TrackedVehicleController import Controller
from l298n_shield import Tank

delay = 2

class Motion(multiprocessing.Process):


    motion_mapping = {
            "E" :"spinRight",
            "NE" : "right",
            "N" : "forward",
            "NW" : "left",
            "W" :"spinLeft",
            "SW" : "leftB",
            "S" : "backward",
            "SE" : "rightB",
            "Q" : "close"
    }

    def __init__(self, motion_queue):
        multiprocessing.Process.__init__(self)
        self.motion_queue = motion_queue



    def run(self):

        self.tank = Tank(enA=13, in1=16, in2=19, enB=26, in3=20, in4=21)
        
        proc_name = self.name
        run = True
        while run:
            next_task = self.motion_queue.get()
            if next_task is None:
                # No motion
                self.tank.stop()
            action = self.motion_mapping.get(next_task[0], "stop")
            speed = min(next_task[1], 1)
            getattr(self.tank, action)(speed)
            self.motion_queue.task_done()
            
            if next_task[0] == "Q":
                run = False

        print("Done, ... closing!")


if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue(1)
   

    motion = Motion(tasks)
    motion.start()

    ds4 = Controller(tasks, debug=True)
    ds4.listen()

   
    tasks.join()
