# port 6 is left and port 10 is right
left_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)   # Not reversed
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)  # Reversed

# velocity of motors
left_motor.set_velocity(50, PERCENT)
right_motor.set_velocity(50, PERCENT)

# Constants
TILE_DEGREES = 424  # i think this is how many degrees for one tile
TURN_TIME_90 = 0.6  # seconds to turn 90 degrees 

# Movement functions
def move_forward(tiles=1):
    degrees = TILE_DEGREES * tiles
    left_motor.spin_for(FORWARD, degrees, DEGREES, wait=False)
    right_motor.spin_for(FORWARD, degrees, DEGREES)

def turn_left():
    left_motor.spin(REVERSE)
    right_motor.spin(FORWARD)
    wait(TURN_TIME_90, SECONDS)
    left_motor.stop()
    right_motor.stop()

def turn_right():
    left_motor.spin(FORWARD)
    right_motor.spin(REVERSE)
    wait(TURN_TIME_90, SECONDS)
    left_motor.stop()
    right_motor.stop()

# i coded it like a grid because our grid was 3 by 4
def when_started1():
    move_forward(1)   # (3,1) → (2,1)

    turn_right()
    move_forward(2)   # (2,1) → (2,3)

    turn_left()
    move_forward(1)   # (2,3) → (1,3)

    turn_left()
    move_forward(1)   # (1,3) → (1,2)

    turn_left()
    move_forward(2)   # (1,2) → (3,2)

    turn_right()
    move_forward(1)   # (3,2) → (3,3)

when_started1()

# i need to sleep now this was quite tiring
