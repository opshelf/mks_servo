class InputRegisters:
    ENCODER_CARRY_VALUE = 0x30  # Length 3 words i32 i16
    ENCODER_ADDITION_VALUE = 0x31  # Length 3 words  i48
    REAL_TIME_MOTOR_SPEED = 0x32  # Length 1 word int16
    NUMBER_OF_PULSES = 0x33  # Length 2 words i32 
    IO_PORT_STATUS = (
        0x34  # Length 1 word u8 bit3 OUT_2, bit2 OUT_1, bit1 IN_2, bit0 IN_1
    )
    """The error is the difference between the angle you want to control minus the real-time angle of the motor, 0~51200 corresponds to 0~360°.for example, when the angle error is 1°, the return error is 51200/360= 142.222, and so on."""
    ERROR_ANGLE = 0x39  # Length 2 word i32
    EN_PIN_STATUS = 0x3A  # Length 1 word boolean 1 = enabled 0 = disabled
    GO_TO_ZERO_STATUS = 0x3B  # Length 1 word u8
    SHAFT_PROTECTION = 0x3E  # Length 1 word boolean 1 = protected 0 = not protected
    MOTOR_STATUS = 0xF1  # Length 1 word boolean 1 = protected 0 = not protected


class HoldingRegisters:
    RELEASE_SHAFT_PROTECTION = 0x3D  # Length 1 Word Boolean
    RESTORE_DEFAULT_PARAMETER = 0x3F  # Length 1 Word boolean
    CALIBRATE_MOTOR = 0x80  # Length 1 Word Boolean
    SET_WORK_MODE = 0x82  # Length 1 Word WorkMode
    SET_WORK_CURRENT = 0x83  # Length 1 Word u16
    SET_HOLD_CURRENT = 0x9B  # Length 1 Word u16 percentage 00 - 100 Only for OPEN mode and CLOSE mode, vFOC mode is invalid.
    SET_SUBDIVISION = 0x84  # Length 1 word Microstep setting
    SET_EN_LOGIC = (
        0x85  #  Length 1 word 00 active low, 01, active high, 02 active always
    )
    SET_DIR = 0x86  #  Length 1 word Motor Rotation
    SET_OFF_SCREEN = 0x87  # Length 1 word Boolean
    SET_ROTOR_LOCK_STATUS = 0x88  # Length 1 word Boolean 00 disabled 01 enabled
    SET_INTERPOLATION = 0x89  # Length 1 word Boolean 00 disabled 01 enabled
    SET_BAUDRATE = 0x8A  # Length 1 word u8 01-07
    SET_SLAVE_ADDRESS = 0x8B  # Length 1 word u8 01-07
    SET_KEYLOCK = 0x8F  # Length 1 word Boolean 00 unlocked 01 locked
    SET_AXIS_TO_ZERO = 0x92  # Length 1 word Boolean 01
    SET_SERIAL_MOTOR_MODE_ENABLE = 0xF3  # Length 1 word Boolean 00 unlocked 01 locked
    SET_HOME_PARAM = 0x90  # Length 3 words
    SET_LIMIT_PORT_REMAP = 0x9E  # Length 1 word Boolean 00 disabled 01 enabled
    ESTOP = 0xF7  # Length 1 word Boolean 01
    GO_HOME = 0x91  # Length 1 word Boolean 01
    SPEED_MODE = 0xF6  # Length 2 words
    MOVE_RELATIVE_PULSES = 0xFD  # Length 4 words
    MOVE_ABSOLUTE_PULSES = 0xFE  # Length 4 words
    MOVE_RELATIVE_AXIS = 0xF4  # Length 4 words
    MOVE_ABSOLUTE_AXIS = 0xF5  # Length 4 words
