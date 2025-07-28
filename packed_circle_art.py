"""
Packed Circle Art - Dense circle packing simulation matching reference image
Creates vibrant, densely packed circles of varying sizes that fill the entire canvas.
"""

import pygame
import math
import random
import sys
import os
import numpy as np
from PIL import Image

# Initialize Pygame
pygame.init()

# Set reasonable window dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Physics constants for circle packing
MIN_RADIUS = 8
MAX_RADIUS = 35
PACK_ATTEMPTS = 100
GROWTH_SPEED = 0.5

# Vibrant color palette matching reference image
VIBRANT_COLORS = [
    (255, 255, 0),    # Bright Yellow
    (255, 215, 0),    # Gold
    (255, 165, 0),    # Orange
    (255, 140, 0),    # Dark Orange
    (255, 69, 0),     # Red Orange
    (148, 0, 211),    # Dark Violet
    (138, 43, 226),   # Blue Violet
    (75, 0, 130),     # Indigo
    (128, 0, 128),    # Purple
    (255, 20, 147),   # Deep Pink
    (255, 105, 180),  # Hot Pink
    (50, 205, 50),    # Lime Green
    (34, 139, 34),    # Forest Green
    (0, 100, 0),      # Dark Green
    (139, 69, 19),    # Saddle Brown
    (160, 82, 45),    # Sienna
    (0, 0, 0),        # Black (accent)
]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class PackedCircle:
    """A circle in the packed circle art with growth animation"""
    
    def __init__(self, x, y, target_radius, color):
        self.x = float(x)
        self.y = float(y)
        self.target_radius = target_radius
        self.radius = 0.0  # Start with 0 radius
        self.color = color
        self.is_growing = True
        self.growth_speed = random.uniform(0.3, 0.8)
        self.glow_intensity = 0
        
    def update(self):
        """Update circle growth animation"""
        if self.is_growing:
            self.radius += self.growth_speed
            if self.radius >= self.target_radius:
                self.radius = self.target_radius
                self.is_growing = False
                self.glow_intensity = 20  # Brief glow when reaching target size
        
        # Fade glow effect
        if self.glow_intensity > 0:
            self.glow_intensity -= 0.5
    
    def draw(self, screen):
        """Render circle with visual effects"""
        if self.radius <= 0:
            return
            
        current_radius = int(self.radius)
        center_pos = (int(self.x), int(self.y))
        
        # Draw glow effect if present
        if self.glow_intensity > 0:
            glow_radius = current_radius + int(self.glow_intensity * 0.5)
            glow_color = tuple(min(255, c + int(self.glow_intensity)) for c in self.color)
            pygame.draw.circle(screen, glow_color, center_pos, glow_radius, 3)
        
        # Draw main circle with gradient effect
        self._draw_gradient_circle(screen, center_pos, current_radius)
        
        # Draw white outline for definition
        pygame.draw.circle(screen, WHITE, center_pos, current_radius, 2)
    
    def _draw_gradient_circle(self, screen, center_pos, radius):
        """Draw circle with gradient shading for depth"""
        # Draw multiple concentric circles for gradient effect
        for i in range(radius, 0, -1):
            intensity = i / radius
            shaded_color = tuple(int(c * (0.4 + 0.6 * intensity)) for c in self.color)
            pygame.draw.circle(screen, shaded_color, center_pos, i)

