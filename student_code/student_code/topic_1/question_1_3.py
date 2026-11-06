import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# TODO: Q1.3
class TutorialTopic_1_3(Node):
    def __init__(self):
        super().__init__('tutorial_node_q_1_3')
        ### STUDENT CODE HERE
        self.topic_publisher = self.create_publisher(
            msg_type = Int32,
            topic = '/tutorial/counter25',
            qos_profile=10
        )
        self.counter = 0

        ### END STUDENT CODE
        
        # This calls the function timer_callback every 0.01 second
        self.timer = self.create_timer(0.01, self.timer_callback)
    

    def timer_callback(self):
        ### STUDENT CODE HERE
        if self.counter < 26:
            value = Int32()
            value.data = self.counter
            self.counter += 1
            self.topic_publisher.publish(value)
        ### END STUDENT CODE
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TutorialTopic_1_3()
    rclpy.spin(node)
