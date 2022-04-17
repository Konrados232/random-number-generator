import matplotlib
from Generator import Generator
from Test import Test

main_generator = Generator(454565756)
main_test = Test(main_generator)

"""
x = 0
for i in range(0, 999):
    main_generator.change_seed(i)
    if main_test.batch_test("G", 10000, 0, 0, 0, 0, 0) == True: # basic generator
        x += 1

print(x)
"""

# first batch of tests
main_test.G_histogram(10000) # basic generator
main_test.J_histogram(10000)
main_test.B_histogram(10000, 0.75)
main_test.B_histogram(10000, 0.15)
main_test.D_histogram(10000, 0.80, 30)
main_test.D_histogram(10000, 0.20, 100)
main_test.P_histogram(10000, 1)
main_test.P_histogram(10000, 5)
main_test.P_histogram(10000, 10)
main_test.W_histogram(10000, 10)
main_test.N_histogram(100000, -3, 10)
main_test.N_histogram(100000, 9765625, 7151)

# second batch of tests
main_generator.change_seed(246457877)
main_test.batch_test("G", 10000, 0, 0, 0, 0, 0)
main_test.batch_test("J", 10000, 0, 0, 0, 0, 0)
"""
main_test.G_histogram(10000) # basic generator
main_test.J_histogram(10000)
main_test.B_histogram(10000, 0.75)
main_test.B_histogram(10000, 0.15)
main_test.D_histogram(10000, 0.80, 30)
main_test.D_histogram(10000, 0.20, 100)
main_test.P_histogram(10000, 1)
main_test.P_histogram(10000, 5)
main_test.P_histogram(10000, 10)
main_test.W_histogram(10000, 10)
main_test.N_histogram(100000, -3, 10)
main_test.N_histogram(10000, 9765625, 7151)
"""

# third batch of tests
main_generator.change_seed(897654345)
main_test.batch_test("G", 10000, 0, 0, 0, 0, 0)
main_test.batch_test("J", 10000, 0, 0, 0, 0, 0)
"""
main_test.G_histogram(10000) # basic generator
main_test.J_histogram(10000)
main_test.B_histogram(10000, 0.75)
main_test.B_histogram(10000, 0.15)
main_test.D_histogram(10000, 0.80, 30)
main_test.D_histogram(10000, 0.20, 100)
main_test.P_histogram(10000, 1)
main_test.P_histogram(10000, 5)
main_test.P_histogram(10000, 10)
main_test.W_histogram(10000, 10)
main_test.N_histogram(100000, -3, 10)
main_test.N_histogram(10000, 9765625, 7151)
"""

# fourth batch of tests
main_generator.change_seed(986168) # 986167
main_test.batch_test("G", 10000, 0, 0, 0, 0, 0)
main_test.batch_test("J", 10000, 0, 0, 0, 0, 0)
"""
main_test.G_histogram(10000) # basic generator
main_test.J_histogram(10000)
main_test.B_histogram(10000, 0.75)
main_test.B_histogram(10000, 0.15)
main_test.D_histogram(10000, 0.80, 30)
main_test.D_histogram(10000, 0.20, 100)
main_test.P_histogram(10000, 1)
main_test.P_histogram(10000, 5)
main_test.P_histogram(10000, 10)
main_test.W_histogram(10000, 10)
main_test.N_histogram(100000, -3, 10)
main_test.N_histogram(10000, 9765625, 7151)
"""