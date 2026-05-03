from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
min_width, seg_min_width, parallel_lines = p.min_width()

print(f'min_width={min_width},')
print(f'seg_min_width={seg_min_width},')
print(f'parallel_lines={parallel_lines}')

