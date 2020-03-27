# 数据读取
# 从sklearn.datasets里导入手写体数字加载器
from sklearn.datasets import load_digits
X, y = load_digits(return_X_y=True)
print(X.shape)
print(y.shape)
# 从通过数据加载器获得手写体数字的数码图像数据，并储存在digits变量中
digits = load_digits()
# 监视数据规模和特征维度
print(digits.data.shape)
import matplotlib.pyplot as plt
plt.figure()
plt.matshow(digits.images[100])
print(digits.images[100])
plt.show()
# 数据分割
# 从sklearn.model_selection中导入rain_test_split用于分割数据
from sklearn.model_selection import train_test_split
# 随机选取75%的数据作为训练样本；其余25%的数据作为测试样本
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
print(y_train.shape)
print(y_test.shape)
# 数据标准化
# 从sklearn.preprocessing里导入数据标准化模块
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()  # 仍然需要对训练和测试的特征数据进行标准化
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
LogisticRegression
# 数字识别及预测
# 从sklearn.linear_model里导入LogisticRegression
from sklearn.linear_model import LogisticRegression

# 初始化
lgr = LogisticRegression(multi_class='auto', solver='liblinear')
# 进行模型训练
lgr.fit(X_train, y_train)
# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = lgr.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of LogisticRegression is:', lgr.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
SGDClassifier
# 数字识别及预测
# 从sklearn.linear_model里导入SGDClassifier
from sklearn.linear_model import SGDClassifier

# 初始化
sgdc = SGDClassifier()
# 进行模型训练
sgdc.fit(X_train, y_train)
# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = sgdc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of SGDClassifier is:', sgdc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
LinearSVC
# 数字识别及预测
# 从sklearn.svm里导入基于线性假设的支持向量机分类器LinearSVC
from sklearn.svm import LinearSVC

# 初始化线性假设的支持向量机分类器LinearSVC
lsvc = LinearSVC(max_iter=10000)
# 进行模型训练
lsvc.fit(X_train, y_train)
# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = lsvc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of Linear SVC is:', lsvc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
SVC
# 数字识别及预测
# 从sklearn.svm里导入支持向量机分类器SVC。
from sklearn.svm import SVC

# 初始化支持向量机分类器SVC。
svc = SVC()

# 进行模型训练
svc.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中。
y_predict = svc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评。
from sklearn.metrics import classification_report
print('The Accuracy of SVC is', svc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做
# 更加详细的分析
print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
NuSVC
# 数字识别及预测
# 从sklearn.svm里导入核支持向量机分类器NuSVC。
from sklearn.svm import NuSVC

# 初始化核支持向量机分类器NuSVC。
nusvc = NuSVC()

# 进行模型训练
nusvc.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中。
y_predict = nusvc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评。
from sklearn.metrics import classification_report
print('The Accuracy of NuSVC is', nusvc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做
# 更加详细的分析
print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
KNeighborsClassifier
# 数字识别及预测
# 从sklearn.neighnors里导入KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

# 初始化KNeighborsClassifier
neighbor = KNeighborsClassifier()
# 进行模型训练
neighbor.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = neighbor.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of KNeighborsClassifier is:',
      neighbor.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
GaussianNB
# 数字识别及预测
# 从sklearn.naive_bayes里导入GaussianNB
from sklearn.naive_bayes import GaussianNB

# 初始化GaussianNB
gsbayes = GaussianNB()
# 进行模型训练
gsbayes.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = gsbayes.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of GaussianNB is:', gsbayes.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
BernoulliNB
# 数字识别及预测
# 从sklearn.naive_bayes里导入BernoulliNB
from sklearn.naive_bayes import BernoulliNB

# 初始化BernoulliNB
bnlbayes = BernoulliNB()
# 进行模型训练
bnlbayes.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = bnlbayes.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of BernoulliNB is:', bnlbayes.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
DecisionTreeClassifier
# 数字识别及预测
# 从sklearn.tree里导入DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# 初始化DecisionTreeClassifier
dtc = DecisionTreeClassifier()
# 进行模型训练
dtc.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = dtc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of DecisionTreeClassifier is:', dtc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
RandomForestClassifier
# 数字识别及预测
# 从sklearn.ensemble里导入RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# 初始化RandomForestClassifier
rfc = RandomForestClassifier()
# 进行模型训练
rfc.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = rfc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of RandomForestClassifier is:', rfc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
GradientBoostingClassifier
# 数字识别及预测
# 从sklearn.ensemble里导入GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingClassifier

# 初始化GradientBoostingClassifier
gbc = GradientBoostingClassifier()
# 进行模型训练
gbc.fit(X_train, y_train)

# 利用训练好的模型对测试样本的数字类别进行预测，
# 预测结果储存在变量y_predict中
y_predict = gbc.predict(X_test)
# 性能分析
# 使用模型自带的评估函数进行准确性测评
from sklearn.metrics import classification_report
print('The Accuracy of GradientBoostingClassifier is:',
      gbc.score(X_test, y_test))

# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析

print(
    classification_report(y_test,
                          y_predict,
                          target_names=digits.target_names.astype(str)))