class CirclePackingGenerator:
    """Generates densely packed circles using circle packing algorithms"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.circles = []
        self.generation_complete = False
        
    def check_collision(self, x, y, radius):
        """Check if a new circle collides with existing circles"""
        for circle in self.circles:
            distance = math.sqrt((x - circle.x)**2 + (y - circle.y)**2)
            if distance < (radius + circle.target_radius + 2):  # Small padding
                return True
        return False
    
    def is_in_bounds(self, x, y, radius):
        """Check if circle is within screen boundaries"""
        return (radius <= x <= self.width - radius and 
                radius <= y <= self.height - radius)
    
    def generate_packed_circles(self, max_circles=800):
        """Generate densely packed circles similar to reference image"""
        self.circles = []
        attempts = 0
        max_attempts = max_circles * 50
        
        while len(self.circles) < max_circles and attempts < max_attempts:
            attempts += 1
            
            # Random position
            x = random.uniform(MAX_RADIUS, self.width - MAX_RADIUS)
            y = random.uniform(MAX_RADIUS, self.height - MAX_RADIUS)
            
            # Try different radii, starting from larger to smaller
            radius_attempts = [
                random.randint(25, MAX_RADIUS),  # Large circles
                random.randint(15, 25),          # Medium circles
                random.randint(MIN_RADIUS, 15)   # Small circles
            ]
            
            for radius in radius_attempts:
                if (self.is_in_bounds(x, y, radius) and 
                    not self.check_collision(x, y, radius)):
                    
                    # Choose vibrant color
                    color = random.choice(VIBRANT_COLORS)
                    circle = PackedCircle(x, y, radius, color)
                    self.circles.append(circle)
                    break
        
        # Fill remaining gaps with smaller circles
        self._fill_gaps()
        
        # Shuffle for random growth order
        random.shuffle(self.circles)
        self.generation_complete = True
        
        return self.circles
    
    def _fill_gaps(self):
        """Fill remaining gaps with smaller circles for denser packing"""
        gap_fill_attempts = 5000
        
        for _ in range(gap_fill_attempts):
            x = random.uniform(MIN_RADIUS, self.width - MIN_RADIUS)
            y = random.uniform(MIN_RADIUS, self.height - MIN_RADIUS)
            
            # Try small radii for gap filling
            for radius in range(MIN_RADIUS, 15):
                if (self.is_in_bounds(x, y, radius) and 
                    not self.check_collision(x, y, radius)):
                    
                    color = random.choice(VIBRANT_COLORS)
                    circle = PackedCircle(x, y, radius, color)
                    self.circles.append(circle)
                    break

class PackedCircleArt:
    """Main application for packed circle art generation"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Packed Circle Art - Dense Circle Packing")
        self.clock = pygame.time.Clock()
        self.running = True
        self.show_info = True
        
        # Generate packed circles
        self.generator = CirclePackingGenerator(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.circles = self.generator.generate_packed_circles()
        self.current_circle_index = 0
        self.animation_speed = 3  # Circles to grow per frame
        
        print(f"Generated {len(self.circles)} packed circles")
    
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Regenerate circles
                    self.circles = self.generator.generate_packed_circles()
                    self.current_circle_index = 0
                    print(f"Regenerated {len(self.circles)} packed circles")
                elif event.key == pygame.K_i:
                    # Toggle info display
                    self.show_info = not self.show_info
                elif event.key == pygame.K_r:
                    # Restart animation
                    for circle in self.circles:
                        circle.radius = 0
                        circle.is_growing = True
                    self.current_circle_index = 0
    
    def update(self):
        """Update circle animations"""
        # Start growing new circles progressively
        if self.current_circle_index < len(self.circles):
            # Start multiple circles growing at once for faster filling
            for i in range(self.animation_speed):
                if self.current_circle_index + i < len(self.circles):
                    circle = self.circles[self.current_circle_index + i]
                    if circle.radius == 0:  # Not started growing yet
                        circle.is_growing = True
            
            # Move to next batch
            self.current_circle_index += self.animation_speed
        
        # Update all circles
        for circle in self.circles:
            circle.update()
    
    def draw(self):
        """Render the packed circle art"""
        self.screen.fill(BLACK)
        
        # Draw all circles
        for circle in self.circles:
            circle.draw(self.screen)
        
        # Draw info if enabled
        if self.show_info:
            self._draw_info()
        
        pygame.display.flip()
    
    def _draw_info(self):
        """Draw information overlay"""
        font = pygame.font.Font(None, 36)
        info_texts = [
            f"Circles: {len(self.circles)}",
            f"Growing: {self.current_circle_index}/{len(self.circles)}",
            "Controls:",
            "SPACE - Regenerate",
            "R - Restart animation", 
            "I - Toggle info",
            "ESC - Exit"
        ]
        
        for i, text in enumerate(info_texts):
            color = WHITE if i < 2 else (200, 200, 200)
            surface = font.render(text, True, color)
            self.screen.blit(surface, (10, 10 + i * 30))
    
    def run(self):
        """Main application loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

def main():
    """Entry point for packed circle art application"""
    app = PackedCircleArt()
    app.run()

if __name__ == "__main__":
    main()