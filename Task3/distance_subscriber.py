import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class RoverDistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        
        # Subscribing to the '/distance' topic that the publisher uses
        self.subscriber = self.create_subscription(
            Int32,
            '/distance',
            self.distance_callback,
            10
        )

    def distance_callback(self, msg):
        print(f'Received distance: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistanceSubscriber()
    
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
