
define r = Character("Ms. Rose", color="#d040cc")
define m = Character("Magnus", color="#3152cd")
define s = Character("Sarah", color="#c4333e")
define u = Character("?", color="#606060")

image bg placeholder = Tile("backgrounds/placeholder.png")
image bg black = Tile("backgrounds/black.png")

image location_text = ParameterizedText(size=50, color="#ebebeb")

label start:

    scene bg black

    python:
        name = renpy.input("What's your name ? (Default is Lucas) :")
        name = name.strip() or "Lucas"
    define p = Character("[name]", color="#25b87a")

    show location_text "Friday - Guidance Counselor Office - College" at truecenter
    with dissolve
    pause 2
    hide location_text
    with dissolve
    scene bg placeholder with dissolve

    r "So... [name] is it ? I'm Ms. Rose, and as you've probably seen on the door, I'm your guidance counselor."
    r "I see here that you're not doing well at school. Not well at all actually... why is that ?"
    p "Hum... I don't really know... I'm not really interested in studying I guess..."
    r "I understand... But you see, due to your grades, the director asked me to find a more suitable establishment for you."
    p "A... A more suitable establishment ? I'm..I need to switch school again ?"
    r "Yes, [name]... And before we find you a more suitable school, we will have to do a physical check on you..."
    p "A physical check ?"
    r "Don't worry, it's nothing much, you just have to undress and I will take your mensurations. It will be useful when it comes to sports school for exemple."
    p "Yeah, sure.."
    "I start undressing to only my boxer"
    r "You need to take that off aswell, [name]."
    p "I-I see.."
    "I take off my boxer"
    "She looks at me up and down for some times before smirking.. She then begins to take some measurements on my body using a tape measure."
    "After some times, she gently grabs my penis. I push her hand back."
    p "H-hey !"
    r "Calm down [name], it's part of the examination..."
    p "I.. I don't see why this measure would be useful."
    r "How would I know ? They ask me for it in the register files.. Probably to check if it won't be annoying when you run.."
    p "Hm.. Makes sense I suppose.."
    "She puts her hand back on my penis and measures it.."
    r "So... 1... 1.9 inches, which makes around 5 centimers.. And we're finished with the examination, you can put your clothes back on."
    "I get dressed as fast as I can"
    r "..."
    r "I think I have the perfect school for you, [name] !"
    p "D-do you ?"
    r "I will send you the address tommorow, you will start there on Monday.."
    p "Ok.. Should I prepare something to go there ? Some notebooks maybe ?"
    r "Oh, don't worry about it [name], the director is an old friend of mine, he will take care of it."
    p "Oh.. Okay. Thank you then.."
    r "I just did my job, don't worry about it ! I pray for you to be successful !"
    "I leave the office while she's looking at me, smirking... What a strange woman.."

    scene bg black with dissolve
    show location_text "Monday - Director's Office - ??? Academy" at truecenter
    with dissolve
    pause 2
    hide location_text
    with dissolve
    scene bg placeholder with dissolve




    return
