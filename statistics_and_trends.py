"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

def plot_relational_plot(df):
    sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
    plt.title('Relational Plot: Sepal Length vs Sepal Width')
    plt.savefig('relational_plot.png')
    plt.close()
    return

def plot_categorical_plot(df):
    sns.barplot(data=df, x='species', y='petal_length', estimator=np.mean)
    plt.title('Categorical Plot: Average Petal Length by Species')
    plt.savefig('categorical_plot.png')
    plt.close()
    return

def plot_statistical_plot(df):
    sns.pairplot(df, hue='species')
    plt.savefig('statistical_plot.png')
    plt.close()
    return

def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    print("Data Summary:")
    print(df.describe())
    return df

def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
   
    skew_type = "right" if moments[2] > 0 else "left" if moments[2] < 0 else "not"
    kurtosis_type = "leptokurtic" if moments[3] > 0 else "platykurtic" if moments[3] < 0 else "mesokurtic"
    
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    print(f'The data was {skew_type} skewed and {kurtosis_type}.')
    return

def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return

if __name__ == '__main__':
    main()
