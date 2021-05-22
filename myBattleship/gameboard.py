#%% Modules
import numpy as np
import numpy.random as rd
from ship import Ship

#%% Gameboard class
class Gameboard:
    def __init__(self):
        self.grid = np.zeros((10,10),dtype=bool)
        self.ships = []
        self.sunkShips = []
        self.hits = set()
        self.gameOver = False

        self.add_random_ship(5)
        self.add_random_ship(5)
        self.add_random_ship(3)
        self.add_random_ship(3)
        pass

    def add_ship(self, ship: Ship)->None:
        '''if possible, adds a ship to the grid'''
        grid = self.grid

        if ship.prow in self._possible_cells(ship.length, ship.orientation):
            try:
                for idx in ship.position:
                    grid[idx] = True
            except IndexError:
                print("Error")
                print("{} doesn't fit in the grid".format(ship.__str__()))
            except:
                print("Unexpected Error happened while adding {}".format(ship.__str__()))
                raise

            self.grid = grid
            self.ships.append(ship)
        else:
            raise Exception("{} cannot be put in the grid".format(ship.__str__()))
        pass
    
    def add_random_ship(self, length:int)-> None:
        ''' adds a ship of random prow & orientation to the gameboard'''
        # -- randomizing the ship
        orientation = rd.randint(2)
        possibleCells = self._possible_cells(length, orientation)
        # taking random possible cell as a prow
        if len(possibleCells) == 0:
            raise ValueError('No ship can be placed anymore')
        prow = list(possibleCells)[rd.randint(len(possibleCells))]
        
        # -- adding the ship to the gameboard
        ship = Ship(length=length, orientation=orientation, prow=prow)
        self.add_ship(ship)
        pass

    def hit(self, cell:tuple)->bool:
        '''hits a cell of the grid'''
        grid = self.grid
        try:
            if grid[cell]:
                grid[cell] = not(grid[cell])
                self.hits.add(cell)
                self.grid = grid
                print("It's a hit !")
                self._refresh_ships()
                self._set_gameOver()
                return True
            else:
                print("In the water ...")
                return False
        except IndexError:
            print('cell {} not in the grid'.format(cell))
            raise
        except:
            print('Unexpected error making a hit')
            raise
        pass

    def _refresh_ships(self)-> None:
        '''Checks if the hit did blow a ship'''
        ships = self.ships
        idxSunk = []

        for idx,ship in enumerate(ships):
            if ship.is_sunk(self.hits):
                idxSunk.append(idx)
        if len(idxSunk)==1:
            sunkShip = ships.pop(idxSunk[-1])
            self.sunkShips.append(sunkShip)
        elif len(idxSunk) > 1:
            raise ValueError("Multiple ships sunk by a single hit")

        self.ships = ships
        return

    def _set_gameOver(self)-> None:
        '''Checks if the game is over'''
        if len(self.ships) == 0 and len(self.sunkShips) > 0:
            self.gameOver = True
            print('Game over, well played !')
            print('##### RECAP #####')
            print('Ended in {} hits'.format(len(self.hits)))
            print('{} sunk ships'.format(len(self.sunkShips)))
            print('#################')
        pass

    def _possible_cells(self, length:int, orientation:bool)->set:
        '''
        Description.
            a possible cell is a cell that could be the prow of the ship.
            You have to take into account:
                - the borders of the grid
                - the positionning rules (ships must not touch nor cross)
        Implementation.
            we proceed in two times:
                1. we compute the possible cells for an abstract ship of unitary length
                2. we consider all the cells of the candidate ship (cdtPosition).
                   If you could not place a ship of unitary length on one of them,
                   then you can discard this candidate.
        '''
        # -- Initialisation
        possibleCells = set({(j,i) for j in range(10) for i in range(10)})
        notPossibleCells = set()
        candidates = set()
        # -- Computation of possible cells for a ship of unitary length
        for ship in self.ships:
            notPossibleCells = notPossibleCells.union(set(ship.position), ship.surrArea)
        possibleCells = possibleCells.difference(notPossibleCells)
        # -- Consider now the length and the orientation of the ship and return the prow candidates
        for y,x in possibleCells:
            cdtPosition = {(y+orientation*k, x+(1-orientation)*k) for k in range(length)}
            try:
                inGrid = True
                [self.grid[tpl] for tpl in cdtPosition]
            except IndexError:
                inGrid = False
            if inGrid and len(cdtPosition.intersection(notPossibleCells))==0:
                candidates.add((y,x))
        return candidates


def main():
    gameboard = Gameboard()
    gameboard.add_ship(Ship(length=5, orientation=0, prow =(3,3)))
    print(gameboard.grid.astype(np.uint8))
    pass

if __name__ == '__main__':
    main()