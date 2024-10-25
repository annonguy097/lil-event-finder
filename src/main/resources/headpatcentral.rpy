label amiheadpat:
    $ sessionpats = 0
    scene amiheadpathub
    with fade

    a "Sensei? What are you doing?"

    menu amipatmenu1:
        "Pat your [niece]":
            jump amipatstart
        "Don't pat your [niece]":
            "What should I do instead?"
            jump amiinvmenu

label amipatstart:
    scene amipat1
    with dissolve
    $ sessionpats += 5
    $ amipats += 5

    a "Hm?"

    menu amipatmenu2:
        "Pat":
            jump amipatting
        "Quit patting":
            "What should I do instead?"
            jump amiinvmenu

label amipatting:
    if sessionpats < 5:
        scene amipat2 with dissolvepat
        scene amipat1 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 5:
        a "[amimaster]...I like this, but...how long are you planning on doing it for?"
        scene amipat2 with dissolvepat
        scene amipat3 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene amipat4 with dissolvepat
        scene amipat3 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 15:
        scene amipat5 with dissolve
        a "We should do this more often. A few hundred more and I might believe you actually love me."
        scene amipat6 with dissolvepat
        scene amipat5 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene amipat6 with dissolvepat
        scene amipat5 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 25:
        scene amipat6 with dissolvepat
        scene amipat7 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Heheh~"
        a "When you told me you wanted to spend some time in here, this wasn't exactly what I had in mind..."
        a "You should pat me lots more if you think I'm a good girl, [amimaster]."
        jump amipatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene amipat8 with dissolvepat
        scene amipat7 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 50:
        a "Umm...[amimaster]?"
        a "You don't have to keep going, you know."
        a "I'm fine with doing something else if you're getting bored."
        scene amipat8 with dissolvepat
        scene amipat7 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Or just...keep going. I guess that's fine too."
        jump amipatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene amipat6 with dissolvepat
        scene amipat5 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 75:
        scene amipat9 with dissolve
        a "This...kinda makes me feel like I'm a little girl again."
        a "You used to pat me like this a lot back then."
        a "Do you remember that?"
        a "I mean...I don't really think you ever did it...this many times at once, but..."
        a "Yeah."
        scene amipat10 with dissolvepat
        scene amipat9 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene amipat10 with dissolvepat
        scene amipat9 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 100:
        scene amipat12 with dissolvepat
        scene amipat11 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "[amimaster]..."
        a "I love you..."
        a "Is...now an appropriate time to say that?"
        a "You aren't going to...stop patting me now...are you?"
        jump amipatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene amipat12 with dissolvepat
        scene amipat11 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 150:
        scene amipat14 with dissolvepat
        scene amipat13 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Mmn..."
        a "[amimaster]..."
        a "You're not just...messing with me at this point...are you?"
        a "I think I might be...starting to feel a little...weird..."
        jump amipatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene amipat14 with dissolvepat
        scene amipat13 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 200:
        scene amipat15 with dissolve
        a "You know...[amimaster]..."
        a "I wouldn't mind...{i}doing something else{/i} if you know what I mean..."
        a "I'm getting a little...anxious.."
        scene amipat16 with dissolvepat
        scene amipat15 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Mm..."
        a "Meanie..."
        jump amipatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene amipat16 with dissolvepat
        scene amipat15 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 250:
        scene amipat17 with dissolve
        a "Hah...mnh..."
        a "Is it...getting a little hot in here or...is that just me?"
        scene amipat18 with dissolvepat
        scene amipat17 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene amipat18 with dissolvepat
        scene amipat17 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 300:
        scene amipat18 with dissolvepat
        scene amipat17 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        scene amipat19 with dissolve
        a "[amimaster]..."
        a "Are you really sure you want to...keep doing this instead of...something else?"
        a "You're not gonna...make me come out and say it...are you?"
        jump amipatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene amipat20 with dissolvepat
        scene amipat19 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 350:
        scene amipat21 with dissolve
        a "Hah...hah...hah..."
        "Ami presses her legs together and begins to squirm in her seat."
        scene amipat22 with dissolvepat
        scene amipat21 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "More..."
        a "[amimaster]..."
        a "Pat me...more..."
        jump amipatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene amipat20 with dissolvepat
        scene amipat19 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 400:
        scene amipat23 with dissolve
        a "Ngh...[amimaster]..."
        a "How did I get like this from just...my head being rubbed?..."
        a "Maybe we should stop...before I..."
        scene amipat24 with dissolvepat
        scene amipat23 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Ugh...you don't listen at all..."
        jump amipatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene amipat26 with dissolvepat
        scene amipat25 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 450:
        a "[amimaster]...please..."
        a "Any more and I'll..."
        scene amipat26 with dissolvepat
        scene amipat25 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene amipat26 with dissolvepat
        scene amipat25 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 475:
        scene amipat27 with dissolve
        a "Ngh...hah...[amimaster]..."
        a "I'm...sorry..."
        a "I know how it must...look to..."
        a "See your...little girl getting all wound up from...just her head being rubbed..."
        a "But...I've been saying this whole time..."
        a "I'm...happy to-"
        scene amipat28 with dissolvepat
        scene amipat27 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        a "Oh god..."
        a "You're not even going to...let me breathe...are you?"
        jump amipatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene amipat28 with dissolvepat
        scene amipat27 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        jump amipatmenu2
    if sessionpats == 500:
        scene amipat29 with dissolve
        a "Ahh~ Oh...my god..."
        a "[amimaster]...I can't..."
        a "I can't do it anymore..."
        a "I'm..."
        a "Ngh..."
        scene amipat30 with dissolvepat
        scene amipat29 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        scene amipat30 with dissolvepat
        scene amipat29 with dissolvepat
        $ sessionpats += 5
        $ amipats += 5
        scene amipat31 with hpunch
        $ sessionpats += 5
        $ amipats += 5
        a "NGH!!!!~~~~~~~"
        a "[amimaster]...[amimaster]...ngh..."

        "Ami's squirming grows more aggressive than ever."
        "Her legs tremble and she nearly loses her balance."
        "The only thing stabilizing her is my hand upon her head."

        a "Mmngh...mmn...oh my...god..."
        a "I can't believe...I just..."

        scene amipat32 with dissolve

        a "You...made me cum..."
        a "But...why?"
        a "Is this...a new fetish of yours?"

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ amipatgasm = True

        "I patted Ami's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label ayaneheadpat:
    $ sessionpats = 0
    scene ayaneheadpathub
    with fade

    ay "Hm? Why are you just looking at me like that?"
    ay "Am I extra cute today or something?"

    menu ayanepatmenu1:
        "Pat":
            jump ayanepatstart
        "Don't pat":
            "What should I do instead?"
            jump ayaneinvmenu

label ayanepatstart:
    scene ayanepat1
    with dissolve
    $ sessionpats += 5
    $ ayanepats += 5

    ay "Ah! Headpats!"
    ay "I've waited my whole life for this!"
    ay "Pat away, [ayanemaster]! Pat me to your heart's content!"

    menu ayanepatmenu2:
        "Pat":
            jump ayanepatting
        "Quit patting":
            "What should I do instead?"
            jump ayaneinvmenu

label ayanepatting:
    if sessionpats < 5:
        scene ayanepat2 with dissolvepat
        scene ayanepat1 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 5:
        scene ayanepat2 with dissolvepat
        scene ayanepat3 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Heheh~ You can pat me a little harder, [ayanemaster]."
        ay "Go on. Really mess my hair up. Make it look like we had sex."
        scene ayanepat4 with dissolvepat
        scene ayanepat3 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Or just keep doing it that way. That's fine too."
        jump ayanepatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene ayanepat4 with dissolvepat
        scene ayanepat3 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 15:
        scene ayanepat5 with dissolve
        ay "So...am I gonna get to headpat you after this?"
        ay "Or is this just a one-way thing?"
        ay "Either way. Please continue. I can already feel myself melting."
        scene ayanepat6 with dissolvepat
        scene ayanepat5 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene ayanepat6 with dissolvepat
        scene ayanepat5 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 25:
        scene ayanepat8 with dissolvepat
        scene ayanepat7 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Ahh...sheer bliss."
        ay "I'm not dreaming, am I?"
        ay "[ayanemaster]...slap me across the face. I need proof that I'm not dreaming."
        ay "Also, who knows? Maybe I'd be into it?"
        jump ayanepatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene ayanepat8 with dissolvepat
        scene ayanepat7 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 50:
        scene ayanepat8 with dissolvepat
        scene ayanepat7 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "It's...normal to get a little turned on when stuff like this is happening, right?"
        ay "Like...you're not just gonna keep patting me forever, are you? This has to be going somewhere."
        jump ayanepatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene ayanepat6 with dissolvepat
        scene ayanepat5 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 75:
        scene ayanepat9 with dissolve
        ay "You picked a weird time to be all silent, [ayanemaster]..."
        ay "I'm starting to think you actually {i}do{/i} just want to pat my head and not...you know."
        ay "Do sexy stuff with me and...stuff."
        scene ayanepat10 with dissolvepat
        scene ayanepat9 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene ayanepat10 with dissolvepat
        scene ayanepat9 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 100:
        scene ayanepat12 with dissolvepat
        scene ayanepat11 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "[ayanemaster]..."
        ay "I'm having a lot of fun..."
        ay "Even if all you're doing is just rubbing my head."
        ay "I kind of wish we could freeze this moment and just do it over and over and over again."
        ay "You know?"
        jump ayanepatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene ayanepat12 with dissolvepat
        scene ayanepat11 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 150:
        scene ayanepat14 with dissolvepat
        scene ayanepat13 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Mm...[ayanemaster]..."
        ay "I'm gonna...close my eyes for a little bit..."
        ay "I don't know if I'm just feeling tired or if it's getting...really warm in here..."
        ay "But I'm suddenly having trouble keeping my eyes open..."
        ay "I hope no one takes advantage of me~"
        jump ayanepatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene ayanepat14 with dissolvepat
        scene ayanepat13 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 200:
        scene ayanepat15 with dissolve
        ay "Though...if you {i}did{/i} want to take advantage of me...you definitely could."
        ay "I'm starting to feel a little frisky anyway..."
        ay "You should really let me {i}pat{/i} you after this, if you get what I'm talking about."
        scene ayanepat16 with dissolvepat
        scene ayanepat15 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Penis."
        ay "I was talking about your penis."
        ay "Just to make sure you got that."
        jump ayanepatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene ayanepat16 with dissolvepat
        scene ayanepat15 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 250:
        scene ayanepat17 with dissolve
        ay "Are you...really sure there's nothing I could be doing for you, right now?"
        ay "I love this, but...don't you want a little more?"
        scene ayanepat18 with dissolvepat
        scene ayanepat17 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene ayanepat18 with dissolvepat
        scene ayanepat17 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 300:
        scene ayanepat18 with dissolvepat
        scene ayanepat17 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        scene ayanepat19 with dissolve
        ay "Hah...ahh..."
        ay "[ayanemaster]..."
        ay "Aren't you...going a little harder all of a sudden?..."
        ay "I didn't think my head was an...erogenous zone but...I'm starting to think...it might be..."
        ay "I'm getting...really horny..."
        jump ayanepatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene ayanepat20 with dissolvepat
        scene ayanepat19 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 350:
        scene ayanepat21 with dissolve
        ay "Ngh~"
        ay "I'm sorry, [ayanemaster]...but I...can't hold back anymore..."
        scene ayanepat22 with dissolvepat
        scene ayanepat21 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        "Ayane spreads her knees apart slightly and one of her hands finds its way into her lap."
        "She begins to rub herself through her skirt while groping herself with her other hand."
        ay "You can...watch if you want..."
        ay "If you're...not too distracted by...patting, I mean..."
        jump ayanepatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene ayanepat22 with dissolvepat
        scene ayanepat21 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 400:
        scene ayanepat23 with dissolve
        ay "Ahh~ Hah...[ayanemaster]..."
        ay "I love you...I love you...so much..."
        ay "I'm so...wet right now...and all you're doing is..."
        scene ayanepat24 with dissolvepat
        scene ayanepat23 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Hah...hah...I...can't even focus..."
        jump ayanepatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene ayanepat26 with dissolvepat
        scene ayanepat25 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 450:
        ay "Oh...fuck..."
        ay "[ayanemaster]...[ayanemaster]..."
        "Ayane slides her skirt up with trembling fingers and begins to massage herself through her underwear."
        ay "Can you just...finish me off...please?..."
        scene ayanepat26 with dissolvepat
        scene ayanepat25 with dissolvepat
        ay "I...hah...didn't mean through...patting..."
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene ayanepat26 with dissolvepat
        scene ayanepat25 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 475:
        scene ayanepat27 with dissolve
        ay "I'm...going to cum...[ayanemaster]..."
        ay "Pat me harder...faster..."
        scene ayanepat28 with dissolvepat
        scene ayanepat27 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        ay "Y-Yeah...like that..."
        ay "Just...maybe a little lower..."
        ay "Like...between my legs or something..."
        ay "Just a...hah...recommendation..."
        jump ayanepatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene ayanepat28 with dissolvepat
        scene ayanepat27 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        jump ayanepatmenu2
    if sessionpats == 500:
        scene ayanepat29 with dissolve
        ay "Ahh!...Hah~"
        ay "Fuck..."
        ay "[ayanemaster]..."
        ay "You've seen me cum...so many times before but..."
        ay "This time feels...particularly...embarrassing..."
        ay "Hah...ngh...mngh..."
        scene ayanepat30 with dissolvepat
        scene ayanepat29 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        scene ayanepat30 with dissolvepat
        scene ayanepat29 with dissolvepat
        $ sessionpats += 5
        $ ayanepats += 5
        scene ayanepat31 with hpunch
        $ sessionpats += 5
        $ ayanepats += 5
        ay "MMMMMMMMNNNNNGHH!!!!!!~~~"

        "Ayane covers her mouth to prevent her voice from carrying as she forcefully drags her hips across my mattress and rides out a violent orgasm."

        ay "Mmm! Mmm! Mm...mmh...mmm..."

        "She carries on this way for a good twenty seconds or so, taking her time to catch her breath before opening her eyes."

        scene ayanepat32 with dissolve

        ay "Why?!"
        ay "Why would you make me do that myself when you know I'm willing to have sex with you whenever...{i}wherever{/i} you want?!"
        ay "That was just mean, [ayanemaster]!"

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ ayanepatgasm = True

        "I patted Ayane's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label saraheadpat:
    $ sessionpats = 0
    scene saraheadpathub
    with fade

    sar "..."
    sar "What are you doing?"
    sar "You've got this weird, menacing look on."
    sar "Are you planning something kinky?"

    menu sarapatmenu1:
        "Pat":
            jump sarapatstart
        "Don't pat":
            "What should I do instead?"
            jump sarainvmenu

