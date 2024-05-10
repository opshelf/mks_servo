from mks_servo import Servo, WorkMode, HomeTrigger, MotorRotation, EndLimit, limitportremap



class Axis(object):

    def __init__(self, name: str, address: int=1):
            self.name = name 
            self._address = address
            self._direction = MotorRotation.CCW
            self._current = 3000
            self._workmode = WorkMode.SR_vFOC
            self._position = -1

    @property
    def address(self):
        return self._address
    
    @property
    def direction(self):
        return self._direction

    @property
    def current(self):
        return self._current
    
    @property 
    def workmode(self):
        return self._workmode
    
    @property
    def position(self):
        return self._position

    
    @address.setter
    def address(self, address: int=1):
        self._address = address

    @direction.setter
    def direction(self, direction: MotorRotation):
        self._direction = direction

    @current.setter
    def current(self, current: int=1):
        self._current = current

    @workmode.setter
    def workmode(self, workmode: WorkMode):
        self._workmode = workmode

    @position.setter
    def position(self, position: int):
        self._position = position
    
class Robot(object):
       
    def __init__(self, port: str):
        self.axis_list = {str, Axis}
        self._Robot = Servo("/dev/tty.usbserial-AQ043LCZ", 0)

    def _get_axis(self, name: str):

        return self.axis_list.get(name)
    
    def _switch_axis(self, name: str):

        switch_axis= self._get_axis(name)
        self._Robot.address = switch_axis.address

        return switch_axis
    
    def add_axis(self, name: str, axis: Axis):
        
        self.axis_list[name] = axis

    def set_axis_work_mode(self, name: str, mode: WorkMode):
        switch_axis = self._switch_axis(name)
        switch_axis.workmode = mode
        self._Robot.set_work_mode(mode)
        
        return name, mode

    def set_axis_work_current(self, name: str, current: int):
        switch_axis = self._switch_axis(name)
        switch_axis.current = current
        self._Robot.set_work_current(current)
        
        return name, current
    
    def set_axis_dir(self, name: str, direction: MotorRotation):
        switch_axis = self._switch_axis(name)
        switch_axis.direction = direction
        self._Robot.set_motor_dir(direction)
        
        return name, direction

    
    def move_axis_by_position(self, name: str, acceleration: int, velocity: int, pulses: int, ):
        self._switch_axis(name)
        self._Robot.go_to_position(acceleration,velocity,pulses)
        self._Robot.wait_for_move_finished()

        return self._Robot.get_pulses()


    def move_axis_by_axis_position(self, name: str, acceleration: int, velocity: int, pulses: int, ):
        switch_axis = self._switch_axis(name)
        self._Robot.go_to_axis_position(acceleration,velocity,pulses)
        self._Robot.wait_for_move_finished()
        switch_axis.position = self._Robot.get_encoder_value_addition()
        
        return switch_axis.position
    
    def home_axis(self, name: str):
        self._switch_axis(name)
        self._Robot.go_home()
        self._Robot.wait_for_homing_finished()

    def stop_by_axis(self, name: str):
        self._switch_axis(name)
        self._Robot.stop()

    def stop_all_axis(self):
        for name in self.axis_list:
            self._switch_axis(name)
            self._Robot.stop()
        



                
        
        

