import os

if __name__ == '__main__':

 while True:
    x = input("Enter what you want to say: ")
    if x == "q":
        break
    command = f'powershell -Command "Add-Type –AssemblyName System.Speech; '\
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
    os.system(command)
