
def solution(AX: int, AY: int, BX: int, BY:int) -> str:
    delta_x_AB = BX - AX
    delta_y_AB = BY - AY

    if delta_y_AB == 0:
        dx = 0
    elif delta_y_AB > 0:
        dx = 1
    elif delta_y_AB < 0:
        dx = -1

    if delta_x_AB == 0:
        dy = 0
    elif delta_x_AB > 0:
        dy = -1
    elif delta_x_AB < 0:
        dy = 1

    delta_x_BC = dx
    delta_y_BC = dy

    def calculate():
        return delta_x_BC * delta_x_AB + delta_y_BC * delta_y_AB

    def next_x():
        nonlocal delta_x_BC
        delta_x_BC += dx

    def next_y():
        nonlocal delta_y_BC
        delta_y_BC += dy

    increase = next_x if dx * delta_x_AB > 0 else next_y
    decrease = next_x if dx * delta_x_AB < 0 else next_y

    while True:
        res = calculate()
        if res == 0:
            x = BX + delta_x_BC
            y = BY + delta_y_BC
            return str(x) + ',' + str(y)
        elif res > 0:
            decrease()
        elif res < 0:
            increase()

input = {
    'AX': -1,
    'AY': 3,
    'BX': 3,
    'BY': 1
}
output = solution(**input)
assert output == '2,-1'
