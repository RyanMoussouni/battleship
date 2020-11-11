#%%
from context import Ship
import unittest
import numpy.random as rd
import pdb

class TestIsSunk(unittest.TestCase):
    def setUp(self):
        # -- CHANGE the parameters of the ship HERE.
        length = 5
        orientation = 0
        prow = (0,0)
        random = True

        # -- Randomization for a single ship (optionnal)
        if random:
            length = rd.choice([3,5])
            orientation = rd.randint(2)
            prow = (max(rd.randint(10)-length*orientation,0), max(rd.randint(10)-length*(1-orientation),0))
        
        # -- Ship definition
        self.ship = Ship(length = length, orientation = orientation, prow = prow)
        pass
    def test_hit_all_ship_cells(self):
        hits = self.ship.position
        self.assertTrue(self.ship.is_sunk(hits= hits))
        pass
    def test_hit_only_part_ship_cells(self):
        position = list(self.ship.position)
        hits = {position[0], position[2]}
        self.assertFalse(self.ship.is_sunk(hits= hits))
        pass
    def test_hit_part_ship_cells(self):
        position = list(self.ship.position)
        hits = {position[0], position[2]}
        for i in range(10):
            rdCell = (rd.randint(10),rd.randint(10))
            if rdCell not in position:
                hits.add(rdCell)
        self.assertFalse(self.ship.is_sunk(hits= hits))
        pass
    def test_hit_no_cells(self):
        hits = {}
        self.assertFalse(self.ship.is_sunk(hits= hits))
        pass

class TestSurrArea(unittest.TestCase):
    def setUp(self):
        # -- CHANGE the parameters of the ship HERE.
        self.orientation = 0
        self.length = 5
        pass
    def test_top_left_corner(self):
        length = self.length
        orientation = self.orientation
        prow = (9-(length-1)*orientation,0)
        ship = Ship(length = length, orientation = orientation, prow = prow)
        if orientation:
            surrArea = { (9 - k, 1) for k in range(length+1)}.union({(10 - (length + 1), 0)})
            self.assertEqual(ship.surrArea, surrArea)
        else:
            surrArea = { (8 , k) for k in range(length+1)}.union({(9, length)})
            self.assertEqual(ship.surrArea, surrArea)
        pass
    def test_bottom_left_corner(self):
        length = self.length
        orientation = self.orientation
        prow = (0,0)
        ship = Ship(length = length, orientation = orientation, prow = prow)
        if orientation:
            surrArea = { (k, 1) for k in range(length+1)}.union({(length, 0)})
            self.assertEqual(ship.surrArea, surrArea)
        else:
            surrArea = { (1 , k) for k in range(length+1)}.union({(0, length)})
            self.assertEqual(ship.surrArea, surrArea)
        pass
    def test_bottom_right_corner(self):
        length = self.length
        orientation = self.orientation
        prow = (0,9 -(length-1)*(1-orientation))
        ship = Ship(length = length, orientation = orientation, prow = prow)
        if orientation:
            surrArea = { (k, 8) for k in range(length+1)}.union({(length, 9)})
            self.assertEqual(ship.surrArea, surrArea)
        else:
            surrArea = { (1 , 9 - k) for k in range(length+1)}.union({(0,10 - (length+1))})
            self.assertEqual(ship.surrArea, surrArea)
        pass
    def test_top_right_corner(self):
        length = self.length
        orientation = self.orientation
        prow = (9-(length-1)*orientation,9-(length-1)*(1-orientation))
        ship = Ship(length = length, orientation = orientation, prow = prow)
        if orientation:
            surrArea = { (9 - k, 8) for k in range(length+1)}.union({(10 - (length+1), 9)})
            self.assertEqual(ship.surrArea, surrArea)
        else:
            surrArea = { (8 , 9 - k) for k in range(length+1)}.union({(9,10 - (length+1))})
            self.assertEqual(ship.surrArea, surrArea)
        pass
    def test_left_side(self):
        pass
    def test_right_side(self):
        pass
    def test_bottom_side(self):
        pass
    def test_upper_side(self):
        pass
class TestPosition(unittest.TestCase):
    def setUp(self):
        pass
    def test_valid_position(self):
        orientation = 0 #horizontal
        length = 5 
        prow = (2,3)
        ship = Ship(length= length,orientation= orientation,prow = prow)
        expPosition = {(2,3),(2,4),(2,5),(2,6),(2,7)}
        self.assertEqual(ship.position,expPosition)
        pass
    def test_invalid_position(self):
        



if __name__ == '__main__':
    unittest.main()