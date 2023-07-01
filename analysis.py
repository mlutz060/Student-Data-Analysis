import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Student_Performance.csv')
df = pd.DataFrame(data)

study_time = df["Hours Studied"].values
extra_act = df["Extracurricular Activities"].values
sleep = df["Sleep Hours"].values
p_index = df["Performance Index"].values

# Filtering
filter = df[["Hours Studied", "Performance Index"]]
print(filter)

bad_sleep = df["Sleep Hours"] < 4

# bad_sleep_score = df[bad_sleep, "Performance Index"]

print(bad_sleep)

# sort

best_to_worst_score = df.sort_values(by=['Performance Index'], ascending=False)
print(best_to_worst_score)

sleep_sort = df.sort_values(by=["Sleep Hours"], ascending=False)
print(sleep_sort)

# aggregate
# Aggregation: a whole formed by combining several (typically disparate) elements.

best_student = df.aggregate({"Performance Index": ['max']})

best_students_info = df.loc[df["Performance Index"] == 100.0]
print(best_students_info)

# graph
df.plot(x='Sleep Hours', y='Performance Index', kind='bar')
plt.title("Sleep vs Score")
plt.xlabel("Hours Slept")
plt.ylabel("Score index")
plt.show()