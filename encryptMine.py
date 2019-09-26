import functools 
import operator
class encryptMine:  

    def __init__(self):
        self.n = 26
        self.m = 26    
        self.matrixAbc =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.dicc= dict(enumerate(self.matrixAbc))      
        self.fullMatrix = self.createMatrix(self.n,self.m)
        self.listNum = self.returnDic(self.n)
        self.zipObj = zip(self.matrixAbc, self.listNum)
        self.diccionario = dict(self.zipObj)

    def returnDic(self, n):
        listNums = [0] * n
        for x in range (n):
            listNums[x] = x
        return listNums

    def createMatrix(self, n,m):
        fullMatriz = [0] * n
        for x in range (n):
            fullMatriz[x] = [0] * m
        apuntador = 0   
        for i in range(0,n):
            for j in range(0,m):
                if(apuntador<m):                
                    fullMatriz[i][j] = self.matrixAbc[apuntador]
                    apuntador = apuntador+1
                   # print(apuntador)
                else:
                    apuntador = 0     
                    fullMatriz[i][j] = self.matrixAbc[apuntador]
                    apuntador = apuntador+1
            apuntador = i+1
        #print(fullMatriz)
        return fullMatriz

    def encryptMessage(self,clave, message):      
        i = 0
        messageE = ""
        while i < len(message):            
            for j in range(0,len(clave)):    
                if(i<len(message)):
                    posKey = self.diccionario[clave[j]]
                    posPlanetxt  = self.diccionario[message[i]]   
                    #print(clave[j],message[i],self.fullMatrix[posPlanetxt][posKey])
                    messageE = messageE + self.fullMatrix[posPlanetxt][posKey]
                    i = i+1        
        return(messageE)

    def decryptMessage(self,clave, message):      
            zipObjFull = zip(self.matrixAbc,self.fullMatrix)
            dictionary = dict(zipObjFull)
            messageDec = ""
            i = 0
            while i < len(message):  
                for j in range(0,len(clave)):    
                    if(i<len(message)): 
                        zipListEnumerate = zip(dictionary[clave[j]], self.listNum)
                        dictionaryKey = dict(zipListEnumerate)
                        messageDec = messageDec +self.dicc[dictionaryKey[message[i]]]
                        i = i+1  
          
            return messageDec
    
    def foundSecuencies(self,message):
        listNumbers = []
        listSequences = []
        for i in range(0,len(message)-1):
            for j in range(i,len(message)-1):
                if(j != i ):
                    strCurrent = message[i]+message[i+1]
                    strCompare = message[j]+message[j+1]
                    if(strCurrent == strCompare):
                         # print(strCurrent, strCompare, j-i)
                          strCurrent = message[i]+message[i+1]+message[i+2]
                          strCompare = message[j]+message[j+1]+message[i+2]
                          if(strCurrent == strCompare):                              
                              if not (j-i) in listNumbers:
                                  #print(strCurrent, strCompare, j-i)
                                  listNumbers.append(j-i)
                                  listSequences.append(strCurrent)
        zipListNumbers = zip(listNumbers, listSequences)
        dictionaryKey = dict(zipListNumbers)
        #print(dictionaryKey)
        listGCD = self.pickValuesToFoundGCD(self.countApparitions(dictionaryKey),dictionaryKey)
        print(listGCD)

    def GCD(self,a, b):
        if b == 0:
            return a
        else:
            return self.GCD(b, a % b)
    
    def countApparitions(self,zipListNumbers):
        listWtRepets = []
        listVals = list(zipListNumbers.values())
        listApparitions = []
        
        for i in range(0,len(listVals )):
            if not (listVals[i]) in listWtRepets:
                listWtRepets.append(listVals[i])

        for i in range(0,len(listWtRepets)):
            listApparitions.append(listVals.count(listWtRepets[i]))

        ziplistWtRepets = zip(listWtRepets, listApparitions)
        dictionaryWtRepets  = dict(ziplistWtRepets)
        sorted_dict = sorted(dictionaryWtRepets.items(), key=lambda kv: kv[1])
        sorted_dict = dict(sorted_dict)
        sortedValuesList = list(sorted_dict.keys())
        enumKeylist = dict(enumerate(sortedValuesList))    
        listToCombinations = {enumKeylist[len(enumKeylist)-1],enumKeylist[len(enumKeylist)-2],enumKeylist[len(enumKeylist)-3],enumKeylist[len(enumKeylist)-4]}
        return list(listToCombinations)
    

    def pickValuesToFoundGCD(self, combinations,zipListNumbers):
        listGCD = []
        listCombinations = [[combinations[0],combinations[1],combinations[2]],
                            [combinations[0],combinations[1],combinations[3]],
                            [combinations[0],combinations[2],combinations[3]],
                            [combinations[1],combinations[2],combinations[3]]]
        listCombinations = list(listCombinations)
        for i in range(0, len(listCombinations)):
            listToFoundGCD = []
            for j in range(0, len(listCombinations[0])):
                for k,v in zipListNumbers.items():                   
                    if(v == listCombinations[i][j]):
                        listToFoundGCD.append(k)
            listGCD.append(functools.reduce(self.GCD,listToFoundGCD))
        return listGCD
    #print(matrix, len(matrix[0]), len(matrix), matrix[0][len(matrix)-1], print(dicc["a"]))

        