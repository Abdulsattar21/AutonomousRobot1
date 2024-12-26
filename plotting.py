import matplotlib.pyplot as mat 

class Plot: 

    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        mat.title = self.title
        mat.xlabel = self.xlabel
        mat.ylabel = self.ylabel

    def plotting(self, time, array_x, array_lable):
        self.time = time
        self.array_x = array_x
        self.array_lable = array_lable
        i = 0
        # for x in range(len(array_x)):
        for x in self.array_x:
            
            mat.plot(self.time, self.array_x[i], label= self.array_lable[i])
            i += 1
            mat.legend()
        mat.grid()
        mat.show()

         


     
