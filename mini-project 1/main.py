import os
import time as tm
import numpy as np
import matplotlib.pyplot as plt


#function to produce n normal random points in d dimensional hypersphere with radius r
def generateNormalRandomPointsInHypersphere(dimension, number_of_points, radius = 1):
    #generate n normal random d dimensional vectors
    points = np.random.normal(size = (dimension, number_of_points))
    #dividing each vector by its norm to scale them between -1 and 1
    points /= np.linalg.norm(points, axis = 0)
    #uniform random radius for making all points on the surface of balls within the unit ball equally likely
    r = np.random.uniform(low = 0.0, high = 1.0, size = number_of_points)
    r **= 1 / dimension
    result = radius * (points * r).T
    return result

#function to calculate std and norm of random generated vector in d dimensional space
def generateNormalRandomPointsInSpace(dimension, number_of_points):
    #generate n normal random d dimensional vectors
    points = np.random.normal(size = (number_of_points, dimension))
    return points

#function to calculate norms of each set
def getNorm(points: np.ndarray) -> np.array:
    norm = np.linalg.norm(points, axis = 1)
    return norm

#function to calculate innter products of each 2 vectors
def getInnerProduct(points: np.ndarray) -> dict:
    inner_prod = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                inner_prod.append(np.inner(points[i], points[j]))
    return inner_prod

#function to calculate std and norm of random generated vector in hypersphere
def interactiveMain():
    while True:
        d = int(input("Enter dimension of hypersphere: "))
        n = int(input("Enter number of random vectors to produce: "))
        points = generateNormalRandomPointsInHypersphere(d, n)
        norm = getNorm(points)
        inner_product = getInnerProduct(points)
        print("Average of norms is: " + str(np.average(norm)))
        print("Standard deviation of norms is: " + str(np.std(norm)))
        print("Average of inner products is: " + str(np.average(inner_product)))
        print("Standard deviation of inner products is: " + str(np.std(inner_product)))
        input("\n\nPress any key to restart...\n\n\n\n")
        #os.system("clear")

#plot std and norm of vectors in  unit hypersphere based on n and d
def graphMain():
    while True:
        d = int(input("Enter upper bound for dimension of hypersphere: "))
        n = int(input("Enter upper bound for number of random vectors to produce: "))
        xs = []
        ys = []
        z0s = []
        z1s = []
        z2s = []
        z3s = []
        for i in range(2, d + 1):
            for j in range(2, n + 1):
                xs.append(i)
                ys.append(j)
                points = generateNormalRandomPointsInHypersphere(i, j)
                norm = getNorm(points)
                inner_product = getInnerProduct(points)
                z0s.append(np.average(norm))
                z1s.append(np.std(norm))
                z2s.append(np.average(inner_product))
                z3s.append(np.std(inner_product))
        #####################
        fig0 = plt.figure()
        ax0 = fig0.add_subplot(111, projection='3d')
        ax0.scatter(xs,ys,z0s, c = "blue")
        ax0.set_xlabel("d")
        ax0.set_ylabel("n")
        ax0.set_zlabel("avg of norms")
        plt.show()
        #####################
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, projection='3d')
        ax1.scatter(xs,ys,z1s, c = "green")
        ax1.set_xlabel("d")
        ax1.set_ylabel("n")
        ax1.set_zlabel("std of norms")
        plt.show()
        #####################
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111, projection='3d')
        ax2.scatter(xs,ys,z2s, c = "black")
        ax2.set_xlabel("d")
        ax2.set_ylabel("n")
        ax2.set_zlabel("avg of inner products")
        plt.show()
        #####################
        fig3 = plt.figure()
        ax3 = fig3.add_subplot(111, projection='3d')
        ax3.scatter(xs,ys,z3s, c = "red")
        ax3.set_xlabel("d")
        ax3.set_ylabel("n")
        ax3.set_zlabel("std of inner products")
        plt.show()
        input("\n\nPress any key to restart...\n\n\n\n")


def main2():
    while True:
        d = int(input("Enter dimension: "))
        n = int(input("Enter number of random vectors to produce: "))
        points = generateNormalRandomPointsInSpace(d, n)
        norm = getNorm(points)
        inner_product = getInnerProduct(points)
        print("Average of norms is: " + str(np.average(norm)))
        print("Standard deviation of norms is: " + str(np.std(norm)))
        print("Average of inner products is: " + str(np.average(inner_product)))
        print("Standard deviation of inner products is: " + str(np.std(inner_product)))
        input("\n\nPress any key to restart...\n\n\n\n")

main2()