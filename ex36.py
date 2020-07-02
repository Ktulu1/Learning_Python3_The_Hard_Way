import secrets

coin = ['Heads', 'Tails']
oneInFour = [1, 2, 3, 4]

def end(why):
    print(why, "\n\n\n\n\n\n\n\n\n\n\n                                 --= The End =--\n\n\n\n\n\n\n\n\n\n\n\n\n")
    exit(0)

def cowardsLife(why):
    print("\n\n-------------------------------------------------------------------------------------\n\n")
    print(why)
    end("\n\n\n\n\nYou spend the rest of your dull, boring, life playing it safe, and you die alone.")

def start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n---------------------------------------------------------------------------\n")
    print("""\n    One day you receive a stange letter in the mail from your uncle Francis.
    What makes this letter particularly strange is that your uncle had recently passed
    away at the ripe old age of 106. He had been in an insane asylum in New England
    someplace since his late 30s. No one in you family liked to talk about uncle
    Francis, but you've heard grumblings from time to time.
    
    You try to read the letter but it's mostly incomprehensible rubbish about old
    things and great ones. The few scraps you can piece togther talk about a box
    containing information on something or other that could be very dangerous, but
    also could be highly valuable to the right people. There's crossed out words,
    lines and arrows pointing back, and forward, to other sentances, comments and
    additional text in the margins. The letter is a mess. The ramblings of an old
    senile man who's been quite mad most of his life.
    
    Huh! You just got an unreadable letter from a, by all accounts, batshit crazy
    uncle whom you've never met and recently died of being older than dirt. What is
    going on? You look at the letter again and chuckle. This is insane.\n""")
    home()

def home():
    print("\n\n-------------------------------------------------------------------------------------\n")
    print("You have a decision to make.\n")
    print("\tIgnore the letter and stay home.\n")
    print("\tDecide that you're going to try and find the box, and plan your next move.\n")
    print("\tLeave it up to chance and toss a coin.\n")
    
    choice = input("> Make a decision. [stay], [plan], or [toss]: ")
    if choice == "stay":
        cowardsLife("    You toss the stupid letter in the fireplace and go to bed.")
    elif choice == "plan":
        whereToStart()
    elif choice == "toss":
        homeToss()
    else:
        home()

def toss():
    print("\n\n-------------------------------- COIN TOSS -------------------------------------------\n")
    print("\nYou take out a liberty dollar and flip the coin high in the air.")
    print("You catch it and slap it on the back of your other hand.\n\n")
    
    result = secrets.choice(coin)
    enter = input("> Hit enter to uncover the coin.\n\n\n")
    if enter == "":
        return result
    else:
        return result

def homeToss():
    print("\n\n-------------------------------------------------------------------------------------\n")
    print("\nHeads you stay home and throw the letter away. Tails you try to find the box.\n")
    
    choice = input("> Flip a coin? [y] or [n]: ")
    if choice == "y":
        result = toss()
        print(f"\n\n--------------------------------- {result}! --------------------------------------------\n")
        if result == "Heads":
            cowardsLife("\n    Oh well. The letter was probably bushit anyway.")
        else:
            whereToStart()
    else:
        home()

def whereToStart():
    print("\n\n-------------------------------------------------------------------------------------\n")
    print("\nWhere to start? You need to come up with a plan.\n")
    print("""    The letter mentions a Professor Angell. Could that be a clue that needs to be 
    followed up?\n""")
    print("""    Your father also had a sister, aunt Judy, who is still alive. You haven't seen 
    her in a long time. Maybe she knows something about uncle Francis.\n""")
    
    choice = input("> Where to start? [angell] or [judy]: ")
    if choice == "angell":
        angell()
    elif choice == "judy":
        judy()
    else:
        whereToStart()

