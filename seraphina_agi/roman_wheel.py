import hashlib
import math
from typing import List, Dict, Any, Optional

class SimpleOcto:
    def __init__(self, coeffs: Optional[List[float]] = None):
        self.coeffs = (coeffs or [])[:8] + [0.0] * 8
        self.coeffs = self.coeffs[:8]

    def norm(self) -> float:
        return math.sqrt(sum(c * c for c in self.coeffs))

    def multiply(self, o: 'SimpleOcto') -> 'SimpleOcto':
        prod = [0.0] * 8
        prod[0] = self.coeffs[0] * o.coeffs[0] - sum(self.coeffs[i+1] * o.coeffs[i+1] for i in range(7))
        for i in range(1, 8):
            prod[i] = self.coeffs[0] * o.coeffs[i] + o.coeffs[0] * self.coeffs[i]
        return SimpleOcto(prod)

    def power(self, d: int = 2) -> 'SimpleOcto':
        if d == 2:
            return self.multiply(self)
        return self

class RomanDecoderWheel:
    def __init__(self, plane: str = 'xy', freq: float = 432.0, hue: float = 600.0):
        self.plane = plane
        self.freq = freq
        self.hue = hue
        self.theta = 0.0
        self.r = hue / 1000.0

    def decode_data(self, hex_str: str) -> str:
        self.theta += 2 * math.pi * (self.freq / 432.0) / 8
        spiral_r = self.r * (math.cos(8 * self.theta) + 1.5) / 2.5
        decoded = []
        for i in range(0, len(hex_str), 8):
            chunk = hex_str[i:i+8]
            oct_coeffs = [0] * 8
            for j, c in enumerate(chunk):
                try:
                    oct_coeffs[j % 8] += int(c, 16)
                except ValueError:
                    pass
            n = SimpleOcto(oct_coeffs).norm() * spiral_r
            if n <= 2:
                decoded.append(chunk)
        return ''.join(decoded)