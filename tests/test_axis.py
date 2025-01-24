from mks_servo import Servo, WorkMode, Enabled
import time


if __name__ == "__main__":
    DEFAULT_ACCEL = 100
    DEFAULT_VELOCITY = 100
    servo1 = Servo("/dev/tty.usbserial-B0019LTE", 1)
    #servo1 = Servo("/dev/tty.usbserial-AQ043LCZ", 1)
    #servo1 = Servo("/dev/tty.usbserial-AQ043LCZ", 1)
    servo1.connect()
    print("Get Encoder Value Addition",servo1.get_encoder_value_addition())
    print("Pulses",servo1.get_pulses())
    print("Lock Protection",servo1.set_shaft_locked(Enabled.ENABLE))
    #servo1.set_work_mode(WorkMode.CR_OPEN)
    #servo1.set_work_mode(WorkMode.SR_CLOSE)
    #servo1.set_work_mode(WorkMode.CR_CLOSE)
    servo1.set_work_mode(WorkMode.CR_CLOSE)
    print("Rotor Lock",servo1.get_rotor_lock())
    print("Motor Status",servo1.get_motor_status())
    print("Enabled",servo1.get_enabled())
    if servo1.get_rotor_lock() == [1]:
        servo1.release_rotor_lock()
    servo1.set_work_current(600)
    """
    servo1.set_shaft_locked(Enabled.ENABLE)
    servo1.set_axis_to_zero()
    while True:
        time.sleep(1)
        print(servo1.get_rotor_lock())
        print(servo1.get_pulses())
    """
