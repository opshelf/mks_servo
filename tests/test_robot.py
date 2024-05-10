from robot import Robot, Axis

if __name__ == "__main__":
    test_robot = Robot("/dev/tty.usbserial-AQ043LCZ")
    axis = Axis("test_z", 1)
    axis2 = Axis("test_x", 2)
    axis3 = Axis("test_y", 3)
    test_robot.add_axis("test_z", axis)
    test_robot.home_axis("test_z")
    print(test_robot.move_axis_by_axis_position("test_z", 100, 3000, -6000000))
    
    test_robot.add_axis("test_x", axis2)
    test_robot.home_axis("test_x")
    print(test_robot.move_axis_by_axis_position("test_x", 140, 3000, -6000000))

    test_robot.add_axis("test_y", axis3)
    test_robot.home_axis("test_y")
    print(test_robot.move_axis_by_axis_position("test_y", 140, 3000, -6000000))