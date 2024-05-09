from mks_servo import Servo, WorkMode, HomeTrigger, MotorRotation, EndLimit, limitportremap
import time
from threading import Thread
import datetime


if __name__ == "__main__":
    DEFAULT_ACCEL = 100
    DEFAULT_VELOCITY = 100
    servo1 = Servo("/dev/tty.usbserial-AQ043LCZ", 4)
    servo1.connect()
    servo1.set_work_mode(WorkMode.SR_vFOC)
    servo1.set_work_current(5000)
    servo1.go_home()
    servo1.wait_for_homing_finished()
    time.sleep(1)
    servo1.go_to_axis_position(200, 2000, -500000)
    servo1.wait_for_move_finished()
    print("close servo1", servo1.get_encoder_value_addition())
    servo1.close()
    time.sleep(1)
    servo2 = Servo("/dev/tty.usbserial-AQ043LCZ", 2)
    servo2.connect()
    servo2.go_to_axis_position(200, 2000, -50000)
    servo2.wait_for_move_finished()
    print("close servo2", servo2.get_encoder_value_addition())
    time.sleep(1)
    servo1.connect()
    servo1.set_work_mode(WorkMode.SR_vFOC)
    servo1.set_work_current(5000)
    servo1.go_home()
    servo1.wait_for_homing_finished()
    time.sleep(1)
    servo1.go_to_axis_position(200, 2000, -500000)
    servo1.wait_for_move_finished()
    print("close servo1", servo1.get_encoder_value_addition())
    '''
    time.sleep(1)
    print("home", servo.get_encoder_value_addition())
    time.sleep(1)
    for i in range(1,30):
        servo.go_to_position(240, 3000, -1000)
        servo.wait_for_move_finished()
        time.sleep(1)
        servo.go_to_position(240, 3000, -3000)
        servo.wait_for_move_finished()
        time.sleep(1)
        i = i + 1
    print("close", servo.get_encoder_value_addition())
    time.sleep(2)
    servo.go_to_position(100, 3000, 0)
    servo.wait_for_move_finished()
    time.sleep(2)
    print("open", servo.get_encoder_value_addition())
    servo.go_to_position(100, 3000, -1000)
    servo.wait_for_move_finished()
    '''
    '''
    servo.set_limit_port_remap(limitportremap.ENABLE)
    servo.set_work_mode(WorkMode.SR_vFOC)
    #servo.set_work_mode(WorkMode.SR_OPEN)
    # print(servo.read_work_current())
    servo.set_work_current(3000)
    servo.address = 2
    servo.set_work_mode(WorkMode.SR_vFOC)
    #servo.set_work_mode(WorkMode.SR_OPEN)
    # print(servo.read_work_current())
    servo.set_work_current(3000)
    servo.address = 1
    servo.go_home()
    servo.address = 2
    servo.go_home()
    servo.wait_for_homing_finished()
    time.sleep(5)
    servo.address = 1
    servo.go_to_position(200, 3000, 4000000)
    servo.address = 2
    servo.go_to_position(200, 3000, 2000000)
    servo.wait_for_move_finished()
    servo.address = 1
    print(servo.get_encoder_value_addition())
    servo.address = 2
    print(servo.get_encoder_value_addition())
    servo.address = 1
    time.sleep(4)
    servo.go_to_position(200, 3000, 0)
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    '''
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
    '''
    servo2.go_home()
    servo2.wait_for_homing_finished()
    servo.go_home()
    servo.wait_for_homing_finished()
    print(servo.get_encoder_value_addition())
    print(servo2.get_encoder_value_addition())
    time.sleep(4)
    servo.go_to_position(200, 3000, 4000000)
    servo2.go_to_position(200, 3000, 4000000)
    servo.wait_for_move_finished()
    servo2.wait_for_move_finished()
    print(servo.get_pulses())
    print(servo2.get_pulses())
    time.sleep(4)
    servo.go_to_position(200, 3000, 0)
    servo.wait_for_move_finished()
    print(servo.get_pulses())
    
    time.sleep(1)

    
    servo_speed = 0
    while True:
        if servo.get_real_time_speed() != servo_speed:
            print(servo.get_real_time_speed())
        servo_speed = servo.get_real_time_speed()
        if servo.get_real_time_speed() == 0:
            break
    '''
    '''
    encoder_position = 0
    while True:
        
        if servo.get_encoder_value_addition() != encoder_position:
            now = datetime.datetime.now().time()
            print(now, servo.get_encoder_value_addition())
        encoder_position = servo.get_encoder_value_addition()
        if servo.get_real_time_speed() == 0:
            break
    servo.wait_for_move_finished()
    print(servo.get_encoder_value_addition())
    print(servo.get_pulses())
    time.sleep(1)
    '''
    #servo.go_home()
    
    #servo.wait_for_homing_finished()
    #print(servo.get_encoder_value_addition())

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
