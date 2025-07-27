<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Sphere Drawings Project Instructions

This is a Python-based physics simulation project that creates artistic sphere drawings using Pygame. When working on this project:

## Code Style and Structure
- Follow Python PEP 8 conventions
- Use descriptive variable names for physics properties (velocity, acceleration, position)
- Maintain clear separation between physics logic, rendering, and user interaction
- Comment physics calculations and formulas for clarity

## Physics Simulation Guidelines
- Ensure physics calculations are frame-rate independent when possible
- Use proper vector mathematics for 2D physics
- Maintain energy conservation principles in collision detection
- Consider performance implications when adding new physics features

## Pygame Best Practices
- Use pygame.Surface for efficient rendering operations
- Implement proper event handling for user interactions
- Optimize drawing operations by minimizing surface operations
- Handle pygame initialization and cleanup properly

## Feature Development
- When adding new sphere properties, ensure they integrate with existing physics
- Maintain backwards compatibility with existing control schemes
- Add appropriate user feedback for new interactive features
- Consider visual clarity when implementing new rendering effects

## Testing and Debugging
- Test physics edge cases (boundary conditions, extreme velocities)
- Verify performance with varying numbers of spheres
- Ensure consistent behavior across different screen resolutions
- Test user interaction responsiveness under various conditions

## Code Organization
- Keep physics calculations in dedicated methods
- Separate rendering logic from game state updates
- Organize constants at the top of files for easy modification
- Use classes to encapsulate related functionality (Sphere, SphereDrawings)

When suggesting code improvements or new features, prioritize:
1. Code readability and maintainability
2. Physics accuracy and realism
3. Performance optimization
4. User experience enhancement
5. Visual appeal and artistic potential
