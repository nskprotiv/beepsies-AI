import sys
import webbrowser
import random
command = ["Hello, Hi, Nothing, exit, What is the fastest animal in the world?, I'm bored!, What are the similarities between sand and water?, What's your name?, Do you have friends?"]
while True:
    print("Hello! My name is Beepsies. I am an AI.")
    print("I know everything!")
    print("What will you ask me?") 
    que = input("Question: ")

    if que == "Hello":
        print("Hi!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    elif que == "Nothing":
        print("Ok!")
        print("Return when you have a question!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "exit":
        sys.exit()

    if que == "What is the fastest animal in the world?":
        print("The Perigrine Falcon!")
        print("There are more answers, than questions,")
        print("To the question What animal is the fastest?")
        print("Type return to restart Beepsies!")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "Hi":
        print("Hello!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "I'm bored!":
        print("Well, maybe go out to the park! Or the beach! Or maybe play video games? Or make your own AI!")
        print("To have more questions type return in your command prompt.")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "What are the similarities between sand and water?":
        print("There are many!")
        print("You can wash the dishes using sand")
        print("That's what they do in the desert")
        print("Where I can't get to work cause of overheating :(")
        print("DID YOU KNOW?: Sand is better at extinguishing fire!")
        print("Better than water anyways!(And wind and a blanket!) ;)")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "What's your name?":
        print("Beepsies That is my name")
        print("I'd rather know yours...")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    if que == "Do you have friends?":
        print("Mmm...")
        print("I have heaps!")
        print("Alexa, Cortana, Google Assistant...")
        print("To ask more, type return in the command prompt!")
        cmd = input("cmd: ")
        if cmd == "return":
            continue

    elif not que == command:

        new=2

        tabUrl = "https://google.com/?#q="
        
        webbrowser.open(tabUrl+que, new=new)