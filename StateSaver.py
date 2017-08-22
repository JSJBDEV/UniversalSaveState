import tkinter as t
import shutil as s
import distutils.core
class Application(t.Frame):
    def __init__(self, master):
        print("Welcome to")
        print("   _____ __        __      _____                      ")
        print("  / ___// /_____ _/ /____ / ___/____ __   _____  _____")
        print("  \__ \/ __/ __ `/ __/ _ \\__ \/ __ `/ | / / _ \/ ___/")
        print(" ___/ / /_/ /_/ / /_/  __/__/ / /_/ /| |/ /  __/ /    ")
        print("/_____\______,_/\__/\___/____/\__,_/ |___/\___/_/     ")
        print("  <  // __ \                                          ")
        print("  / // / / /                                          ")
        print(" / // /_/ /                                           ")
        print("/_(_)____/    ")                                        
        t.Frame.__init__(self, master)
        self.master.geometry("400x220")
        self.grid()
        self.widgets()

    def widgets(self):
        self.Directory = t.Entry(self)
        self.Directory.insert(0, "Directory to saves")
        self.Directory.grid(row = 0, column = 0)

        self.File = t.Entry(self)
        self.File.insert(0, "Save name")
        self.File.grid(row = 0, column = 1)

        var = t.StringVar()
        self.var = var
        self.output = t.Label(self, textvariable = var)
        self.output.grid(row = 3, column = 2)
        
        self.save = t.Button(self, text="Save", command = self.save)
        self.save.grid(row = 4, column = 1)

        self.save = t.Button(self, text="Restore", command = self.restore)
        self.save.grid(row = 4, column = 2)

        self.state = t.Listbox(self)
        self.state.grid(row = 3, column = 1)
        for i in range(0, 10): # This should produce an array of 9?
            self.state.insert(t.END, str(i))

    def save(self):
        statevar = int(str(self.state.curselection()).replace(',)', "").replace('(', ''))
        if statevar != None:
            dir2 = self.Directory.get() + "\\" + self.File.get()
            if self.var.get().count('\r') > 4:
                self.var.set("")
            self.print2("Savestate number is " + str(statevar))
            self.print2("Saving World to " + str(self.File.get()) + "...")
            distutils.dir_util.copy_tree(dir2, dir2 + str(statevar))
            self.print2(self.Directory.get() + "Backup\\" + self.File.get() + str(statevar))
            distutils.dir_util.copy_tree(dir2, self.Directory.get() + "\\Backup\\" + self.File.get() + str(statevar))
            self.print2("Saved as " + str(self.File.get()) + str(statevar))

    def restore(self):
        statevar = int(str(self.state.curselection()).replace(',)', "").replace('(', ''))
        dir2 = self.Directory.get() + "\\" + self.File.get()
        if self.var.get().count('\r') > 4:
            self.var.set("")
        self.print2("Restoring world")
        distutils.dir_util.copy_tree(self.Directory.get() + "\\Backup\\" + self.File.get() + str(statevar), dir2 + str(statevar))
        self.print2("Restored done!")
    def print2(self, msg):
        print(msg)
        self.var.set(self.var.get() + "\r" + msg)
        self.output.grid(row = 3, column = 2)

root = t.Tk()
root.title("Savestater")
app = Application(root)
root.mainloop