def angell():
    print("\n\n-------------------------------------------------------------------------------------\n")
    print("\nProfessor Angell...\n")
    print("""    You Google Professor Angell and find there are actually many more Professor Angells 
    than you had hoped. You spend hours looking over the search results and find a 
    Professor George Gammell Angell the 3rd at the University of Chicago. Not too far from 
    your home. A few hours in a plane, one or two more in a car. Noted. You move on.
    
    There's another Professor George Gammell Angell from Brown University. HA! New
    England! Oh, no, this guys been dead for over a hundred years. Probably not our guy.
    
    Here's another George Angell from Miskatonic University. Why is everyone named Angell
    a professsor? Could this be any harder? Never heard of Miskatonic. Huh, also in New 
    England. Wait, this guy is Professor George Gammell Angell Jr. and he worked at the
    Arkham Asylum. I remember that name from the wispered talk about uncle Francis. 
    GAH! This clown is also dead.
    
    Wait, wasn't there a "the 3rd". Yeah, the guy in Chicago. That's got to be something.
    
    Chicago... Chicago.
    
    You look up flights to Chicago. Eight hundred bucks for a flight tomorrow morning. 
    Crap. If you left early tomorrow morning and drove all day, you could be there by
    early afternoon to catch this dude at the school.\n""")

    choice = travel()
    if choice == "fly":
        fly()
    elif choice == "drive":
        drive()
    else:
        angell()


def judy():
    print("\n\n-------------------------------------------------------------------------------------\n")
    print("\nJudy. Your father and uncle Francis' sister. Maybe she knows something about all this.\n")
    print("""    You rifle through some junk drawers looking for the old address book. Finally
    you find it in the last place you look. Funny. Should have just looked there first. 
    Anyway, you find Judy's number and ring her up.

    The phone rings for a bit and just as you're about to hang up you hear, "Hello?"

    You explain the letter and everything to aunt Judy and there's nothing for a long 
    while then Juday says, "Huh!" Then there's another long pause. Given this time to 
    think, you realize how silly you must sound. You're just about to apologize to Judy 
    for wasting her time when she says, "I think I have something you need to see." "Get 
    here as fast as you can. I think I know where it's at. I'll find it before you get
    here."
    
    You thank aunt Judy and tell her you'll be there as soon as possible.
    
    You look up flights to Philadelphia. Eight hundred bucks for a flight tomorrow 
    morning. Crap. If you left early tomorrow morning and drove all day, you could be at 
    aunt Judy's by early afternoon.\n""")

    choice = travel()
    if choice == "fly":
        fly()
    elif choice == "drive":
        drive()
    else:
        judy()

def travel():
    print("\n\n--------------------------------- Travel --------------------------------------------\n")
    choice = input("\n> What are you going to do? [fly], [drive], or [give] up: ")
    if choice == "fly":
        return choice
    elif choice == "drive":
        return choice
    elif choice == "give":
        cowardsLife("""\n    It cost to much to fly and you're too lazy to drive. Fuck it. Stupid anyway. You turn 
    off the computer, toss the letter in the fireplace, and go to bed.""")
    else:
        travel()

def fly():
    print("\n\n--------------------------------- Flying --------------------------------------------\n")
    print("""\n    You decide to fly. After all, time is money and you dont have much of either. 
    You pack light for a day trip, grab your bag, and go. You drive to the airport, park 
    your car, and head into the terminal. You don't need to check a bag so you move right 
    through securtiy, find your gate, and wait for your flight. You've got plenty of time 
    so you take out uncle Francis' letter and read it again. Man that guy was nuts. What
    are you doing? You're about to get on a plane and fly to talk to someone about this 
    horseshit all, suposedly, with a straight face. The joke is cleary on you. Maybe you... 
    Wait, you just missed an announcement in the terminal. Was that your flight number?
    You move to the flight display and, fuck, your flight is delayed.\n""")
    
    choice = input("""\n What are you going to do now?\n
> [wait], [drive] instead, or just go [home] and forget all this tomfoolery: """)
    if choice == "wait":
        print("\nSkyin' like a bird.")
    elif choice == "drive":
        drive()
    elif choice == "home":
        driveHome()
    else:
        fly()

