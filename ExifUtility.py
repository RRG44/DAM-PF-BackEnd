import subprocess
import re

# IMPORTANT 
# You need to download the executable version of exiftool for your OS: https://exiftool.org/
# Add the executable in your system variables e.i.: C:\exiftool\exiftool.exe

exiftool = "exiftool"

def readExif(image_path):
  process = subprocess.Popen([exiftool, "-a",  "-u", "-g1", image_path], stdout=subprocess.PIPE)
  output, standar_error = process.communicate()
  output_string = output.decode('latin-1')
  return formatString(output_string)

def deleteExif(image_path):
  process = subprocess.Popen([exiftool, "-all=", image_path], stdout=subprocess.PIPE)
  # output, standar_error = process.communicate() # not necessary
  # output_string = output.decode('latin-1') # not necessary

def formatString(string):
  pattern = r"---- File ----(.*)"
  match = re.search(pattern, string, re.DOTALL)
  if match:
    return "---- File ----"+match.group(1)
  else:
    return None

def processImage(name, base64Data):
  return 0

# TEST IT
# image_path = r"C:\Users\gr_mi\Desktop\AaToSave\Ing en Software\6to semestre\Aplicaciones Móbiles\olympus-d320l.jpg"
# print(readExif(image_path))