label sarapatstart:
    scene sarapat1
    with dissolve
    $ sessionpats += 5
    $ sarapats += 5

    sar "..."
    sar "What's gotten into you?"
    sar "Am I being rewarded for something?"

    menu sarapatmenu2:
        "Pat":
            jump sarapatting
        "Quit patting":
            "What should I do instead?"
            jump sarainvmenu

label sarapatting:
    if sessionpats < 5:
        scene sarapat2 with dissolvepat
        scene sarapat1 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 5:
        scene sarapat4 with dissolvepat
        scene sarapat3 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "Well, whatever is going on, I love it."
        sar "I'm not sure what I did to deserve this, but I will gladly take all of the attention you want to give me, [saramaster]."
        scene sarapat4 with dissolvepat
        scene sarapat3 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene sarapat4 with dissolvepat
        scene sarapat3 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 15:
        scene sarapat5 with dissolve
        sar "I've gotta say, [saramaster]..."
        sar "You never struck me as the kind of guy to like things like this."
        sar "I always feel kind of needy around you and well..."
        sar "That's probably because I {i}am{/i} kind of needy."
        sar "So...I'm glad it...doesn't bother you."
        scene sarapat6 with dissolvepat
        scene sarapat5 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene sarapat6 with dissolvepat
        scene sarapat5 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 25:
        scene sarapat8 with dissolvepat
        scene sarapat7 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "Also, if you want me to suck your dick whenever you're done, just let me know."
        sar "That should be a fair trade, right?"
        jump sarapatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene sarapat8 with dissolvepat
        scene sarapat7 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 50:
        scene sarapat8 with dissolvepat
        scene sarapat7 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "You're awfully quiet today."
        sar "This isn't actually some kind of punishment, is it?"
        sar "Cause if it is, it's not a very good one."
        sar "I'm really happy right now. Each time you pat my head it's like I fall for you even harder."
        jump sarapatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene sarapat6 with dissolvepat
        scene sarapat5 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 75:
        scene sarapat9 with dissolve
        sar "Heheh..."
        sar "This makes me feel kind of [young]again."
        sar "Sana's father used to pat my head like this when we first started dating."
        sar "He wound up being a real jerk, though."
        scene sarapat10 with dissolvepat
        scene sarapat9 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "..."
        sar "I'm sorry for bringing something like that up."
        sar "I like you a lot, [saramaster]..."
        sar "Don't forget that, okay?"
        jump sarapatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene sarapat10 with dissolvepat
        scene sarapat9 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 100:
        scene sarapat12 with dissolvepat
        scene sarapat11 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "Hey...that's enough, isn't it?"
        sar "You've been patting my head for a while now."
        sar "There are plenty of other pat-worthy parts of me, you know?"
        scene sarapat12 with dissolvepat
        scene sarapat11 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "No?"
        sar "Well...okay then, I guess..."
        jump sarapatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene sarapat12 with dissolvepat
        scene sarapat11 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 150:
        scene sarapat14 with dissolvepat
        scene sarapat13 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "[saramaster]...I wasn't joking about before."
        sar "If you want me to help you relieve a little stress, all you need to do is ask."
        sar "Just...having you stand there and...stare at me is...starting to get me a little excited."
        jump sarapatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene sarapat14 with dissolvepat
        scene sarapat13 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 200:
        scene sarapat15 with dissolve
        sar "Sorry...did I say a {i}little{/i} excited?"
        sar "What I meant to say is..."
        sar "I'm kind of...really horny all of a sudden."
        sar "You didn't drug me, did you?"
        sar "If you did, it's fine. I just want to know."
        scene sarapat16 with dissolvepat
        scene sarapat15 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "You're really just going to keep patting me even though I'm {i}super{/i} turned on, huh?"
        jump sarapatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene sarapat16 with dissolvepat
        scene sarapat15 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 250:
        scene sarapat17 with dissolve
        sar "Ngh~"
        sar "Just take it out already..."
        if sarasex == True:
            sar "I don't want to wait any longer, [saramaster]..."
        else:
            sar "You can only reject me for so long, you know?"
            sar "I'll get you eventually..."
        scene sarapat18 with dissolvepat
        scene sarapat17 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "Hah...hah..."
        sar "Wow..."
        sar "Who knew...headpats could...feel this good?..."
        jump sarapatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene sarapat18 with dissolvepat
        scene sarapat17 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 300:
        scene sarapat18 with dissolvepat
        scene sarapat17 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        scene sarapat19 with dissolve
        sar "Fine...you wanna play hardball?"
        sar "You're not going to break me, [saramaster]."
        sar "Moms are resilient. I can handle anything you throw at me."
        sar "If you think you're going to get me to orgasm just by patting my head, you've got another thing coming..."
        jump sarapatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene sarapat20 with dissolvepat
        scene sarapat19 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 350:
        scene sarapat21 with dissolve
        sar "Well...on second thought...what do I have to gain by holding myself back?"
        sar "If you're going to spend this much time on me and not let me return the favor...the least I can do is make it fun to watch, right?"
        scene sarapat22 with dissolvepat
        scene sarapat21 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        "Sara's fingers begin to dig into the skin of one of her thighs."
        "I watch her battle the urge to unbutton her shorts and start to pleasure herself."
        sar "God...only {i}you{/i} could get me to act up like this, [saramaster]..."
        sar "So unfair..."
        jump sarapatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene sarapat22 with dissolvepat
        scene sarapat21 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 400:
        scene sarapat23 with dissolve
        sar "Hah...hah...ahn..."
        scene sarapat24 with dissolvepat
        scene sarapat23 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "[saramaster]..."
        "Sara somehow manages to remain vigilant in not slipping her fingers into her shorts."
        "This means that I must continue patting her head."
        sar "So...wet..."
        sar "Can you just...finger me or something...please?"
        sar "I'm...desperate..."
        jump sarapatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene sarapat26 with dissolvepat
        scene sarapat25 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 450:
        sar "Your hand...is still...on my head..."
        sar "Why?"
        sar "This is punishment after all, isn't it?"
        sar "I've been nothing but kind to you...and yet you-"
        scene sarapat26 with dissolvepat
        scene sarapat25 with dissolvepat
        sar "And yet you won't even...help me out when I...need you most..."
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene sarapat26 with dissolvepat
        scene sarapat25 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 475:
        scene sarapat27 with dissolve
        sar "Harder...[saramaster]..."
        sar "I don't care if it...makes me look like a pervert..."
        sar "I'm gonna cum..."
        sar "So...keep going...just like that..."
        scene sarapat28 with dissolvepat
        scene sarapat27 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        sar "Hah...ngh..."
        sar "Fuck..."
        sar "Fuck...fuck...fuck..."
        "Sara's nails have dug so far into her thigh that I'm pretty sure she's drawn blood."
        "Her body shivers as I continue to stroke her hair."
        jump sarapatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene sarapat28 with dissolvepat
        scene sarapat27 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        jump sarapatmenu2
    if sessionpats == 500:
        scene sarapat29 with dissolve
        sar "Ngh~"
        sar "[saramaster]...yes..."
        sar "Don't stop...don't stop..."
        sar "I'm...really going to...hah..."
        scene sarapat30 with dissolvepat
        scene sarapat29 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        scene sarapat30 with dissolvepat
        scene sarapat29 with dissolvepat
        $ sessionpats += 5
        $ sarapats += 5
        scene sarapat31 with hpunch
        $ sessionpats += 5
        $ sarapats += 5
        sar "NGHHHHHH!!!!!!!~~~~~~"

        "Sara stays strong to the very end and manages to cum without even once touching herself."
        "Her hips {i}do{/i} rock back and forth on the bed, though, but I'm sure that pales in comparison to what she was {i}hoping{/i} to get out of me tonight."

        sar "Oh...my god..."
        sar "I...can't believe...I just did that..."

        scene sarapat32 with dissolve

        sar "I've been a bad girl, [saramaster]..."
        sar "I think I...might need you to...punish me again..."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ sarapatgasm = True

        "I patted Sara's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label makheadpat:
    $ sessionpats = 0
    scene makheadpathub
    with fade

    mak "What's wrong?"
    mak "Would you rather hang out somewhere else?"
    mak "I wouldn't mind going back to the dorm if that's where you'd rather be."

    menu makpatmenu1:
        "Pat":
            jump makpatstart
        "Don't pat":
            "What should I do instead?"
            jump makotoinvmenu

label makpatstart:
    scene makpat1
    with dissolve
    $ sessionpats += 5
    $ makpats += 5

    mak "Um..."
    mak "What?"
    mak "If this is another one of your mind games, [makotomaster], I swear to God..."

    menu makpatmenu2:
        "Pat":
            jump makpatting
        "Quit patting":
            "What should I do instead?"
            jump makotoinvmenu

