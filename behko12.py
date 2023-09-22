import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
s1 = pd.Series([15,16,17])
s2 = pd.Series([56,64,60])
s3 = pd.Series([166,173,158])
dframe = pd.DataFrame([s1,s2,s3]).T
dframe.columns = ["Age","Weight","Height"]
dframe.to_csv("Information.csv",index=False)
dframe1 = pd.DataFrame({'Age':[45,34,29,29,47,34],"Weight":[54,65,np.nan,45,np.nan,76],"Height":[165,np.nan,np.nan,160,176,153]})
dframe1.columns = ["Age","Weight","Height"]
# to remove all the rows with NaN value:
#dframe1.dropna(inplace=True)
dframe1.fillna(value= dframe1.mean(),inplace=True)
# inplace = True will remove every row that doesn't have the same value for each category given
print(dframe1)
print(dframe1.groupby(["Age"]).max())
# groupby fuction will remove any similar value in the Dataframe given and we use max to
# pick out the greatest value from each column for each category
# eg: we use groupby and max on column Age so all the same ages will be removed and the age with the
# highest weight and height will be kept.
# more and more exercise:
dframe2 = pd.read_csv(r"D:\Python\PythonFiles\Datasets\NintendoGames.csv")
# biến đổi dữ liệu từ một file csv sang một Dataframe để có thể dùng các câu lệnh trong Dataframe
# như fillna dropna, columns= , groupby...etc
dframe3 = pd.DataFrame(dframe2.loc[:20,"meta_score"])
dframe3.fillna(value= dframe3.mean(),inplace=True)
print(dframe3)
dframe4 = pd.DataFrame(dframe2.loc[:20,"user_score"])
dframe4.fillna(value= dframe4.mean(), inplace= True)
print(dframe4)
dframe4.hist(edgecolor = "black")
plt.show()
dframe2["platform"].hist()
plt.show()
