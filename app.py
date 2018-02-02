
from DTree.train import train

if __name__=='__main__':
    input_data = pd.read_csv('./dataset/credit_train.csv')
    input_data = input_data.dropna()

    column_names='Current Loan Amount,Term,Credit Score,Annual Income,Years in current job,Home Ownership,Purpose,Monthly Debt,\
        Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit,Bankruptcies,Tax Liens'.split(',')
    target_feature='Loan Status'
    input_data = input_data[column_names]
    print(train(input_data, target_feature='Loan Status',epsilon=0.1))