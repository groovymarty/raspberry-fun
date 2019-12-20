from gpiozero import LEDBoard

class Snowman(LEDBoard):
    # Set up a Snowman using GPIO Zero to build a class.
    # To use:
    # snowman = Snowman() for a simple instance using LED class.
    # snowman = Snowman(pwm=True) for a version which can use PWM.
    # See example files in this repo for more examples of use...
    def __init__(self, pwm=False, initial_value=False, pin_factory=None):
        super(Snowman, self).__init__(
            face=LEDBoard(
                leftEye=23, rightEye=24, nose=25,
                pwm=pwm, initial_value=initial_value,
                _order=('leftEye', 'rightEye', 'nose'),
                pin_factory=pin_factory),
            body=LEDBoard(
                left=LEDBoard(
                    top=7, middle=8, bottom=9,
                    pwm=pwm, initial_value=initial_value,
                    _order=('top', 'middle', 'bottom'),
                    pin_factory=pin_factory),
                right=LEDBoard(
                    top=17, middle=18, bottom=22,
                    pwm=pwm, initial_value=initial_value,
                    _order=('top', 'middle', 'bottom'),
                    pin_factory=pin_factory),
                pwm=pwm, initial_value=initial_value,
                _order=('left', 'right'),
                pin_factory=pin_factory),
            pwm=pwm, initial_value=initial_value,
            _order=('face', 'body'),
            pin_factory=pin_factory
            )
