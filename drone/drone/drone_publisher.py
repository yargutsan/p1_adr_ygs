import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random

class DronePositionPublisher(Node):
    def __init__(self):
        super().__init__('drone_position_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'drone_position', 10)
        self.timer = self.create_timer(1.0, self.publish_position)
        self.get_logger().info("Publicador de posición del dron iniciado.")

    def publish_position(self):
        msg = NavSatFix()
        msg.latitude = random.uniform(-90, 90)    
        msg.longitude = random.uniform(-180, 180)
        msg.altitude = random.uniform(0, 1000)   

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publicando posición: Lat={msg.latitude}, Lon={msg.longitude}, Alt={msg.altitude}")

def main(args=None):
    rclpy.init(args=args)
    node = DronePositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
