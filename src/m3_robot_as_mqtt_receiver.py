"""
Using a Brickman (robot) as the receiver of messages.
"""
import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def say_it(self, left_speed, right_speed):
        print("Message received!", left_speed, right_speed)


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.
