import pyautogui as pag
import sys
import time



def selectChar():
    while True:
        print("Waiting for champ select...") 
        inQueue = pag.locateOnScreen('assets/inQueue.png', confidence=0.7)
        if inQueue != None:
            #If the queue is still visible, hop back to main, game got dodged
            main()
        else:
            #If the queue is no longer visible we are in champion select
            print("Finding champion search...")
            select = pag.locateOnScreen('assets/champSearch.png', confidence=0.7)
            if select != None:
                #Find the search bar to search for the champion
                print("Finding champion...")
                pag.click(select)
                pag.typewrite(sys.argv[1])
                time.sleep(0.2)
                #After writing the champion we search for the portrait
                champion = "assets/" + sys.argv[1].capitalize() + ".png"
                #I could click on a static place here however it wouldnt work on all screens
                findChamp = pag.locateOnScreen(champion, confidence=0.7)
                if(findChamp != None):
                    #If the champion was located we click it after a short amount of time for consistency
                    time.sleep(0.2)
                    print("Found the champion!")
                    pag.click(findChamp)
                    break

def callPosition():
    #Finds chat box, when found it clicks and says position three times.
    #Three times because sometimes when entering champion select the first message
    #arrives faster than the client can handle and it doesnt register for others
    chatLocation = pag.locateOnScreen('assets/chatBox.png', confidence=0.7)
    if chatLocation != None:
        time.sleep(0.1)
        pag.click(chatLocation)
        for i in range(3):
            position = "I'm " + sys.argv[2] + "!"
            pag.typewrite(position)
            time.sleep(0.1)
            pag.press('enter')

def main():
    while True:
        print("Waiting for queue pop...") #While loop that continually looks for the accept button
        queuePop = pag.locateOnScreen('assets/accept.png', confidence=0.7)
        if queuePop != None: #If the accept button is found, sleep for a short while and then click, otherwise its too quick to register
            print("Found the accept button!")
            time.sleep(0.2)
            pag.click(queuePop)
            print("Accepted the game!")
            lockIn = pag.locateOnScreen('assets/editRunePage.png', confidence=0.8) 
            while True:
                print("Searching for champion select...")
                #This loops waits until it finds the edit rune page, meaning we are in champion select
                lockIn = pag.locateOnScreen('assets/editRunePage.png', confidence=0.8)
                if lockIn != None:
                    print("Breaking out of main loop, entered champion select.")
                    break
            break
    arguments = len(sys.argv)
    #if a second argument is added with position we add callPosition 
    if(arguments > 2):
        callPosition()    
    #if an additional argument is added with champion name we call selectChar function
    if(arguments > 1):
        selectChar()

if __name__=="__main__":
    main()