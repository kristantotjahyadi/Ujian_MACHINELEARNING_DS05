import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.svm import SVC


df = pd.read_csv('data.csv')
df.drop('Unnamed: 0',axis=1, inplace=True)
target = df[(df['Age'] <= 25) & (df['Overall'] >= 80) & (df['Potential'] >= 80)]
dfNonTarget = df.drop(list(target.index))
dfTarget = df.drop(list(dfNonTarget.index))
dfTarget['target'] = 1
dfNonTarget['target'] = 0
frames = [dfNonTarget, dfTarget]
dfFinal = pd.concat(frames,ignore_index=True)
dfFinal.drop(['ID','Name','Photo', 'Nationality', 'Flag', 'Club', 'Club Logo', 'Value', 'Wage', 'Special',
       'Preferred Foot', 'International Reputation', 'Weak Foot',
       'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position',
       'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until',
       'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause'],axis = 1,inplace = True)

x = dfFinal.drop('target', axis = 1)
y = dfFinal['target']
xtr, xts, ytr, yts = train_test_split(
    x,
    y,
    test_size = .2
)

scoreRNN = (round(np.mean(cross_val_score(
    RandomForestClassifier(n_estimators=100),xts,yts,cv=3)
    )*100,2))
scoreLR = (round(np.mean(cross_val_score(
    LogisticRegression(solver='lbfgs'),xts,yts,cv=3)
    )*100,2))
scoreSVC = (round(np.mean(cross_val_score(
    SVC(gamma='auto', probability=True),xts,yts,cv=3)
    )*100,2))

print(
    f'Hasil score model RandomForestClassifier : {scoreRNN}%' + '\n'
    f'Hasil score model LogisticRegression : {scoreLR}%' + '\n'
    f'Hasil score model SVC : {scoreSVC}%'
)

dataPemain = [
    {'Name':'Andik Vermansyah','Age':27,'Overall':87,'Potential':90},
    {'Name':'Awan Setho Raharjo','Age':22,'Overall':75,'Potential':83},
    {'Name':'Bambang Pamungkas','Age':38,'Overall':85,'Potential':75},
    {'Name':'Christian Gonzales','Age':43,'Overall':90,'Potential':85},
    {'Name':'Egy Maulana Vikri','Age':18,'Overall':88,'Potential':90},
    {'Name':'Evan Dimas','Age':24,'Overall':85,'Potential':87},
    {'Name':'Febri Hariyadi','Age':23,'Overall':77,'Potential':80},
    {'Name':'Hansamu Yama Pranata','Age':24,'Overall':82,'Potential':85},
    {'Name':'Septian David Maulana','Age':22,'Overall':83,'Potential':80},
    {'Name':'Stefano Lilipaly','Age':29,'Overall':88,'Potential':86},
]
dfPemain = pd.DataFrame(dataPemain)
columns = ['Name','Age','Overall','Potential']
dfPemain = dfPemain.reindex(columns=columns)

predict = []
model = RandomForestClassifier(n_estimators=100)
model.fit(xtr,ytr)
for i in dfPemain.values:
    prediksi = model.predict([i[1:]])[0]
    if prediksi == 0:
        predict.append('Tidak untuk di rekrut')
    else:
        predict.append('Cocok untuk di rekrut')
dfPemain['Target'] = predict
print(dfPemain)