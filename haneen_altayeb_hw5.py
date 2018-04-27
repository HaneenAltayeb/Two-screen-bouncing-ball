from Tkinter import *
import time
from socket import *

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'red'


class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            # Message Receiver
            print "Server running"
            self.speedx*=-1
            addr = ("10.50.84.109", 8080)
            UDPSock = socket(AF_INET, SOCK_DGRAM)
            UDPSock.sendto(str(pos), addr)
            UDPSock.close()

            addr = ("", 1000)  # 100 is The port of this computer...
            UDPSock = socket(AF_INET, SOCK_DGRAM)
            UDPSock.bind(addr)
            (pos, addr) = UDPSock.recvfrom(1024)

        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1


    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(40, self.move_active) # changed from 10ms to 30ms



# print "Server running"
addr = ("", 1000)  # 100 is The port of this computer...
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
# while True:
# print "hey there"
(pos, addr) = UDPSock.recvfrom(1024)

print pos
UDPSock.close()


ball = Ball()
tk.mainloop()