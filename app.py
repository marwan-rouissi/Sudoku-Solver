import pygame

class App():
     
    def __init__(self, gridInit:list, gridsoluce:list) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((504, 720))
        pygame.display.set_caption("Sudoku Solver")

        self.gridInit = gridInit
        self.gridSoluce = gridsoluce

        self.x = 0
        self.y = 0
        self.dif = 500 / 9
        self.val = 0

        self.font1 = pygame.font.SysFont("comicsans", 40)
        self.font2 = pygame.font.SysFont("comicsans", 20)

    def get_cord(self, pos):
        # global x
        self.x = pos[0]//self.dif
        # global y
        self.y = pos[1]//self.dif

    # Function to draw required lines for making Sudoku grid        
    def draw(self):
        # Draw the lines
            
        for i in range (9):
            for j in range (9):
                if int(self.gridInit[j][i]) == self.gridSoluce[j][i]:
                    # print(self.grid[j][i])
    
                    # Fill blue color in already numbered grid
                    pygame.draw.rect(self.screen, (0, 153, 153), (i * self.dif, j * self.dif, self.dif + 1, self.dif + 1))
    
                    # Fill grid with default numbers specified
                    text1 = self.font1.render(str(self.gridSoluce[j][i]), 1, (0, 0, 0))
                    self.screen.blit(text1, (i * self.dif + 15, j * self.dif - 1))
                
                else:
                    # Fill blue color in already numbered grid
                    pygame.draw.rect(self.screen, (150, 153, 153), (i * self.dif, j * self.dif, self.dif + 1, self.dif + 1))

                    # Fill grid with default numbers specified
                    text1 = self.font1.render(str(self.gridSoluce[j][i]), 1, (0, 0, 0))
                    self.screen.blit(text1, (i * self.dif + 15, j * self.dif - 1))

        # Draw lines horizontally and verticallyto form grid          
        for i in range(10):
            if i % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.dif), (500, i * self.dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.dif, 0), (i * self.dif, 500), thick)     

    # Fill value entered in cell     
    def draw_val(self, val):
        text1 = self.font1.render(str(val), 1, (0, 0, 0))
        self.screen.blit(text1, (self.x * self.dif + 15, self.y * self.dif + 15)) 

    def run_pygame(self):
            running = True

            while running:
                # White color background
                self.screen.fill((255, 255, 255))
                # Loop through the events stored in event.get()
                for event in pygame.event.get():
                    # Quit the game window
                    if event.type == pygame.QUIT:
                        running = False
                    # Get the mouse position to insert number   
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        pos = pygame.mouse.get_pos()
                        self.get_cord(pos)
                
                self.draw()

                # Update window
                pygame.display.update()
            
            pygame.quit()