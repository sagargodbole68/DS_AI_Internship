import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_csv('skewness_dataset.csv')

#task 1

plt.subplot(1,3,1)
sns.histplot(data['Heights'], kde=True)
plt.subplot(1,3,2)
sns.histplot(data['Income'], kde=True)
plt.subplot(1,3,3)
sns.histplot(data['ExamScores'], kde=True)
plt.tight_layout()
plt.show()
print("Heights Mean:", data['Heights'].mean())
print("Heights Median:", data['Heights'].median())
print()
print("Income Mean:", data['Income'].mean())
print("Income Median:", data['Income'].median())
print()
print("ExamScores Mean:", data['ExamScores'].mean())
print("ExamScores Median:", data['ExamScores'].median())


#task 2

mean = data["Heights"].mean()
std = data["Heights"].std()
data["z_score"]=(data["Heights"]-mean)/std
print(data["z_score"])
if (data["z_score"]>3).any():
    print("All are greater then 3")
else:
    print("All are not more then 3")
    
#task 3

means = []

for _ in range(1000):
    sample = np.random.choice(data["Income"], size=30)
    means.append(sample.mean())

sns.histplot(means,bins=30, kde = True)
plt.title("Distribution of Sample Means")
plt.show()