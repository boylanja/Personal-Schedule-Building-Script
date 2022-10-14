'''
data regarding each classes time slot
first number = day of the week
second number = start time
third number = length of class

not my actual classes btw
'''

algo = [ [0, 15, 3], [0, 9, 3], [2, 10, 3] ]

linux = [ [[2, 13, 2], [4, 9, 2]], 
        [[2, 16, 2], [4, 16, 2]], 
        [[1, 8, 2], [3, 8, 2]] ]

prog = [ [[2, 17, 2], [4, 17, 2]], 
      [[1, 10, 2], [3, 10, 2]], 
      [[0, 15, 2], [3, 15, 2]] ]

stats = [ [[0, 13, 2], [2, 13, 2]], 
      [[3, 11, 2], [4, 11, 2]], 
      [[0, 9, 2], [1, 15, 2]] ]

dbase = [ [0, 8, 3], [2, 12, 3], [4, 9, 3] ]


time = 8 #keeps track of time that is printed on screen
count = 0 #keeps track of number of schedules generated
rows, cols = (13, 5) #number of rows & columns
matrix = [["-----" for i in range(cols)] for j in range(rows)] #make a 5 by 13 2d array

#-------------------------------algorithms
for a in range(len(algo)):
  #reset matrix
  valid = True 
  matrix = [["-----" for i in range(cols)] for j in range(rows)]

  #look for and remove prev. instances of this class on sched
  matrix = [[val.replace("algo", "-----") for val in row] for row in matrix]

  #check if slot can  be added
  for j in range(algo[0][2]):
    if matrix [algo[a][1]-8+j] [algo[a][0]] != "-----":
      valid = False #sched isn't valid
  if valid == False:
    continue
  
  for j in range(algo[0][2]):
    if valid == True: #if sched is valid
      matrix [algo[a][1]-8+j] [algo[a][0]] = "algo" #add to sched
  #-------------------------------database
  for d in range(len(dbase)):
    #look for and remove prev. instances of this class on sched
    valid = True
    matrix = [[val.replace("dbase", "-----") for val in row] for row in matrix]

    #check if slot can be added
    for j in range(dbase[0][2]):
      if matrix [dbase[d][1]-8+j] [dbase[d][0]] != "-----":
        valid = False #sched isn't valid
    if valid == False:
      continue
    for j in range(dbase[0][2]):
      if valid == True: #if sched is valid
        matrix [dbase[d][1]-8+j] [dbase[d][0]] = "dbase" #add to sched    
    time = 8 #reset time
    #-------------------------------linux
    for l in range(len(linux)):
      #look for and remove prev. instances of this class on sched
      valid = True
      matrix = [[val.replace("linux", "-----") for val in row] for row in matrix]
  
      #check if slot can be added
      for j in range(linux[0][0][2]):
        if matrix [linux[l][0][1]-8+j] [linux[l][0][0]] != "-----":
          valid = False #sched isn't valid
      for j in range(linux[0][0][2]):
        if matrix [linux[l][1][1]-8+j] [linux[l][1][0]] != "-----":
          valid = False #sched isn't valid
      if valid == False:
        continue
      
      for j in range(linux[0][0][2]):
        if valid == True: #if sched is valid
          matrix [linux[l][0][1]-8+j] [linux[l][0][0]] = "linux" #add to sched
          matrix [linux[l][1][1]-8+j] [linux[l][1][0]] = "linux" #add to sched
      #-------------------------------programming
      for p in range(len(prog)):
        #look for and remove prev. instances of this class on sched
        valid = True
        matrix = [[val.replace("progr", "-----") for val in row] for row in matrix]
    
        #check if slot can be added
        for j in range(prog[0][0][2]):
          if matrix [prog[p][0][1]-8+j] [prog[p][0][0]] != "-----":
            valid = False #sched isn't valid
        for j in range(prog[0][0][2]):
          if matrix [prog[p][1][1]-8+j] [prog[p][1][0]] != "-----":
            valid = False #sched isn't valid
        if valid == False:
          continue
        
        for j in range(prog[0][0][2]):
          if valid == True: #if sched is valid
            matrix [prog[p][0][1]-8+j] [prog[p][0][0]] = "progr" #add to sched
            matrix [prog[p][1][1]-8+j] [prog[p][1][0]] = "progr" #add to sched
        #-------------------------------stats
        for s in range(len(stats)):
          #look for and remove prev. instances of this class on sched
          valid = True
          matrix = [[val.replace("stats", "-----") for val in row] for row in matrix]
      
          #check if slot can be added
          for j in range(stats[0][0][2]):
            if matrix [stats[s][0][1]-8+j] [stats[s][0][0]] != "-----":
              valid = False #sched isn't valid
          for j in range(stats[0][0][2]):
            if matrix [stats[s][1][1]-8+j] [stats[s][1][0]] != "-----":
              valid = False #sched isn't valid
          if valid == False:
            continue
          
          for j in range(stats[0][0][2]):
            if valid == True: #if sched is valid
              matrix [stats[s][0][1]-8+j] [stats[s][0][0]] = "stats" #add to sched
              matrix [stats[s][1][1]-8+j] [stats[s][1][0]] = "stats" #add to sched
          time = 8 #reset time
          if valid == True:
            for l in matrix: # print schedule
              print(time, l)
              time += 1
          print(count, "\n")
          count += 1