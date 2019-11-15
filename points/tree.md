- 决策树
    - ID3: 信息增益(H(D) - H(D|A))
        - ID3决策树偏向于取值较多的属性进行分割，存在一定的偏好
    - C4.5: 基于信息增益率准则选择最优分割属性的算法
        - 信息增益高于平均水平的属性，在从中选择增益率最高
    - CART: 基尼系数
- 随机森林
    - 数据的随机选取
    - 待选特征的随机选取
- Boost
    - AdaBoost
        - 初始化训练数据的权值分布: 相同
        - 抽样产生训练数据, 得到基分类器
        - 通过训练数据上的分类误差率, 计算其系数
        - 更新训练数据集的权值分布
        - 基本分类器的线性组合
    - GDBT
    - XGBoost
    - LightGBM