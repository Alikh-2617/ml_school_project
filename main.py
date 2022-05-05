import pandas as pd
import numpy as np
import collections as counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn import metrics

def info_print(value, gender):
    print('-'*60)
    print('the T-shirt size which KNN ML choosed: ')
    print(f'---> Size : {value} \n'
          f'---> Still : {gender}')


def choes(x , gender):
    x = int(x)
    if (gender=='male'):
        for key, value in male_chest_size.items():
            if (x in value):
                for key1, value1 in size.items():
                    if (key1 == key):
                        info_print(value1, gender)

    else:
        for key, value in female_chest_size.items():
            if (x in value):
                for key1, value1 in size.items():
                    if (key1 == key):
                        info_print(value1, gender)



def ml(stature, weight, gender):
    res = []
    data = pd.read_csv(f'{gender}_new_data.csv')
    x = pd.DataFrame(data, columns=['stature', 'weightkg']).values
    y = data.chestbreadth.values.reshape(-1, 1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    neighbors_range = range(1 ,21)
    for neighbors in neighbors_range:
        clfi1 = KNeighborsClassifier(neighbors)
        clfi1.fit(x_train, y_train.ravel())
        y_pridc1 = clfi1.predict(x_test)
        res.append(int(y_pridc1[0]))
    most = [element for element,count in Counter(res).most_common()]
    x3 = most[0]/10
    print('the processing is on going please wait...')
    choes(x3, gender)



def main():
    print('*' * 60)
    print('Hi !\nwe can help you to which T-shirt size you maybe have !! ')
    print('-' * 60)
    while (True):
        stature = input('Please enter your Stature in CM : ')
        weight = input('Please enter your Weight in kg : ')
        gender = input('Are you Female or male ? : ')
        if stature.strip().isdigit():
            if weight.strip().isdigit():
                if gender.isalpha():
                    if gender == 'm':
                        gender = 'male'
                        break
                    if gender == 'f':
                        gender = 'female'
                        break
        print('Please inter right info and try again ..!')

    print('Please wait to process be done ...')
    ml(stature, weight, gender)

size = {
    0: 'XXX Small',
    1: 'XX Small',
    2: 'X Small',
    3: 'Small',
    4: 'Medium',
    5: 'Large',
    6: 'X Large',
    7: 'XX Large',
    8: 'XXX Large',
    9: 'XXXX Large'
}
male_chest_size = {
    0: [36, 37],
    1: [38, 39],
    2: [40, 41],
    3: [42, 43],
    4: [44, 45],
    5: [46, 47],
    6: [48, 49],
    7: [50, 51],
    8: [52, 53],
    9: [54, 55]
}
female_chest_size = {
    0: [36, 37],
    1: [38, 39],
    2: [40, 41],
    3: [42, 43],
    4: [44, 45],
    5: [46, 47],
    6: [48, 49],
    7: [50, 51],
    8: [52, 53],
    9: [54, 55]
}

female_chest_size = {
    0: range(0, 36),
    1: range(36, 39),
    2: range(40, 42 ),
    3: range(42, 43),
    4: range(44, 46),
    5: range(46, 48),
    6: range(48, 50),
    7: range(50, 52),
    8: range(53, 58),
    9: range(58, 100)
}

male_chest_size = {
    0: range(0, 36),
    1: range(36, 39),
    2: range(40, 42 ),
    3: range(42, 43),
    4: range(44, 46),
    5: range(46, 48),
    6: range(48, 50),
    7: range(50, 52),
    8: range(53, 58),
    9: range(58, 100)
}
legngth_size_mape_f = {
    0: range(0 , 61),
    1: range(61, 63),
    2: range(63, 65),
    3: range(65, 67),
    4: range(67, 70),
    5: range(70, 71),
    6: range(71, 72),
    7: range(72, 74),
    8: range(75, 77),
    9: range(77,100)
}
legngth_size_mape_m = {
    0: range(0 , 61),
    1: range(61, 63),
    2: range(63, 65),
    3: range(65, 67),
    4: range(67, 70),
    5: range(70, 71),
    6: range(71, 72),
    7: range(72, 74),
    8: range(75, 77),
    9: range(77,100)
}

if __name__ == '__main__':
    print(main())



