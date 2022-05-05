from matplotlib import pyplot

pyplot.bar([1,2,3,4],[4200,1595,2150,3800])
pyplot.xlabel("bridges")
pyplot.ylabel("heights")

pyplot.xticks([1,2,3,4],
              ["Golden Gate","Brooklin","Delaware Memorial",
               "Mackinac"])

pyplot.show()

            
