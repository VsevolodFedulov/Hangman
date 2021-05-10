import random
print("H A N G M A N")
go = input('Type "play" to play the game, "exit" to quit: ')
while go not in ['play', 'exit']:
    go = input('Type "play" to play the game, "exit" to quit: ')
if go == 'play':
    words = ('python', 'java', 'kotlin', 'javascript')
    ch = random.choice(words)
    ch2 = list("-" * len(ch))
    ch3 = list('abcdefghijklmnopqrstuvwxyz')
    ch4 = []
    lives = int(0)
    i = int(1)
    while lives != 8:
        if "-" in ch2:
            print()
            print(''.join(ch2))
            if "-" in ch2:
                l = input("Input a letter: ")
                if len(l) == 1:
                    if l not in ch3:
                        print('Please enter a lowercase English letter')
                    else:
                        if (l in ch) and not (l in ch2):
                            for i in range(len(ch)):
                                if ch[i] == l:
                                    ch2[i] = l
                        elif not (l in ch) and not (l in ch4):
                            print("That letter doesn't appear in the word")
                            ch4.append(l)
                            lives += 1
                        elif (l in ch2) or (l in ch4):
                            print("You've already guessed this letter")
                else:
                    print('You should input a single letter')
            else:
                print("""You guessed the word""", ch + '!')
                print("""You survived!""")
                break
        else:
            print("""You guessed the word""", ch + '!')
            print("""You survived!""")
            break
    if "-" in ch2:
        print("""You lost!""")