def driveHome():
    cowardsLife("""\n    This is just too much! You ball up your uncle's letter, toss it in the 
    trash, storm out of the airport, and drive home. You drive distracted and angry. So 
    you don't see the truck that blows off the stop light. You wake up in the hospital, 
    have a breathing tube down your throat, and you start to panic before you pass out. 
    The next time you wake up, they're taking the tube out. You're aware of a pain in 
    your lower back that makes you want to screem at the top of your lungs. The pain is so 
    bad your head starts to swim and you pass out again. The next time you wake up you 
    realize you can't move your legs and you start to panic again. A nurse is in the room, 
    he settles you down, and explains what happened.
        
    After weeks in the hospital and months learning to walk again, you can finally put all 
    of this behind you and return to your regular life. Fuck you uncle Francis!""")

def drive():
    print("\n\n------------------------------ Road Trippin! ----------------------------------------\n")
    
    choice = input("""\nYou climb behind the wheel of your automobile. Where to?\n
> Angell in [chicago], aunt Judy in [philly], or go [home] and forget this nonsense: """)
    if choice == "chicago":
        print("\nChicago!")
        chicago()
    elif choice == "philly":
        print("\nPhiladelphia!")
        philadelphia()
    elif choice == "home":
        driveHome()
    else:
        drive()

def chicago():
    print("\nThe Windy City!")
    print("""\n    You start off down the open road thinking about how much you love road trips. They're 
    the definition of freedom. After a few hours you start to get bored, your butt is 
    falling asleep, and you just want to get to the University of Chicago already. You 
    finally pull into the lot, climb, more like tumble, out of the car and stretch like 
    a bear that's been hibernating for months.
    
    You walk up to the history building and overhear a conversation on the steps.
    
    \"...but Doctor Angell... I've completed all the assignments, don't you want me to...\"
    
    \"Wait a minute Cortney. You know you need to pass my final to get credit. Just
    show up for a change. You're a smart girl. You'll do fine.\")

    Sigh, \"Whatever professor. Someday you'll regret not... helping me.\" Cortney bounces
    off toward the parking lot and the whole world seems to pause until she's out of sight.

    Professor Angell mumbles to himself, \"I already do.\"

    You walk up to the professor and introduce yourself. You explain the letter and, 
    surprisingly, the guy doesn't run screaming from you. He says he has some information
    that might be of interest to you, but he can't tell you here and there's something 
    you need to see.

    He asks for your phone number and texts you an address. The professor asks you to meet 
    him there at 10:30 pm.

    You thank him for his time and walk back to your car.

    When you get in the car you lookup the address on Google Maps and it looks like an 
    industrial area. Huh, 11pm in, what looks like, a run down industrial park. Great! That 
    sounds safe. This just keeps getting better. You drive off and look for a place to get 
    a bite to eat and burn some time.
    
    While eating pizza, that's shaped like an apple pie, stuffed with pizza toppings, and 
    made out of pizza dough, you roll the encounter with Angell over in your head.
    
    He seemed like a good guy. Just about any breathing human, male or female, would have
    done anything for that "Courney" in half a heartbeat. Granted, this was a very brief
    encounter, but he seemed to care for his student. Maybe he can be trusted.\n""")
    print("What to do?\n")
    
    choice = input(">[meet] with Angell, or this is not worth the risk, drive [home]?: ")
    if choice == "meet":
        meetingAngell()
    elif choice == "home":
        cowardsLife("""\n    You start the car and drive home. You spend the entire trip in silence, 
    steaming about how stupid this whole thing has been. You've wasted an entire day, ate 
    some shitty pizza, and... what the heck were you thinking?""")
    else:
        chicago()

