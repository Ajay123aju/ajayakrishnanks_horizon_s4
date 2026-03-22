import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class RoverDistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        
        # Set up the publisher on the '/distance' topic. 
        # A queue size of 10 helps prevent dropped messages if the system lags.
        self.publisher = self.create_publisher(Int32, '/distance', 10)
        
        # Publishing new sensor data every 1 second
        publish_interval = 1.0  
        self.timer = self.create_timer(publish_interval, self.publish_random_distance)

    def publish_random_distance(self):
        msg = Int32()
        
        # Simulating a rover sensor reading a distance between 0 and 100.
        msg.data = random.randint(0, 100) 
        
        self.publisher.publish(msg)
        
        # Logging it on the publisher side , so we know that it's actively sending data.
        self.get_logger().info(f'Published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistancePublisher()
    
    try:
        # the spin() keeps the node running and checking for events.
        rclpy.spin(node) 
    except KeyboardInterrupt:
        # Allows us to cleanly exit the program
        pass
    finally:
        # Clean up the node before completely shutting down.
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
