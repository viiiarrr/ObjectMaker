# Auto Sphere Art

An automatic sphere creation project using Pygame that transforms images into beautiful sphere animations. Spheres appear one by one from the center and move to form artistic patterns based on your input images.

## Features

- **Automatic Sphere Generation**: Spheres appear progressively from screen center
- **Image Pattern Formation**: Converts any image into sphere-based artwork
- **Physics Animation**: Realistic growth and movement animations
- **Configurable Images**: Easy switching between different source images
- **Adaptive Sizing**: Smart sphere sizing based on image characteristics
- **Ultra-Fine Detail**: Enhanced pattern detection for precise logo reproduction

## Quick Start Tutorial

### 1. Installation

Ensure you have Python 3.7+ and install dependencies:
```bash
pip install pygame pillow numpy
```

### 2. Prepare Your Images

Place your images in the `assets/images/` folder. Supported formats: PNG, JPG, JPEG.

Available sample images:
- `Artboard1.png` - Original artwork
- `Logo_Evos.png` - Gaming logo  
- `smiley.png` - Smiley face
- `yellow_star.png` - Star shape
- `cyan_diamond.png` - Diamond shape
- `red_circle.png` - Circle shape

### 3. Configure Your Image

Edit the top of `auto_sphere_art.py` to choose which image to use:

```python
# ==================== IMAGE CONFIGURATION ====================
IMAGE_NAME = "Logo_Evos.png"  # Change this to your desired image
# ============================================================
```

### 4. Run the Application

```bash
python auto_sphere_art.py
```

### 5. Watch the Magic

The application will:
1. Load your configured image
2. Analyze the image for patterns and colors
3. Start creating spheres from the center of the screen
4. Animate each sphere growing from invisible to full size
5. Move spheres to their target positions to form your image pattern

## Controls

- **ESC**: Exit the application
- **SPACE**: Restart the animation with the same image

## Customization Options

### Image Selection
Simply change the `IMAGE_NAME` variable at the top of the file:
```python
IMAGE_NAME = "your_image.png"  # Use any image from assets/images/
```

### Sphere Parameters
Adjust these constants for different effects:
```python
SPHERE_SPACING = 8          # Distance between sphere sampling (lower = more detail)
MIN_SPHERE_RADIUS = 4       # Smallest sphere size
MAX_SPHERE_RADIUS = 12      # Largest sphere size
SPHERE_GROWTH_SPEED = 2.0   # How fast spheres grow
SPHERE_MOVE_SPEED = 0.12    # How fast spheres move to targets
CREATION_DELAY = 1          # Frames between creating new spheres
```

### Optimization for Different Image Types

**For detailed logos/complex images:**
- Set `SPHERE_SPACING = 6` or `8` for fine detail
- Use `MIN_SPHERE_RADIUS = 3` for ultra-precision
- Set `CREATION_DELAY = 1` for fast creation

**For simple shapes/artwork:**
- Set `SPHERE_SPACING = 12` for faster creation
- Use larger radius ranges like `8-18`
- Set `CREATION_DELAY = 3` for smoother animation

## How It Works

### Image Processing
1. **Image Loading**: Reads your image from assets/images/
2. **Scaling**: Automatically scales image to fit screen optimally
3. **Pattern Analysis**: Samples image at regular intervals
4. **Color Extraction**: Captures color information at each sample point
5. **Background Filtering**: Ignores white/transparent backgrounds

### Sphere Creation Algorithm
1. **Center Origin**: All spheres start from screen center (invisible)
2. **Progressive Growth**: Each sphere grows from 0 to target radius
3. **Target Movement**: After reaching full size, spheres move to image positions
4. **Adaptive Sizing**: Sphere size varies based on local image contrast
5. **Natural Ordering**: Spheres are created in order from center outward

### Physics Animation
- **Growth Animation**: Smooth radius increase with glow effects
- **Movement Physics**: Velocity-based movement to target positions
- **Boundary Checking**: Ensures spheres stay within screen bounds
- **Visual Effects**: Glow effects during growth phase

## Advanced Features

### Adaptive Sphere Sizing
The application analyzes local image characteristics:
- **Dark areas**: Use smaller spheres for fine detail
- **High contrast regions**: Use medium spheres for clarity
- **Uniform areas**: Use larger spheres for efficiency

### Performance Optimization
- **Smart sampling**: Only creates spheres for non-background pixels
- **Efficient rendering**: Optimized drawing operations
- **Memory management**: Proper cleanup and resource handling

## Troubleshooting

**Image not loading?**
- Check that your image is in the `assets/images/` folder
- Verify the filename matches exactly (case-sensitive)
- Ensure the image format is supported (PNG, JPG, JPEG)

**Animation too slow?**
- Increase `CREATION_DELAY` to reduce sphere density
- Increase `SPHERE_SPACING` to sample fewer points
- Use larger `MIN_SPHERE_RADIUS` for bigger spheres

**Animation too fast?**
- Decrease `CREATION_DELAY` to 1
- Decrease `SPHERE_SPACING` for more detail
- Increase `SPHERE_GROWTH_SPEED` for faster appearing

## Example Configurations

### For Logo_Evos.png (detailed logo):
```python
IMAGE_NAME = "Logo_Evos.png"
SPHERE_SPACING = 8
MIN_SPHERE_RADIUS = 4
MAX_SPHERE_RADIUS = 12
```

### For simple shapes:
```python
IMAGE_NAME = "smiley.png"
SPHERE_SPACING = 12
MIN_SPHERE_RADIUS = 6
MAX_SPHERE_RADIUS = 18
```

## Technical Requirements

- Python 3.7+
- Pygame 2.0.0+
- Pillow (PIL) for image processing
- NumPy for array operations

## License

This project is open source and available under the MIT License.
