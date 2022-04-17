# class containing every generator
import math

class Generator():
    def __init__(self, seed):
        self.seed = seed
        self.first_seed = seed

    # random number generator of uniform distribution
    # additive generator
    def G_generator(self):
        a = 9765625 # 5^10
        c = 7151 # because GCD(2147483647, 7151) = 1
        m = pow(2, 31) - 1 # max integer value
        n = (a * self.seed + c) % m
        self.seed = n
        return n

    # random number generator of uniform distribution within the range (0,1)
    def J_generator(self):
        m = pow(2, 31) - 1 # max integer value
        n = (self.G_generator() + 1) / (m + 1)
        return n

    # Bernoulli distribution generator
    def B_generator(self, percentage):
        n = self.J_generator()
        if n <= percentage:
            return 1
        else:
            return 0

    # binomial distribution generator
    def D_generator(self, percentage, how_many):
        number_of_zeroes = 0
        number_of_ones = 0

        for i in range(0,how_many):
            result = self.B_generator(percentage)
            if result == 1:
                number_of_ones += 1
            else:
                number_of_zeroes += 1

        return number_of_ones


    # Poisson distribution generator
    def P_generator(self, lamb):
        number_of_events = -1
        next_probability = 1
        expected_value = math.exp(-lamb)
        while next_probability > expected_value:
            result = self.J_generator()
            next_probability *= result
            number_of_events += 1

        return number_of_events


    # exponential distribution generator
    def W_generator(self, lamb):
        result = self.J_generator()
        inverse_distribution = (-math.log(result))/lamb
        return inverse_distribution

    # normal distribution generator
    def N_generator(self, multiplier, addition):
        first_value = self.J_generator()
        second_value = self.J_generator()
        x = math.sqrt(-1 * math.log(1 - first_value))*math.cos(2 * math.pi * second_value)
        # y = math.sqrt(-1 * math.log(1 - first_value))*math.sin(2 * math.pi * second_value)
        result = multiplier * x + addition

        return result

    def reset_seed(self):
        self.seed = self.first_seed

    def change_seed(self, new_seed):
        self.seed = new_seed
        self.first_seed = new_seed