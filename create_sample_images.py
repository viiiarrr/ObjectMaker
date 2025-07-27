"""
Sample Image Creator - Creates simple test images for sphere drawings
Run this script to generate sample images in the assets/images directory
"""

import pygame
import os
import math

def create_sample_images():
    """Create sample images for testing"""
    pygame.init()
    
    # Ensure assets/images directory exists
    assets_dir = os.path.join("assets", "images")
    os.makedirs(assets_dir, exist_ok=True)
    
    size = 64
    
    # Create a simple circle image
    circle_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, (255, 100, 100, 255), (size//2, size//2), size//2 - 2)
    pygame.draw.circle(circle_surface, (255, 255, 255, 255), (size//2, size//2), size//2 - 2, 3)
    pygame.image.save(circle_surface, os.path.join(assets_dir, "red_circle.png"))
    
    # Create a star image
    star_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    center_x, center_y = size//2, size//2
    star_points = []
    for i in range(10):
        angle = math.pi * 2 * i / 10
        if i % 2 == 0:
            radius = size//2 - 5
        else:
            radius = size//4
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        star_points.append((x, y))
    
    pygame.draw.polygon(star_surface, (255, 255, 0, 255), star_points)
    pygame.draw.polygon(star_surface, (255, 255, 255, 255), star_points, 2)
    pygame.image.save(star_surface, os.path.join(assets_dir, "yellow_star.png"))
    
    # Create a diamond image
    diamond_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    diamond_points = [
        (size//2, 5),           # top
        (size - 5, size//2),    # right
        (size//2, size - 5),    # bottom
        (5, size//2)            # left
    ]
    pygame.draw.polygon(diamond_surface, (0, 255, 255, 255), diamond_points)
    pygame.draw.polygon(diamond_surface, (255, 255, 255, 255), diamond_points, 3)
    pygame.image.save(diamond_surface, os.path.join(assets_dir, "cyan_diamond.png"))
    
    # Create a simple smiley face
    smiley_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    # Face
    pygame.draw.circle(smiley_surface, (255, 255, 0, 255), (size//2, size//2), size//2 - 2)
    pygame.draw.circle(smiley_surface, (0, 0, 0, 255), (size//2, size//2), size//2 - 2, 2)
    # Eyes
    pygame.draw.circle(smiley_surface, (0, 0, 0, 255), (size//2 - 10, size//2 - 8), 3)
    pygame.draw.circle(smiley_surface, (0, 0, 0, 255), (size//2 + 10, size//2 - 8), 3)
    # Smile
    pygame.draw.arc(smiley_surface, (0, 0, 0, 255), 
                   (size//2 - 12, size//2 - 2, 24, 16), 0, math.pi, 2)
    pygame.image.save(smiley_surface, os.path.join(assets_dir, "smiley.png"))
    
    print("Sample images created in assets/images/:")
    print("- red_circle.png")
    print("- yellow_star.png")
    print("- cyan_diamond.png")
    print("- smiley.png")
    print("\nYou can now run sphere_drawings.py and use Right Click or 'I' key to add image spheres!")

if __name__ == "__main__":
    create_sample_images()
