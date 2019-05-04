from math import log

class decisionTree:
    # 数据集：
    def createDataSet(self):
        dataSet = [[0, 0, 0, 0, 'no'],                        #数据集
                   [0, 0, 0, 1, 'no'],
                   [0, 1, 0, 1, 'yes'],
                   [0, 1, 1, 0, 'yes'],
                   [0, 0, 0, 0, 'no'],
                   [1, 0, 0, 0, 'no'],
                   [1, 0, 0, 1, 'no'],
                   [1, 1, 1, 1, 'yes'],
                   [1, 0, 1, 2, 'yes'],
                   [1, 0, 1, 2, 'yes'],
                   [2, 0, 1, 2, 'yes'],
                   [2, 0, 1, 1, 'yes'],
                   [2, 1, 0, 1, 'yes'],
                   [2, 1, 0, 2, 'yes'],
                   [2, 0, 0, 0, 'no']]
        labels = ['年龄', '有工作', '有自己的房子', '信贷情况']        #特征标签
        return dataSet, labels

    def calcShannonEnt(self, dataSet):
        numEntries = len(dataSet) #返回数据集的行数
        labelCounts = {}   #保存每个标签(Label)出现次数的字典
        for featVec in dataSet:
            currentLabel = featVec[-1]  #提取标签(Label)信息
            if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts: #计算香农熵
            prob = float(labelCounts[key])/numEntries
            shannonEnt -= prob * log(prob,2)
        return shannonEnt

    def splitDataSet(self, dataSet, axis, value):    #待划分的数据集、划分数据集的特征、特征的返回值
        retDataSet = []      #创建返回的数据集列表
        for featVec in dataSet:   #遍历数据集
            if featVec[axis] == value:
                reducedFeatVec = featVec[:axis]   #去掉axis特征
                reducedFeatVec.extend(featVec[axis+1:])    #将符合条件的添加到返回的数据集
                retDataSet.append(reducedFeatVec)
        return retDataSet

    def chooseBestFeatureToSplit(self, dataSet):
        numFeatures = len(dataSet[0]) - 1     #特征数量
        baseEntropy = self.calcShannonEnt(dataSet)    #计算数据集的香农熵
        bestInfoGain = 0.0      #信息增益
        bestFeature = -1    #最优特征的索引值
        for i in range(numFeatures):    #遍历所有特征
            featList = [example[i] for example in dataSet]
            uniqueVals = set(featList)  #创建set集合{},元素不可重复
            newEntropy = 0.0    #经验条件熵
            for value in uniqueVals:   #计算信息增益
                subDataSet = self.splitDataSet(dataSet, i, value)   #subDataSet划分后的子集
                prob = len(subDataSet) / float(len(dataSet))     #计算子集的概率
                newEntropy += prob * self.calcShannonEnt(subDataSet)  #根据公式计算经验条件熵
            infoGain = baseEntropy - newEntropy    #信息增益
            print("第%d个特征的增益为%.3f" % (i, infoGain)) #打印每个特征的信息增益
            if (infoGain > bestInfoGain):    #计算信息增益
                bestInfoGain = infoGain  #更新信息增益，找到最大的信息增益
                bestFeature = i   #记录信息增益最大的特征的索引值
        return bestFeature

    # 创建决策树：
    def majorityCnt(self, classList):
        classCount={}
        for vote in classList:    #统计classList中每个元素出现的次数
            if vote not in classCount.keys(): classCount[vote] = 0
            classCount[vote] += 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0] #返回classList中出现次数最多的元素

    def createTree(self, dataSet, labels, featLabels):
        classList = [example[-1] for example in dataSet]   #取分类标签(是否放贷:yes or no)
        if classList.count(classList[0]) == len(classList):   #如果类别完全相同则停止继续划分
            return classList[0]
        if len(dataSet[0]) == 1:   #遍历完所有特征时返回出现次数最多的类标签
            return majorityCnt(classList)
        bestFeat = self.chooseBestFeatureToSplit(dataSet)   #选择最优特征
        bestFeatLabel = labels[bestFeat]    #最优特征的标签
        featLabels.append(bestFeatLabel)
        myTree = {bestFeatLabel:{}}      #根据最优特征的标签生成树
        del(labels[bestFeat])     #删除已经使用特征标签
        featValues = [example[bestFeat] for example in dataSet]   #得到训练集中所有最优特征的属性值
        uniqueVals = set(featValues)  #去掉重复的属性值
        for value in uniqueVals:       #遍历特征，创建决策树。                       
            myTree[bestFeatLabel][value] = self.createTree(self.splitDataSet(dataSet, bestFeat, value), labels, featLabels)
        return myTree

if __name__ == '__main__':
    tree = decisionTree()
    dataSet, labels = tree.createDataSet()
    featLabels = []
    myTree = tree.createTree(dataSet, labels, featLabels)
    print(myTree) 