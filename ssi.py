# import pandas as pd
# import random
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split as tts
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt
# import numpy as np
# import tkinter as tk
# from tkinter import ttk

# random_seed = 42
# random.seed(random_seed)
# np.random.seed(random_seed)

# class Data:
#     def __init__(self):
#         self.day = ['понедельник', 'вторник', 'среда',
#                     'четверг', 'пятница', 'суббота', 'воскресенье']
#         self.mood = ['веселое', 'грустное', 'спокойное', 'раздражительное']
#         self.task = ['спорт', 'учеба', 'отдых', 'уборка', 
#                     'работа', 'поесть', 'ничего']
#         self.advice = ['занимайся спортом', 'лучше сосредоточиться на учебе',
#                     'можешь отдохнуть', 'пора приступить к работе', 
#                     'можешь заняться уборкой', 'можешь поесть']
#         datas = []

#         for _ in range(100):
#             time = random.randint(0, 23)
#             day = random.choice(self.day)
#             mood = random.choice(self.mood)
#             task = random.choice(self.task)
        
#             if time > 18 and mood == 'раздражительное' and task != 'можешь поесть':
#                 advice = 'можешь отдохнуть'
#             elif time > 18 and task == 'можешь поесть':
#                 advice = 'можешь поесть'
#             elif time < 10 and mood in ['веселое', 'спокойное']:
#                 advice = 'пора приступить к работе'
#             elif time < 20 and task == 'спорт':
#                 advice = 'занимайся спортом'
#             elif mood in ['спокойное', 'веселое'] and task in ['учеба', 'отдых', 'ничего']:
#                 advice = 'лучше сосредоточиться на учебе'
#             elif 9 < time < 22 and task == 'уборка':
#                 advice = 'можешь заняться уборкой'
#             else:
#                 advice = 'пора приступить к работе'

#             datas.append([time, day, mood, task, advice])
        
#         self.datas = pd.DataFrame(datas, columns=['time', 'day', 'mood', 'task', 'advice'])

#         self.le_day = LabelEncoder()
#         self.le_mood = LabelEncoder()
#         self.le_task = LabelEncoder()
#         self.le_advice = LabelEncoder()

#         self.datas['day'] = self.le_day.fit_transform(self.datas['day'])
#         self.datas['mood'] = self.le_mood.fit_transform(self.datas['mood'])
#         self.datas['task'] = self.le_task.fit_transform(self.datas['task'])
#         self.datas['advice'] = self.le_advice.fit_transform(self.datas['advice'])
# dataset = Data()
# df = dataset.datas

# class Model:
#     def __init__(self, data_obj):
#         self.data_obj = data_obj
#         self.clf = DecisionTreeClassifier(random_state=random_seed)

#         self.x = df.drop('advice', axis=1)
#         self.y = df['advice']

#         self.x_train, self.x_test, \
#         self.y_train, self.y_test = tts(self.x, self.y, test_size = 0.2, random_state=42) 

#         self.clf.fit(self.x_train, self.y_train)
#         self.y_pred = self.clf.predict(self.x_test)

#         self.accuracy = accuracy_score(self.y_test, self.y_pred)
    
#     def tree(self):
#         print(self.accuracy)
#         plt.figure(figsize=(16, 10))
#         plot_tree(self.clf, feature_names=self.x.columns, filled=True)
#         plt.show()

#     def predict_advice(self, time, day, mood, task):
#         day = self.data_obj.le_day.transform([day])[0]
#         mood = self.data_obj.le_mood.transform([mood])[0]
#         task = self.data_obj.le_task.transform([task])[0]

#         self.data = pd.DataFrame([[time, day, mood, task]], columns=['time', 'day', 'mood', 'task'])
#         self.predict = self.clf.predict(self.data)[0]

#         self.text = self.data_obj.le_advice.inverse_transform([self.predict])[0]
#         return self.text


# model = Model(dataset)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Day Planner Helper')
#         self.geometry('480x330+450+150')
#         self.resizable(False, False)

#         self.label = tk.Label(self, text='Привет! Это твой умный советчик.' \
#                               '\nДля получения совета нужно будет указать несколько параметров')
#         self.label.pack(pady=10)

#         def answer():
#             try:
#                 self.tg = int(self.time_entry.get())
#                 if not (0 <= self.tg <= 23):
#                     self.advice.config(text='Ошибка: время должно быть от 0 до 23')
#                     return
                
#                 self.dg = self.day_combobox.get().lower()
#                 self.mg = self.mood_combobox.get().lower()
#                 self.tag = self.task_combobox.get().lower()

#                 if not all([self.dg, self.mg, self.tag]):
#                     self.advice.config(text='Пожалуйста, выберите все параметры')
#                     return

#                 self.advice.config(text=model.predict_advice(self.tg, self.dg, 
#                                                              self.mg, self.tag))
#             except ValueError:
#                 self.advice.config(text='Ошибка: введи корректное число во времени.')    
#             except Exception as e:
#                 print('Ошибка ввода:', e)

#         self.time_label = tk.Label(self, text='Для начала укажи свое время (0-23)').pack()
#         self.time_entry = tk.Entry(self)
#         self.time_entry.pack()

#         self.day_label = tk.Label(self, text='Отлично, теперь укажи свой день недели').pack()
#         self.day_combobox = ttk.Combobox(self, values=model.data_obj.day, state='readonly')
#         self.day_combobox.pack()

#         self.mood_label = tk.Label(self, text='Теперь выбери настроение, которое тебе ближе').pack()
#         self.mood_combobox = ttk.Combobox(self, values=model.data_obj.mood, state='readonly')
#         self.mood_combobox.pack()

#         self.task_label = tk.Label(self, text='Теперь выбери свою ближайюшую задачу').pack()
#         self.task_combobox = ttk.Combobox(self, values=model.data_obj.task, state='readonly')
#         self.task_combobox.pack()

#         self.advice = tk.Label(self, text='Здесь появится совет')
#         self.advice.pack()

#         self.advice_button = tk.Button(self, text='Запросить совет', command=answer).pack()
#         self.tree_button = tk.Button(self,text='Показать, как думает советчик', 
#                                      command=model.tree).pack()

        

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import os

print(os.path.abspath("ssi.py"))