#Savestate creater
import shutil
while True:
    an = input("source world directory (will be save as 'src'1):")
    new = an+"1"
shutil.copytree(an,new)