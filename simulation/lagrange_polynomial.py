def lagrange_basis(x, excluding_index, x_list):
    excluded_x = x_list[excluding_index]
    output_polynomial = 1
    for i in range(len(x_list)):
        if i != excluding_index:
            output_polynomial = output_polynomial * (x - x_list[i])/(excluded_x - x_list[i])
    return output_polynomial


def lagrange_polynomial(x, x_list, y_list):
    lagrange_value = 0
    for i in range(len(x_list)):
        lagrange_value += y_list[i] * lagrange_basis(x, i, x_list)
    return lagrange_value


x_list = [0,1,2]
y_list = [0,1,4]
print(lagrange_polynomial(3, x_list, y_list))
