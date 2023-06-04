import math

areas = [(5, 31), (6, 67), (7, 116), (8, 208), (9, 315), (10, 483), (11, 670), (12, 958)]

perimeters = []
circle_areas = []
grid_areas = []
unit_area = math.sqrt(3)/4
for n in range(5, 13):
    P = n*(n+1)//2
    perimeters.append((n, n*(n+1)//2))
    circle_areas.append((n, round(P*P/(4*math.pi*unit_area), 1)))
    grid_areas.append((n, round(P*P*math.pi/(48*unit_area), 1)))

print('areas =   {}'.format(areas))
print('perimeters = {}'.format(perimeters))
print('circle_areas = {}'.format(circle_areas))
print('grid_areas = {}'.format(grid_areas))

print("| $n$      | Laukums | Perimetrs  | Riņķa laukums | \"Režģa riņķa\" laukums |")
print("| -------- | ------- | ---------- | ------------- | --------------------- |")

for n in range(5, 13):
    area = next(v for k, v in areas if k == n)
    perimeter = next(v for k, v in perimeters if k == n)
    circle_area = next(v for k, v in circle_areas if k == n)
    grid_area = next(v for k, v in grid_areas if k == n)
    print(f"| {n}        | {area}      | {perimeter}        | {circle_area}          | {grid_area}                  |")

# | $n$      | Laukums | Perimetrs  | Riņķa laukums | "Režģa riņķa" laukums |
# | -------- | ------- | ---------- | ------------- | --------------------- |
# | 5        | 31      | 15         | 41.3          | 34.0                  |
# | 6        | 2       | 21         | 81.0          | 66.7                  |


