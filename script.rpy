# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = DynamicCharacter("player_name")

define a = Character("Viera")
define b = Character("Varian")

define c = Character("Sweet")

define d = DynamicCharacter("corn_name")


# define text shouts and whispers

define mc_shout = DynamicCharacter("player_name",what_size = 34)
define mc_whisper = DynamicCharacter("player_name",what_size = 18)

define a_shout = Character("Viera",what_size = 34)
define a_whisper = Character("Viera",what_size = 18)

define b_shout = Character("Varian",what_size = 34)
define b_whisper = Character("Varian",what_size = 18)

define c_shout = Character("Sweet",what_size = 34)
define c_whisper = Character("Sweet",what_size = 18)

define d_shout = Character("Dent",what_size = 34)
define d_whisper = Character("Dent",what_size = 18)

# The game starts here.

label start:

    #affection variables
    $ a_points = 0

    # branching path variables
    $ HCA_pathA = False
    $ HCA_pathA_choseB = False
    
    #set dent corn to default name
    $ corn_name = "???"

    #Prologue Scene
    #__________________________________________________________________________
    
    play music "/audio/babysong.mp3" fadein 1.0
    scene cornbgnight
    "EXT. Buford Corn Maze, Buford GA, 9 PM"
    
    #player input
    
    show mc 
    
    $ player_name="???"
    
    mc_shout "UGHHH!!!" with vpunch
    mc "I'm losing my mind out here. Next thing you know, I won't even remember my name!"
    $ player_name = renpy.input("What was my name again?")
    
    if player_name == "":
        $ player_name="Alex"
        
    mc "AH! {p}[player_name!u], IT'S [player_name!u]!"
    mc "Well, at least I knew it off the top of my head. {p}Somewhat."
    
    hide mc
    
    #prologue official start
    "It’s dark outside, the only lumination present being the light that comes from the moon in the night sky." 
    "You are in the middle of a corn maze, no perceivable end in sight, and the gloom of night time casts a blue light on your surroundings. "
    "There’s a dark path ahead of you, surrounded by repeating corn stalk silhouettes."
    
    label PROmc_choice1:
        menu:
            "Try to find your way out":
                jump PRO_r1a
            "Yell out for help":
                jump PRO_r1b
            "Check your phone":
                jump PRO_r1c
                
    label PRO_r1a:
        "You can’t see your way ahead–that’s just courting danger. "
        "If you already got yourself this lost when it was light out, trying when there’s no light probably isn’t the best idea…"
        "Damn, why don’t they have lamps lit out here?"
        jump PROmc_choice1

    label PRO_r1b:
        "You yell to know if anyone’s nearby. "
        "There’s no response, even when you yell your loudest. "
        "Damn, you know you shouldn’t have split up with your friends earlier, you’ve always had a terrible sense of direction. "
        "Welp, anything’s better than being a third wheel."
        jump PROmc_choice1

    label PRO_r1c:
        "You check your phone, your battery is at 5\%. "
        "Gosh, if only you hadn’t lent your portable charger to your friend earlier. "
        "Maybe you shouldn’t have drained your battery playing G*nshin Imp*ct when you got bored…"
        jump PRO_nar1
        
    label PRO_nar1:
        "The time says 9PM, only an hour before the corn maze closes, but you don’t see any employees nearby"
        "–in fact you hadn’t seen any for quite a while. {p}Maybe they’ll start searching for you right about now? "
        "So the best thing would be to wait, right? {p}But… you’ve never been good at that."
        jump PROmc_choice2
    
    label PROmc_choice2:
        menu:
            "Stay still and wait":
                jump PRO_r2a
            "Use your flashlight to try and find your way through":
                jump PRO_r2b
            "Try to call for help":
                jump PRO_r2c
                
    label PRO_r2a:
        "You don’t move a muscle. "
        "Your bad sense of direction got you here, if you move any further you may end up somewhere completely unexpected. "
        "The corn stalks sway menacingly just beyond you, and your legs start to tremble. "
        "You have been walking around for hours, and you're getting pretty tired…"
        jump PRO_r2aEXTEND
    
    label PRO_r2aEXTEND:
        "And it has been hours, hasn’t it? Why did you even agree to go to this stupid maze! "
        "Your stomach grumbles in sorrow, yearning for the pack of snacks you accidentally left back at the start of the maze. "
        "Too bad none of the corn around you is edible–one of the employees made sure to let you and your friends know that." 
        "But a bit of forbidden corn could be a nice treat… maybe? No, your already weak stomach probably wouldn’t like that."

        "You succumb to your weak and tired legs, moving to sit down on the ground. "
        "At least the dirt is nice and soft, feeling like memory foam after so many hours of walking through tall grass and corn stalks." 
        "Actually, sitting down may feel nice but–yawn–laying down might feel even better~ And you deserve a nap! "
        "As a reward for all the steps you’ve recorded in your Health app today! Heck, you probably set a new record! "
        "If anyone finds you they can carry you out. You’re gonna get some well deserved shut-eye!"
        "As you closed your eyes to sleep, you felt a slow breeze pick up around you–nothing too turbulent, "
        "but strange given the fact that you’re surrounded by miles of corn. You don’t notice this though as you slowly close your eyes… "
        "drifting off until…"
        "THUD!!"
        jump PRO_transition1

    label PRO_r2b:
        "Even though your phone’s about to die, you reason you can ration your battery if you just use the flashlight and nothing else. "
        "But which direction should you go?"
        jump PRO_r2bEXTEND
    
    label PRO_r2bEXTEND:
        "The moment your brain cells so much as twitch to choose a direction, your flashlight abruptly turns off. "
        "Thinking you may have accidentally tapped the screen to turn it off, you look down at your phone and see… black. "
        "Did it lock itself?"

        "You press the power button and see that the battery has run out…{p}tough luck."

        "You slump down onto the ground, disgruntled, and put your phone away. Guess all you can do is sit down and wait for help. "
        "And with how tired you are, you’re quick to start dozing off…"
        "THUD!!"
        jump PRO_transition1

    label PRO_r2c:
        "You tap on the screen to call one of your friends but… damn, there’s no service in here! "
        "But you were just playing a game on it earlier…"
        jump PROmc_choice2
    
    # transition to new world
    
    label PRO_transition1:
        scene cornbgday
        "EXT. ??? Corn Maze, ???, Daytime (?)"
        d "Hello...?"
        "RUSTLE"
        show d
        d "You... {p}down there..."
        mc "ZZZ..."
        d "… So you’re asleep… {p}at least you’re not dead."
        "!! {p}Dead?"
        mc "...bwuh?"
        
        "You open up your eyes finally, and immediately want to close them again once the summer sun shines into your face. "
        "You take a quick, bleary glance around to see that you’re.. Still in the corn maze? "
        "But wait, for some reason it feels different…"
        
        "Your train of thought ends once you notice the sun is no longer beaming down on your face, and when you look up you see a person instead. "
        "They look rather… solemn. And their quilted cape coat whatever definitely is NOT weather appropriate." 
        "You notice that they are looking straight at you and have been offering their hand this entire time… awkward.."

        jump PROmc_choice3
        
    label PROmc_choice3:
        menu:
            "Take their hand":
                jump PRO_r3a
            "Stand up on your own":
                jump PRO_r3b
            "Stare at them":
                jump PRO_r3c
    
    label PRO_r3a:
        "You take their hand gratefully, and they pull you up with no effort at all. Woah. "
        "In your astonishment you forget to let go of their hand once you’re steady on your feet. "
        "They don’t seem to mind, but their eyebrows pinch questioningly when they take a closer look at you."

        jump PRO_continue1
        
    label PRO_r3b:
        "You move to stand up, but the moment you try to get on your feet, you stumble and flail about, "
        "about to return from whence you came. Luckily, you don’t fall flat on your ass as the person in front "
        "of you steadies you rather quickly. Nice reflexes."

        jump PRO_continue1
        
    label PRO_r3c:
        "You stare at them. They stare back at you. You notice that they only have one eye visible, the other covered by a dark red eyepatch. "
        "That’s… pretty cool honestly. As you do not move to get up, the stranger instead sits down next to you."
        jump PRO_continue1
    
    label PRO_continue1:
        d "You don’t look like you’re from around here…"
        "The stranger says softly with a gentle, inquisitive look. "
        "Their voice sounds warm and strong, and their demeanor is sedate as they take your appearance in."
        
        "NOT from around here??? "
        "You live 15 minutes away from the maze, as you always have since you were born! What do they mean not from around here!"
        mc "What do you mean by that? {p}And who are you?"
        
        $ corn_name = "Dent"
        d "You… may call me Dent. "
        d "As for where… you are in one of the main royal corn fields, in the kingdom of Cornucopia."
        
        mc "… Cornucopia? {p}Like, as in corn?"
        
        "DENT huffs softly in what could possibly be a laugh. {p}You can’t really tell as their expression doesn’t change much."
        d "You really aren’t from here, are you… How curious…"
    
    stop music fadeout 1.0
    scene transition
    jump startWarRoomScene

    #__________________________________________________________________________

    