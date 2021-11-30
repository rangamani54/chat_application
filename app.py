import socket
import threading
import speech_recognition as sr
import pyttsx3



serverip = "127.0.0.1"
serverport = 1000
st = "<sep>"

#receiverip = ""
#receiverport = 4648

       

#Client Socket
send = socket.socket()
print("Socket created")
send.connect((serverip, serverport))
print("Socket connected")
name = input("Enter your name: ")


def sender():
    while True:
        msgs = send.recv(1024).decode()
        print("\n"+ msgs)
        
t1 = threading.Thread(target=sender)
t1.daemon = True
t1.start()


while True:
    login=input("Enter the message Speak [S] or Quit [Q]: ")
    if login=="S":
        r=sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak("please say something")
            print("\t\t\t\tstart say")
            audio = r.listen(source)
            print("\t\t\t\tspeech done")
            pyttsx3.speak("Ok working on it")
            try:
                msg = r.recognize_google(audio)
                msg = f"{name}:{msg}"
                send.send(msg.encode())
            except Exception as e:
                print(f"Error occured: {e}")


    
    elif login == "Q":
        msg = f"{name} left chat"
        send.send(msg.encode())
        break
    else:
        msg = login
        msg = f"{name}:{msg}"
        send.send(msg.encode())

send.close()
