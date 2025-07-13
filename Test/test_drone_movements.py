import random
import os
import time

def make_random_path(size):
     """Returns a random sequence of drone commands."""
     all_commands = ["ASCEND", "DESCEND", "FORWARD", "BACKWARD", "HOVER"]

     path = []
     for step in range(size):
         command = random.choice(all_commands)
         path.append(command)

     return path


def visualize_drone_movement(path, delay=0.5):
    """Visualizes the drone movement showing altitude and horizontal position with path trail."""
    # Starting position
    altitude = 5  # Start at middle altitude (0-10 scale)
    horizontal_pos = 10  # Start at middle horizontal position
    start_pos = (horizontal_pos, altitude)  # Remember starting position
    
    # Track the path history - use dictionary to overwrite old positions
    path_history = {}  # Key: (horizontal_pos, altitude), Value: command
    
    print("Drone Flight Visualization")
    print("=" * 40)
    print("Commands: ASCEND ↑, DESCEND ↓, FORWARD →, BACKWARD ←, HOVER ●")
    print("Trail shows path history with small dots")
    print("Press ENTER to advance to the next step...")
    print("=" * 40)
    input("Press ENTER to start the visualization...")
    
    for i, command in enumerate(path):
        os.system('cls')
        
        # Save current position before moving (will overwrite if position is revisited)
        path_history[(horizontal_pos, altitude)] = command
        
        # Update position based on command
        if command == "ASCEND":
            altitude = min(10, altitude + 1)
        elif command == "DESCEND":
            altitude = max(0, altitude - 1)
        elif command == "FORWARD":
            horizontal_pos = min(20, horizontal_pos + 1)
        elif command == "BACKWARD":
            horizontal_pos = max(0, horizontal_pos - 1)
        # HOVER doesn't change position
        
        # Display the visualization
        print(f"Step {i+1}/{len(path)} - Command: {command}")
        print("=" * 40)
        
        # Draw altitude scale and horizontal position
        for alt_level in range(10, -1, -1):
            line = f"{alt_level:2d} |"
            
            # Add horizontal position visualization
            for pos in range(21):
                if pos == horizontal_pos and alt_level == altitude:
                    line += "🚁"  # Current drone position
                elif alt_level == 0:
                    line += "▁"   # Ground level
                else:
                    # Check if this position is in the path history
                    trail_symbol = " "
                    if (pos, alt_level) in path_history:
                        trail_symbol = "·"  # Smaller dot for trail positions
                    line += trail_symbol
            
            print(line)
        
        # Horizontal position scale
        print("   +" + "-" * 21)
        scale_line = "   "
        for pos in range(0, 21, 5):
            scale_line += f"{pos:2d}   "
        print(scale_line)
        
        print(f"\nAltitude: {altitude}/10")
        print(f"Horizontal Position: {horizontal_pos}/20")
        print(f"Current Command: {command}")
        print(f"Unique positions visited: {len(path_history)}")
        
        # Wait for user input to continue (except on the last step)
        if i < len(path) - 1:
            input("\nPress ENTER for next step...")
        else:
            print("\nFlight complete! Press ENTER to see final path summary...")
            input()
            
    # Final path summary without drone icon
    end_pos = (horizontal_pos, altitude)
    os.system('cls')
    print("Final Flight Path Summary")
    print("=" * 40)
    print("🟢 = Start Position, 🔴 = End Position, · = Path Trail")
    print("=" * 40)
    
    # Draw final summary
    for alt_level in range(10, -1, -1):
        line = f"{alt_level:2d} |"
        
        for pos in range(21):
            if (pos, alt_level) == start_pos:
                line += "🟢"  # Start position
            elif (pos, alt_level) == end_pos and (pos, alt_level) != start_pos:
                line += "🔴"  # End position (only if different from start)
            elif alt_level == 0:
                line += "▁"   # Ground level
            else:
                # Check if this position is in the path history
                trail_symbol = " "
                if (pos, alt_level) in path_history:
                    # Don't show trail dots at start/end positions
                    if (pos, alt_level) != start_pos and (pos, alt_level) != end_pos:
                        trail_symbol = "·"
                line += trail_symbol
        
        print(line)
    
    print(f"\nStart Position: ({start_pos[0]}, {start_pos[1]})")
    print(f"End Position: ({end_pos[0]}, {end_pos[1]})")
    print(f"Total unique positions visited: {len(path_history)}")
    print(f"Total steps taken: {len(path)}")
    
    input("\nPress ENTER to exit...")


flight_path = make_random_path(15)
print(flight_path)

# Add visualization demo
print("\nStarting drone visualization in 3 seconds...")
time.sleep(3)
visualize_drone_movement(flight_path)

