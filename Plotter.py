import numpy as np
import math
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
#%matplotlib inline

data = pd.read_csv('ResultFixed.csv', sep=';')


method = data['Method']
size = data['Size']
r_time = data['Run Time']
arity = data['Arity']
r = data['R']
msq = data['Mean-squared Error']
d_time = data['Delta Time']

# Prepare Data
# Create as many colors as there are unique midwest['category']
# categories = np.unique(data['Method'])
# colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
#
# # Draw Plot for Each Category
# plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
#
# for i, category in enumerate(categories):
#     plt.scatter('Size', 'Run Time',
#                 data=data.loc[data.Method == category, :],
#                 s=60, c=colors[i], label=str(category))
#
# # Decorations
# plt.gca().set(xlim=(4, 15), ylim=(0.01, 8000),
#               xlabel='Number of Nodes', ylabel='Run Time')
#
# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Scatterplot of Network Size vs Run Time", fontsize=22)
# plt.legend(fontsize=12)
# plt.yscale('log')
# plt.show()

# # Plot
# sns.set_style("white")
# gridobj = sns.lmplot(x="Arity", y="Run Time", hue="Method", data=data,
#                      height=7, aspect=1.6, robust=True, palette='tab10',
#                      scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
#
# # Decorations
# gridobj.set(xlim=(0, 10), ylim=(0, 8000))
# plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
# plt.show()

# # Draw Stripplot
# fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
# sns.stripplot(data['Arity'], data['Run Time'], jitter=0.25, size=8, ax=ax, linewidth=.5)
#
# # Decorations
# plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
# plt.show()

#
# # Draw Plot
# plt.figure(figsize=(13,10), dpi= 80)
# sns.boxplot(x='Method', y='Run Time', data=data, notch=False)
#
# # Add N Obs inside boxplot (optional)
# def add_n_obs(df,group_col,y):
#     medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
#     xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
#     n_obs = df.groupby(group_col)[y].size().values
#     for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
#         plt.text(x, medians_dict[xticklabel]*1.01, "#obs : "+str(n_ob), horizontalalignment='center', fontdict={'size':14}, color='white')
#
# add_n_obs(data,group_col='Method',y='Run Time')
#
# # Decoration
# plt.title('Box Plot of BE vs MB', fontsize=22)
# plt.ylim(0.0001, 8000)
# plt.yscale('log')
# plt.show()
#
# # Draw Stripplot
# fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
# sns.stripplot(data['R'], data['Run Time'], jitter=0.25, size=8, ax=ax, linewidth=.5)
#
# # Decorations
# plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
# plt.show()
#
# Draw Plot for Each Category
# plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
#
# for i, category in enumerate(categories):
#     plt.scatter('Run Time', 'Mean-squared Error',
#                 data=data.loc[data.Method == category, :],
#                 s=20, c=colors[i], label=str(category))
#
# # Decorations
# plt.gca().set(xlim=(0.0, 1500), ylim=(0, 0.2),
#               xlabel='Run Time', ylabel='Mean-squared Error')
#
# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Scatterplot of Time vs error", fontsize=22)
# plt.legend(fontsize=12)
# plt.show()

# # Plot
# for elem in data['Arity']:
#     if not math.isnan(elem):
#         elem = int(elem)
# sns.set_style("white")
# gridobj = sns.lmplot(x="Run Time", y="Mean-squared Error", hue="Arity", data=data,
#                      height=7, aspect=1.6, robust=True, palette='tab10',
#                      scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
#
# # Decorations
# gridobj.set(xlim=(0.01, 200), ylim=(0, 0.2))
# plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
# plt.xscale('log')
# plt.show()


# Plot

be_data = data[data.Method != 'MB']
mb_data = data[data.Method != 'BE']
# Prepare Data

ratio = [i.R / i.Arity for index, i in mb_data.iterrows()]

mb_data.insert(3, 'Ratio', ratio, True)

print(mb_data.head())
# Create as many colors as there are unique midwest['category']
categories = np.unique(mb_data['Size'])

n = len(categories)
colors = sns.color_palette('Blues', n)

# Draw Plot for Each Category
# Plot
sns.set_style("white")
gridobj = sns.regplot(x="Ratio", y="Mean-squared Error",  data=mb_data, robust=True,
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0, 1), ylim=(0, 0.15))
plt.title("Best Fit for Ratio vs. Error", fontsize=20)
plt.show()
