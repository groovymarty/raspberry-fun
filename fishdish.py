from gpiozero import LEDBoard, Button, Buzzer

class FishDish(LEDBoard):
    # Set up a Fish Dish using GPIO Zero to build a class.
    # To use:
    # fishdish = FishDish() for a simple instance using LED class.
    # fishdish = FishDish(pwm=True) for a version which can use PWM.
    # See example files in this repo for more examples of use...
    def __init__(self, pwm=False, initial_value=False, pin_factory=None):
        super(FishDish, self).__init__(
            red=9, yellow=22, green=4,
            pwm=pwm, initial_value=initial_value,
            _order=('red','yellow','green'),
            pin_factory=pin_factory
            )
        self.button=Button(7)
        self.buzzer=Buzzer(8)
