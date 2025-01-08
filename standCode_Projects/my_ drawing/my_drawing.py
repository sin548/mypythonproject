"""
File: my_drawing.py
Name: 李安哲
----------------------
Title: My zodiac sign
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My zodiac sign

    Is this a cat? or a bear? or maybe a lion?
    """
    window = GWindow(width=700, height=600, title='My zodiac sign')
    circle1 = GOval(200, 200, x=60, y=120)
    circle1.filled = True
    circle1.fill_color = "brown"
    circle1.color = "brown"
    window.add(circle1)
    circle2 = GOval(200, 200, x=175, y=10)
    circle2.filled = True
    circle2.fill_color = "brown"
    circle2.color = "brown"
    window.add(circle2)
    circle3 = GOval(200, 200, x=325, y=10)
    circle3.filled = True
    circle3.fill_color = "brown"
    circle3.color = "brown"
    window.add(circle3)
    circle4 = GOval(200, 200, x=430, y=120)
    circle4.filled = True
    circle4.fill_color = "brown"
    circle4.color = "brown"
    window.add(circle4)
    circle5 = GOval(200, 200, x=60, y=250)
    circle5.filled = True
    circle5.fill_color = "brown"
    circle5.color = "brown"
    window.add(circle5)
    circle6 = GOval(200, 200, x=430, y=250)
    circle6.filled = True
    circle6.fill_color = "brown"
    circle6.color = "brown"
    window.add(circle6)
    circle7 = GOval(200, 200, x=175, y=350)
    circle7.filled = True
    circle7.fill_color = "brown"
    circle7.color = "brown"
    window.add(circle7)
    circle8 = GOval(200, 200, x=325, y=350)
    circle8.filled = True
    circle8.fill_color = "brown"
    circle8.color = "brown"
    window.add(circle8)
    ear1 = GPolygon()
    ear1.add_vertex((90, 100))
    ear1.add_vertex((190, 110))
    ear1.add_vertex((140, 190))
    ear1.filled = True
    ear1.fill_color = "orange"
    ear1.color = "orange"
    window.add(ear1)
    ear2 = GPolygon()
    ear2.add_vertex((610, 100))
    ear2.add_vertex((510, 110))
    ear2.add_vertex((560, 190))
    ear2.filled = True
    ear2.fill_color = "orange"
    ear2.color = "orange"
    window.add(ear2)
    ear3 = GPolygon()
    ear3.add_vertex((110, 110))
    ear3.add_vertex((160, 120))
    ear3.add_vertex((140, 150))
    ear3.filled = True
    ear3.fill_color = "peachpuff"
    ear3.color = "peachpuff"
    window.add(ear3)
    ear4 = GPolygon()
    ear4.add_vertex((590, 110))
    ear4.add_vertex((540, 120))
    ear4.add_vertex((560, 150))
    ear4.filled = True
    ear4.fill_color = "peachpuff"
    ear4.color = "peachpuff"
    window.add(ear4)
    head = GOval(400, 400, x=150, y=80)
    head.filled = True
    head.fill_color = "orange"
    head.color = "orange"
    window.add(head)
    eye1 = GOval(65, 65, x=210, y=200)
    eye1.filled = True
    window.add(eye1)
    eye2 = GOval(65, 65, x=430, y=200)
    eye2.filled = True
    window.add(eye2)
    pupil1 = GOval(20, 20, x=245, y=215)
    pupil1.filled = True
    pupil1.fill_color = "white"
    pupil1.color = "white"
    window.add(pupil1)
    pupil2 = GOval(20, 20, x=465, y=215)
    pupil2.filled = True
    pupil2.fill_color = "white"
    pupil2.color = "white"
    window.add(pupil2)
    mouse = GOval(200, 170, x=window.width//2-100, y=295)
    mouse.filled = True
    mouse.fill_color = "white"
    mouse.color = "white"
    window.add(mouse)
    nose1 = GArc(100, 200, 330, 240, x=300, y=220)
    nose1.filled = True
    nose1.color = "peachpuff"
    nose1.fill_color = "peachpuff"
    window.add(nose1)
    nose2 = GOval(100, 50, x=300, y=293)
    nose2.filled = True
    nose2.color = "maroon"
    nose2.fill_color = "maroon"
    window.add(nose2)
    mouse1 = GArc(50, 300, 110, 75, x=345, y=335)
    mouse1.color = "maroon"
    window.add(mouse1)
    mouse2 = GArc(80, 50, 140, 270, x=310, y=375)
    mouse2.color = "maroon"
    window.add(mouse2)


if __name__ == '__main__':
    main()
