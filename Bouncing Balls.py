def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while h * bounce > window:
        h = h * bounce
        count += 2
    if h == window:
        count += 1

    return count
print(bouncing_ball(4, 0.25, 1))