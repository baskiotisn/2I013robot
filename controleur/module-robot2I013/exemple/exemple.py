from robot2I013 import Robot2I013
import time
import numpy as np
class TestControler(object):
    def __init__(self):
        """ Initialise le controleur et un robot """
        self.robot = Robot2I013(self,fps=10.)
        self.cpt = 0
    def set_led(self,col):
        """ Allume les leds du robot au triplet col=(r,g,b) """
        self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE,*col)
    def set_speed(self,lspeed,rspeed):
        """ Fait tourner les moteurs a la vitesse lspeed pour le moteur gauche, rspeed pour le moteur droit """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,lspeed)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,rspeed)
    def forward(self,speed):
        """ Avant le robot a la vitesse speed """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,speed)

    def update(self):
        """ Exemple de fonction update : 
            Pour 50 pas fait avancer le robot, puis le tourne pour 20 pas puis s'arrete.
            Affiche la distance et enregistre une image tous les 10 pas, tourne la tete a gauche et a droite. 
        """
        self.cpt+=1
        if (self.cpt % 10)==0:
            print("Distance : ", self.robot.get_distance()," Position des roues : ", self.robot.get_motor_position())
            #self.robot.get_image().save("/tmp/Img_"+str(self.cpt)+".jpg")
            if (self.cpt % 20) == 0:
                self.robot.servo_rotate(30)
            else:
                self.robot.servo_rotate(120)

        if self.cpt<50:
            self.set_led((0,255,0))
            self.forward(100)
            return
        if self.cpt<70:
            self.set_speed(0,100)
            return
        self.set_led((255,0,0))
        self.set_speed(0,0)
    def stop(self):
        return self.cpt>80
    def run(self):
        self.robot.run()

if __name__=="__main__":
    ctrl = TestControler()
    ctrl.run()