def meetingAngell():
    print("\n\n------------------------------ Meeting Angell ---------------------------------------\n")
    print("""    Someone once said, \"Life is a daring adventure, or nothing at all.\" \"In for a penny
    in for a pound.\" You're doing this. You're going to solve the mystery, get rich, and 
    maybe go back and see if Courney wants to go out some time. Hell YEAH! You're the... 
    person (this story is gender neutral).
    
    You pay the bill. Down your ice trea and float, yes float, out the door and into you 
    car. Wow! You feel good. It's like you just watched a Rocky movie, You're pumped. You 
    cannot be stopped.
    
    You start the car and tear off down the road a little too agressively. You giggle to 
    yourself and back off the gas alitte. You try and contain your excitement while you 
    continue on down the road. Your nav system keeps you on track and you hardly notice 
    where you're going.
    
    You round the last corner and reality slaps you in the face. This is not a nice place.
    Maybe you made a mistake. Maybe you should turn back. hell no. HELL NO!
    
    You kill your lights a few buildings before ariving at your destination. No reason not 
    to be a little cautious. You park a little bit away and get out. It's dark. Maybe you 
    should turn back. Heck no.
    
    You move quietly along the run down, abandoned, buildings. You can see the one you're
    supposed to meet Angell at. It's dark. Real dark. You hear something rustling at the 
    edge of an overgrown parking lot. Maybe you should turn back. Um, na... nah.
    
    You come up to the building and see most of the windows are broken and there's a big hole
    in the middle of one of the exterior walls. You can barely make out a tree growing
    inside the building. Maybe you really should turn back while you still can. Maybe.
    
    You press on and enter the building through the hole in the wall. You now can see a 
    light leaking out of a room towards the back. You move in that direction. You bump up 
    against something and grasp at it as it falls over. You cringe as the metal rack falls 
    over making, what seems, like the loadest sound ever. You swear you can hear things 
    scurrying in all directions, but as the clanging ringing in your ears fades, you're not 
    sure you heard anything, or will ever hear anything ever again.
    
    Suddenly, you feel something. Something unexplainable. You feel like you're going to 
    get physically ill. The air feels like wet seaweed again you skin, and you feel like you 
    have a fever. Your head starts to swim. You feel like your going to pass out. You kind 
    of hope that you do pass out to get this sensation to stop. You probably should...\n""")

    choice = input(">Run, [run] for your fucking life, or [push] through: ")
    if choice == "run":
        run()
    elif choice == "push":
        pushThrough()
    else:
        indecisive()

