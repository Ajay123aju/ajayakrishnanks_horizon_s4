import math

def calculateRoverJourney():
    print("--- Rover Navigation System ---")
    
    # Part C: Basic Error Handling for Inputs
    try:
        x1 = float(input("Enter origin X coordinate: "))
        y1 = float(input("Enter origin Y coordinate: "))
        x2 = float(input("Enter destination X coordinate: "))
        y2 = float(input("Enter destination Y coordinate: "))

        u = float(input("Enter initial velocity (m/s): "))
        a = float(input("Enter acceleration (m/s^2): "))
        vMax = float(input("Enter Max speed (m/s): "))
        
        if u < 0 or a < 0 or vMax <= 0:
            print("Error: Velocity, acceleration, and max speed must be positive values.")
            return 
        
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
        return

    # Part A: Calculate Distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Part B: Calculate Time
    # 1. Distance needed to reach top speed
    if a > 0:
         d_acc = (vMax**2 - u**2) / (2 * a)
    else:
         d_acc = float('inf') # If acceleration is 0, it never reaches a higher top speed

    time = 0
    if d_acc < distance:
          # Rover reaches top speed, then cruises
          timeToTopSpeed = (vMax - u) / a
          remainingDistance = distance - d_acc
          timeCruising = remainingDistance / vMax
          time = timeToTopSpeed + timeCruising
    else:
          # Rover never reaches top speed (constantly accelerating)
          # Using quadratic formula: 0.5*a*t^2 + u*t - distance = 0
          if a > 0:
                time = (-u + math.sqrt(u**2 - 4 * (0.5 * a) * (-distance))) / a
          else:
                time = distance / u # Constant speed if a=0


    # Output Results
    print(f"\nDistance to destination: {distance:.1f} m")
    print(f"Time required: {time:.1f} seconds")

if __name__ == "__main__":
    calculateRoverJourney()