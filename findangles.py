import math


def find_angle(previous_blind, blind):
    x1 = int(previous_blind[0])
    x2 = int(blind[0])
    z1 = int(previous_blind[1])
    z2 = int(blind[1])
    opposite = x1-x2
    adjacent = z1-z2
    ref_angle = abs(math.degrees(math.atan(opposite/adjacent)))
    if opposite>=0 and adjacent>=0:
        actual_angle = 180 - ref_angle
    elif opposite<0 and adjacent<0:
        actual_angle = 0 - ref_angle
    elif opposite<0 and adjacent>=0:
        actual_angle = ref_angle - 180
    else:
        actual_angle = ref_angle
    actual_angle = round(actual_angle, 2)
    return actual_angle



angles_list = []

f_angles = open("angles.txt", "w")
f_coords = open("coords.txt", "r")
contents = f_coords.readlines()

for i in range(128):
    if i == 127:
        break
    previous_blind = (contents[i]).split()
    blind = (contents[i+1]).split()
    angles_list.append(str(find_angle(previous_blind, blind)) + "\n")

for i in range(len(angles_list)):
    angles_list[i] = f'Stronghold {i+2}: {angles_list[i]}'


for i in range(len(angles_list)):
     f_angles.write(angles_list[i])

f_angles.close()
f_coords.close()


