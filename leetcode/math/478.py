import math
import random
from typing import List

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        theta = 2 * math.pi * random.random()
        r = self.radius * math.sqrt(random.random())
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]
