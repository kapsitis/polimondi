from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
hex_bounds = p.get_hex_bounds()
print(f'hex_bounds={hex_bounds}')
h_ns = hex_bounds[1] - hex_bounds[0]
h_nw_se = hex_bounds[3] - hex_bounds[2]
h_ne_sw = hex_bounds[5] - hex_bounds[4]
print(f'h_ns={h_ns}, h_nw_se={h_nw_se}, h_ne_sw={h_ne_sw}')
hex_area = p.get_bounding_hexagon().get_area()
print(f'hex_area={hex_area}')

# hex_bounds=(-29, 112, -159, 10, -38, 113)
# h_ns=141, h_nw_se=169, h_ne_sw=151
# hex_area=25617