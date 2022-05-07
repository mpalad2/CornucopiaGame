#War Room Scene
    #__________________________________________________________________________

    label startWarRoomScene:
        "TRANSITION TO WAR ROOM SCENE"
        "INT. WAR ROOM"
        
        play music "/audio/medieval_af.mp3" fadein 1.0
        scene war room

        #dialogue
        
        show a formal at left
        a "..."
        
        show d at right
        d "..."
        
        hide d
        show c at right
        c "..."
        
        mc "... {p}{i}God, this silence is killing me!{/i}"
        mc "Um -"
        
        hide c
        show b at right
        "SLAM!!"
        b "I apologize for my tardiness - I had to attend to a patient."
        
        show a formal ohface
        a "That’s quite alright - are they well?"
        show a formal
        
        b "They will survive the night."
        "[b]'s expression hardens."
        b "But I cannot say the same for the coming days."
        
        show a formal angry ohface
        a "We cannot keep continuing like this! We must act now!"
        show a formal angry
        
        hide b
        show d at right
        d "And what, charge at the enemies head on? We would sustain meaningless casualties and be none closer to our desired freedom."
        
        show a formal angry ohface
        a "So we should instead stand by and allow our brethren to suffer?!"
        a "My father chose to take a peaceful approach and look at where we ended up - "
        show a formal angry
        
        "[a] looks down and wraps her arms around herself, as if she were to fall apart into pieces at any moment."
        "[b] rushes over to his sister’s aid."
        
        show b
        b "[a]… "
        hide b
        
        d "…{p}I know…that it must be agonizing–that we seem to remain idle in the face of our enemies' cruelty."
        d "But to turn the tides against our enemies is no simple matter."
        d "Our already disadvantaged position amplifies each loss we are sure to have by striking head first whenever our rage sees fit."
        d "It could cause more bloodshed than if we were to bide our time."
        d "These decisions have never been easy ones to make, not for anyone who has held the position that you do."
        d "You’ve been shouldering the responsibility ever since your father’s passing -"
        
        "[a] grimaces."
        
        d "- but it is not your obligation to take this burden all upon yourself. {p}It never should be."
        d "[a]..."
        d "Let us help you."
        
        "[a] furls her eyebrows, deep in thought, before heaving a heavy sigh."
        
        show a formal ohface
        a "Perhaps you are right."
        "[a] casts a glance at you, and you immediately straighten to attention."
        a "What did you have in mind?"
        show a formal
        
        mc "Um, me as well! I would also like to help."
        
        d "As you know, I brought [player_name] here as a new ally."
        d "I had met them in the cornfield outskirts of the city, "
        d "and the knowledge they have about agriculture and this invention - they called it like a “smoke bomb”, they have could help turn the tide. "
        
        show a formal ohface
        a "And how do we know that we can trust this outlander?"
        show a formal
        
        d "Would they not have been thrown out the moment you saw them if you did not get a good impression from them already?"
        
        a "…"
        show a formal happy
        "[a] gives a light smile."
        a "You know me well."
        
        hide d
        hide a
        show a formal
        "[a] turns to look at you. You can’t help but feel like you’re beginning to sweat like a pig."
        show a formal ohface
        a "Care to explain this…smoke bomb of yours?"
        show a formal
        
        label WARmc_choice1:
        menu:
            "Sure thing!":
                jump WARa_reply1a
            "Yes, your majesty.":
                jump WARa_reply1a
            "Who’s to say…":
                jump WARa_reply1b
                
        label WARa_reply1a:
            mc "The main chemicals inside of it would be akin to a thing called a pesticide in my world. We use it all the time in our crops back at home."
            mc "It doesn’t affect the plants, but it knocks out the locusts. It’s fatal for the locusts at home, but here, it appears to intoxicate them for a brief period of time."
            jump WAR_dialogue1

        label WARa_reply1b:
            show a formal angry
            a "This is not the time for games."
            $ a_points -= 1
            jump WAR_dialogue2
            
        label WAR_dialogue1:
            show a formal ohface
            a "I see… Intriguing."
            show a formal
            $ a_points += 1
            jump WAR_continue1
            
        label WAR_dialogue2:
            "You bow your head."
            mc "I’m sorry."
            show a formal
            mc "Basically, the main chemicals inside of it would be akin to a thing called a pesticide in my world. We use it all the time in our crops back at home."
            mc "It doesn’t affect the plants, but it knocks out the locusts. It’s fatal for the locusts at home, but here, it appears to intoxicate them for a brief period of time."
            jump WAR_continue1
            
        label WAR_continue1:
            hide a
            show a formal at left
            show b at right
            b "You’ve got guts for someone that does not belong in this realm. Why are you helping us?"
            
            mc "I consider myself quite the green thumb at home."
            "Everyone looks at you, confused. {p}Guess they don’t know the term “green thumb”."
            mc "Ah, basically I’ve been taking care of plants for as long as I can remember. My family prides in it. I can’t in good conscience just leave this be without helping in some manner."
            mc "I’m not quite sure how much use I can be in the war…and I have never fought before. But if creating these smoke bombs as an advantage can be used to help, then… I will do my best."
            
            "[a] looks at you, eyes narrowed as if trying to assess you any further than the eye can see. You begin to fidget."
            
            show a formal ohface
            a "... {p}Very well."
            a "[d]."
            show a formal
            
            hide b
            show d at right
            d "Yes?"
            
            show a formal ohface
            a "Given your relationship with this outlander, I will grant this request."
            a "However, I trust you will also take responsibility for anything that may occur."
            show a formal
            
            d "But of course."
            
            show a formal ohface
            a "Now… {p} We have much to discuss."
            show a formal
            
            "The meeting continues into the night…"
            
            
        stop music fadeout 1.0
        scene transition
        jump startHCAscene
    #__________________________________________________________________________


    return
    