import numpy as np

wheel_angle = 35 / 180 * np.pi

wheel_angles = np.zeros(3)
wheel_vectors = [np.array([np.sin(wheel_angle) * np.cos(phi), np.sin(wheel_angle) * np.sin(phi), -np.cos(wheel_angle)]) for phi in [0., 2.*np.pi/3, 4.*np.pi/3]]
wheel_normal_vectors = list(map(lambda x : x / np.linalg.norm(x), [np.array([np.cos(wheel_angle) * np.cos(phi), np.cos(wheel_angle) * np.sin(phi), np.sin(wheel_angle)]) for phi in [0., 2.*np.pi/3, 4.*np.pi/3]]))
wheel_direction_vectors = list(map(lambda x : x / np.linalg.norm(x), [np.cross(v,n) for v,n in zip(wheel_vectors, wheel_normal_vectors)]))
coeff_matrix = np.row_stack([np.cross(v,d).flatten() for v,d in zip(wheel_vectors, wheel_direction_vectors)])
coeff_matrix = coeff_matrix @ np.diag([-1,1,-1])

# print("Coefficient matrix to be used in the orb's code:")
# print(coeff_matrix)

print("const double coeffs[3][3] = {")
print("    {{{:12s}, {:12s}, {:12s}}},".format(*map(str, np.round(coeff_matrix[0], 8))))
print("    {{{:12s}, {:12s}, {:12s}}},".format(*map(str, np.round(coeff_matrix[1], 8))))
print("    {{{:12s}, {:12s}, {:12s}}}".format(*map(str, np.round(coeff_matrix[2], 8))))
print("};")
