file1 = open('wordle.txt', 'r')
Lines = file1.readlines()
words = []
for line in Lines:
    words.append(line.strip())
file2 = open("letters_sorted.txt","r")
f2 = file2.readlines()
file3 = open("percents_sorted.txt","r")
f3 = file3.readlines()
for i in range(26):
    letters.append([f2[i],f3[i]])
attempt = 0
while(attempt<7)
    scores = []
    scoresi = []
    for i in words:
        score = 0
        for j in words:
            for a in letters:
                if a[0] == j:
                    score+=int(a[1][:-1])
        scores.append(score)
        scoresi.append(i)
    max_v = max(scores)
    max_i = scores.index(max_v)
    guess = scoresi[max_i]
    print(guess)
    print("put that word into the puzzle")
    in1 = input("first letter: ")
    in2 = input("second letter: ")
    in3 = input("third letter: ")
    in4 = input("fourth letter: ")
    in5 = input("fifth letter: ")
    parms = [in1,in2,in3,in4,in5]
    if parms != ["g","g","g","g","g"]:
        for i in range(len(parms)):
            if (parms[i]=="n"):
                badindex = letters.index(guess[i])
                del letters[badindex]
                del percents[badindex]
                for j in words:
                    if guess[i] in j:
                        del words[j]
                        j+=1
                        break
            if (parms[i]=="g"):
                for j in words:
                    if j[i] != word[i]:
                        del words[j]
                        j+=1
                        break
            if (parms[i]=="y"):
                for j in words:
                    if j[i] == word[i]:
                        del words[j]
                        j+=1
                        break
    else:
        print("done")
        break
    attempt +=1
        