def run():
    print("\n\n---------------------------- Run for your LIFE! -------------------------------------\n")
    print("""    You turn around 180 degrees and run. With your head spinning the way it is, you try and 
    run towards your car, but it feels like, no matter how hard you try, you can't run in 
    that direction. It feels like you're running on the side of a hill, and you lean to 
    compensate. You lean more and more as you run until you're on such an angle, to the 
    perfectly flat ground, that your shoes lose traction. You take a very hard fall. If 
    you think you were feeling bad before, you feel much worse now. You squirm a bit and 
    roll over. Ouch! You wallow in your misery a bit, but the pain of your spectacular
    wipeout is actually clearing your head a bit.
    
    You try to steady your breathing so you can hear what's going on around you. Nothing. 
    Nothing in pursuit. Nothing about to be on top of you. Just nothing. You start to 
    feel a little silly. But, that awful feeling. What was that? It needed to be run from.

    You start to sit up and notice you're surrounded by... what? WHAT!?! There's about 
    fifteen individuals in a circle around you. You gasp as you get a better look at them. 
    They're about six feet tall and look like fish people. You mind reels as you realize 
    these are... fish people. They move towards you in unison.

    The fish people reach out with human arms and webbed fingers. They pick you up, and 
    carry you back into the building. You don't really struggle, because it would be 
    pointless. You can feel their iron grip and you just know there is no escaping it. 
    Your struggle right now is with not losing your mind completely, and that's when 
    the terrible feeling comes back. You vomit.
    
    You vomit fountains of Chicago style pizza with every muscle in your body. 
    It comes out with such force that it shoots out your nose without slowing down in 
    the slightest. Your body heaves and your muscles contract. You spew iced tea and 
    pizza and what might be a lung... everywhere. It feels like your going to hurt yourself 
    with the force, but it finally subsides. 

    By the time you're done wiping your mouth, you're being deposited, not gently, on the 
    floor of the lighted room you noticed before you freaked the fuck out, got captured 
    by..., fuck, fish people, and almost vomited your feet out through your nose.
    
    The fish people fade, back, into the shadows and out of a shadow steps professor
    Angell.""")

    choice = input("\n>Run, try and [run] again, or [stand] up and face Angell:")
    if choice == "run":
        print("\n\n-------------------------------------------------------------------------------------\n\n")
        print("\nYou decide to run.\n")
        print("""    You get to your feet, pretend you're going to say something to the professor, and take 
    off running.

    This time your head is clear, and you dash back through the building towards the hole 
    in the wall. It's dark but you can see it's slightly brighter outside through the hole.
    You hear the squishy foot sounds of the fish people in pursuit. You turn to look, but 
    it's too dark. As you turn back, you run straight into something in the dark. Whatever 
    you hit lays you out flat, and you groan from the combination of pain and being dazed 
    from the impact.
    
    You start to rise as the first of the fish things is on you. You roll 
    to your left as it reaches out with it's iron grip, slips, loses its balance, and 
    crashes into thing you just ran into. Chicago style vonit! Other fish men slide and 
    smash into what must be a support pole. You start running again just as you hear a 
    load crack form the area of the pole, and the building begins to crumble around you.
    
    You make it outside and keep running as fast as you can as you hear, what sounds like, 
    the roof of the building caving in. You quickly check over your shoulder and you can't
    detect any pursuit. You are almost to the car and start to get the keys out. You fumble 
    them in your hand and drop them. As you stop to stoop and pick up the keys, you look 
    towards the building. Fish men are flooding out of the partially collapsed building. 
    You find the keys, your ass hits car seat, ingintion first try, and you peel off right
    pass the closest fish thing. In the head lights you make eye contact with the thing 
    and see, a rage and hatred that makes your blood run cold. As you power down the road 
    you try and shake the feeling of looking in those eyes.
    
    You drive straight home in silence. No radio. Nothing but the sound of the car on the 
    road. You pull up in your drive. Go in the house and lock the door. By now, the sun 
    is starting to rise. You turn on the TV, and plop down in the chair. You don't sleep.
    
    You spend the next few days and weeks waiting for them to come for you. You second 
    guess everything you did and every decision you made. After a while you stop living in 
    fear and return to a somewhat normal life. You never tell anyone about what happend 
    and you try not to think about it. Fuck you uncle Francis. What the fuck?\n""")
    
        end("You never sleep well anymore, and on most nights when you close your eyes, you see its eyes.")
    elif choice == "stand":
        print("\nYou stand up and turn toward Professor Angell.\n")
        print("""   You look into his eyes and they're diffrent from before. You realize that is what madness looks like. 
    He notices the enlightenment and your face, and his face snaps into a broad grin. "If 
    you only knew," he says and waves his hand towards you.\n""")
        end("""    The fish things errupt from the shadows and are on you before you can even bring your hands up to 
    defend yourself. You can feel them biting and ripping at your limbs. You screem. One 
    bites at your ear, but you're able to pull your head away and to the side. This brings 
    you face to face with one of them and it sinks its teeth into your cheek. Through the 
    pain and over the horrible sounds, you can hear someone laughing. Angell. You remain 
    consious for what seems like forever as the fish things continue to eat. Finnaly your 
    brain shuts down and you are gone.\n""")
    else:
        indecisive()
        
        
def indecisive():
    print("\n\n-------------------------------------------------------------------------------------\n\n")
    end("""Your mind has finally had enough. You do nohthing but collapse in a slobbering, sobbing, lump.
\n\nYou're never seen, or heard from, again.""")


def pushThrough():
    print("Man up!")

def philadelphia():
    print("\nCity of Brotherly Love!")








start()

print("Yippie!")
