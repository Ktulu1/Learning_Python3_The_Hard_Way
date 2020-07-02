print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("""The bear runs away.
        There is a door in the far wall labeled 1a.
        Do you open this door or back out and take door #2?
        1. Door 1a
        2. Door 2""")
        door1 = input("> ")
        if door1 == "1":
            print("You enter a room full of gold coins.")
            print("Do you take the coins?")
            print("1. Yes")
            print("2. No")
            coins = input("> ")
            if coins == "1":
                print("Just when you finish filling your pockets with the coins, the bear returns.")
                print("What do you do?")
                print("1. Run")
                print("2. Fight the bear")
                fightORflight = input("> ")
                if fightORflight == "1":
                    print("You try and run but the weight of the coins slows you down. The bear easily catches you and kills you dead.")
                elif fightORflight == "2":
                    print("""You put your hands up and tell the bear to bring it on.
                    The bear backs down and tells you that he doesn't want anything to do with fighting you.
                    You walk out the door with your pockets stuffed with gold coins and live out the rest of your days rich and happy.""")
                else:
                    print("What?!? The bear fucks you up and you die with your pockets full of gold.")
            elif coins == "2":
                print("You leave the coins and the strange doors forever. The next day you get hit by a car and die a sad, pennyless, person.")
            else:
                print("""You stand in the room not making the choices presented to you forever.
                You feel hungrey and thirsty and tired.
                You feel like you're going to die, but you never do.
                You spend the rest of eternity in that room... not following directions.""")
        elif door1 == "2":
            print("You back out of the room and run into the bear. He's not amused. You die by bear.")
        else:
            print("You get transported directly to hell because you can't follow dirtections. Burn in hell loser.")   

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")