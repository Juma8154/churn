# churn
Churn for bank customers
Exploratory data analysis (EDA) is used by data scientists to analyze and 
investigate data sets and summarize their main characteristics, often employing data 
visualization methods.
It helps determine how best to manipulate data sources to get the 
answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypothesis, or check 
assumptions.
EDA is primarily used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a better understanding of data set variables and the relationships between them.
It can also help determine if the statistical techniques you are considering for data analysis are appropriate
# Data preparation
Load the dataset into the code

db = pd.read_csv("C://Users/wawes/OneDrive/Desktop/ZETECH UNIVERSITY/Y4S2/MACHINE LEARNING/Topic 2/churn.csv")
Display a summary of the dataset to familiarize yourself with the data

db
View the database structure to get the datatypes, number of entries, and null values

db.info()
Convert data into a format that easily be used to perform comparisons and plotting

def label_encoder(db_: pd.DataFrame(), columns_name_: list): le = LabelEncoder() for i in columns_name_: le.fit(db_[i]) db_[i] = le.transform(db_[i]) return db_

db = label_encoder(db, ['Geography', 'Gender'])

db

Exploratory Data analysis
The following are the different techniques used to explore the data

Plotting the credit score and balance to get an insight into the two variables

mpl.scatter(db.CreditScore, db.Balance)
mpl.title('Credit Score vs Balance')
mpl.xlabel('CreditScore')
mpl.ylabel('Balance')
Getting a summary of the population from different geographical regions

db['Geography'].value_counts()
Classifying other variables from the dataset to get further insight into the dataset.
