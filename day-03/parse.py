import re

class FabricBoard:
    def __init__(self):
        self.board = {}

    def add_sq(self, x, y):
        key = f"{x}:{y}"
        if key in self.board:
            self.board[key] += 1
        else:
            self.board[key] = 1

    def add_claim(self, claim):
        for h in range(claim.height):
            for w in range(claim.width):
                self.add_sq(claim.nleft + w + 1, claim.ntop + h + 1)

    def rm_sq(self, x, y):
        key = f"{x}:{y}"
        self.board[key] -= 1

    def rm_claim(self, claim):
        for h in range(claim.height):
            for w in range(claim.width):
                self.rm_sq(claim.nleft + w + 1, claim.ntop + h + 1)

    def get_overlapping_squares(self):
        count = 0
        for k, v in self.board.items():
            if v > 1:
                count += 1
        return count

    def check_empty(self, claim):
        for h in range(claim.height):
            for w in range(claim.width):
                x, y = claim.nleft + w + 1, claim.ntop + h + 1
                key = f"{x}:{y}"
                if self.board.get(key, 0) != 0:
                    return False
        return True

class Claim:
    def __init__(self, claim_txt):
        rx = re.compile("[0-9]+")
        claim_id, nleft, ntop, width, height = rx.findall(claim_txt)
        self.claim_id = claim_id
        self.nleft = int(nleft)
        self.ntop = int(ntop)
        self.width = int(width)
        self.height = int(height)
