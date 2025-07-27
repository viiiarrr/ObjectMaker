"""
Sphere Drawings - Physics-based Artistic Sphere Animation
A physics simulation that creates artistic sphere drawings using Pygame.
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

class ProgressiveDotCreator:
    """Creates dots progressively from image pattern with appearing animation"""
    def __init__(self):
        self.dot_queue = []
        self.is_active = False
        self.dots_per_frame = 1  # ONLY 1 sphere per frame for true one-by-one
        self.frame_counter = 0
        self.creation_delay = 3  # 3 frames between each sphere for visible separation
        self.spawn_delay_counter = 0
        
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
            
            # Sample every 8 pixels for dot pattern
            for y in range(0, new_height, 8):
                for x in range(0, new_width, 8):
                    r, g, b = img_array[y, x]
                    
                    # Skip white/light background
                    if (r + g + b) / 3 > 240:
                        continue
                    
                    screen_x = x + offset_x + random.randint(-2, 2)
                    screen_y = y + offset_y + random.randint(-2, 2)
                    
                    # Ensure within bounds
                    screen_x = max(10, min(SCREEN_WIDTH - 10, screen_x))
                    screen_y = max(10, min(SCREEN_HEIGHT - 10, screen_y))
                    
                    dot_info = {
                        'x': screen_x,
                        'y': screen_y,
                        'color': (r, g, b),
                        'radius': random.randint(4, 8)
                    }
                    self.dot_queue.append(dot_info)
            
            # Shuffle for random creation order
            random.shuffle(self.dot_queue)
            print(f"🎯 Loaded {len(self.dot_queue)} dots for progressive creation")
            return True
            
        except Exception as e:
            print(f"Error loading pattern: {e}")
            return False
    
    def start_creation(self, speed=3):
        """Start one-by-one sphere creation"""
        self.is_active = True
        self.creation_delay = max(1, 6 - speed)  # Speed 1=5 frames, 2=4 frames, 3=3 frames, etc.
        self.dots_per_frame = 1  # Always only 1 sphere at a time
        self.frame_counter = 0
        self.spawn_delay_counter = 0
        print(f"🎯 Starting ONE-BY-ONE sphere creation - delay {self.creation_delay} frames")
        print("✨ Each sphere appears individually!")
    
    def get_next_dots(self):
        """Get next single dot to create - TRUE one by one"""
        if not self.is_active or not self.dot_queue:
            return []
        
        self.frame_counter += 1
        if self.frame_counter >= self.creation_delay:
            self.frame_counter = 0
            
            # Get ONLY ONE dot at a time
            next_dots = []
            if self.dot_queue:
                dot_data = self.dot_queue.pop(0)
                dot_data['spawn_delay'] = 0  # No delay, immediate appearance
                next_dots.append(dot_data)
            
            # Check if finished
            if not self.dot_queue:
                self.is_active = False
                print("✅ One-by-one sphere creation complete!")
            
            return next_dots
        
        return []
    
    def is_creating(self):
        return self.is_active
    
    def remaining_count(self):
        return len(self.dot_queue)

class Sphere:
    def __init__(self, x, y, radius, color, velocity_x=0, velocity_y=0):
        self.target_x = x  # Final destination position
        self.target_y = y
        self.x = SCREEN_WIDTH // 2  # Start from center
        self.y = SCREEN_HEIGHT // 2
        self.target_radius = radius
        self.radius = 0  # Start with 0 radius (invisible)
        self.color = color
        self.velocity_x = 0  # Will be calculated to reach target
        self.velocity_y = 0
        self.trail = []  # Store previous positions for trail effect
        self.max_trail_length = 50
        self.is_growing = True
        self.growth_speed = 1.5  # Faster growth for quick appearance
        self.spawn_delay = 0  # Delay before starting to grow
        self.is_moving_to_target = False
        self.move_speed = 0.1  # Speed of movement to target position
        
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
        
        # Store position for trail (only when visible)
        if self.radius > 0:
            self.trail.append((int(self.x), int(self.y)))
            if len(self.trail) > self.max_trail_length:
                self.trail.pop(0)
    
    def draw(self, screen):
        # Only draw if sphere has some size
        if self.radius <= 0:
            return
            
        # Draw trail
        for i, pos in enumerate(self.trail):
            alpha = i / len(self.trail)  # Fade effect
            trail_radius = max(1, int(self.radius * alpha * 0.5))
            trail_color = tuple(int(c * alpha) for c in self.color)
            pygame.draw.circle(screen, trail_color, pos, trail_radius)
        
        # Draw main sphere with growing effect
        current_radius = int(self.radius)
        if current_radius > 0:
            # Add a subtle glow effect during growth
            if self.is_growing:
                # Outer glow
                glow_radius = current_radius + 3
                glow_color = tuple(min(255, c + 50) for c in self.color)
                pygame.draw.circle(screen, glow_color, (int(self.x), int(self.y)), glow_radius, 2)
            
            # Main sphere
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_radius)
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), current_radius, 2)

class SphereDrawings:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Auto Sphere Art - Creating from center...")
        self.clock = pygame.time.Clock()
        self.spheres = []
        self.running = True
        self.drawing_mode = True  # When True, trails persist
        self.dot_creator = ProgressiveDotCreator()  # Progressive dot creator
        self.physics_enabled = False  # Start with physics OFF for clean pattern
        
        # Load Artboard1 pattern
        artboard_path = os.path.join("assets", "images", "Artboard1.png")
        if os.path.exists(artboard_path):
            success = self.dot_creator.load_pattern(artboard_path)
            if success:
                print("✅ Artboard1.png loaded for auto creation!")
                # AUTO START - No need to press G
                self.start_progressive_creation(speed=3)
            else:
                print("❌ Failed to load Artboard1 pattern")
        else:
            print("❌ Artboard1.png not found in assets/images/")
        
        print("🎯 Auto-creating spheres from center to form your image!")
    
    def start_progressive_creation(self, speed=3):
        """Start progressive dot creation"""
        self.spheres.clear()
        self.dot_creator.start_creation(speed)
        self.physics_enabled = False
        print(f"🎬 One-by-one sphere creation started - speed {speed}")
        print("🎯 Watch each sphere appear individually!")
    
    def add_sphere(self, x, y):
        """Add a new sphere at the given position"""
        radius = random.randint(8, 25)
        color = random.choice(COLORS)
        velocity_x = random.uniform(-8, 8)
        velocity_y = random.uniform(-8, 8)
        
        sphere = Sphere(x, y, radius, color, velocity_x, velocity_y)
        self.spheres.append(sphere)
        return sphere
    
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
                    self.start_progressive_creation(speed=3)
                    print("🔄 Restarting auto creation from center!")
    
    def update(self):
        """Update all spheres and handle progressive dot creation"""
        # Handle progressive dot creation
        new_dots = self.dot_creator.get_next_dots()
        for dot_data in new_dots:
            sphere = Sphere(
                dot_data['x'], dot_data['y'], dot_data['radius'], dot_data['color'], 0, 0
            )
            # Set spawn delay for staggered appearance
            sphere.spawn_delay = dot_data.get('spawn_delay', 0)
            self.spheres.append(sphere)
        
        # Update all spheres (including growth animation)
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
        font = pygame.font.Font(None, 16)
        instructions = [
            "� ONE-BY-ONE SPHERE CREATION:",
            "G: Start Individual Sphere Creation",
            "1: Slow (5 frames) | 2: Medium (3 frames) | 3: Fast (1 frame)",
            "+/-: Adjust delay between spheres",
            "",
            "⚙️ CONTROLS:",
            "P: Toggle Physics | SPACE: Toggle Trails",
            "C: Clear | ESC: Exit",
            "",
            f"Status: {'Creating ONE BY ONE' if self.dot_creator.is_creating() else 'Ready'}",
            f"Spheres: {len(self.spheres)} | Remaining: {self.dot_creator.remaining_count()}"
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
