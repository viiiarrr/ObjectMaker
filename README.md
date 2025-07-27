# Sphere Drawings

A physics-based artistic sphere animation project using Pygame. This application creates beautiful visual patterns through simulated sphere physics with gravity, collisions, and trail effects.

## Features

- **Physics Simulation**: Realistic gravity, friction, and bounce mechanics
- **Interactive Drawing**: Click to add spheres and watch them create artistic patterns
- **Trail Effects**: Beautiful fading trails that follow sphere movement
- **Multiple Drawing Modes**: Toggle between persistent and fading trail modes
- **Colorful Spheres**: Random colors and sizes for varied visual appeal
- **Real-time Controls**: Add, clear, and modify spheres during runtime

## Controls

- **Left Click**: Add sphere with **Artboard1.png** image at cursor position
- **Right Click**: Add regular colored sphere at cursor position  
- **Middle Click**: Add sphere with other available images
- **SPACE**: Toggle between trail drawing modes
- **R**: Add a random colored sphere at random location
- **I**: Add random **Artboard1** sphere at random location
- **A**: Add **Artboard1** sphere at random position
- **C**: Clear screen and reset with initial spheres
- **ESC**: Exit the application

## Primary Feature: Artboard1 Integration

This application is optimized to use **Artboard1.png** as the primary image texture:

- **Default behavior**: Left-click creates spheres with your Artboard1 image
- **Auto-loading**: Artboard1.png is automatically detected and prioritized
- **Physics integration**: Image spheres follow the same physics as colored spheres
- **Artistic output**: Creates unique patterns using your custom artwork

## Image Support

The application now supports custom images for spheres:

- **Right Click**: Add sphere with image texture at cursor position
- **I Key**: Add random image sphere at random location
- Place your images in `assets/images/` directory
- Supported formats: PNG, JPG, JPEG, GIF, BMP
- Images are automatically scaled to sphere size

### Creating Sample Images

Run the sample image creator first:
```bash
python create_sample_images.py
```

This creates test images (circle, star, diamond, smiley) in the `assets/images/` folder.

## Installation

1. Ensure you have Python 3.7+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python sphere_drawings.py
```

## How It Works

The application creates a physics simulation where:

1. **Spheres** have position, velocity, radius, and color properties (and optional image textures)
2. **Gravity** pulls spheres downward continuously
3. **Friction** gradually slows down sphere movement
4. **Boundary Collision** causes spheres to bounce off screen edges
5. **Trail System** records previous positions to create artistic paths
6. **Interactive Elements** allow real-time sphere creation and manipulation

## Drawing Modes

- **Persistent Mode**: Trails fade slowly, creating layered artistic patterns
- **Clear Mode**: Screen clears each frame, showing only current sphere positions

## Customization

You can modify various parameters in the code:

- `GRAVITY`: Strength of gravitational pull
- `FRICTION`: Air resistance factor
- `BOUNCE_DAMPENING`: Energy loss on collision
- `COLORS`: Available sphere colors
- `FPS`: Animation frame rate
- Trail length and opacity effects

## Physics Concepts

This project demonstrates several physics concepts:

- **Kinematics**: Position and velocity updates
- **Forces**: Gravity and friction implementation
- **Collisions**: Elastic and inelastic boundary interactions
- **Energy Conservation**: Momentum and energy transfer

## Visual Art

The combination of physics simulation and trail rendering creates unique artistic patterns that emerge from the interaction of multiple spheres. Each run produces different visual results based on:

- Initial sphere positions and velocities
- User interaction timing and placement
- Random color and size variations
- Physics parameter settings

Enjoy creating beautiful sphere-based art through physics simulation!

## Requirements

- Python 3.7+
- Pygame 2.0.0+

## License

This project is open source and available under the MIT License.
