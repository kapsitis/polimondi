from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
inertia_tensor = p.get_inertia_tensor()
print(f'inertia_tensor={inertia_tensor}')
lambdas = p.get_inertia_eigenvalues()
print(f'lambda1={lambdas[0]}, lambda2={lambdas[1]}')
print(f'I_z={p.get_polar_inertia_moment()}')
print(f'FA={p.get_fractional_anisotropy()}')