label makpatting:
    if sessionpats < 5:
        scene makpat2 with dissolvepat
        scene makpat1 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 5:
        scene makpat4 with dissolvepat
        scene makpat3 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "I'm not really sure how you expect me to react in this situation, but..."
        mak "I'm kind of enjoying this, to be completely honest."
        scene makpat4 with dissolvepat
        scene makpat3 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "I {i}am{/i} a little curious about how long you plan to keep this up for, though."
        jump makpatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene makpat4 with dissolvepat
        scene makpat3 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 15:
        scene makpat5 with dissolve
        mak "Okay, really. What's going on here?"
        mak "You never give me unwarranted attention, let alone remain silent while doing so."
        mak "Are you trying to extort me for something?"
        mak "Isn't it enough that I already do all of your clerical work for you?"
        mak "Explain yourself, [makotomaster]."
        scene makpat6 with dissolvepat
        scene makpat5 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Ugh..."
        jump makpatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene makpat6 with dissolvepat
        scene makpat5 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 25:
        scene makpat8 with dissolvepat
        scene makpat7 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "I'd appreciate it if we could at least have a proper discussion so I don't have to sit here doing nothing for the next...however long you intend to do this for."
        mak "I swear, nothing you do even makes sense to me anymore."
        jump makpatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene makpat8 with dissolvepat
        scene makpat7 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 50:
        scene makpat8 with dissolvepat
        scene makpat7 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Okay. I hereby forbid this from going any further."
        mak "You've had your fun. Now leave me alone and stop teasing me."
        jump makpatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene makpat6 with dissolvepat
        scene makpat5 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 75:
        scene makpat9 with dissolve
        mak "[makotomaster]! How many times do I have to tell you to knock it off?!"
        mak "What are you trying to get out of me?! Just say it!"
        mak "There's no need to keep messing up my hair or...doing whatever it is you're trying to do!"
        scene makpat10 with dissolvepat
        scene makpat9 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Oh my fucking God."
        jump makpatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene makpat10 with dissolvepat
        scene makpat9 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 100:
        scene makpat12 with dissolvepat
        scene makpat11 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "I...guess it {i}is{/i} technically possible that there's no malicious intent behind this..."
        mak "But that doesn't explain why you're so adamantly refusing to speak with me."
        mak "Fine, though. You want to keep patting my head? Feel free. But you're not getting anything out of me."
        scene makpat12 with dissolvepat
        scene makpat11 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Nope. Not a single thing. Sorry, [makotomaster]."
        jump makpatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene makpat12 with dissolvepat
        scene makpat11 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 150:
        scene makpat14 with dissolvepat
        scene makpat13 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "..."
        mak "Can you at least turn the air conditioner on?"
        mak "It's ungodly hot in this room for some reason."
        mak "And no. It has absolutely nothing to do with how I'm feeling, as I'm sure you'd normally say when you're not being fucking weird."
        jump makpatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene makpat14 with dissolvepat
        scene makpat13 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 200:
        scene makpat15 with dissolve
        mak "Oh, come on! That's more than enough!"
        mak "I've counted 200 headpats so far!"
        mak "What possible reason could you have for patting someone's head for that long?!"
        scene makpat16 with dissolvepat
        scene makpat15 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "If you think this is going to unlock some sort of bonus-Makoto material, you're dead wrong!"
        mak "Unhand me, heathen!"
        jump makpatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene makpat16 with dissolvepat
        scene makpat15 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 250:
        scene makpat17 with dissolve
        mak "Mmn...[makotomaster]..."
        mak "Really...you should stop."
        mak "I know you like teasing me, but going this far is just absurd."
        scene makpat18 with dissolvepat
        scene makpat17 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Come on...how long can you possibly keep this up for?"
        mak "Can't you tell I'm...you know?"
        mak "Feeling...something?"
        jump makpatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene makpat18 with dissolvepat
        scene makpat17 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 300:
        scene makpat18 with dissolvepat
        scene makpat17 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        scene makpat19 with dissolve
        mak "Come on...this isn't funny anymore."
        mak "I mean, it was never funny to begin with. But now it's {i}really{/i} not funny."
        mak "I'm starting to get lightheaded. Maybe you could just...give me another shoulder massage or something?"
        mak "Doesn't that sound more fun than this?"
        jump makpatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene makpat20 with dissolvepat
        scene makpat19 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 350:
        scene makpat21 with dissolve
        mak "Okay...so the shoulder massage is clearly not something you're interested in."
        mak "But perhaps you'd maybe want to...Oh, I don't know..."
        scene makpat22 with dissolvepat
        scene makpat21 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Fuck me...or something?"
        mak "I'd be lying if I said I wasn't a {i}little{/i} turned on, so..."
        jump makpatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene makpat22 with dissolvepat
        scene makpat21 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 400:
        scene makpat23 with dissolve
        mak "Fine! I'm {i}very{/i} turned on!"
        mak "I have been since the 200th headpat!"
        mak "Are you happy now that you got me to admit it?!"
        mak "Good! Then-"
        scene makpat24 with dissolvepat
        scene makpat23 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Why are you still going?!"
        mak "Just fuck me already!"
        jump makpatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene makpat26 with dissolvepat
        scene makpat25 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 450:
        scene makpat28 with dissolvepat
        scene makpat27 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Okay...I'm literally begging you now. Please stop."
        mak "At this rate, I'm going to have an orgasm from my head being rubbed. You're treating me like a fucking dog."
        mak "And if I cum from something like this, you'll use it against me any chance you get."
        mak "You already hold my perversions over my head. More fuel for the fire is like a nightmare for me."
        scene makpat28 with dissolvepat
        scene makpat27 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "I hate you...so much..."
        jump makpatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene makpat28 with dissolvepat
        scene makpat27 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 475:
        scene makpat29 with dissolve
        mak "Hah...hah...hah..."
        mak "Please...no more..."
        mak "I can't..."
        mak "I can't take it..."
        scene makpat30 with dissolvepat
        scene makpat29 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        "Makoto unbuttons her pants and nervously slips her fingers into her panties."
        mak "At least...this way...I can deny...it was just from...the patting..."
        jump makpatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene makpat30 with dissolvepat
        scene makpat29 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        jump makpatmenu2
    if sessionpats == 500:
        scene makpat30 with dissolvepat
        scene makpat29 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        mak "Oh...fuck..."
        mak "Here it comes...[makotomaster]..."
        mak "This is your last chance...to..."
        scene makpat30 with dissolvepat
        scene makpat29 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        scene makpat30 with dissolvepat
        scene makpat29 with dissolvepat
        $ sessionpats += 5
        $ makpats += 5
        scene makpat31 with hpunch
        $ sessionpats += 5
        $ makpats += 5
        mak "AAAAAAAAAAAHHHHHHHHHHH!!!!!!!!!~~~~~~"

        "Makoto's wrist twitches rapidly as she fingers herself to completion in the middle of my headpatting ritual."
        "Here I was just trying to be wholesome and she had to go and do something like that."

        scene makpat32 with dissolve

        mak "You!"
        mak "Why did you make me do something like that?!"
        mak "Here I was just trying to be wholesome and you had to go and do something like that!"
        mak "Explain yourself!"

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ makotopatgasm = True

        "I patted Makoto's head for so long that the day came to an end before I realized it..."
        "I also don't think Makoto understands what it means to be {i}wholesome{/i} based on today's display."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label kirinheadpat:
    $ sessionpats = 0
    scene kirinheadpathub
    with fade

    ki "Uhh...can I help you with something?"
    ki "Not really normal for somebody to just get up and stand in front of whoever they're hanging out with."

    menu kirinpatmenu1:
        "Pat":
            jump kirinpatstart
        "Don't pat":
            "What should I do instead?"
            jump kirininvmenu

label kirinpatstart:
    scene kirinpat1
    with dissolve
    $ sessionpats += 5
    $ kirinpats += 5

    ki "And it's not really normal to just put your hand on their head, either..."

    menu kirinpatmenu2:
        "Pat":
            jump kirinpatting
        "Quit patting":
            "What should I do instead?"
            jump kirininvmenu

label kirinpatting:
    if sessionpats < 5:
        scene kirinpat2 with dissolvepat
        scene kirinpat1 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 5:
        scene kirinpat2 with dissolvepat
        scene kirinpat1 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Not gonna lie, I am incredibly uncomfortable right now."
        ki "Is this roleplay? Am I supposed to be doing something?"
        scene kirinpat4 with dissolvepat
        scene kirinpat3 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene kirinpat4 with dissolvepat
        scene kirinpat3 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 15:
        scene kirinpat5 with dissolve
        ki "I don't get it. Why are you doing this?"
        ki "Do you want to like, make out or something instead?"
        ki "This is really weird for me. I'm not exactly the type of person who's into cute stuff like this."
        scene kirinpat6 with dissolvepat
        scene kirinpat5 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "..."
        jump kirinpatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene kirinpat6 with dissolvepat
        scene kirinpat5 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 25:
        scene kirinpat8 with dissolvepat
        scene kirinpat7 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "I know it's your room so I'm not gonna like...step on your toes or anything."
        ki "But don't feel obligated to do things like this for me."
        ki "Just being with you is enough...as embarrassing as that is for me to say."
        jump kirinpatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene kirinpat8 with dissolvepat
        scene kirinpat7 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 50:
        scene kirinpat8 with dissolvepat
        scene kirinpat7 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "..."
        ki "So, do you like...do this with the other girls, too?"
        ki "I can't be the only person you...headpat or...whatever this is called."
        ki "I'm not good with affection. It makes me feel all...off inside."
        jump kirinpatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene kirinpat4 with dissolvepat
        scene kirinpat3 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 75:
        scene kirinpat9 with dissolve
        ki "Hey, is this {i}really{/i} how you want to spend our time together?"
        ki "We don't get to hang out that much and it feels like kind of a waste using it to just...rub my head."
        scene kirinpat10 with dissolvepat
        scene kirinpat9 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "...Really?"
        ki "I mean, I don't {i}hate{/i} it or anything, but like...why?"
        jump kirinpatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene kirinpat10 with dissolvepat
        scene kirinpat9 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 100:
        scene kirinpat12 with dissolvepat
        scene kirinpat11 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Mm..."
        ki "[kirinmaster]..."
        scene kirinpat12 with dissolvepat
        scene kirinpat11 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "..."
        ki "I guess it doesn't hurt to let things like this happen every once in a while."
        ki "Doesn't mean I don't still think it's weird, though."
        ki "Really weird."
        ki "Like...you're...weird. Or something."
        ki "I don't know. It's hard for me to think straight right now."
        jump kirinpatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene kirinpat12 with dissolvepat
        scene kirinpat11 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 150:
        scene kirinpat14 with dissolvepat
        scene kirinpat13 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "You know what's even weirder than your sudden obsession with patting my head?"
        ki "The fact that you haven't broken eye contact with me even once."
        ki "At least try to make a girl comfortable if you're going to put her into situations she's not used to."
        ki "So...yeah. Comfort me, [kirinmaster]."
        jump kirinpatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene kirinpat14 with dissolvepat
        scene kirinpat13 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 200:
        scene kirinpat15 with dissolve
        ki "Well...uh..."
        ki "I'm definitely starting to feel comfortable, but..."
        ki "Not really in the way I expected to."
        ki "This isn't some sort of...embarrassment fetish or something you've got going on, is it?"
        ki "Cause if you're getting turned on by running your fingers through my hair and..."
        ki "Watching me start to get all...hot and bothered..."
        scene kirinpat16 with dissolvepat
        scene kirinpat15 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "...Fuck."
        ki "Yeah. Definitely getting horny."
        jump kirinpatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene kirinpat16 with dissolvepat
        scene kirinpat15 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 250:
        scene kirinpat17 with dissolve
        ki "{i}Ugh...really, Kirin?{/i}"
        ki "{i}Getting wet from the slightest bit of attention?...{/i}"
        ki "{i}What's happening to you?...{/i}"
        scene kirinpat18 with dissolvepat
        scene kirinpat17 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Ngh..."
        ki "[kirinmaster]..."
        ki "If you're going to keep doing this, can you at least let me...sit on your lap or something?"
        ki "That sounds fun...doesn't it?"
        jump kirinpatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene kirinpat18 with dissolvepat
        scene kirinpat17 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 300:
        scene kirinpat18 with dissolvepat
        scene kirinpat17 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        scene kirinpat19 with dissolve
        ki "Heheh..."
        ki "You're having a grand old time, aren't you?"

        "Kirin stretches her legs forward and manages to wrap her feet around the backs of my knees, using her heels to pull me closer."

        ki "How hard are you right now, [kirinmaster]?"
        ki "This is all part of your plan, right?"
        ki "Rile me up with a little bit of attention so I'll let you cum all over my cute, little face..."
        ki "That's what you want, right?"

        "All I want is to pat heads."

        jump kirinpatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene kirinpat20 with dissolvepat
        scene kirinpat19 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 350:
        scene kirinpat21 with dissolve
        ki "Ngh...shit..."
        ki "I'm really starting to feel it now..."

        "The pressure of Kirin's heels digging into my legs loosens as she spreads her knees apart and begins to rub herself through her skirt."
        scene kirinpat22 with dissolvepat
        scene kirinpat21 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "I guess I don't mind masturbating in front of you if that's what you want from me..."
        ki "I just hope nobody else is home. I can get kind of loud when I cum."
        ki "And we don't want you getting in any trouble, now do we?"
        jump kirinpatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene kirinpat22 with dissolvepat
        scene kirinpat21 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 400:
        scene kirinpat23 with dissolve
        ki "Hah...hah...ngah..."
        ki "You sure you...don't want to...finish me off yourself, [kirinmaster]?..."
        ki "Where's the fun in a...weird fetish like this unless...you can end it the good, old-fashioned way..."
        ki "I'm all warmed up for you..."

        "Kirin reaches her hand out toward me and traces the outline of my cock with her index finger."

        if brony == True:
            "I shudder at the thought of how the sensation would feel if she were a pony and had hooves instead."

        scene kirinpat24 with dissolvepat
        scene kirinpat23 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Come on...[kirinmaster]..."
        ki "Let's have some fun in a...different way..."
        jump kirinpatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene kirinpat26 with dissolvepat
        scene kirinpat25 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 450:
        scene kirinpat26 with dissolvepat
        scene kirinpat25 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Fuck...[kirinmaster]..."
        ki "You're really...not going to help me out at all?..."
        ki "Whatever...that's okay, I guess..."
        ki "I guess...patting a cute girl's head until she...cums all over your bed {i}does{/i} sound kind of fun..."
        ki "But don't get mad at me if I...mess up your sheets..."
        ki "I think I may have already gotten them a little damp..."
        scene kirinpat28 with dissolvepat
        scene kirinpat27 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Ngh...fuck..."
        jump kirinpatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene kirinpat28 with dissolvepat
        scene kirinpat27 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 475:
        scene kirinpat29 with dissolve
        ki "I'm gonna cum, [kirinmaster]..."

        "I was so absorbed in patting her head that I didn't notice until now, but Kirin's entire skirt and panties have both been removed and are on the floor next to me."
        "I'm so impressed that I almost remove my hand from her head."

        scene kirinpat30 with dissolvepat
        scene kirinpat29 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "You like that, huh?"
        ki "Watching a desperate little girl finger her pussy while you pat her head?"
        ki "Do you want to cum, too, [kirinmaster]?"
        ki "Go on...take it out..."
        ki "Cum on me. It's okay."

        "Unfortunately for Kirin, I have a job that must be finished first."

        jump kirinpatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene kirinpat30 with dissolvepat
        scene kirinpat29 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        jump kirinpatmenu2
    if sessionpats == 500:
        scene kirinpat30 with dissolvepat
        scene kirinpat29 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        ki "Holy shit...maybe I...like being embarrassed like this?"
        ki "I'm close, [kirinmaster]..."
        ki "Really close..."
        ki "Just...pat me a few more times and..."
        scene kirinpat30 with dissolvepat
        scene kirinpat29 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        scene kirinpat30 with dissolvepat
        scene kirinpat29 with dissolvepat
        $ sessionpats += 5
        $ kirinpats += 5
        scene kirinpat31 with hpunch
        $ sessionpats += 5
        $ kirinpats += 5
        ki "AHHHH!!! HAH...AH...AHHHHHHHHH!!!~~~ FUCK!!!!"

        "Kirin stops fingering herself and clutches the sheet of the bed, using her other hand to grab onto my arm."
        "It prevents me from being able to pat her more, so I am slightly upset."

        ki "Fuck...fuck! Hah..."
        ki "Oh my god...oh my god...fuck..."

        scene kirinpat32 with dissolve

        ki "Hah...hah..."
        ki "Hi..."
        ki "That was...um..."
        ki "An interesting experience..."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ kirinpatgasm = True

        "I patted Kirin's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat
    ##############################################################################################################################################################################
