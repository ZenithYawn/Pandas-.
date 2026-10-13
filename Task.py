import pandas as pd
import numpy as np

np.random.seed(42)

first_names = [
    "Олександр", "Дмитро", "Максим", "Артем", "Богдан", "Владислав", "Денис", "Ярослав", "Андрій", "Олексій",
    "Анастасія", "Анна", "Софія", "Вікторія", "Марія", "Дарина", "Юлія", "Олена", "Катерина", "Наталія"
]

last_names = [
    "Коваленко", "Бондаренко", "Ткаченко", "Кравченко", "Ковальчук", "Шевченко", "Поліщук", "Бондар", "Ткач", "Мороз",
    "Марченко", "Лисенко", "Руденко", "Гаврилюк", "Кравчук", "Захарченко", "Мельник", "Савченко", "Петренко", "Павленко"
]

n_students = 100

names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(n_students)]
ages = np.random.randint(17, 25, size=n_students)
math_scores = np.random.randint(0, 101, size=n_students)
prog_scores = np.random.randint(0, 101, size=n_students)

df = pd.DataFrame({
    'Ім\'я': names,
    'Вік': ages,
    'Оцінка з математики': math_scores,
    'Оцінка з програмування': prog_scores
})

df['Середній бал'] = (df['Оцінка з математики'] + df['Оцінка з програмування']) / 2

high_achievers = df[df['Середній бал'] > 80]
print(high_achievers)

df['Status'] = np.where(df['Середній бал'] >= 75, 'Pass', 'Fail')

status_counts = df['Status'].value_counts()
print(status_counts)

df.to_csv('students_results.csv', index=False, encoding='utf-8-sig')