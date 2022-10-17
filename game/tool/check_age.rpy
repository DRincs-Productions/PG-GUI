define pegi_18 = "/interface/pegi_18.webp"
define button_no_idle = "/interface/button-no.webp"
define button_yes_idle = "/interface/button-yes.webp"

transform check_age_button:
    xsize 360
    ysize 80
    on selected_idle:
        yanchor 0 matrixcolor BrightnessMatrix(-0.3)
    on idle:
        yanchor 0 matrixcolor BrightnessMatrix(0)
    on hover:
        yanchor 1 matrixcolor BrightnessMatrix(0.3)
    on selected_hover:
        yanchor 1 matrixcolor BrightnessMatrix(-0.5)
    on insensitive:
        yanchor 0 matrixcolor BrightnessMatrix(-0.8)
    on action:
        yanchor 0 matrixcolor BrightnessMatrix(-0.5)

screen check_age():
    add Frame(pegi_18, xfill=True, yfill=True)
    hbox:
        xalign 0.5
        yalign 0.93
        spacing 70
        imagebutton:
            idle Frame(button_yes_idle, xfill=True, yfill=True)
            action Return()
            at check_age_button
        imagebutton:
            idle Frame(button_no_idle, xfill=True, yfill=True)
            action MainMenu(confirm=False)
            at check_age_button