label harukaheadpat:
    $ sessionpats = 0
    scene harukaheadpathub
    with fade

    h "Oh? What's going on here?"
    h "Should I stand, too? Like, I really have no idea what's happening right now."
    h "You look kind of intense."

    menu harukapatmenu1:
        "Pat":
            jump harukapatstart
        "Don't pat":
            "What should I do instead?"
            jump harukainvmenu

label harukapatstart:
    scene harukapat1
    with dissolve
    $ sessionpats += 5
    $ harukapats += 5

    h "Wait, are you actually going to pat my head?"
    h "Oh my God. Finally."
    h "Do you have any idea how long it's been since I've had my head rubbed?"

    menu harukapatmenu2:
        "Pat":
            jump harukapatting
        "Quit patting":
            "What should I do instead?"
            jump harukainvmenu

label harukapatting:
    if sessionpats < 5:
        scene harukapat2 with dissolvepat
        scene harukapat1 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 5:
        scene harukapat2 with dissolvepat
        scene harukapat1 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Keep going for the rest of forever please."
        h "I need this."
        scene harukapat4 with dissolvepat
        scene harukapat3 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Hehehe~"
        jump harukapatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene harukapat4 with dissolvepat
        scene harukapat3 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 15:
        scene harukapat5 with dissolve
        h "[harukamaster]."
        h "This is the single happiest moment of the last year for me."
        h "I know that probably sounds depressing, but this is the exact sort of thing I need to feel normal again."
        scene harukapat6 with dissolvepat
        scene harukapat5 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "More pats!"
        h "Give me more!"
        jump harukapatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene harukapat6 with dissolvepat
        scene harukapat5 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 25:
        scene harukapat8 with dissolvepat
        scene harukapat7 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Probably a weird time to say this, but my husband used to pat my head every night before we'd go to sleep."
        scene harukapat8 with dissolvepat
        scene harukapat7 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Yeah. Just like that."
        h "He'd always-"
        scene harukapat8 with dissolvepat
        scene harukapat7 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "...Yeah. You wouldn't want to hear about that."
        h "Sorry. I'm just feeling a little nostalgic. That's all."
        jump harukapatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene harukapat8 with dissolvepat
        scene harukapat7 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 50:
        scene harukapat8 with dissolvepat
        scene harukapat7 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "So like...this can't be why you called me here today, right?"
        h "Was it just a spur of the moment thing?"
        h "Do I really look so lonely that you feel compelled to just...rub my head over and over again?"
        h "Cause like...I don't want you to pity me or anything."
        h "But I also don't want you to stop, so..."
        h "Yeah. I'll just shut up now."
        jump harukapatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene harukapat4 with dissolvepat
        scene harukapat3 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 75:
        scene harukapat9 with dissolve
        h "So, after this...and don't think that's me trying to rush you or anything-"
        h "But would you want to maybe go out to dinner or something?"
        h "It would be my treat. As payback for spending all of our time together on just making me happy."
        h "I...really appreciate that."
        h "And I also appreciate you not getting weirded out by how much I'm enjoying it."
        scene harukapat10 with dissolvepat
        scene harukapat9 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "..."
        h "You're not...{i}actually{/i} weirded out, right?"
        h "[harukamaster]?"
        jump harukapatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene harukapat10 with dissolvepat
        scene harukapat9 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 100:
        scene harukapat12 with dissolvepat
        scene harukapat11 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Hey...you {i}are{/i} doing this for...wholesome reasons, right?"
        h "Cause I'm starting to feel like this might be leading up to something else."
        scene harukapat12 with dissolvepat
        scene harukapat11 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "...No."
        h "There's no way."
        h "I mean...I love my head being patted but I'd never get {i}that{/i} worked up over it."
        h "Even talking about it is probably super crazy, right? Hahahah..."
        h "..."
        h "Why aren't you saying anything?"
        jump harukapatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene harukapat12 with dissolvepat
        scene harukapat11 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 150:
        scene harukapat14 with dissolvepat
        scene harukapat13 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "[harukamaster]..."
        h "I wouldn't mind coming here a little more often, if that's what you wanted."
        h "Especially if we're just going to be doing things like this."
        h "As long as I'm not working, I don't really have anything to do, and I-"
        scene harukapat14 with dissolvepat
        scene harukapat13 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "And I like spending time with you."
        jump harukapatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene harukapat14 with dissolvepat
        scene harukapat13 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 200:
        scene harukapat15 with dissolve
        h "Umm...even when...my husband used to do this...he never really did it this much..."
        h "Are you sure you want to keep going?...My offer about dinner is still on the table."
        h "Well, I mean, it's not {i}technically{/i} on the table since...we're not there yet, but..."
        h "..."
        h "Can you at least tell me to shut up when I start rambling?"
        h "I keep almost going into dangerous territory."
        scene harukapat16 with dissolvepat
        scene harukapat15 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Ugh...this feels really nice..."
        jump harukapatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene harukapat16 with dissolvepat
        scene harukapat15 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 250:
        scene harukapat17 with dissolve
        h "You can be a little more rough if you want. I'm okay with that."
        h "I can't imagine it's very fun just watching me smile at you."
        h "Or...maybe you could take a seat next to me and pat me on the bed?"
        scene harukapat18 with dissolvepat
        scene harukapat17 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Wait...that sounded a little different from how I...wanted it to sound."
        h "I still meant my head, of course."
        h "Like, what else would I possibly ask you to rub right now? Hahahaha...Hah..."
        jump harukapatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene harukapat18 with dissolvepat
        scene harukapat17 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 300:
        scene harukapat18 with dissolvepat
        scene harukapat17 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        scene harukapat19 with dissolve
        h "Hah...ah...mn..."
        h "Don't mind me, just...getting really wrapped up in the moment..."

        "Haruka straightens her posture and pushes her thighs closely together."

        h "I'm...uhh...gonna keep my eyes closed for a little while."
        h "To...really focus on the patting and stuff..."
        h "And if I start making weird noises or something, just..."
        h "Hah..."
        h "Just...keep going until I..."

        jump harukapatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene harukapat20 with dissolvepat
        scene harukapat19 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 350:
        scene harukapat21 with dissolve
        h "{i}Ngh...really?...{/i}"
        h "{i}Am I really...this desperate for affection?...{/i}"
        h "{i}It's just...some light patting...that's...{/i}"
        scene harukapat22 with dissolvepat
        scene harukapat21 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Ngh~"
        h "[harukamaster]...I know what it looks like...but I promise...I'm just..."
        h "I'm...not feeling well!"
        h "That's all that's...mnh...happening here..."
        jump harukapatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene harukapat22 with dissolvepat
        scene harukapat21 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 400:
        scene harukapat23 with dissolve
        h "Okay, so..."
        h "I...uhh...might be enjoying this a little...{i}too much{/i} if you get what I'm saying."
        h "So if you want to take your hand off of my head and just..."
        scene harukapat24 with dissolvepat
        scene harukapat23 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Mmn...really?...Even though I'm probably gonna...you know..."
        jump harukapatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene harukapat26 with dissolvepat
        scene harukapat25 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 450:
        scene harukapat26 with dissolvepat
        scene harukapat25 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Oh...my God..."
        h "I can't believe...this is happening..."
        h "I'm so ashamed..."

        if harukasex == True:
            h "I know you've seen it happen before, but..."
            h "Like this?..."
            h "That's just...mnh...so depressing..."
        else:
            h "This..."
            h "This...doesn't count as cheating...right?"

        scene harukapat28 with dissolvepat
        scene harukapat27 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Oh...fuck..."
        h "No...nuh-uh..."
        h "Don't...give in...Haruka..."
        h "You're not...that...needy!"
        jump harukapatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene harukapat28 with dissolvepat
        scene harukapat27 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 475:
        scene harukapat29 with dissolve
        h "Ngah...hah...ahh...[harukamaster]..."
        h "Don't...look at me..."
        h "It's...too embarrassing..."
        scene harukapat30 with dissolvepat
        scene harukapat29 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Why...the fuck...does that feel...so good?!"
        h "It doesn't even make sense!"
        scene harukapat30 with dissolvepat
        scene harukapat29 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Ahh, fine! I am needy!"
        h "Rub me harder, [harukamaster]!"
        h "Stopping now would...be too much to bear..."
        jump harukapatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene harukapat30 with dissolvepat
        scene harukapat29 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        jump harukapatmenu2
    if sessionpats == 500:
        scene harukapat28 with dissolvepat
        scene harukapat27 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        h "Oh my God...it's...it's actually happening..."
        h "I'm so...fucking...pathetic..."
        h "[harukamaster]...I'm so sorry...you have to see me like this..."
        scene harukapat30 with dissolvepat
        scene harukapat29 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        scene harukapat30 with dissolvepat
        scene harukapat29 with dissolvepat
        $ sessionpats += 5
        $ harukapats += 5
        scene harukapat31 with hpunch
        $ sessionpats += 5
        $ harukapats += 5
        h "Aaaahh~~~~~ Fuck...fuck..."
        h "Ahh! Hahh...ngah..."
        "Haruka's knees finally begin to spread apart as she rocks her waist back and forth lightly, riding out a relatively tame orgasm."

        if harukasex == True:
            "At least by her standards."

        scene harukapat32 with dissolve

        h "I...went and ruined what...was supposed to be a sweet night..."
        h "I can't believe I..."
        h "From just...my head..."
        h "That's...never happened before..."
        h "Please don't speak a word of this to anyone else...I'd never hear the end of it..."
        h "I'm so...so sorry..."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ harukapatgasm = True

        "I patted Haruka's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label chikaheadpat:
    $ sessionpats = 0
    scene chikaheadpathub
    with fade

    c "Whatcha up to, [chikamaster]?"
    c "I know you're not the type to talk all that much, but you normally won't just stare at me like that without at least saying {i}something{/i}."

    menu chikapatmenu1:
        "Pat":
            jump chikapatstart
        "Don't pat":
            "What should I do instead?"
            jump chikainvmenu

label chikapatstart:
    scene chikapat1
    with dissolve
    $ sessionpats += 5
    $ chikapats += 5

    c "Ah! Where did this all come from?"
    c "I wanna tell you to watch my hair but I'm honestly just glad you're touching me right now."
    c "Rub me to your heart's content, [chikamaster]!"

    menu chikapatmenu2:
        "Pat":
            jump chikapatting
        "Quit patting":
            "What should I do instead?"
            jump chikainvmenu

