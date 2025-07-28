"""
Auto Sphere Art - Automatic sphere creation from center
Spheres appear one by one from center and move to form the image pattern.
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

# Get full screen dimensions
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Sphere:
    def __init__(self, target_x, target_y, radius, color):
        self.target_x = target_x  # Final destination position
        self.target_y = target_y
        self.x = SCREEN_WIDTH // 2  # Start from center
        self.y = SCREEN_HEIGHT // 2
        self.target_radius = radius
        self.radius = 0  # Start with 0 radius (invisible)
        self.color = color
        self.velocity_x = 0  # Will be calculated to reach target
        self.velocity_y = 0
        self.is_growing = True
        self.growth_speed = 2.5  # Faster growth for larger spheres
        self.spawn_delay = 0  # Delay before starting to grow
        self.is_moving_to_target = False
        self.move_speed = 0.06  # Slightly slower movement for larger spheres
        
    def update(self):
        # Handle sphere growth animation (appearing effect)
        if self.is_growing and self.spawn_delay <= 0:
            if self.radius < self.target_radius:
                self.radius += self.growth_speed
                if self.radius >= self.target_radius:
                    self.radius = self.target_radius
                    self.is_growing = False
                    self.is_moving_to_target = True  # Start moving to target after growing
        elif self.spawn_delay > 0:
            self.spawn_delay -= 1
        
        # Move towards target position after growing
        if self.is_moving_to_target and not self.is_growing:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance > 2:  # Still moving to target
                # Calculate velocity towards target
                self.velocity_x = dx * self.move_speed
                self.velocity_y = dy * self.move_speed
            else:
                # Reached target, stop moving
                self.x = self.target_x
                self.y = self.target_y
                self.velocity_x = 0
                self.velocity_y = 0
                self.is_moving_to_target = False
        
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
    
    def draw(self, screen):
        # Only draw if sphere has some size
        if self.radius <= 0:
            return
            
        # Draw main sphere with growing effect
        current_radius = int(self.radius)
        if current_radius > 0:
            # Add a subtle glow effect during growth
            if self.is_growing:
                # Outer glow - ensure color values don't exceed 255
                glow_radius = current_radius + 3
                glow_color = tuple(min(255, int(c) + 50) for c in self.color)
                pygame.draw.circle(screen, glow_color, (int(self.x), int(self.y)), glow_radius, 2)
            
            # Main sphere
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_radius)
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), current_radius, 2)

class AutoSphereCreator:
    """Creates spheres automatically from image pattern"""
    def __init__(self):
        self.dot_queue = []
        self.is_active = False
        self.frame_counter = 0
        self.creation_delay = 4  # frames between each sphere creation
        
    def load_pattern(self, image_path):
        """Load image and create dot pattern data"""
        try:
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Scale image to fit screen
            img_width, img_height = img.size
            scale = min(SCREEN_WIDTH/img_width, SCREEN_HEIGHT/img_height) * 0.7
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Calculate offset to center
            offset_x = (SCREEN_WIDTH - new_width) // 2
            offset_y = (SCREEN_HEIGHT - new_height) // 2
            
            img_array = np.array(img)
            self.dot_queue = []
            
            # Sample with larger spacing for bigger spheres
            sphere_spacing = 18  # Increased spacing for larger spheres
            for y in range(0, new_height, sphere_spacing):
                for x in range(0, new_width, sphere_spacing):
                    r, g, b = img_array[y, x]
                    
                    # Convert to int to avoid overflow warnings
                    r, g, b = int(r), int(g), int(b)
                    
                    # Skip white/light background
                    if (r + g + b) / 3 > 240:
                        continue
                    
                    screen_x = x + offset_x + random.randint(-3, 3)
                    screen_y = y + offset_y + random.randint(-3, 3)
                    
                    # Ensure within bounds with more padding for larger spheres
                    screen_x = max(25, min(SCREEN_WIDTH - 25, screen_x))
                    screen_y = max(25, min(SCREEN_HEIGHT - 25, screen_y))
                    
                    dot_info = {
                        'x': screen_x,
                        'y': screen_y,
                        'color': (r, g, b),
                        'radius': random.randint(15, 25)  # Much larger spheres
                    }
                    self.dot_queue.append(dot_info)
            
            # Shuffle for random creation order
            random.shuffle(self.dot_queue)
            return True
            
        except Exception as e:
            return False
    
    def start_creation(self):
        """Start automatic sphere creation"""
        self.is_active = True
        self.frame_counter = 0
    
    def get_next_sphere(self):
        """Get next sphere to create - ONE by ONE"""
        if not self.is_active or not self.dot_queue:
            return None
        
        self.frame_counter += 1
        if self.frame_counter >= self.creation_delay:
            self.frame_counter = 0
            
            # Get ONLY ONE sphere at a time
            if self.dot_queue:
                sphere_data = self.dot_queue.pop(0)
                
                # Check if finished
                if not self.dot_queue:
                    self.is_active = False
                
                return sphere_data
        
        return None
    
    def is_creating(self):
        return self.is_active
    
    def remaining_count(self):
        return len(self.dot_queue)

class AutoSphereArt:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Auto Sphere Art - Creating from center...")
        self.clock = pygame.time.Clock()
        self.spheres = []
        self.running = True
        self.sphere_creator = AutoSphereCreator()
        
        # Load Artboard1 pattern and AUTO START
        artboard_path = os.path.join("assets", "images", "Artboard1.png")
        if os.path.exists(artboard_path):
            success = self.sphere_creator.load_pattern(artboard_path)
            if success:
                # AUTO START - No need to press anything
                self.sphere_creator.start_creation()
            else:
                print("❌ Failed to load Artboard1 pattern")
        else:
            print("❌ Artboard1.png not found in assets/images/")
        
        print("🎯 Auto-creating spheres from center to form your image!")
    
    def handle_events(self):
        """Handle pygame events - minimal controls for auto mode"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Restart the animation
                    self.spheres.clear()
                    if os.path.exists(os.path.join("assets", "images", "Artboard1.png")):
                        self.sphere_creator.load_pattern(os.path.join("assets", "images", "Artboard1.png"))
                        self.sphere_creator.start_creation()
                    print("🔄 Restarting auto creation from center!")
    
    def update(self):
        """Update all spheres and handle automatic sphere creation"""
        # Handle automatic sphere creation
        new_sphere_data = self.sphere_creator.get_next_sphere()
        if new_sphere_data:
            sphere = Sphere(
                new_sphere_data['x'], 
                new_sphere_data['y'], 
                new_sphere_data['radius'], 
                new_sphere_data['color']
            )
            self.spheres.append(sphere)
        
        # Update all spheres (including growth and movement animation)
        for sphere in self.spheres:
            sphere.update()
    
    def draw(self):
        """Draw everything to the screen"""
        # Always clear screen for clean animation
        self.screen.fill(BLACK)
        
        # Draw all spheres
        for sphere in self.spheres:
            sphere.draw(self.screen)
        
        # No text displays - full screen art only
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
    """Main function to run the auto sphere art application"""
    app = AutoSphereArt()
    app.run()

if __name__ == "__main__":
    main()
