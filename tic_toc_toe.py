import random
import stddraw

def checker_PC(list):
    '''
        its choose a home and return the number of that
    '''

    pc_chosen_home = random.choice(list)
    while pc_chosen_home == 'taken' :
        pc_chosen_home = random.choice(list)


    if pc_chosen_home == 1 or pc_chosen_home == 2 or pc_chosen_home == 3:
        playground[0][pc_chosen_home - 1] = 2
    elif pc_chosen_home == 4 or pc_chosen_home == 5 or pc_chosen_home == 6:
        playground[1][pc_chosen_home - 4] = 2
    elif pc_chosen_home == 7 or pc_chosen_home == 8 or pc_chosen_home == 9:
        playground[2][pc_chosen_home - 7] = 2
    home_numbers[pc_chosen_home-1] = "taken"

    return None


def referee() :
    '''
        its choose that game is on or game is over and then clears the winner
    '''


    for j in range(0,3):
        if playground[0][0] == playground[1][1] == playground[2][2] == 1 :
            print("human wins1")
            return False

        elif playground[j][0] == playground[j][1] == playground[j][2] == 1 :
            print("human wins2")
            return False

        elif playground[0][j] == playground[1][j] == playground[2][j] == 1 :
            print("human wins3")
            return False

        elif playground[0][0] == playground[1][1] == playground[2][2] == 2 :
            print("PC wins1")
            return False

        elif playground[j][0] == playground[j][1] == playground[j][2] == 2 :
            print("PC wins2")
            return False

        elif playground[0][j] == playground[1][j] == playground[2][j] == 2 :
            print("PC wins3")
            return False

        elif home_numbers == ["taken"] *9:
            print("draw")
            return False



def draw() :


    pass



def checker_human(n) :

    '''
        this function clear homes with 1 (for human), 2 (for PC) and 0 for (free)
    '''
    if (a == 1 or a == 2 or a==3) and home_numbers[a-1] != 'taken':
        playground[0][a-1] = 1
    elif (a == 4 or a== 5 or a==6 ) and home_numbers[a-1] != 'taken':
        playground[1][a-4] = 1
    elif (a== 7 or a==8 or a==9 ) and home_numbers[a-1] != 'taken':
        playground[2][a-7] = 1
    home_numbers[a-1] = "taken"

    return None




playground = [ [0]*3, [0]*3, [0]*3 ]

home_numbers = [1,2,3,4,5,6,7,8,9]



while True :
    a = int(input("enter the number"))
    if a in home_numbers :
        
        checker_human(a)
        referee()
        print(referee())
        checker_PC(home_numbers)
        print(playground)
        print(home_numbers)
        print(referee())
        referee()
        if referee() == False :
            break
    else :
        print("that home is taken choose another")
