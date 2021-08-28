# The game starts here.

label start:
    stop music fadeout 1.0
    call screen check_age
    show screen watermark
    return
