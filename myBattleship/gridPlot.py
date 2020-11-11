#%% Modules
import matplotlib.pyplot as plt
import numpy as np
from ship import Ship
from gameboard import Gameboard

#%% Gridplot Class
class GridShow:
  def __init__(self,gameboard:Gameboard):
    self.grid = gameboard.grid
    self.ships = gameboard.ships
    self.grid_show()
    pass
  def grid_show(self):
    '''plots the grid together with the ships and shows it'''
    ships = self.ships
    grid = self.grid

    # -- figure parameters
    fig = plt.figure('Gameboard',figsize=(12,6))
    plt.scatter(np.where(grid == True)[1]+0.5,np.where(grid == True)[0]+0.5, color = 'red', marker = 'x', label = 'ships')
    plt.scatter(np.where(grid == False)[1]+0.5,np.where(grid == False)[0]+0.5, color = 'blue', label = 'ocean')
    plt.xticks(np.arange(1, 11, 1))
    plt.yticks(np.arange(1, 11, 1))
    plt.rc('grid', linestyle="-", color='black')
    plt.grid(True)
    plt.legend(loc = 'upper right', shadow = True, fontsize = 12).get_frame().set_facecolor('C0')
    
    # -- ship plot
    self.ship_plot()
    plt.show()
    pass

  def ship_plot(self):
    '''called by grid_plot method'''
    # -- sorting position to get extreme values
    ships = self.ships
    tempPos = [ list(ship.position) for ship in ships]
    sortedPos = [sorted(sorted(pos, key= lambda tpl:tpl[0]), key = lambda tpl:tpl[1]) for pos in tempPos]
    
    # -- plot
    positions = [[pos[0],pos[-1]] for pos in sortedPos]
    orientations = [ship.orientation for ship in ships]
    for idx,position in enumerate(positions):
      if orientations[idx]:
        plt.vlines(position[0][1] + 0.5 , ymin=position[0][0] + 0.5 , ymax= position[1][0] + 0.5, linestyles='dashed', color = 'red')
      else:
        plt.hlines(position[0][0] + 0.5, xmin=position[0][1] + 0.5 , xmax= position[1][1] + 0.5, linestyles = 'dashed', color = 'red')
    
    plt.show()
    return

if __name__ == '__main__':
    gameboard = Gameboard()
    gameboard.add_random_ship(length = 5)
    gameboard.add_random_ship(length = 3)
    gameboard.add_random_ship(length = 5)
    gameboard.add_random_ship(length = 3)
    gameboard.add_random_ship(length = 3)
    gameboard.add_random_ship(length = 3)
    gameboard.add_random_ship(length = 3)
    for ship in gameboard.ships:
        print(str(ship))
    while len(gameboard.ships) > 0:
      ship = gameboard.ships[0]
      for cell in ship.position:
        gameboard.hit(cell)

