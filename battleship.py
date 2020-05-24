from typing import Tuple

class Solution:
    def solution(self, N: int, S: str, T: str) -> str:
        ships = S.split(',')
        hits = T.split(' ')

        ship_hits_dict = {}
        for hit in hits:
            for ship in ships:
                if self.hit_ship(hit, ship):
                    ship_hits_dict[ship] = ship_hits_dict.get(ship, 0) + 1
                    break

        sunk_count, hit_count = 0, 0
        for ship in ships:
            if ship not in ship_hits_dict: continue
            if ship_hits_dict[ship] == self.ship_size(ship):
                sunk_count += 1
            else:
                hit_count += 1

        return str(sunk_count) + ',' + str(hit_count)

    def get_row_column(self, description: str) -> Tuple[int, int]:
        row_str, column_str = description[:-1], description[-1]
        row_num = int(row_str)
        column_num = ord(column_str) - ord('A') + 1
        return (row_num, column_num)

    def ship_size(self, description: str) -> int:
        top_left, bottom_right = description.split(' ')
        tl_row, tl_col = self.get_row_column(top_left)
        br_row, br_col = self.get_row_column(bottom_right)
        size = (br_row - tl_row) * (br_col - tl_col)
        return size

    def hit_ship(self, hit_cell: str, ship: str) -> bool:
        ship_tl, ship_br = ship.split(' ')
        ship_tl_row, ship_tl_col = self.get_row_column(ship_tl)
        ship_br_row, ship_br_col = self.get_row_column(ship_br)
        cell_row, cell_col = self.get_row_column(hit_cell)
        return ship_tl_row <= cell_row <= ship_br_row and ship_tl_col <= cell_col <= ship_br_col

input = {
    'N': 4,
    'S': '1B 2C,2D 4D',
    'T': '2B 2D 3D 4D 4A'
}
output = Solution().solution(**input)
assert output == '1,1'

input = {
    'N': 3,
    'S': '1A 1B,2C 2C',
    'T': '1B'
}
output = Solution().solution(**input)
assert output == '0,1'

input = {
    'N': 12,
    'S': '1A 2A,12A 12A',
    'T': '12A'
}
output = Solution().solution(**input)
assert output == '0,1'
