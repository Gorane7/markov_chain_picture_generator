import pygame
import time
import random
import math

class Simulator:
    def __init__(self, xSize, ySize, screen):
        self.pixels = pixelArr
        self.xSize = xSize
        self.ySize = ySize
        self.pixelTotals = []
        self.pixelCounts = []
        self.maxPixelCount = 0
        self.pixelsDrawn = 0
        self.startTime = int(time.time())
        for y in range(ySize):
            totals = []
            counts = []
            for x in range(xSize):
                totals.append([0, 0, 0])
                counts.append(0)
            self.pixelTotals.append(totals)
            self.pixelCounts.append(counts)
        self.x = random.random() * xSize
        self.y = random.random() * ySize
        self.colour = (255, 255, 255)
        self.colours = {
            "white": (255, 255, 255),
            "red": (255, 75, 75),
            "green": (0, 255, 0),
            "blue": (150, 150, 255),
            "brown": (160, 82, 45),
            "yellow": (255, 255, 0)
        }
        #self.colour = self.colours["blue"]

        zoomFactor = 1.5

        """
        self.mappers = [
            [self.attract(1000 - 1000 * zoomFactor, 1000 - 1000 * zoomFactor, 1), self.circle_repel(1000, 1000, 100 * zoomFactor), self.color("white")],
            [self.attract(1000 - 1000 * zoomFactor, 1000 + 1000 * zoomFactor, 1), self.circle_repel(1000, 1000, 100 * zoomFactor), self.color("red")],
            [self.attract(1000 + 1000 * zoomFactor, 1000 + 1000 * zoomFactor, 1), self.circle_repel(1000, 1000, 100 * zoomFactor), self.color("green")],
            [self.attract(1000 + 1000 * zoomFactor, 1000 - 1000 * zoomFactor, 1), self.circle_repel(1000, 1000, 100 * zoomFactor), self.color("blue")]
        ]"""
        strength = 0.1
        """
        self.mappers = [
            [self.circle_repel(0, 0, 100), self.attract(1000, 1000, strength), self.color("white")],
            [self.circle_repel(2000, 0, 100), self.attract(1000, 1000, strength), self.color("red")],
            [self.circle_repel(0, 2000, 100), self.attract(1000, 1000, strength), self.color("green")],
            [self.circle_repel(2000, 2000, 100), self.attract(1000, 1000, strength), self.color("blue")]
        ]"""

        """
        self.mappers = [
            [self.attract(1000, 0, 1), self.blend_color("red", 1)],
            [self.attract(0, 2000, 1), self.blend_color("green", 1)],
            [self.attract(2000, 2000, 1), self.blend_color("blue", 1)]
        ]"""

        """
        self.mappers = [
            [self.map_attract(lambda x, y: (y, 0), 0.5), self.color("white")],
            [self.map_attract(lambda x, y: (y, 2000), 0.5), self.color("red")],
            [self.map_attract(lambda x, y: (0, x), 0.5), self.color("green")],
            [self.map_attract(lambda x, y: (2000, x), 0.5), self.color("blue")],
            [self.map_attract(lambda x, y: (2000 - y, 0), 0.5), self.color("white")],
            [self.map_attract(lambda x, y: (2000 - y, 2000), 0.5), self.color("red")],
            [self.map_attract(lambda x, y: (0, 2000 - x), 0.5), self.color("green")],
            [self.map_attract(lambda x, y: (2000, 2000 - x), 0.5), self.color("blue")]
        ]"""

        """
        self.mappers = [
            [self.map_attract(lambda x, y: (1000, y), 2), self.color("brown")],
            [self.map_attract(lambda x, y: (1000 - (2000 - y) / 2, y), 1), self.color("green")],
            [self.map_attract(lambda x, y: (1000 + (2000 - y) / 2, y), 1), self.color("green")]
        ]"""

        """
        self.mappers = [
            [self.map_attract(lambda x, y: (1000, 100), 1), self.blend_color("white", 1)],
            [self.map_attract(lambda x, y: (100, 750), 1), self.blend_color("blue", 1)],
            [self.map_attract(lambda x, y: (1900, 750), 1), self.blend_color("red", 1)],
            [self.map_attract(lambda x, y: (300, 1900), 1), self.blend_color("yellow", 1)],
            [self.map_attract(lambda x, y: (1700, 1900), 1), self.blend_color("green", 1)]
        ]"""

        """
        self.mappers = [
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (1000 + 1000 * math.cos(theta), 1000 + 1000 * math.sin(theta))][1], 10)]
        ]"""

        """
        self.mappers = [
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (500 + 400 * math.cos(theta), 500 + 400 * math.sin(theta))][1], 30)],
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (500 + 400 * math.cos(theta), 1500 + 400 * math.sin(theta))][1], 30)],
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (1500 + 400 * math.cos(theta), 500 + 400 * math.sin(theta))][1], 30)],
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (1500 + 400 * math.cos(theta), 1500 + 400 * math.sin(theta))][1], 30)]
        ]"""

        """
        self.mappers = [
            [self.attract_random(lambda: [theta := random.random() * math.pi * 2, (1000 + 1000 * math.cos(theta), 1000 + 1000 * math.sin(theta))][1], 33), self.color("blue")],
            [self.attract_random(lambda: (1000, random.randint(0, 1999)), 10), self.color("red")]
        ]"""

        self.mappers = [
            [self.attract(500, 0, 1), self.blend_color("red", 1)],
            [self.attract(0, 1000, 1), self.blend_color("green", 1)],
            [self.attract(1000, 1000, 1), self.blend_color("blue", 1)]
        ]

    def attract_random(self, random_gen, strength):
        """Basic attractor to a randomly generated point, where the point is generated by random_gen."""
        def attractor():
            x, y = random_gen()
            return self.attract(x, y, strength)()
        return attractor

    def map_attract(self, mapper, strength):
        """Basic attractor to a point, that is generated by a function that takes current coordinates as input."""
        def attractor():
            x, y = mapper(self.x, self.y)
            return self.attract(x, y, strength)()
        return attractor

    def square_repel(self, x, y, strength):
        def repeller():
            self.x = self.x + strength / (self.x - x)
            self.y = self.y + strength / (self.y - y)
        return repeller

    def circle_repel(self, x, y, strength):
        def repeller():
            xDiff = self.x - x
            yDiff = self.y - y
            length = math.sqrt(xDiff**2 + yDiff**2)
            xDiff /= length
            yDiff /= length
            self.x = self.x + xDiff * strength
            self.y = self.y + yDiff * strength
        return repeller

    def attract(self, x, y, strength):
        """Basic attractor to a point."""
        def attractor():
            self.x = (self.x + strength * x) / (1 + strength)
            self.y = (self.y + strength * y) / (1 + strength)
        return attractor

    def color(self, colour):
        def colorer():
            self.colour = self.colours[colour]
        return colorer

    def blend_color(self, colour, strength):
        def colorer():
            chosen_color = self.colours[colour]
            self.colour = (
                    (self.colour[0] + strength * chosen_color[0]) / (1 + strength),
                    (self.colour[1] + strength * chosen_color[1]) / (1 + strength),
                    (self.colour[2] + strength * chosen_color[2]) / (1 + strength)
            )
        return colorer

    def recreateRandom(self):
        x = random.randint(0, self.xSize - 1)
        y = random.randint(0, self.ySize - 1)
        self.pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def step(self):
        for mapper in random.choice(self.mappers):
            mapper()
        if self.xSize > self.x >= 0 and self.ySize > self.y >= 0:
            self.pixelsDrawn += 1
            x = int(self.x)
            y = int(self.y)
            self.pixelTotals[y][x][0] += self.colour[0]
            self.pixelTotals[y][x][1] += self.colour[1]
            self.pixelTotals[y][x][2] += self.colour[2]
            self.pixelCounts[y][x] += 1
            if self.pixelCounts[y][x] > self.maxPixelCount:
                self.maxPixelCount = self.pixelCounts[y][x]
                self.renormalize()
            self.pixels[int(self.x), int(self.y)] = (
                    self.pixelTotals[y][x][0] // self.maxPixelCount,
                    self.pixelTotals[y][x][1] // self.maxPixelCount,
                    self.pixelTotals[y][x][2] // self.maxPixelCount
            )
        else:
            pass
            #print(f"Out of bounds: ({int(self.x)}, {int(self.y)})")

    def renormalize(self):
        secondsPassed = int(time.time()) - self.startTime
        print(f"Renormalizing: Max depth: {self.maxPixelCount}, Pixels drawn: {self.pixelsDrawn}, Per second: {self.pixelsDrawn / secondsPassed}")
        for y, row in enumerate(self.pixelTotals):
            for x, total in enumerate(row):
                self.pixels[x, y] = (
                    total[0] // self.maxPixelCount,
                    total[1] // self.maxPixelCount,
                    total[2] // self.maxPixelCount
                )


if __name__ == '__main__':
    xSize = 1000
    ySize = 1000
    pygame.init()
    screen = pygame.display.set_mode([xSize, ySize])
    pixelArr = pygame.PixelArray(screen)
    simulator = Simulator(xSize, ySize, pixelArr)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #simulator.recreateRandom()
        simulator.step()
        if simulator.pixelsDrawn % 10000 == 0:
            pygame.display.flip()
    pixelArr.close()
    pygame.image.save(screen, "pictures/" + str(time.time()).replace(".", "_") + ".png")
    pygame.quit()