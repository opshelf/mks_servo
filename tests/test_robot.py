from robot import Robot

if __name__ == "__main__":
    test_robot = Robot("/dev/tty.usbserial-AQ043LCZ")
    test_robot.add_axis("test_x", 4)
    test_robot.home_axis("test_x")
    print(test_robot.move_axis_by_axis_position("test_x", 100, 3000, -6000000))