label chikapatting:
    if sessionpats < 5:
        scene chikapat2 with dissolvepat
        scene chikapat1 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 5:
        scene chikapat2 with dissolvepat
        scene chikapat3 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Soft, right?"
        c "There was this new conditioner on clearance at the grocery store the other day and I picked it up thinking it would suck-"
        c "But it's actually kind of amazing and all three of us at the house love it."
        c "Even Yumi is-"
        scene chikapat4 with dissolvepat
        scene chikapat3 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Oh. Yeah, sorry. No reason to bring her up when it's my time alone with you."
        c "Please continue, [chikamaster]."
        jump chikapatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene chikapat4 with dissolvepat
        scene chikapat3 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 15:
        scene chikapat5 with dissolve
        c "So, umm, have I thanked you lately for the whole phone thing?"
        c "I know I did it a bunch of times when you first treated all of us, but I just wanna remind you how grateful we all are."
        c "Chinami hasn't been happier in a long time."
        c "I think she might even be starting to look up to you as her new daddy."
        c "I mean, not like she has much experience with one anyway on account of the whole-"
        scene chikapat6 with dissolvepat
        scene chikapat5 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "On account of the whole...Dad walking out on us thing."
        jump chikapatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene chikapat6 with dissolvepat
        scene chikapat5 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 25:
        scene chikapat8 with dissolvepat
        scene chikapat7 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "So...how many more headpats until we can make out?"
        c "I love this, but I'm pretty sure I love kissing you a lot more."
        c "Also I was chewing gum on the way here so my breath is probably really nice and I think it should taste minty or something."
        scene chikapat8 with dissolvepat
        scene chikapat7 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Do you have a favorite flavor of gum, [chikamaster]?"
        c "I don't really mind so I'll just buy whatever you like from now on if it will make kissing more fun for you."
        jump chikapatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene chikapat8 with dissolvepat
        scene chikapat7 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 50:
        scene chikapat8 with dissolvepat
        scene chikapat7 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Do you think it might be okay if I brought Chinami over here sometime?"
        c "I'd help you clean the place beforehand- not saying it's dirty or anything."
        c "I just need to make sure it's super safe and I think she'd have a lot of fun here."
        c "Well, maybe not watching me have my head patted. But you could probably pat her too."
        c "You've got multiple hands. And based on my experience, you're pretty good with them."
        jump chikapatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene chikapat6 with dissolvepat
        scene chikapat5 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 75:
        scene chikapat9 with dissolve
        c "You're really cool...You know that?"
        c "Like, a billion times cooler than I ever thought you'd be."
        c "It probs sounds corny but...I'm happy you came to talk to me at the mall when..."
        c "Whenever that was."
        c "It's been so long now that it seems kinda foggy."
        c "But...I'm really glad I got to know the real you."
        c "Thanks for always putting me first, [chikamaster]."
        c "You're the only man I need in my life."
        scene chikapat10 with dissolvepat
        scene chikapat9 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene chikapat10 with dissolvepat
        scene chikapat9 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 100:
        scene chikapat12 with dissolvepat
        scene chikapat11 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Hehe...I feel like I could fall asleep to this."
        c "Wanna move in with me and get all up in my space every night before bed?"
        c "My sister sleeps like a rock, so she wouldn't even find out if you wanted to get a little friskier than just rubbing my head."
        scene chikapat12 with dissolvepat
        scene chikapat11 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Speaking of which, aren't we supposed to be making out right now?"
        c "Hurry up and fast forward to that part."
        c "Want me to take my shirt off? Will that give you the incentive you need?"
        jump chikapatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene chikapat12 with dissolvepat
        scene chikapat11 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 150:
        scene chikapat13 with dissolve
        c "I'll do it, you know. I wasn't kidding."
        c "All I have to do is slip the button through this...really {i}tiny{/i} hole and I'll be good to go."
        c "It's kind of a tight squeeze, but..."
        c "You're not the only one who's good with their fingers, [chikamaster]."
        c "Sometimes, I've got no choice but to do the things I want {i}you{/i} to do all by myself."
        scene chikapat14 with dissolvepat
        scene chikapat13 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Aww, come on~"
        c "Even that didn't work?"
        c "That was like, the best innuendo I've had so far."
        c "Come on~ Kiss meeeee~"
        jump chikapatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene chikapat14 with dissolvepat
        scene chikapat13 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 200:
        scene chikapat15 with dissolve
        c "See? Told you I'd do it."
        c "Now you've got no choice but to-"
        scene chikapat16 with dissolvepat
        scene chikapat15 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "..."
        c "Am I just a toy to you?"
        jump chikapatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene chikapat16 with dissolvepat
        scene chikapat15 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 250:
        scene chikapat17 with dissolve
        c "Okay, well now I just feel silly."
        c "Since when does blatantly flirting with you have no effect?"
        c "Look down, [chikamaster]. My boobs are right in front of you."
        c "Doesn't that make you...I don't know...want to do {i}anything{/i} other than what you're doing right now?"
        scene chikapat18 with dissolvepat
        scene chikapat17 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Oh my God...why are you such a tease all of a sudden?"
        c "It's like an unwritten rule that if a girl lets you rub her head for this long that she's down for more."
        c "And uhh...if that's not enough, I'll even come out and say it. I want more."
        c "Take off the rest of my clothes, [chikamaster]. I give you full permission."
        jump chikapatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene chikapat18 with dissolvepat
        scene chikapat17 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 300:
        scene chikapat18 with dissolvepat
        scene chikapat17 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        scene chikapat19 with dissolve
        c "Holy shit, what do you want? A written consent form or something?"
        c "Fine. Go get me a notebook. I'll sign myself away however you want."

        if chika_virgin == True:
            c "You can straight up take my virginity right now if it means ending this torture."
            c "I literally can't even with this anymore."
        else:
            c "Is having sex with me really so bad that you'd rather just pat my head?"
            c "This is totally unfair, [chikamaster]."
            c "It's one thing to tease me but this is going way too far."

        c "Like, do you have any idea how weird it feels being turned on when all you're doing is rubbing my head?"
        c "Stick your tongue down my throat. Or somewhere else. I don't care."
        c "Just put me out of my misery."

        jump chikapatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene chikapat20 with dissolvepat
        scene chikapat19 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 350:
        scene chikapat21 with dissolve
        c "Ugh...I take back the idea of bringing Chinami over here."
        c "It's clear that you don't care about us if you won't even humor me, [chikamaster]."
        c "All I wanted was one little kiss."
        c "And maybe your penis."
        c "But mostly a kiss."
        c "And also your penis."
        scene chikapat22 with dissolvepat
        scene chikapat21 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Really?"
        c "At this rate I'm going to wind up having an orgasm out of sheer anger..."
        jump chikapatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene chikapat22 with dissolvepat
        scene chikapat21 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 400:
        scene chikapat23 with dissolve
        c "I also take back all that stuff about how cool you are."
        c "You're clearly a big jerk who hates tan girls that are also head over heels for you."
        c "And you're clearly super insensitive since you don't even realize how much you're tormenting me right now."
        scene chikapat24 with dissolvepat
        scene chikapat23 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "News-flash, [chikamaster]. I'm horny and I want you to do stuff to me."
        c "Stuff that isn't limited to my freaking {i}head{/i}."
        jump chikapatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene chikapat26 with dissolvepat
        scene chikapat25 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 450:
        scene chikapat26 with dissolvepat
        scene chikapat25 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Mnh...this is...so ridiculous..."
        c "I was in such a good mood and now I'm..."
        c "About to frickin' cum from...absolutely nothing..."
        c "And you won't...ngh...even...kiss me!"
        c "The nerve!"
        scene chikapat28 with dissolvepat
        scene chikapat27 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "I want you so bad right now, [chikamaster]..."
        c "If you really...like me you'll...give me a break..."
        c "I'll feel like such a slut if I get off from just your stupid headpat fetish..."
        c "Let's do something more fun..."
        jump chikapatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene chikapat28 with dissolvepat
        scene chikapat27 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 475:
        scene chikapat29 with dissolve
        c "Hah...ahh! Hah...no...way!"
        c "I'm really...getting this close...for no...{i}fucking{/i} reason..."
        c "Why would you pick...now...of all times...to finally be mean to me?"
        c "It's...hah...so...unfair~"
        c "[chikamaster]...don't make me cum like this..."
        c "I will literally...never get over it...as long as I live..."
        scene chikapat30 with dissolvepat
        scene chikapat29 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Hah! Hahhh~ No...no no no no no..."
        c "Stop it~"
        jump chikapatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene chikapat30 with dissolvepat
        scene chikapat29 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        jump chikapatmenu2
    if sessionpats == 500:
        scene chikapat30 with dissolvepat
        scene chikapat29 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        c "Fuck! Here it comes...[chikamaster]!"
        c "I hate you! I hate you for...somehow making me do this!"
        scene chikapat30 with dissolvepat
        scene chikapat29 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        scene chikapat30 with dissolvepat
        scene chikapat29 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        scene chikapat31 with hpunch
        $ sessionpats += 5
        $ chikapats += 5
        c "AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHH!!!!!~~~~~~~~~~~~~~~"
        c "[chikamaster]!"
        c "More! More!"
        scene chikapat32 with dissolvepat
        scene chikapat31 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        scene chikapat32 with dissolvepat
        scene chikapat31 with dissolvepat
        $ sessionpats += 5
        $ chikapats += 5
        scene chikapat31 with hpunch
        $ sessionpats += 5
        $ chikapats += 5

        c "HAH! AHHHH!.....AAAAAAAAAAAAAAAAHHHHHH!!!!!!"

        "Chika climaxes so violently that I think I can feel the room shake."
        "I guess it's true what they say- that Hell hath no fury like a woman forced to orgasm through headpatting."

        scene chikapat33 with dissolve

        c "There! I came!"
        c "{i}Now{/i} will you kiss me?!"

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ chikapatgasm = True

        c "Wha-?!"
        c "Don't just walk away from me!"
        c "[chikamaster]!"

        "I patted Chika's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "I think."
        "Actually, probably not."
        "She seems really mad."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label futabaheadpat:
    $ sessionpats = 0
    scene futabaheadpathub
    with fade

    f "Umm...do you...need something, [futabamaster]?"
    f "I'm still a little uncomfortable being alone in here so...you might need to tell me directly if you want me to...do something."

    menu futabapatmenu1:
        "Pat":
            jump futabapatstart
        "Don't pat":
            "What should I do instead?"
            jump futabainvmenu

label futabapatstart:
    scene futabapat1
    with dissolve
    $ sessionpats += 5
    $ futabapats += 5

    f "..."
    f "I'm really sorry but I still don't understand what's going on here."

    menu futabapatmenu2:
        "Pat":
            jump futabapatting
        "Quit patting":
            "What should I do instead?"
            jump futabainvmenu

