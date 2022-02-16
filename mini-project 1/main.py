import os
import time as tm
import numpy as np
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

#function to calculate 
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
        print("Standard deviation of inner products is: " + str(np.average(inner_product)))
        input("\n\nPress any key to restart...\n\n\n\n")
        #os.system("clear")

#function
def graphMain():
    while True:
        d = int(input("Enter upper bound for dimension of hypersphere: "))
        n = int(input("Enter upper bound for number of random vectors to produce: "))
        
        for i in range(2, d + 1):
            for j in range(2, n + 1):
                points = generateNormalRandomPointsInHypersphere(i, j)
                norm = getNorm(points)
                inner_product = getInnerProduct(points)
                print("Average of norms is: " + str(np.average(norm)))
                print("Standard deviation of norms is: " + str(np.std(norm)))
                print("Average of inner products is: " + str(np.average(inner_product)))
                print("Standard deviation of inner products is: " + str(np.average(inner_product)))
                input("\n\nPress any key to restart...\n\n\n\n")

#interactiveMain()