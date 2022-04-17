# class for tests and plots

import math
import matplotlib
import matplotlib.pyplot as plt
import statistics

from Generator import Generator

class Test():
    def __init__(self, generator):
        self.generator = generator


    def batch_test(self, gen, how_many, percentage, iterations, lamb, multiplier, addition):
        self.generator.reset_seed()

        arr = self.return_array_from_generator(gen, how_many, percentage, iterations, lamb, multiplier, addition)

        median = statistics.median(arr)

        alt_arr = self.symbolize_array(median, arr, how_many) # arrays with A and B symbols

        k = 1
        for i in range(0, len(alt_arr) - 1):
            if (alt_arr[i] == "A" and alt_arr[i+1] == "B") or (alt_arr[i] == "B" and alt_arr[i+1] == "A"):
                k += 1

        number_of_A = alt_arr.count("A")
        number_of_B = alt_arr.count("B")


        # standardization of normal distribution
        E = (2 * number_of_A * number_of_B) / how_many + 1
        D = (2 * number_of_A * number_of_B * (2 * number_of_A * number_of_B - how_many)) /\
            ((how_many - 1) * math.pow(how_many, 2))
        Z = (k - E) / (math.sqrt(D))


        if Z < 1.96 and Z > -1.96:
            print("Positive test result")
            return True
        else:
            print("Negative test result")
            return False


    def symbolize_array(self, median, arr, how_many):
        alr_arr = []

        for i in range(0, how_many):
            if arr[i] < median:
                alr_arr.append("A")
            if arr[i] > median:
                alr_arr.append("B")

        return alr_arr


    # generators histograms
    def G_histogram(self, how_many):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("G", how_many, 0, 0, 0, 0, 0)

        plt.hist(arr)
        plt.show()

    def J_histogram(self, how_many):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("J", how_many, 0, 0, 0, 0, 0)

        plt.hist(arr)
        plt.show()

    def B_histogram(self, how_many, percentage):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("B", how_many, percentage, 0, 0, 0, 0)

        plt.hist(arr)
        plt.show()

    def D_histogram(self, how_many, percentage, iterations):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("D", how_many, percentage, iterations, 0, 0, 0)

        plt.hist(arr)
        plt.show()

    def P_histogram(self, how_many, lamb):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("P", how_many, 0, 0, lamb, 0, 0)

        plt.hist(arr, 30)
        plt.show()

    def W_histogram(self, how_many, lamb):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("W", how_many, 0, 0, lamb, 0, 0)

        plt.hist(arr)
        plt.show()

    def N_histogram(self, how_many, multiplier, addition):
        self.generator.reset_seed()

        arr = self.return_array_from_generator("N", how_many, 0, 0, 0, multiplier, multiplier)

        plt.hist(arr)
        plt.show()


    def return_array_from_generator(self, gen, how_many, percentage, iterations, lamb, multiplier, addition):
        arr = []

        if gen == "G":
            for i in range(0, how_many):
                arr.append(self.generator.G_generator())
        if gen == "J":
            for i in range(0, how_many):
                arr.append(self.generator.J_generator())
        if gen == "B":
            for i in range(0, how_many):
                arr.append(self.generator.B_generator(percentage))
        if gen == "D":
            for i in range(0, how_many):
                arr.append(self.generator.D_generator(percentage, iterations))
        if gen == "P":
            for i in range(0, how_many):
                arr.append(self.generator.P_generator(lamb))
        if gen == "W":
            for i in range(0, how_many):
                arr.append(self.generator.W_generator(lamb))
        if gen == "N":
            for i in range(0, how_many):
                arr.append(self.generator.N_generator(multiplier, addition))

        return arr