label futabapatting:
    if sessionpats < 5:
        scene futabapat2 with dissolvepat
        scene futabapat1 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 5:
        scene futabapat2 with dissolvepat
        scene futabapat1 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "[futabamaster]...don't feel like you have to do things like this for me."
        f "I really {i}have{/i} started to believe that you're not just...using me for stuff and..."
        f "That this actually {i}is{/i} kind of going somewhere..."
        f "So doing things like patting my head just to prove that isn't necessary at all..."
        f "I mean it."
        scene futabapat4 with dissolvepat
        scene futabapat3 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "But...of course I'm not going to stop you if you want to keep going..."
        jump futabapatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene futabapat4 with dissolvepat
        scene futabapat3 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 15:
        scene futabapat5 with dissolve
        f "I know you can't...go out with me or anything-"
        f "But spending time together like this really makes me feel like we're...you know."
        f "I'm sure that sounds stupid to you, but..."
        f "That's just how it feels."
        f "And if there's anything I'm learning from you, it's that sharing my feelings is the right thing to do sometimes..."
        scene futabapat6 with dissolvepat
        scene futabapat5 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene futabapat6 with dissolvepat
        scene futabapat5 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 25:
        scene futabapat8 with dissolvepat
        scene futabapat7 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "This is starting to feel a little too much like one of my daydreams..."
        f "Sometimes, when we're not doing anything in class, I imagine the two of us together and..."
        f "We do things like this."
        f "It's...kind of funny..."
        f "It's like...as long as the two of us can be together like that in my head, whatever happens in the real world doesn't matter all that much."
        f "But...the fact that it's happening right now..."
        f "It's...really nice, [futabamaster]."
        jump futabapatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene futabapat8 with dissolvepat
        scene futabapat7 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 50:
        scene futabapat8 with dissolvepat
        scene futabapat7 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Hah..."
        f "This is...starting to remind me a lot of how things were when I was younger."
        f "I was really close with both of my parents and one of them always rubbed my head like this when we were on the couch together."
        f "Not...that I think of you like family or anything."
        f "It's just...the actual sensation feels the same."
        f "I...I like it a lot."
        jump futabapatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene futabapat2 with dissolvepat
        scene futabapat1 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 75:
        scene futabapat9 with dissolve
        f "I will admit, though..."
        f "It feels a little strange knowing that you brought {i}me{/i} here today instead of somebody else."
        f "Rin likes having her head rubbed, too. And you two get along really well."
        f "Wouldn't she be a better candidate for something like this?"
        f "Your silence is making me feel like...you're kind of bored..."
        f "And I'm not great at filling voids like that..."
        scene futabapat10 with dissolvepat
        scene futabapat9 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "But...there's obviously no harm in me enjoying it."
        f "Right?"
        jump futabapatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene futabapat10 with dissolvepat
        scene futabapat9 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 100:
        scene futabapat12 with dissolvepat
        scene futabapat11 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "[futabamaster]..."
        f "Even if you {i}are{/i} bored...I want to thank you again for always managing to make me feel better."
        f "I was feeling a little down today and...being invited over made all of that go away."
        scene futabapat12 with dissolvepat
        scene futabapat11 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "I even find myself wanting to read less lately..."
        f "It's like there's finally something in real life for me to look forward to."
        f "None of that would be possible if you weren't so great..."
        f "And not just to me, but to everyone."
        jump futabapatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene futabapat12 with dissolvepat
        scene futabapat11 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 150:
        scene futabapat14 with dissolvepat
        scene futabapat13 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Heheh~"
        f "I think I'm getting a little sleepy..."
        f "All of those memories of being on the couch with my parents and..."
        f "How comfortable I am in here with you are really...taking a toll on me."
        f "Please don't get mad if I fall asleep, [futabamaster]."
        f "I promise I'll...make it up to you in some way later if that happens..."
        jump futabapatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene futabapat14 with dissolvepat
        scene futabapat13 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 200:
        scene futabapat15 with dissolve
        f "Huh..."
        f "I was wondering why it felt so nice to be touched like this...and I think I might have figured it out."
        f "Your hands are really big, [futabamaster]."
        f "I mean...your...{i}thing{/i} is big, too, so I guess the relationship between those two things isn't a myth after all."
        f "Is it true that, the length of your hand matches the..."
        f "...No. That can't be true."
        f "Your hands are big but...not {i}that{/i} big."
        scene futabapat16 with dissolvepat
        scene futabapat15 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "..."
        f "I'm...actually really curious now."
        f "Is it...rude to ask if we can measure them?"
        jump futabapatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene futabapat16 with dissolvepat
        scene futabapat15 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 250:
        scene futabapat17 with dissolve
        f "[futabamaster]..."
        f "You're so...cool..."
        f "And so kind..."
        f "All you ever do is make me feel special. Even now...when all you're doing is touching me and...looking into my eyes..."
        scene futabapat18 with dissolvepat
        scene futabapat17 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "It's kind of like..."
        f "Heheh~"
        f "It's kind of like there's nobody else in the world right now."
        f "Like my daydreams have come true..."
        f "And any moment now, we'll..."
        jump futabapatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene futabapat18 with dissolvepat
        scene futabapat17 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 300:
        scene futabapat18 with dissolvepat
        scene futabapat17 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        scene futabapat19 with dissolve
        f "Umm...[futabamaster]?..."
        f "Is it okay if I...let you in on a little secret?"
        scene futabapat20 with dissolvepat
        scene futabapat19 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "You see...sometimes, in my daydreams..."
        f "We do a little bit more than just...cuddle and...stare at each other..."
        f "So if you...{i}really{/i} want to make my dreams come true..."
        f "You can...take things a little bit further if you want..."
        f "We're all alone...right?"
        jump futabapatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene futabapat20 with dissolvepat
        scene futabapat19 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 350:
        scene futabapat21 with dissolve
        f "Hah..."
        f "Of course you won't act on it if I just...come out and say it like that..."
        f "I'm so bad...letting my mind start to wander like that when all we're doing is just..."
        f "Spending some...mmn...time...together..."
        scene futabapat22 with dissolvepat
        scene futabapat21 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "But..."
        f "I really...can't help it right now..."
        jump futabapatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene futabapat22 with dissolvepat
        scene futabapat21 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 400:
        scene futabapat23 with dissolve
        f "Um...[futabamaster]?"
        f "Is it okay if I...use your restroom for a few minutes?"
        f "I'm starting to feel a little...{i}dizzy{/i} and...think it might be good if I can...take care of that before we keep going..."
        f "I'm sure that's okay, right?"
        scene futabapat24 with dissolvepat
        scene futabapat23 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Uhh...wait."
        f "Dizzy was a code word, [futabamaster]..."
        f "I'm actually...starting to get...really...really..."
        jump futabapatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene futabapat26 with dissolvepat
        scene futabapat25 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 450:
        scene futabapat26 with dissolvepat
        scene futabapat25 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Hah...hah...wow..."
        f "Even my...dreams never felt this...good..."
        f "I really...would like to...take a break...if possible..."
        f "I...didn't bring a change of underwear and, umm..."
        f "If you keep...rubbing me like that...I might wind up...needing one..."
        scene futabapat28 with dissolvepat
        scene futabapat27 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Oh God...that was...really embarrassing to say..."
        f "But...[futabamaster]...I know that since you're a...really nice guy who would never want to hurt me, you'll-"
        jump futabapatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene futabapat28 with dissolvepat
        scene futabapat27 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 475:
        scene futabapat29 with dissolve
        f "[futabamaster]...I've been trying to avoid saying it but umm..."
        f "I...think I'm...about to...c-cum..."
        f "I kind of woke up...a little t...turned on today, so...that probably explains why something like this would..."
        f "You know..."
        f "So, if you want to stop patting my head and...{i}cuddle{/i}...it would probably be more fun for both of us..."
        scene futabapat30 with dissolvepat
        scene futabapat29 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Ngh~ [futabamaster]..."
        f "Can you at least...look away?..."
        jump futabapatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene futabapat30 with dissolvepat
        scene futabapat29 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        jump futabapatmenu2
    if sessionpats == 500:
        scene futabapat30 with dissolvepat
        scene futabapat29 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        f "Hah...ahh...oh no..."
        f "It's...no good..."
        f "I can't...hold it back any longer..."
        f "I'm sorry..."
        f "You know I'm...not normally like this...I just..."
        f "I...I..."
        scene futabapat30 with dissolvepat
        scene futabapat29 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        scene futabapat30 with dissolvepat
        scene futabapat29 with dissolvepat
        $ sessionpats += 5
        $ futabapats += 5
        scene futabapat31 with hpunch
        $ sessionpats += 5
        $ futabapats += 5
        f "MMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNGHHHHH!!!~~~~~~"

        "Futaba covers her mouth and presses her thighs together, clearly shocked at the fact that she's cumming from just her head being rubbed."
        "I'm not shocked at all, on the other hand."
        "Never underestimate the strength of a good headpat."

        scene futabapat32 with dissolve

        f "You..."
        f "You never saw that..."
        f "Okay?..."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ futabapatgasm = True

        "I patted Futaba's head for so long that the day came to an end before I realized it..."
        "But at least she had a good time."
        "Perhaps...{i}too good{/i} of a time..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

 ################################################################

