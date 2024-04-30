from mks_servo import Servo, WorkMode, HomeTrigger, MotorRotation, EndLimit
import time

if __name__ == "__main__":
    DEFAULT_ACCEL = 100
    DEFAULT_VELOCITY = 100
    servo = Servo("/dev/tty.usbserial-AQ043LCZ", 1)
    servo.set_work_mode(WorkMode.SR_OPEN)
    # print(servo.read_work_current())
    servo.set_work_current(1500)
    # servo.go_to_position(100, 100, 0)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, 3600)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, -3600)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, 3600)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # print(servo.home(HomeTrigger.HIGH, MotorRotation.CCW, 1000, EndLimit.ENABLE))
    servo.set_work_mode(WorkMode.SR_vFOC)

    servo.go_home()
    servo.wait_for_homing_finished()
    print(servo.get_encoder_value_addition())
    
    time.sleep(1)

    servo.go_to_position(200, 3000, 10000000)
    time.sleep(9)
    print(servo.get_real_time_speed())
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())

    time.sleep(1)

    servo.go_home()
    
    servo.wait_for_homing_finished()
    print(servo.get_encoder_value_addition())

    # time.sleep(1)
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, 0)
    ## servo.go_to_axis_position(100, 100, 0)
    # servo.wait_for_move_finished()
    # servo.go_to_position(100, 100, 7200)  # 1 REV
    ## servo.go_to_axis_position(100, 100, 3600)  # 1 REV
    # servo.wait_for_move_finished()
    # time.sleep(1)
    # print(servo.get_encoder_value_addition())
    ## time.sleep(1)
    ## print(servo.get_encoder_value_addition())
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_axis_position(100, 100, 3600)
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, 0)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_position(100, 100, 3600)
    # print(servo.get_encoder_value_addition())
    # servo.stop()
    # servo.set_axis_to_zero()
    """
    for i in range(0, 10):
        # servo.go_to_position(100, 100, 0)
        # servo.wait_for_move_finished()
        # print(servo.get_encoder_value_addition())
        # servo.go_to_position(100, 100, 3600)
        print(servo.go_to_position(100, 100, 3600 * i))
        servo.wait_for_move_finished()
        time.sleep(1)
    for i in range(10, 0):
        # servo.go_to_position(100, 100, 0)
        # servo.wait_for_move_finished()
        # print(servo.get_encoder_value_addition())
        # servo.go_to_position(100, 100, 3600)
        print(servo.go_to_position(100, 100, 3600 * i))
        servo.wait_for_move_finished()
        time.sleep(1)
    """

    '''
    servo.stop()
    servo.set_axis_to_zero()
    servo.go_to_position(100, 255, 0)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    servo.go_to_position(100, 255, 36000)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    servo.go_to_position(100, 255, 36000 * 2)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())

    servo.stop()
    servo.set_axis_to_zero()
    servo.go_to_position(100, 255, 0)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    servo.go_to_axis_position(100, 255, -36000)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    servo.go_to_axis_position(100, 255, -36000 * 2)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    time.sleep(2)

    '''

    # servo.stop()
    # servo.set_axis_to_zero()
    # time.sleep(1)
    # servo.go_to_axis_position(100, 100, 0)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_axis_position(100, 100, 12800)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())
    # servo.go_to_axis_position(100, 100, 12800 * 2)
    # servo.wait_for_move_finished()
    # print(servo.get_encoder_value_addition())

    # print(servo.go_to_position(100, 100, 3600 * i))
    # servo.wait_for_move_finished()
