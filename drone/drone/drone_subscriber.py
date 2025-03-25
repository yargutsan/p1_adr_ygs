import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class DronePositionSubscriber(Node):
    def __init__(self):
        super().__init__('drone_position_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            'drone_position',
            self.listener_callback,
            10)
        self.subscription  
        self.get_logger().info("Suscriptor de posición del dron iniciado.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Recibido: Lat={msg.latitude}, Lon={msg.longitude}, Alt={msg.altitude}")

def main(args=None):
    rclpy.init(args=args)
    node = DronePositionSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
