class Ship:
    def __init__(self, length:int, orientation:bool, prow:tuple):
        '''
        Description.
            a ship is defined by:
                - its length
                - its orientation (0 horizontal, 1 vertical)
                - its front cell (or prow, "proue" en français) in the form (y-axis value, x-axis value).
        Notes.
            - for the computations, cell positions are tuple of the form (y-axis value, x-axis value).
            - we use sets to store the different cell positions as they are useful to compute intersections, unions, ...
        '''
        self.length = length
        self.orientation = orientation
        self.prow = prow
        self.set_position()
        self.set_surrArea()
        pass
    def __str__(self)->str:
        orToStr = dict({0 : 'Horizontal', 1 : 'Vertical'})
        return '{} ship of length {} and prow {}'.format(orToStr[self.orientation], self.length, self.prow)
    def set_position(self):
        prow = self.prow
        length = self.length
        orientation = self.orientation

        # -- values check
        if orientation not in {0,1}:
            raise ValueError("orientation must be either 0 or 1")
        if length not in {2,3,4,5}:
            raise ValueError("length should be an int in [2,5]")
        if prow[0] not in {k for k in range(10)} or prow[1] not in {k for k in range(10)}:
            raise ValueError("prow should be in the grid")

        # -- position set
        self.position = {(prow[0]+orientation*k, prow[1]+(1-orientation)*k) for k in range(length)}
        pass
    def set_surrArea(self):
        '''
        Description.
            finds the cells that surround the ship. They are represented by the crosses below.
                x x x x x x
                x s h i p x
                x x x x x x
        Implementation.
            errors can happen if the ship is close to a border, so we check the surroundings beforehand.
        '''
        # -- getting position of the ship
        position = self.position
        surrCells = set()
        # -- checking surroundings; left indicates if the cells at the left of ship exist in the grid. Same for up, down and right
        left, right, up, down = (True, True, True, True)
        for y,x in position:
            if x <= 0:
                left = False
            if x >= 9:
                right = False
            if y <= 0:
                down = False
            if y >= 9:
                up = False
        # -- getting surrounding cells together with ship cells
        for y,x in position:
            surrCells.add((y,x))
            if left:
                surrCells.add((y,x-1))
            if right:
                surrCells.add((y,x+1))
            if up:
                surrCells.add((y+1,x))
            if down:
                surrCells.add((y-1,x))
            if up and right:
                surrCells.add((y+1,x+1))
            if down and right:
                surrCells.add((y-1,x+1))
            if up and left:
                surrCells.add((y+1,x-1))
            if down and left:
                surrCells.add((y-1,x-1))
        self.surrArea = surrCells.difference(position) # keeping only surrounding cells
        pass
    def is_sunk(self, hits:set)->bool:
        '''tells if the hits can sink the ship'''
        if self.position.issubset(hits):
            return True



if __name__ == "__main__":
    ship = Ship(3,1,(5,4))
    print(ship.__str__())