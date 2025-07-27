"""
Sphere Drawings - Physics-based Artistic Sphere Animation
A physics simulation that creates artistic sphere drawings using Pygame.
"""

import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
FRICTION = 0.99
BOUNCE_DAMPENING = 0.8

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE]

class Sphere:
    def __init__(self, x, y, radius, color, velocity_x=0, velocity_y=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.trail = []  # Store previous positions for trail effect
        self.max_trail_length = 50
        
    def update(self):
        # Apply gravity
        self.velocity_y += GRAVITY
        
        # Apply friction
        self.velocity_x *= FRICTION
        self.velocity_y *= FRICTION
        
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Store position for trail
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)
        
        # Boundary collision detection
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.velocity_x = -self.velocity_x * BOUNCE_DAMPENING
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = SCREEN_WIDTH - self.radius
                
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.velocity_y = -self.velocity_y * BOUNCE_DAMPENING
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = SCREEN_HEIGHT - self.radius
    
    def draw(self, screen):
        # Draw trail
        for i, pos in enumerate(self.trail):
            alpha = i / len(self.trail)  # Fade effect
            trail_radius = max(1, int(self.radius * alpha * 0.5))
            trail_color = tuple(int(c * alpha) for c in self.color)
            pygame.draw.circle(screen, trail_color, pos, trail_radius)
        
        # Draw main sphere
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)

class SphereDrawings:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sphere Drawings - Physics Art")
        self.clock = pygame.time.Clock()
        self.spheres = []
        self.running = True
        self.drawing_mode = True  # When True, trails persist
        
        # Create initial spheres
        self.create_initial_spheres()
        
    def create_initial_spheres(self):
        """Create some initial spheres with random properties"""
        for _ in range(5):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            radius = random.randint(10, 30)
            color = random.choice(COLORS)
            velocity_x = random.uniform(-10, 10)
            velocity_y = random.uniform(-10, 10)
            
            sphere = Sphere(x, y, radius, color, velocity_x, velocity_y)
            self.spheres.append(sphere)
    
    def add_sphere(self, x, y):
        """Add a new sphere at the given position"""
        radius = random.randint(8, 25)
        color = random.choice(COLORS)
        velocity_x = random.uniform(-8, 8)
        velocity_y = random.uniform(-8, 8)
        
        sphere = Sphere(x, y, radius, color, velocity_x, velocity_y)
        self.spheres.append(sphere)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Toggle drawing mode
                    self.drawing_mode = not self.drawing_mode
                elif event.key == pygame.K_c:
                    # Clear screen and reset spheres
                    self.spheres.clear()
                    self.create_initial_spheres()
                elif event.key == pygame.K_r:
                    # Add random sphere
                    x = random.randint(50, SCREEN_WIDTH - 50)
                    y = random.randint(50, SCREEN_HEIGHT - 50)
                    self.add_sphere(x, y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.add_sphere(mouse_x, mouse_y)
    
    def update(self):
        """Update all spheres"""
        for sphere in self.spheres:
            sphere.update()
    
    def draw(self):
        """Draw everything to the screen"""
        if not self.drawing_mode:
            self.screen.fill(BLACK)
        else:
            # Create fade effect for persistent trails
            fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            fade_surface.set_alpha(10)
            fade_surface.fill(BLACK)
            self.screen.blit(fade_surface, (0, 0))
        
        # Draw all spheres
        for sphere in self.spheres:
            sphere.draw(self.screen)
        
        # Draw instructions
        font = pygame.font.Font(None, 24)
        instructions = [
            "Left Click: Add Sphere",
            "SPACE: Toggle Trail Mode",
            "R: Add Random Sphere",
            "C: Clear & Reset",
            "ESC: Exit"
        ]
        
        for i, instruction in enumerate(instructions):
            text = font.render(instruction, True, WHITE)
            self.screen.blit(text, (10, 10 + i * 25))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

def main():
    """Main function to run the sphere drawings application"""
    app = SphereDrawings()
    app.run()

if __name__ == "__main__":
    main()
