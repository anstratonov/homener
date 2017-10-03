from urwid import MainLoop, SolidFill, Filler, Pile, Overlay, LineBox

interior = Filler(Pile([]))

window = LineBox(interior, title='Choose enviroment')
background = SolidFill(' ')

body = Overlay(
    window,
    background,
    'center', 30, 'middle', 10
)

main_loop = MainLoop(body)
main_loop.run()
