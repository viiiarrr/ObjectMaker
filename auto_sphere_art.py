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

# ==================== IMAGE CONFIGURATION ====================
# Change this to use different images from assets/images/
# Available images: Artboard1.png, cyan_diamond.png, red_circle.png, smiley.png, yellow_star.png, Logo_Evos.png
IMAGE_NAME = "RRQLAMA.png"  # Change this to your desired image
# ============================================================

# Initialize Pygame
pygame.init()

# Set reasonable window dimensions  
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Sphere configuration constants - Optimized for detailed logo reproduction
SPHERE_SPACING = 8   # Much finer sampling for precise detail capture
MIN_SPHERE_RADIUS = 4   # Smaller minimum for ultra-fine details
MAX_SPHERE_RADIUS = 12  # Smaller maximum for consistent detail level
SPHERE_GROWTH_SPEED = 2.0  # Moderate growth for smooth animation
SPHERE_MOVE_SPEED = 0.12   # Faster movement for quicker formation
CREATION_DELAY = 1  # Very fast creation - 1 frame delay for maximum density

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
        self.growth_speed = SPHERE_GROWTH_SPEED  # Use configurable constant
        self.spawn_delay = 0  # Delay before starting to grow
        self.is_moving_to_target = False
        self.move_speed = SPHERE_MOVE_SPEED  # Use configurable constant
        
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
        self.creation_delay = CREATION_DELAY  # Use configurable constant
        
    def load_pattern(self, image_path):
        """Load image and create dot pattern data with enhanced detail detection"""
        try:
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Scale image to fit screen with higher resolution preservation
            img_width, img_height = img.size
            scale = min(SCREEN_WIDTH/img_width, SCREEN_HEIGHT/img_height) * 0.85
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Calculate offset to center
            offset_x = (SCREEN_WIDTH - new_width) // 2
            offset_y = (SCREEN_HEIGHT - new_height) // 2
            
            img_array = np.array(img)
            self.dot_queue = []
            
            # Enhanced sampling with adaptive sphere sizing based on local contrast
            for y in range(0, new_height, SPHERE_SPACING):
                for x in range(0, new_width, SPHERE_SPACING):
                    if y >= img_array.shape[0] or x >= img_array.shape[1]:
                        continue
                        
                    r, g, b = img_array[y, x]
                    r, g, b = int(r), int(g), int(b)
                    
                    # More nuanced background detection for better detail capture
                    brightness = (r + g + b) / 3
                    if brightness > 250:  # Very bright pixels only
                        continue
                    
                    # Calculate local contrast for adaptive sphere sizing
                    local_contrast = self._calculate_local_contrast(img_array, x, y)
                    
                    # Adaptive radius based on local image characteristics
                    if brightness < 50:  # Dark areas - smaller spheres for detail
                        radius = random.randint(MIN_SPHERE_RADIUS, MIN_SPHERE_RADIUS + 3)
                    elif local_contrast > 50:  # High contrast areas - medium spheres
                        radius = random.randint(MIN_SPHERE_RADIUS + 2, MAX_SPHERE_RADIUS - 2)
                    else:  # Uniform areas - larger spheres for efficiency
                        radius = random.randint(MAX_SPHERE_RADIUS - 3, MAX_SPHERE_RADIUS)
                    
                    screen_x = x + offset_x + random.randint(-1, 1)
                    screen_y = y + offset_y + random.randint(-1, 1)
                    
                    # Ensure within bounds with proper padding
                    screen_x = max(radius + 2, min(SCREEN_WIDTH - radius - 2, screen_x))
                    screen_y = max(radius + 2, min(SCREEN_HEIGHT - radius - 2, screen_y))
                    
                    dot_info = {
                        'x': screen_x,
                        'y': screen_y,
                        'color': (r, g, b),
                        'radius': radius
                    }
                    self.dot_queue.append(dot_info)
            
            # Sort by distance from center for natural growth pattern
            center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
            self.dot_queue.sort(key=lambda dot: 
                math.sqrt((dot['x'] - center_x)**2 + (dot['y'] - center_y)**2))
            
            return True
            
        except Exception as e:
            print(f"Error loading pattern: {e}")
            return False
    
    def _calculate_local_contrast(self, img_array, x, y):
        """Calculate local contrast around a pixel for adaptive sphere sizing"""
        try:
            # Sample 3x3 neighborhood for contrast calculation
            min_val, max_val = 255, 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < img_array.shape[0] and 
                        0 <= nx < img_array.shape[1]):
                        pixel_brightness = sum(img_array[ny, nx]) / 3
                        min_val = min(min_val, pixel_brightness)
                        max_val = max(max_val, pixel_brightness)
            
            return max_val - min_val
        except:
            return 30  # Default moderate contrast
    
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
        pygame.display.set_caption(f"Auto Sphere Art - {IMAGE_NAME}")
        self.clock = pygame.time.Clock()
        self.spheres = []
        self.running = True
        self.sphere_creator = AutoSphereCreator()
        
        # Load image from configuration and AUTO START
        image_path = os.path.join("assets", "images", IMAGE_NAME)
        if os.path.exists(image_path):
            success = self.sphere_creator.load_pattern(image_path)
            if success:
                # AUTO START - No need to press anything
                self.sphere_creator.start_creation()
                print(f"✅ Loaded {IMAGE_NAME} successfully!")
            else:
                print(f"❌ Failed to load {IMAGE_NAME}")
        else:
            print(f"❌ {IMAGE_NAME} not found in assets/images/")
            print("Available images:", os.listdir("assets/images"))
        
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
                    # Restart the animation with configured image
                    self.spheres.clear()
                    image_path = os.path.join("assets", "images", IMAGE_NAME)
                    if os.path.exists(image_path):
                        self.sphere_creator.load_pattern(image_path)
                        self.sphere_creator.start_creation()
                        print(f"🔄 Restarting auto creation with {IMAGE_NAME}!")
    
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
