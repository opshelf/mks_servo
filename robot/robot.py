from mks_servo import Servo, WorkMode


    
class Robot(object):
    
    class Axis(object):

        def __init__(self, name: str, address: int=1):
            self.name = name 
            self._address = address

        @property
        def address(self):
            return self._address
    
    def __init__(self, port: str):
        self.axis_list = {}
        self._Robot = Servo("/dev/tty.usbserial-AQ043LCZ", 0)

    def add_axis(self, name: str, address: int=1):
        
        self.axis_list[name] = self.Axis(name, address)

    def _get_axis(self, name: str):

        return self.axis_list.get(name)
    
    def _switch_axis(self, name: str):
        switch_axis= self._get_axis(name)
        axis_address = switch_axis.address
        self._Robot.address = axis_address

        return self._Robot.address

    def set_axis_work_mode(self, name: str, mode: WorkMode):
        self._switch_axis(name)
        self._Robot.set_work_mode(mode)

        return name, mode

    def set_axis_work_current(self, name: str, current: int):
        self._switch_axis(name)
        self._Robot.set_work_current(current)

        return name, current
    
    def move_axis_by_position(self, name: str, acceleration: int, velocity: int, pulses: int, ):
        self._switch_axis(name)
        self._Robot.go_to_position(acceleration,velocity,pulses)
        self._Robot.wait_for_move_finished()

        return self._Robot.get_pulses()


    def move_axis_by_axis_position(self, name: str, acceleration: int, velocity: int, pulses: int, ):
        self._switch_axis(name)
        self._Robot.go_to_axis_position(acceleration,velocity,pulses)
        self._Robot.wait_for_move_finished()

        return self._Robot.get_encoder_value_addition()
    
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
        



                
        
        