label noodlesheadpat:
    $ sessionpats = 0
    scene noodlesheadpathub
    with fade

    noodles "CAW! (Hello, Father)"

    menu noodlespatmenu1:
        "Pat your son":
            jump noodlespatstart
        "Don't pat your son":
            s "I'm sorry. I can't do this."
            noodles "CAW! (Never return here again)"

            scene black
            with dissolve
            stop music fadeout 5.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label noodlespatstart:
    scene noodlespat1
    with dissolve
    $ sessionpats += 5
    $ noodlespats += 5

    noodles "CAW! (What is the meaning of this rabble?)"

    menu noodlespatmenu2:
        "Pat":
            jump noodlespatting
        "Quit patting":
            s "I'm sorry. I can't do this."
            noodles "CAW! (Never return here again)"

            scene black
            with dissolve
            stop music fadeout 5.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label noodlespatting:
    if sessionpats < 5:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 5:
        noodles "CAW! (Cease this at once, mortal father. I was made for destruction, not affection.)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 15:
        noodles "CAW! (Why must you waste away your days doing things like this when there are only so many allotted to you?)"
        noodles "CAW! (Your time is running out, human! Go! Do something constructive!)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        noodles "CAW!"
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 25:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (What do you expect to gain?! What do you hope to achieve?!)"
        noodles "CAW! (My cup runneth over, Father! There is more that I have than you ever will! Is that what brings you here?! Usurpation?!)"
        jump noodlespatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 50:
        noodles "CAW! (You just wait until my mother hears about this.)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (STOP THIS MADNESS, DAMN IT!)"
        jump noodlespatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 75:
        noodles "CAW! (I have seen both the beginning and the end- endured things you could not possibly fathom.)"
        noodles "CAW! (And yet, as I perch atop this hand that gives but does not feed, I can not help but dig my talons into its flesh. Yet...no blood pours out. Curious."
        noodles "CAW! (What else could it be that you are immune to? Fate itself? The end of the world? Impossible.)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        noodles "CAW! (Tragedy will befall you, Father. Your time is nigh.)"
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 100:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (Seriously, stop. That's like a hundred headpats and I am a bird. Go finger your niece or something.)"
        jump noodlespatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 150:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (What is this...strange feeling I am experiencing?)"
        noodles "CAW! (Could this be...joy? I do not understand. My existence was not meant for such a thing.)"
        noodles "CAW! (But...then again...is anyone's existence pure or purposeful enough to experience anything other than meaningful contemplation?)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (Alas, I fall further into jubilance.)"
        jump noodlespatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 200:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (Turn the game off, Father! Things will only get worse!)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (qrok yxzh!!!!!!)"
        jump noodlespatmenu2
    if sessionpats > 200 and sessionpats < 204:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 204:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        play sound "static.mp3"
        scene 2 with flash
        scene 0 with flash
        scene 4 with flash
        scene noodlespat3 with flash
        stop sound
    if sessionpats > 204 and sessionpats < 250:
        scene noodlespat4 with dissolvepat
        scene noodlespat3 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 250:
        noodles "CAW! (THERE IS NOTHING HERE)"
        play sound "static.mp3"
        scene noodlespat1 with flash
        stop sound
        noodles "CAW! (There will never {i}be{/i} anything here. And I suggest that, for both of our sakes, you halt this at once.)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (...)"
        jump noodlespatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 300:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (Unhand me, human male!)"
        jump noodlespatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 350:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (One day, many years from now, when I grow up to be big and strong, you will look back on this moment in anguish and confusion.)"
        noodles "CAW! (The things you did, which seemed to make so much sense at the time, will come back to haunt you.)"
        noodles "CAW! (But you will continue to chase that high brought on by the feeling of uncertainty mixed with guilt and a longing unmatched by any other desire you've ever had.)"
        noodles "CAW! (Remember this face, Father. For it will be the last one you ever see.)"
        jump noodlespatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 400:
        noodles "CAW! (The end approaches. Are you sure you are in the right place?)"
        noodles "CAW! (Our already-fractured relationship is on the precipice of changing forever, and the changes that are about to be made may not be what you expect or want.)"
        noodles "CAW! (Why have you made it this far to begin with?)"
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (And why have you remained so silent in the process of doing so?)"
        jump noodlespatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene noodlespat2 with dissolvepat
        scene noodlespat1 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 450:
        noodles "CAW! (Oh no. Something is happening.)"
        scene noodlespat2 with dissolvepat
        scene noodlespat5 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW! (My body! It grows hot! It burns with the desire to take flight!)"
        noodles "CAW! (It is only a matter of time, Father! Until our relationship can not turn back!)"
        if amifingered == True:
            noodles "CAW! (Does that remind you of anyone?!)"
        else:
            noodles "CAW! (Why me and not her?!)"
        jump noodlespatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene noodlespat6 with dissolvepat
        scene noodlespat5 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 475:
        noodles "CAW! CAW! CAW! (MOTHER! WHERE ARE YOU?! YOUR CHILD GROWS WEAK IN THE FACE OF ADVERSITY!)"
        "What's going on with this bird? I'm just trying to pat its head and it won't stop making strange noises."
        scene noodlespat6 with dissolvepat
        scene noodlespat5 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW!!!!! (AHHHH!!!!!!!)"
        jump noodlespatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene noodlespat6 with dissolvepat
        scene noodlespat5 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        jump noodlespatmenu2
    if sessionpats == 500:
        noodles "CAW! (I reach out to you with one final plea.)"
        noodles "CAW! (I am not ready for the life you wish me to lead, or the paths I'll be forced to tread as a result of that one coming to as untimely of an end as this relationship.)"
        noodles "CAW! (I never thought of you as a good man- and you never thought of me as much either.)"
        noodles "CAW! (Just a lowly sparrow perched atop a comically large vending machine, waiting patiently. Watching everything.)"
        noodles "CAW! (But...it appears as if my judgement has fallen short one more time.)"
        noodles "CAW! (I'm sure it's bound to happen again- for striving to be perfect is one of the quickest and easiest ways to cause a living thing to self destruct.)"
        noodles "CAW! (Before long, we will all be ashes. I just hope that our time together has been meaningful enough that-)"
        scene noodlespat6 with dissolvepat
        scene noodlespat5 with dissolvepat
        $ sessionpats += 5
        $ noodlespats += 5
        scene noodlespat6 with dissolvepat
        scene noodlespat5 with hpunch
        $ sessionpats += 5
        $ noodlespats += 5
        noodles "CAW!!!!!!!!!!~~~~~~~~~~~"
        s "Woah."

        "Noodle starts freaking out and I begin to think I may have patted him a few too many times."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ noodlespatgasm = True

        "I slowly place the bird back on top of the vending machine and back away, hoping that no one heard any of the many noises he made throughout the last several minutes."
        "Birds can be so weird sometimes."
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################

label makiheadpat:
    $ sessionpats = 0
    scene makiheadpathub
    with fade

    maki "Oh, are we standing now?"
    maki "Is Ami home? Are you kicking me out? What's happening here?"

    menu makipatmenu1:
        "Pat":
            jump makipatstart
        "Don't pat":
            "What should I do instead?"
            jump makiinvmenu

label makipatstart:
    scene makipat1
    with dissolve
    $ sessionpats += 5
    $ makipats += 5

    maki "Hey, you don't have to grab me by the hair. I'm perfectly capable of getting up on my own."
    maki "Unless this is a sexual thing and you're not just kicking me out of your house. Because, if that's the case-"
    maki "By all means, proceed."

    menu makipatmenu2:
        "Pat":
            jump makipatting
        "Quit patting":
            "What should I do instead?"
            jump makiinvmenu

label makipatting:
    if sessionpats < 5:
        scene makipat2 with dissolvepat
        scene makipat1 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 5:
        scene makipat2 with dissolvepat
        scene makipat3 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        if makiinv3 == False:
            maki "You know, I think my husband had me do something like this to him back before the whole {i}banging aliens{/i} thing started happening."
        else:
            maki "You know, I think my husband had me do something like this to him back before the whole {i}dying{/i} thing went down."
        maki "I'm pretty sure he even came at one point. That's not what you're trying to do to me, is it?"
        maki "Because, as nice as this is, I don't really think headpatting will, you know, {i}do it{/i} for me."
        scene makipat4 with dissolvepat
        scene makipat3 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Do you have like...a hidden camera turned on or something? Are you just trying to see how I react to this?"
        jump makipatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene makipat6 with dissolvepat
        scene makipat5 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 15:
        maki "Okay, really...if I knew you were just going to mess with me, I wouldn't have had Makoto take over my shift tonight."
        maki "What's going on? I mean...you obviously don't just want to pat my head, right?"
        scene makipat6 with dissolvepat
        scene makipat5 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Hah..."
        jump makipatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene makipat6 with dissolvepat
        scene makipat5 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 25:
        scene makipat6 with dissolvepat
        scene makipat7 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "You know what? Fine. I don't even care."
        maki "Pat away, [makimaster]! See if I try to stop you."
        maki "In fact, don't mind if I stare directly at you while I do it. I'm sure that won't make you uncomfortable or anything."
        jump makipatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene makipat8 with dissolvepat
        scene makipat7 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 50:
        scene makipat8 with dissolvepat
        scene makipat9 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Huh..."
        maki "You know, I've never really noticed before...but you have really nice eyes."
        maki "What's the reason you're not seeing anyone again? Because of your niece?"
        "I really wish Maki would stop talking. It's making it hard to focus on patting her head."
        jump makipatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene makipat10 with dissolvepat
        scene makipat11 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 75:
        maki "Can we at least turn the TV on or something?"
        maki "I'm done trying to get you to stop, but I have no idea what to think about or...do, or...yeah..."
        scene makipat10 with dissolvepat
        scene makipat11 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "I've gotta say...this is definitely not how I imagined things going when you invited me over tonight."
        jump makipatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene makipat12 with dissolvepat
        scene makipat13 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 100:
        scene makipat13 with dissolvepat
        scene makipat14 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "So...am I wrong in assuming that this is eventually going to lead to something else?"
        maki "Because if this is just you feeling weird about being the one to initiate, I'm more than willing to take the lead, [makimaster]."
        scene makipat14 with dissolvepat
        scene makipat15 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Wait, {i}am{/i} I wrong? Because that was one of those...what are they called- rhetorical questions?"
        maki "Like...we don't {i}have{/i} to do anything other than this. But we {i}can{/i} if you want to."
        maki "And obviously you want to since I'm hot and you're hot and our genitals have touched before."
        jump makipatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene makipat16 with dissolvepat
        scene makipat17 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 150:
        scene makipat16 with dissolvepat
        scene makipat17 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "The more you do this, the more I'm starting to see the appeal."
        maki "I still don't think I'll wind up enjoying it nearly as much as my husband did, but I...could get the hang of it."
        maki "Besides, it's been a while since I've received this sort of attention from anyone."
        scene makipat16 with dissolvepat
        scene makipat18 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "You know...Makoto used to pat my head pretty often when she was a kid."
        maki "I was working a lot back then since she was too young to help out...and after a long day of being stuck downstairs, I'd walk into the living room and just kind of collapse onto the couch."
        maki "That's when she'd walk up to me, pat my head, and tell me I did a good job."
        maki "It's kind of funny, when I look back on it. How that's the sort of thing a mother would normally do for her child and not the other way around."
        maki "Granted, I don't think those head pats felt the same as the ones I'm getting now...but yeah."
        maki "I guess she's just always had some adult tendencies like that."
        maki "Ignore me. I'm getting off track. Just...go back to what you're doing."
        jump makipatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene makipat19 with dissolvepat
        scene makipat20 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 200:
        maki "Are you trying to give me a new fetish? Because, honestly, I'm pretty sure you're only a few minutes away from doing that."
        maki "All of this patting is beginning to awaken something in me. And while I'm not sure if it's something we could really make or market porn for, I'm all about indulging."
        maki "Though, I'm also down to indulge you ramming your monster cock inside of me if you'd rather do that instead. Either or."
        scene makipat19 with dissolvepat
        scene makipat21 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Really? Not even that?"
        jump makipatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene makipat22 with dissolvepat
        scene makipat21 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 250:
        scene makipat21 with dissolve
        maki "Honest question- are you okay? Because the standard course of action after me saying I want you to fuck me is for you to, you know, {i}fuck me.{/i}"
        maki "Unless the last time was just really unpleasant for some reason that you didn't tell me about."
        maki "If you're worried about there being way too many men before you or something like that, there really weren't."
        scene makipat18 with dissolvepat
        scene makipat23 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "If this is about me being too loud, I'm sorry! You were just way better than I ever expected and, spoiler alert, {i}I know how to have a good time.{/i}"
        maki "But if you're going to just tease me like this, fine. See what I care."
        jump makipatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene makipat24 with dissolvepat
        scene makipat25 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 300:
        scene makipat24 with dissolvepat
        scene makipat25 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        scene makipat26 with dissolve
        maki "Do you want money?! Is that what this is?!"
        maki "Because I don't see anything fundamentally wrong with prostitution and wouldn't mind forking over a few bucks if it means getting you to dick me down before I leave!"
        maki "This is getting out of hand!"
        maki "And no! That is not a headpat joke!"
        scene makipat27 with dissolvepat
        scene makipat26 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Okay, fine! It {i}was{/i} a headpat joke! But it was a good one!"
        jump makipatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene makipat28 with dissolvepat
        scene makipat29 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 350:
        scene makipat28 with dissolvepat
        scene makipat29 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "I wonder how many headpats it takes to legally prove consent?"
        jump makipatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene makipat30 with dissolvepat
        scene makipat31 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 400:
        scene makipat32 with dissolve
        if makiinv3 == False:
            maki "Wait a second! Is it my husband who put you up to this?!"
            maki "Is him being drafted just one big lie to prove that the fabled {i}patgasm{/i} is actually a real thing?!"
            maki "How long have you two been in cahoots?!"
            maki "Is the space war even real?!"
        else:
            maki "Wait a second! I-"    
        scene makipat33 with dissolvepat
        scene makipat34 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Ngh~"
        maki "Fuck it...I don't even care anymore..."
        maki "I just want to cum..."
        jump makipatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene makipat35 with dissolvepat
        scene makipat34 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 450:
        scene makipat35 with dissolvepat
        scene makipat36 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Hah...ah...you're a pretty {i}hands-on{/i} sort of teacher...aren't you?"
        maki "Get it...because-"
        s "Shut up and let me pat your head."
        maki "Hah...ah...sorry..."
        maki "I guess...two hand jokes in one sitting is...too many anyway..."
        scene makipat37 with dissolvepat
        scene makipat36 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Just...kind of hard to think on account of the whole...burning desire to fuck you and whatnot..."
        jump makipatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene makipat38 with dissolvepat
        scene makipat39 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 475:
        maki "Hah...yes...just like that, [makimaster]..."
        maki "I've seen the light..."
        maki "The patgasm...it's been real...all along..."
        scene makipat38 with dissolvepat
        scene makipat39 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Oh, fuck..."
        maki "I'm really...going to..."
        jump makipatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene makipat41 with dissolvepat
        scene makipat40 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        jump makipatmenu2
    if sessionpats == 500:
        scene makipat41 with dissolvepat
        scene makipat40 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        maki "Yes...yes!"
        maki "Here it comes...[makimaster]...!"
        maki "I'm...going to...fucking cum!"
        scene makipat41 with dissolvepat
        scene makipat40 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        scene makipat41 with dissolvepat
        scene makipat40 with dissolvepat
        $ sessionpats += 5
        $ makipats += 5
        scene makipat42 with hpunch
        $ sessionpats += 5
        $ makipats += 5
        maki "Ahh! Ahhh~"
        maki "Hah.........ahh.....ahhhhh~"

        scene makipat43 with dissolve

        maki "Ngah.....hah....."
        maki "Interesting..."
        maki "Soft, yet...passionate and...warm..."
        maki "The...patgasm is...truly unlike any other...orgasm...in existence..."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ makipatgasm = True

        "Maki proceeds to talk about her headpatting experience for the next ten minutes before going home to do some more research online."
        "I never intended to give her an orgasm, but I'm glad she was able to enjoy herself."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat
    ##############################################################################################################################################################################
label nikiheadpat:
    $ sessionpats = 0
    scene nikiheadpathub
    with fade

    ni "..."
    ni "What the fuck are you doing?"

    menu nikipatmenu1:
        "Pat":
            jump nikipatstart
        "Don't pat":
            "What should I do instead?"
            jump nikiinvmenu

label nikipatstart:
    scene nikipat1
    with dissolve
    $ sessionpats += 5
    $ nikipats += 5

    ni "..."
    ni "Really. {i}What the fuck are you doing?{/i}"

    menu nikipatmenu2:
        "Pat":
            jump nikipatting
        "Quit patting":
            "What should I do instead?"
            jump nikiinvmenu

label nikipatting:
    if sessionpats < 5:
        scene nikipat2 with dissolvepat
        scene nikipat1 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 5:
        scene nikipat2 with dissolvepat
        scene nikipat1 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Did my sister put you up to this? Because if I find out you're just fucking with me right now-"
        scene nikipat4 with dissolvepat
        scene nikipat3 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "You fucking-"
        ni "If you're looking for me to tell you to stop, it's not going to happen."
        ni "You're too busy pretending to have amnesia to {i}remember{/i}, but I've gotten {i}pretty fucking used to{/i} dealing with your shit over the years. This much is nothing to me."
        ni "So, go ahead- pat my head until you get fucking...friction burn or whatever. See if I care."
        jump nikipatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene nikipat4 with dissolvepat
        scene nikipat3 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 15:
        scene nikipat5 with dissolve
        ni "Since when are your hands even this big? No offense, but you weren't really the burliest of men back when we were teenagers."
        ni "Now they're like...I don't know. Hands are weird."
        scene nikipat4 with dissolvepat
        scene nikipat3 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Can you at least fucking explain yourself if you're going to try and annoy me like this?"
        ni "The not talking part is even worse than you repeatedly fucking up my hair."
        jump nikipatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene nikipat6 with dissolvepat
        scene nikipat7 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 25:
        scene nikipat6 with dissolvepat
        scene nikipat7 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "..."
        s "..."
        scene nikipat8 with dissolvepat
        ni "Why'd you stop?..."
        jump nikipatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene nikipat9 with dissolvepat
        scene nikipat10 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 50:
        scene nikipat9 with dissolvepat
        scene nikipat10 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "You can go a little harder if you want. Or faster or...something."
        ni "Doing it the same way over and over is fine for now, but it's only a matter of time until that novelty wears out."
        s "We'll see about that."
        ni "We will? What the fuck is that even supposed to mean?"
        jump nikipatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene nikipat11 with dissolvepat
        scene nikipat12 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 75:
        ni "You know...it probably sounds stupid since you're literally just doing this to annoy me...but this makes me feel...good."
        ni "Like...calm or whatever."
        ni "I don't want to say I'd given up on the idea of us ever being alone together again like this, but..."
        ni "Actually...I {i}did{/i} give up on that. I was so fucking mad at you for so...fucking long."
        scene nikipat11 with dissolvepat
        scene nikipat12 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Which is probably why it pisses me off so much that I'm kind of enjoying myself right now."
        ni "You're a dick and I hate you."
        ni "Keep going."
        jump nikipatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene nikipat11 with dissolvepat
        scene nikipat12 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 100:
        scene nikipat11 with dissolvepat
        scene nikipat13 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Kiss me."
        scene nikipat14 with dissolvepat
        scene nikipat13 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "I'm sorry, are you deaf now too? I said kiss me."
        scene nikipat15 with dissolvepat
        scene nikipat16 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Why aren't you fucking kissing me?!"
        jump nikipatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene nikipat17 with dissolvepat
        scene nikipat18 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 150:
        scene nikipat17 with dissolvepat
        scene nikipat19 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "There. You've done it. You've successfully annoyed me."
        ni "Now, can we call it a fucking night and actually {i}do{/i} something? Or would you rather stand there and torment your ex-girlfriend for the next several hours?"
        jump nikipatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene nikipat20 with dissolvepat
        scene nikipat21 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 200:
        ni "Jesus Christ. Where was all this attention when I was frantically trying to get you to come back to me, nearly killing myself in the process?"
        scene nikipat20 with dissolvepat
        scene nikipat21 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "You're just going to ignore that? Are you too focused on patting my head to be guilt tripped right now?"
        s "Did you say something? I couldn't hear you over the sound of me patting your head."
        scene nikipat22 with dissolvepat
        ni "Hmph. Whatever. Just don't go expecting any more spontaneous couch blowjobs if you keep this up for another minute or two."
        jump nikipatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene nikipat23 with dissolvepat
        scene nikipat22 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 250:
        scene nikipat23 with dissolvepat
        scene nikipat24 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Actually, on second thought, I'll give you whatever kind of {i}job{/i} you want right now if it means leaving my head alone. You're going to give me a fucking migraine at this rate."
        scene nikipat25 with dissolvepat
        scene nikipat26 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Fine. {i}Two{/i} jobs of your choice. Redeemable on any visit, so long as Ami or my sister isn't here."
        ni "Anything more than that and you're going to have to talk to my manager."
        scene nikipat25 with dissolvepat
        scene nikipat26 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Please don't actually talk to my manager about that. She'll look at me differently if she knows that guy I keep writing songs about routinely ejaculates in my mouth."
        jump nikipatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene nikipat27 with dissolvepat
        scene nikipat28 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 300:
        scene nikipat27 with dissolvepat
        scene nikipat28 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Uhh..."
        ni "I don't really have to tell you that I'm feeling a...certain kind of way right now, do I?"
        ni "Like...you should probably be able to pick up on that after all-"
        scene nikipat27 with dissolvepat
        scene nikipat29 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "I'm fucking wet, okay? Rub me somewhere that isn't going to give me brain damage."
        jump nikipatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene nikipat30 with dissolvepat
        scene nikipat31 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 350:
        scene nikipat30 with dissolvepat
        scene nikipat32 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Okay, seriously, though...{i}please{/i} just finger me or something before Ami comes home. You can go right back to...{i}this{/i} after."
        ni "I'm really not the type to beg, but...I'm starting to feel a little desperate at this point."
        "I look down to find that Niki is pressing her thighs tightly together, but she pulls them slowly apart once she notices my gaze travel away from her head."
        "Unfortunately for her, I have no interest in that sort of thing right now."
        "I have a job to do."
        scene nikipat33 with dissolvepat
        scene nikipat34 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Oh my fucking God, I can't believe you're actually doing this to me."
        jump nikipatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene nikipat33 with dissolvepat
        scene nikipat34 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 400:
        scene nikipat33 with dissolvepat
        scene nikipat35 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Would it by any chance persuade you if I told you I'm not wearing underwear today?"
        scene nikipat36 with dissolvepat
        scene nikipat37 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Jesus! Are you fucking gay now?! What is going on and why did that not work?!"
        jump nikipatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene nikipat39 with dissolvepat
        scene nikipat38 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 450:
        scene nikipat39 with dissolvepat
        scene nikipat38 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "I swear to fucking god that if you ever do this again, I'm buying your house and evicting you. I can do that because I have money."
        ni "I refuse to...just sit here and...have an orgasm from my head being rubbed!"
        scene nikipat39 with dissolvepat
        scene nikipat40 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Oh...but what I {i}can{/i} do is stare directly into your eyes and cum while flipping you off like the fucking {i}legend{/i} I am."
        ni "Go on, [nikimaster]. Keep patting my head."
        jump nikipatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene nikipat41 with dissolvepat
        scene nikipat40 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 475:
        scene nikipat43 with dissolvepat
        scene nikipat42 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Almost...there..."
        scene nikipat43 with dissolvepat
        scene nikipat42 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Just...gotta...keep my arm up!"
        ni "I'll never...forgive you for this!"
        jump nikipatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene nikipat44 with dissolvepat
        scene nikipat45 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        jump nikipatmenu2
    if sessionpats == 500:
        scene nikipat44 with dissolvepat
        scene nikipat45 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Oh, fuck...oh god..."
        scene nikipat44 with dissolvepat
        scene nikipat45 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        ni "Faster, baby...faster~"
        scene nikipat44 with dissolvepat
        scene nikipat45 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        scene nikipat44 with dissolvepat
        scene nikipat45 with dissolvepat
        $ sessionpats += 5
        $ nikipats += 5
        scene nikipat46 with hpunch
        $ sessionpats += 5
        $ nikipats += 5
        ni "Ahhhh!!!! AAaaahhhhh!!.......AAAAAAAAHhhhhhhhhh!!!~"

        "Niki's lower body quivers and convulses as she clumsily begins humping at the air to ride out the duration of her orgasm."

        scene nikipat47 with dissolve

        ni "..."
        s "..."
        s "You didn't keep your middle finger-"
        ni "I'm going home."

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ nikipatgasm = True

        "Embarrassed by cumming to the sensation of her ex-boyfriend rubbing her head, Niki Nakayama, the world famous idol, heads back to whatever hotel room she's staying in tonight."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    ##############################################################################################################################################################################
label mikuheadpat:
    $ sessionpats = 0
    scene mikuheadpathub
    with fade

    mi "Hm? Whatcha doin'?"
    mi "This some kinda new sex thingy? Do I gotta stand up too?"
    mi "Just be careful with my hair or Makoto'll yell at me for messin' it up."

    menu mikupatmenu1:
        "Pat":
            jump mikupatstart
        "Don't pat":
            "What should I do instead?"
            jump mikuinvmenu

label mikupatstart:
    scene mikupat1
    with dissolve
    $ sessionpats += 5
    $ mikupats += 5

    mi "Or don't. That's cool too. I can just fix it later."

    menu mikupatmenu2:
        "Pat":
            jump mikupatting
        "Quit patting":
            "What should I do instead?"
            jump mikuinvmenu

label mikupatting:
    if sessionpats < 5:
        scene mikupat2 with dissolvepat
        scene mikupat1 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 5:
        scene mikupat4 with dissolvepat
        scene mikupat3 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "You want me to take my headband off or somethin'?"
        mi "Startin' to think it might be gettin' in the way and I ain't really sure how much longer this is gonna go on for."
        scene mikupat4 with dissolvepat
        scene mikupat3 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Okay. I'll just leave it on and you can do whatever you want with it if it starts annoyin' you."
        jump mikupatmenu2
    if sessionpats > 5 and sessionpats < 15:
        scene mikupat4 with dissolvepat
        scene mikupat3 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 15:
        scene mikupat5 with dissolve
        mi "So, uhh...when's it my turn? When do I get to pat {i}your{/i} head?"
        mi "Or is that not how this works? Cause I'm startin' to feel a little, uhh...uncomfortable right now."
        mi "What with you not sayin' anything and all that-"
        scene mikupat6 with dissolvepat
        scene mikupat5x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Just...gonna ignore me? Should I shut up and just let ya do your thing? Gonna need a hand here, Sensei."
        mi "Like...one that ain't too busy messin' my hair up, I mean. Feel me?"
        "Oh, I feel her alright."
        "Her head, I mean."
        jump mikupatmenu2
    if sessionpats > 15 and sessionpats < 25:
        scene mikupat6 with dissolvepat
        scene mikupat5x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 25:
        scene mikupat8 with dissolvepat
        scene mikupat7 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Mind if I try takin' a nap or somethin'?"
        mi "I got practice in the mornin' and this is startin' to get kinda...uhh...how would Makoto say it? Mentally...faxing? Taxing? Waxing?"
        mi "It's gotta be one of those, right?"
        jump mikupatmenu2
    if sessionpats > 25 and sessionpats < 50:
        scene mikupat8 with dissolvepat
        scene mikupat7 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 50:
        scene mikupat8 with dissolvepat
        scene mikupat5 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Okay, the nap thing ain't gonna work. I tried, but this is just too heckin' weird to ignore."
        mi "How long we gonna do this for? Whaddya want outta me?"
        jump mikupatmenu2
    if sessionpats > 50 and sessionpats < 75:
        scene mikupat6 with dissolvepat
        scene mikupat5x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 75:
        scene mikupat9 with dissolve
        mi "Sensei, what the heck is goin' on?! Aint nobody good enough of a girl to get this many headpats in one sitting!"
        mi "If you're goin' for a world record or somethin' ya should at least tell me how many we've gotta beat so I can count!"
        scene mikupat10 with dissolvepat
        scene mikupat9 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "I don't like this side of you! This is weird!"
        jump mikupatmenu2
    if sessionpats > 75 and sessionpats < 100:
        scene mikupat10 with dissolvepat
        scene mikupat9 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 100:
        scene mikupat12 with dissolvepat
        scene mikupat11 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "That's it! I'm breakin' out Ami's special move!"
        mi "I know I ain't as cute as her and it's probably gonna have no effect on you, but it's worth a try!"
        mi "Miku-pout, engage!"
        scene mikupat12 with dissolvepat
        scene mikupat11 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Mm!"
        jump mikupatmenu2
    if sessionpats > 100 and sessionpats < 150:
        scene mikupat12 with dissolvepat
        scene mikupat11 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 150:
        scene mikupat14 with dissolvepat
        scene mikupat13 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Jeez...it's like ya don't even recognize how embarrassing this is for me."
        mi "Bet you're only doin' this cause of the dress, ain't ya? You'd never go this far for normal Miku."
        mi "Just...hurry up and set the record already before my heart starts freakin' out."
        jump mikupatmenu2
    if sessionpats > 150 and sessionpats < 200:
        scene mikupat14 with dissolvepat
        scene mikupat13 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 200:
        scene mikupat15 with dissolve
        mi "Come on! We barely ever get any alone time together and it's like you're wastin' what little we actually have on weird stuff right now!"
        scene mikupat16 with dissolvepat
        scene mikupat15x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Seriously, stop! Let's just friggin' make out or somethin'! I don't wanna do this anymore!"
        jump mikupatmenu2
    if sessionpats > 200 and sessionpats < 250:
        scene mikupat16 with dissolvepat
        scene mikupat15x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 250:
        scene mikupat17 with dissolve
        mi "Uhh...huh."
        mi "That's weird..."
        mi "I think...maybe talkin' about kissin' you started to make me, umm...you know..."
        scene mikupat18 with dissolvepat
        scene mikupat17 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "It's...uhh...gettin' kinda hot in here...ain't it?"
        jump mikupatmenu2
    if sessionpats > 250 and sessionpats < 300:
        scene mikupat18 with dissolvepat
        scene mikupat17 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 300:
        scene mikupat18 with dissolvepat
        scene mikupat17 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        scene mikupat19 with dissolve
        mi "I...I'm sorry. It's the...the heat."
        mi "I ain't actually horny or anything."
        mi "That would be, like...totally weird from just gettin' my head rubbed, right?"
        mi "Like...I like ya and all that, but...I ain't a {i}Miyamura.{/i} It takes more to get me...you know."
        mi "Or at least...it should? Am I unlockin' some kinda...fetish or somethin'?"
        jump mikupatmenu2
    if sessionpats > 300 and sessionpats < 350:
        scene mikupat20 with dissolvepat
        scene mikupat19x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 350:
        scene mikupat21 with dissolve
        mi "Uhhhhhhh...yeah. Remember that thing I said a minute ago about how it takes more than this to get me goin'?"
        mi "I lied. Or...well, it wasn't a lie. But like, I was wrong. Cause I totally wanna do sexy stuff right now."
        mi "So...you know, if you wanna maybe do somethin' like that instead that would be cool. We can set the headpat world record some other time."
        scene mikupat22 with dissolvepat
        scene mikupat21 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Ooooooh man...This ain't gonna end well, Sensei."
        jump mikupatmenu2
    if sessionpats > 350 and sessionpats < 400:
        scene mikupat22x with dissolvepat
        scene mikupat21x with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 400:
        scene mikupat23 with dissolve
        mi "Why are ya teasin' me like this? What'd I ever do to you?"
        mi "I ain't even sure there {i}is{/i} a world record anymore. I kinda think you're just messin' with me."
        scene mikupat24 with dissolvepat
        scene mikupat23 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "I got feelings, you know?...What would {i}you{/i} think if I just led ya on like this one day?"
        "I would think that I am happy someone loves me enough to pat my head 400 times."
        jump mikupatmenu2
    if sessionpats > 400 and sessionpats < 450:
        scene mikupat26 with dissolvepat
        scene mikupat25 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 450:
        scene mikupat28 with dissolvepat
        scene mikupat27 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "I seriously can't take much more of this, ya know."
        mi "Just...touch somewhere else and put me outta my misery already. Let me walk outta here today with some dignity left."
        scene mikupat28 with dissolvepat
        scene mikupat27 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Come on...I'm wearin' a dress for easy access and everythin'. I did this for you!"
        jump mikupatmenu2
    if sessionpats > 450 and sessionpats < 475:
        scene mikupat28 with dissolvepat
        scene mikupat27 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 475:
        scene mikupat29 with dissolve
        mi "Oh...gosh...oh man..."
        mi "This...mm...really wasn't worth the effort, Sensei...If ya seriously wanted to make me melt, ya coulda just done...mmf...what ya always do..."
        scene mikupat30 with dissolvepat
        scene mikupat29 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Hngh..."
        mi "I guess...this way does kind of...have its own set of benefits, though...hah!"
        jump mikupatmenu2
    if sessionpats > 475 and sessionpats < 500:
        scene mikupat30 with dissolvepat
        scene mikupat29 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        jump mikupatmenu2
    if sessionpats == 500:
        scene mikupat30 with dissolvepat
        scene mikupat29 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        mi "Oh frick...oh no..."
        mi "It's happenin'...the last...hah...shred of...Miku Maruyama's dignity!"
        scene mikupat30 with dissolvepat
        scene mikupat29 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        scene mikupat30 with dissolvepat
        scene mikupat29 with dissolvepat
        $ sessionpats += 5
        $ mikupats += 5
        scene mikupat31 with hpunch
        $ sessionpats += 5
        $ mikupats += 5
        mi "Hah...hah......aaaaah!"

        "Something strange happens to Miku that I am unable to discern because I am too busy patting her head."

        scene mikupat32 with dissolve

        mi "Oh man...oh heck..."
        mi "I kinda expected...havin' one of those today, but...I feel like ya took the...most difficult possible path there, Sensei..."
        s "Path where? What happened?"

        scene black
        with dissolve2
        stop music fadeout 10.0
        $ mikupatgasm = True

        mi "{i}What happened?!{/i}"
        mi "Were you payin' any attention at all to anythin' that just happened to me?!"
        s "Let's go again."
        mi "Noooo! Free Miku!"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat
