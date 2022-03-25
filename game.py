list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (list)
player1_pocket = 0
player2_pocket = 0
def inputs():
    global player1_pocket
    global player2_pocket
    player1 = int(input("player1 choose a number from the list :  " ))
    list.remove(player1)
    player1_pocket += player1
    print(list)
    print("player1 values is : ",  player1_pocket )

    player2 = int(input("player2 choose a number from the list :  " ))
    list.remove(player2)
    player2_pocket +=  player2
    print(list)
    print("player2 values is : ",  player2_pocket )

def checker():
    for i in list:
        if player1_pocket == 15:
            print("player1 wins")
        break

    for j in list:
        if player2_pocket == 15:
            print("player2 wins")
            break
    for a in list:
        if len(list) < 0 :
            print ("draw")
            break

inputs()


inputs()


inputs()

checker()

inputs()

checker()
for k in list :
    if player1_pocket != 15 and player2_pocket != 15 :
        print("draw")
        break