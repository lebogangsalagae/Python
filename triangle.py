
    
def classify_by_angle(side_a, side_b, side_c):
        # Find largest side
        if side_c >= side_a and side_c >= side_b:
            value = pow(side_a, 2)+pow(side_b, 2)-pow(side_c, 2)
        elif side_b >= side_a and side_b >= side_c:
            value = pow(side_a, 2)+pow(side_c, 2)-pow(side_b, 2)
        else: 
            value = pow(side_b, 2)+pow(side_c, 2)-pow(side_a, 2)


        EPSILON = 0.00005 # Dealing with floating point, so working with a margin of +/- 5x10^-5.
        if abs(value) < EPSILON:
            # Right
            return 'right'
        elif value < 0:
            # Obtuse
            return 'obtuse'
        else:
            # Acute
            return 'acute'