from sys import exit
def gold_room():
    print "This roomis full of gold,how much do you take?"

    next = raw_input(">")
    if "0" in next or "1" in next:
	how_much = int(next)
    else:
	dead("Man, learn to type a number.")

    if how_much < 50:
	print "Nice ,you are not greedy, you win!"
	exit(0)
    else:
	dead("you greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
	next = raw_input("> ")

	if next == "take honey":
	    dead("the bear looks at you then slaps your face")
	elif next == "taunt bear" and not bear_moved:
	    print "The bear has moved from the door ,you can go through now"
	    bear_moved = True
	elif next == "taunt bear" and bear_moved:
	    dead("the bear gets pissed off and chews your leg off")
	elif next == "open door" and bear_moved:
	    gold_room()
	else:
	    print "I got no idea what means."
	
def cthulhu_hoom():
    print "Here you see the great evil cthulhu."
    print "He, it, whatever stars at you and you go insane"
    print "Do you flee for your life or eat your head?"

    next = raw_input(">")
    if "flee" in next:
	start()
    elif "head" in next:
	dead("well that was tasty!")
    else:
	cthulhu_room()

def dead(why):
    print why,"good job"
    exit(0)

def start():
    print "you are in a dark room."
    print "There is a door to your right and left."
    print "which one do you take?"

    next = raw_input(">")
    if next == "left":
	bear_room()
    elif next == "right":
	cthulhu_room()
    else:
	dead("you stumble around the room until you starve.")

start()
