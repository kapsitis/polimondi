from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
inertia_tensor = p.get_inertia_tensor()
print(f'inertia_tensor={inertia_tensor}')
