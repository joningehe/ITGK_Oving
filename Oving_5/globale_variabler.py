from math import sqrt
def delA():
    GRAVITY = 9.81
    def set_gravity(gravity):
        global GRAVITY
        GRAVITY = gravity
        return GRAVITY

    def get_fall_time():
        d = float(input('Meter: '))
        tid = sqrt((2 * d) / set_gravity(float(input('Gravitasjonskonstant: '))))
        return (tid)

    print('Det tar', get_fall_time(), 'sekund for objektet å falle.')

delA()
