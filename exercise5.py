def md_nre_single_sample(y, y_hat, n, p):
    root_y = y ** (1 / n)
    root_y_hat = y_hat ** (1 / n)
    difference = abs(root_y - root_y_hat) ** p
    return difference