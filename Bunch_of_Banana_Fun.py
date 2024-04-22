# -*- coding: utf-8 -*-
"""
Dataset: Banana Quality
https://www.kaggle.com/datasets/l3llff/banana/data

"""

#import packages
import matplotlib.pyplot as plt
import pandas as pd
import io

#load dataset
banana = pd.read_csv(r'banana_quality.csv')

#export table with column list in image format
buffer = io.StringIO()
banana.info(buf=buffer)
lines = buffer.getvalue().splitlines()
df = (pd.DataFrame([x.split() for x in lines[5:-2]], columns=lines[3].split())
       .drop('Count',axis=1)
       .rename(columns={'Non-Null':'Non-Null Count'}))

plt.close('all')

plt.axis('off')
plt.table(cellText=df.values,colWidths = [0.25]*len(df.columns),
      	rowLabels=df.index,
      	colLabels=df.columns,
      	cellLoc = 'center', rowLoc = 'center',
      	loc='top')
plt.savefig('01_info.png',bbox_inches="tight", dpi=150)

#export table with column description in image format
df2 = banana.describe().transpose()
plt.close('all')

plt.axis('off')
plt.table(cellText=df2.values,colWidths = [0.25]*len(df2.columns),
      	rowLabels=df2.index,
      	colLabels=df2.columns,
      	cellLoc = 'center', rowLoc = 'center',
      	loc='top')

plt.savefig('02_describe.png',bbox_inches="tight", dpi=150)

#Build a correlation matrix with numeric variables
banana_narrow = banana[['Size', 'Weight', 'Sweetness', 'Softness',
         'HarvestTime', 'Ripeness', 'Acidity']]
matrix = banana_narrow.corr()

plt.close('all')

plt.axis('off')
plt.table(cellText=matrix.values,colWidths = [0.25]*len(matrix.columns),
      	rowLabels=matrix.index,
      	colLabels=matrix.columns,
      	cellLoc = 'center', rowLoc = 'center',
      	loc='top')

plt.savefig('03_correlation.png',bbox_inches="tight", dpi=150)

#Export a correlation plot
alpha = ['Size', 'Weight', 'Sweetness', 'Softness',
         'HarvestTime', 'Ripeness', 'Acidity']

plt.close('all')
figure = plt.figure()
axes = figure.add_subplot(111)
caxes = axes.matshow(matrix, interpolation ='nearest')
figure.colorbar(caxes)
 
axes.set_xticklabels(['']+alpha, rotation = 50)
axes.set_yticklabels(['']+alpha, rotation = 50)
title_corr = 'Correlation Heatmap of Banana Characteristics'
plt.title( title_corr ) 
plt.savefig('04_heat.png',bbox_inches="tight", dpi=150)

#Export a boxplot of sweetness and quality
plt.close('all')
banana.boxplot(column='Sweetness', by='Quality', patch_artist=True, boxprops = dict(facecolor = "darkgrey"),medianprops = dict(color = "yellow", linewidth = 2))
title_boxplot = 'Sweetness Rating by Quality'
plt.title( title_boxplot )
plt.suptitle('') 
plt.grid(False)
plt.savefig('05_boxplot.png',bbox_inches="tight", dpi=150)

