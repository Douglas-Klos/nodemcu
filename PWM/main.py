import machine

pwm = machine.Pin(13)
pwm = machine.PWM(pwm)

pwm.duty(10) #bright
pwm.duty(1000) #dim