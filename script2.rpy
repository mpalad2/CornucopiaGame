    #Heirloom Corn A Scene
    #__________________________________________________________________________

    label startHCAscene:
        "TRANSITION TO HEIRLOOM CORN A SCENE"
        "INT. [a!u]’S ROOM"
        
        play music "/audio/gentle.mp3" fadein 1.0
        scene bg room

        show a

        #dialogue

        "[a] sits at the bed, tapping lightly on her knee as you get the ointment ready. She clears her throat."

        a "Wellll…"
        show a ohface
        a "that could have been worse."

    label HCAmc_choice1:
        menu:
            "ARE YOU STUPID ?? YOU COULD HAVE DIED.":
                jump HCAa_reply1a
            "How are you feeling?":
                jump HCAa_reply1b
            "Uh huh.":
                jump HCAa_reply1c

    label HCAa_reply1a:
        show a happy
        a "Ah, but I didn’t. {p}…"
        show a
        a "But I apologize, I will be more careful in the future. "
        $ a_points += 2
        jump HCA_dialogue1

    label HCAa_reply1b:
        a "It stings a bit, but it's quite alright."
        $ a_points += 1
        jump HCA_dialogue1

    label HCAa_reply1c:
        a "..."
        $ a_points -= 1
        jump HCA_dialogue1

    label HCA_dialogue1:
        show a ohface
        a "Stir the ointment a little."
        show a
        a "You just need to apply it to the wounds directly on my back."
        show a ohface
        a "One moment, I need to get this top off."
        show a
        mc "Alright, let me know when."
        "You turn away to give [a] some privacy."
        show a ohface
        a "Alright, I'm ready."
        show a
        "As you turn back around to face [a], she gives you a quick nod and begins to turn her back towards you to give you a better angle."
        mc "...!!"
        show a ohface
        a "Is something the matter?"
        show a
        "You look down at the tattoo design stretching across the top of [a]’s back."
        "Even at a glance, you can recognize the level of complexity within the tattoo consisting of only gray and black tones."

    label HCAmc_choice2:
        menu:
            "Your tattoo...":
                jump HCAa_reply2a
            "...":
                jump HCAa_reply2b

    label HCAa_reply2a:
        show a ohface
        a "Ah? It’s a family crest…I had gotten it the day I took over as the family head. "
        jump HCAmc_choice3

    label HCAa_reply2b:
        a "Hmm...?"
        show a ohface
        a "Ah! {p}Is it perhaps about the tattoo? It’s a family crest…I had gotten it the day I took over as the family head."
        jump HCAmc_choice3

    label HCAmc_choice3:
        menu:
            "It's beautiful.":
                jump HCAa_reply3a
            "...":
                jump HCAa_reply3b
            "Okay.":
                jump HCAa_reply3c

    label HCAa_reply3a:
        show a happy
        a "Thank you..."
        $ a_points += 1
        jump HCAmc_choice4

    label HCAa_reply3b:
        show a
        a "..."
        jump HCAmc_choice4

    label HCAa_reply3c:
        show a
        a "It's nothing big."
        jump HCAmc_choice4

    label HCAmc_choice4:
        show a
        "You begin to apply the ointment. [a] squirms at the slight sting but jumps a bit at it being applied to a particularly tender wound."
        menu:
            "Ah! I'm sorry!":
                jump HCAa_reply4a
            "You okay?":
                jump HCAa_reply4b
            "Your majesty is a little sensitive, huh?":
                jump HCAa_reply4c
            "...":
                jump HCAa_reply4d

    label HCAa_reply4a:
        show a ohface
        a "It's fine."
        $ a_points += 1
        jump HCAmc_choice5

    label HCAa_reply4b:
        show a happy
        a "It's alright, don't worry. Like I said, it could be worse."
        $ a_points += 1
        jump HCAmc_choice5

    label HCAa_reply4c:
        show a happy
        a "Hmph perhaps."
        $ a_points += 1
        jump HCAmc_choice5

    label HCAa_reply4d:
        a "..."
        jump HCAmc_choice5

    label HCAmc_choice5:
        show a
        menu:
            "You take your hands away and move to close the ointment jar.":
                jump HCAa_reply5a
            "You look a bit closer at the tattoo.":
                "You hadn’t had the time to look at it earlier, but it really is quite an intricate and unique design."
                mc "{i}It’s made up of all things corn…how cute… {p}corn flowers and corn husks beautifully drawn to the finest detail…surrounding the finest piece of all…{p}the corn snake…{/i}"
                "Without a second thought, you trace part of the tail end of the snake."

                jump HCAa_reply5b

    label HCAa_reply5a:
        show a ohface
        a "Is it done? Thank you."
        jump HCA_branchingPoint

    label HCAa_reply5b:
        show a blush
        a_shout "-?!!"
        "[a] stiffens under [player_name!c]’s touch."
        show a ohface blush
        a "What was that for?"
        $ a_points += 1
        jump HCA_special_1

    label HCA_special_1:
        show a blush
        menu:
            "You glance over at what little you can see of [a]’s expression.":
                "It’s not much, but you can see the tips of [a]’s ears burning red. You can’t help but smirk at the reaction."
                mc "{i}How cute.{/i}"
                "Without a second thought, you wordlessly repeat the motion."
                jump HCA_SPreply1_a
            "Nothing.":
                jump HCA_SPreply1_b

    label HCA_SPreply1_a:
        "[a] makes a visible shiver."
        show a ohface blush
        a_shout "[player_name!c], HONESTLY WHAT -"
        $ a_points += 1
        jump HCA_branchingPoint

    label HCA_SPreply1_b:
        show a ohface
        "[a] looks over to stare at you, mouth open to reply. But she falters and seems to contemplate for a moment, before clearing her throat."
        a "Well -"
        jump HCA_branchingPoint

    label HCA_branchingPoint:
        if (a_points >= 5):
            jump HCA_patha
        else:
            jump HCA_pathb

    label HCA_patha:
        show a blush
        $ HCA_pathA = True
        "The air is stiff between them. [a] seems lost in thought, before -"
        "THUD!!!" with vpunch
        show a ohface blush
        a "[player_name!c]..."
        show a blush
        "You suddenly find your view to be completely different from the moment before,"
        "your back against the bed as [a] hovers above you just a few inches away."
        mc "Ah - ?"
        show a ohface blush
        a "Is this..."
        show a happy blush
        a "okay?"
        menu:
           "Yes...":
               jump HCA_PAreplya
           "NO -":
               show a
               "[a]’s expression immediately falls and she moves to give you some space."
               mc "UM WAIT - {p} I don’t mean that I’m not interested, but I just…"
               "Your voice trails off, unsure how to explain."
               jump HCA_PAreplyb
           "What are you doing ??":
               jump HCA_PAreplyc

    label HCA_PAreplya:
        show a happy blush
        a "Consider this a token of gratitude..."
        $ a_points += 1
        jump HCA_CGA

    label HCA_PAreplyb:
        show a happy blush
        "[a] softens her expression, a gentle smile on her face."
        a "It’s alright, no need to rush anything."
        $ a_points += 1
        $ HCA_pathA_choseB = True
        jump HCA_pathb

    label HCA_PAreplyc:
        show a
        a "I um - sorry -"
        "[a] stumbles back and looks away."
        a "I apologize. I misunderstood."
        jump HCA_pathb

    label HCA_CGA:
        "[a] raises her hand and cups your cheek."
        "The expression on her face is soft yet determined, {p}and her hand is warm and ever so slightly shaking. "
        "She seems nervous. "
        "Nevertheless, she dips her head closer,"
        "and you close your eyes as she takes the final step."
        $ a_points += 5
        jump temp_stop

    label HCA_pathb:
        "[a] takes a deep breath in, before getting up from the bed and motioning you to follow."
        show a ohface
        a "…thank you again for your help. Really."
        show a
        mc "It’s no trouble."
        if HCA_pathA and HCA_pathA_choseB:
            a "[a] seems to fidget nervously for a second, before quietly making a gesture towards your hand."
            show a ohface
            a "May I?"
            show a
            menu:
                "No way.":
                    jump HCA_PBreplya
                "You may...":
                    jump HCA_PBreplyb
                "Heh, so your majesty is bold enough to try to kiss me, but my hands are too much?":
                    jump HCA_PBreplyc
        else:
            jump HCA_CGB

    label HCA_PBreplya:
        a "..."
        jump HCA_CGB

    label HCA_PBreplyb:
        "[a] softens at [player_name!c]’s response and gently takes [player_name!c]’s hand in hers, "
        "closing her eyes as if to process the moment."
        $ a_points += 2
        jump HCA_CGB

    label HCA_PBreplyc:
        "[a] is silent for a moment before giving an energetic chuckle."
        show a happy
        a "It is a little backwards, is it?"
        "[a] softens at [player_name!c]’s response and gently takes [player_name!c]’s hand in hers, "
        "closing her eyes as if to process the moment."
        $ a_points += 1
        jump HCA_CGB

    label HCA_CGB:
        show a
        show a ohface
        a "I will see you tomorrow."
        show a
        mc "Good night, [a]."
        if HCA_pathA and HCA_pathA_choseB:
            show a happy
            a "Good night and sweet dreams, [player_name!c]."
            $ a_points += 5
            jump temp_stop
        else:
            show a ohface
            a "Good night. Get some rest."
            jump temp_stop

    label temp_stop:
        stop music fadeout 1.0
        scene transition
        "This marks the end of the demo! Thank you for play testing!"
        
    # This ends the game.
    #__________________________________________________________________________


    return


    