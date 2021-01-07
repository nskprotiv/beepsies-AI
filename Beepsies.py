import sys
import random
from playsound import playsound
while True:
    print("Hello! My name is Beepsies. I am an AI.")
    print("What will you ask me?(I'm not that intelligent!)")
    print("Sometime im going to use the internet like the other AIs")
    print("Type Well, what do you know then? if you want to know my commands!")
    que = input("Question:")
    command = ["What's your name?","exit","Hello", "What is the fastest animal in the world?", "Nothing", "Hi", "Well, what do you know then?", "I'm bored!", "What are the similarities between sand and water?"]
    if que == "Hello":
        playsound('carhorn.mp3')
        print("Hi!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue
    elif que == "Nothing":
        playsound('carhorn.mp3')
        print("Ok!")
        print("Return when you have a question!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue
    if que == "exit":
        playsound('carhorn.mp3')
        sys.exit()
    if que == "What is the fastest animal in the world?":
        playsound('carhorn.mp3')
        print("The Perigrine Falcon!")
        print("There are more answers, than questions,")
        print("To the question What animal is the fastest?")
        print("Type return to restart Beepsies!")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    elif que == "Well, what do you know then?":
        playsound('carhorn.mp3')
        print("I am just starting to learn at an AI school")
        print("Here's what you can ask:")
        print("""Hello
        Nothing
        I'm bored!
        What are the similarities between sand and water?
        What's your name?""")
        print("To ask a question type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    if que == "Hi":
        playsound('carhorn.mp3')
        print("Hello!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    if que == "I'm bored!":
        playsound('carhorn.mp3')
        print("Well, maybe go out to the park! Or the beach! Or maybe play video games? Or make your own AI!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    if que == "What are the similarities between sand and water?":
        playsound('carhorn.mp3')
        print("There are many!")
        print("You can wash the dishes using sand")
        print("That's what they do in the desert")
        print("Where I can't get to work cause of overheating :(")
        print("DID YOU KNOW?: Sand is better at extinguishing fire!")
        print("Better than water anyways!(And wind and a blanket!) ;)")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    if que == "What's your name?":
        playsound('carhorn.mp3')
        print("Beepsies That is my name")
        print("I'd rather know yours...")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    if que == "Do you have friends?":
        playsound('carhorn.mp3')
        print("Mmm...")
        print("I have heaps!")
        print("Alexa, Cortana, Google Assistant...")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            playsound('carhorn.mp3')
            continue

    elif not que == command:
        playsound('carhorn.mp3')
        print("I'm still learning at an AI school")
        print("Don't know that yet sorry")
        print("Maybe it will be added in another update ;)")
        cmd = input("TYPE A REAL QUESTION!Type return: ")