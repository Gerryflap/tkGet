import urllib.request
import tkinter
import time
import _thread

MAX_Y = float(1500)
SERVER_ADDR = "http://192.168.178.1"

class App(tkinter.Frame):
    def __init__(self, maxTimes, master = None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.title = "Lagfeest"
        self.times = []
        self.maxTimes = maxTimes
        self.view = []
        self.createWidgets()
        _thread.start_new_thread(self.netThread, tuple([]))

    def createWidgets(self):
        self.c = tkinter.Canvas(self, width=500, height=500)
        self.c.pack()

        #Create the bars:
        for i in range(self.maxTimes):
            x = i * 5
            self.view.append(self.c.create_rectangle(x, 500, x + 5, 500, fill='#F00'))
            i += 1

        #Create x lines:
        lineNum = 4
        dy = 500/(lineNum+1)
        y = 0
        y += dy
        for i in range(lineNum):
            self.c.create_line(0, y, 500, y, fill='#0F0')
            self.c.create_text(20, y + 10, text = str(int((500 - y)/(500.0/MAX_Y))), fill='#00F')
            y += dy
            
            

    def addTime(self, time1):
        if self.maxTimes <= len(self.times):
            self.times = self.times[1:]
        self.times.append(time1)
        self.update()

    def update(self):
        i = 0
        for val in self.times:
            x1, y1, x2, y2 = self.c.coords(self.view[i])
            self.c.coords(self.view[i], x1, 500, x2, 500 - (val * (500.0/MAX_Y)))
            i += 1
            
        
    def netThread(self):
        t = 0
        while True:
            t = time.time()
            try:
                urllib.request.urlopen(SERVER_ADDR)
            except:
                pass
            t = (time.time() - t)*1000
            self.addTime(t)
            time.sleep(0.1)

root = tkinter.Tk()
app = App(100, master=root)
root.title("Lagfeest")
root.mainloop()

