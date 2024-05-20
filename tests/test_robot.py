from robot import Robot, Axis
import time
if __name__ == "__main__":
    test_robot = Robot("/dev/tty.usbserial-AQ043LCZ")
    axis = Axis("test_z", 1)
    axis2 = Axis("test_x", 2)
    axis3 = Axis("test_y", 3)
    axis4 = Axis("claw", 4)
    test_robot.add_axis("test_z", axis)
    test_robot.add_axis("test_x", axis2)
    test_robot.add_axis("test_y", axis3)
    test_robot.add_axis("claw", axis4)
    test_robot.home_axis("test_y")
    test_robot.home_axis("test_x")
    time.sleep(1)
    test_robot.move_xz_axis_by_position("test_x", "test_y", 640000, 1280000, 200, 202)


    #test_robot.home_axis("test_z")
    #print("test_z_axis", test_robot.move_axis_by_axis_position("test_z", 100, 3000, -6000000))
    #print("z_axis", axis.position)
    
    #test_robot.home_axis("test_x")
    #print("test_x_axis", test_robot.move_axis_by_axis_position("test_x", 140, 3000, -6000000))
    #print("x_axis", axis2.position)
    '''
    test_robot.home_axis("test_y")
    print("test_y_axis", test_robot.move_axis_by_axis_position("test_y", 140, 3000, -16384))
    print("y_axis", axis3.position)

    time.sleep(4)
    print("test_y_axis", test_robot.move_axis_by_position("test_y", 140, 3000, -3200))
    print("y_axis", axis3.position)
    '''