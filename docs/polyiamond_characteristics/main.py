from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
(a60, a120, a240, a300) = p.internal_angles()
print(f'(a60, a120, a240, a300) = ({a60}, {a120}, {a240}, {a300})')
(acute, obtuse) = (a60 + a300, a120 + a240)
print(f'(acute, obtuse) = ({acute}, {obtuse})')

