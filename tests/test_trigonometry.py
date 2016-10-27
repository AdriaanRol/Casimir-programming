
import numpy as np
from unittest import TestCase

from trigonometry import circles


class TestCircles(TestCase):
    def test_circumferences(self):
        r = 2
        per = circles.circumference(r)
        self.assertEqual(per, 2*np.pi*r)

    def test_surface(self):
        r = 2
        per = circles.surface(r)
        self.assertEqual(per, np.pi*r*2)
