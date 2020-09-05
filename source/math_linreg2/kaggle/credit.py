import pathlib as pl
import pandas as pd

root = pl.Path('/home/devoted/Downloads/home-credit-default-risk')
# paths = list(root.glob('**/*.csv'))

LIMIT = 30

# DF_sample_submission = pd.read_csv(root.joinpath('sample_submission').with_suffix('.csv'), nrows=LIMIT)
# DF_bureau_balance = pd.read_csv(root.joinpath('bureau_balance').with_suffix('.csv'), nrows=LIMIT)
# DF_bureau = pd.read_csv(root.joinpath('bureau').with_suffix('.csv'), nrows=LIMIT)
# DF_POS_CASH_balance = pd.read_csv(root.joinpath('POS_CASH_balance').with_suffix('.csv'), nrows=LIMIT)
# DF_application_test = pd.read_csv(root.joinpath('application_test').with_suffix('.csv'), nrows=LIMIT)
# DF_previous_application = pd.read_csv(root.joinpath('previous_application').with_suffix('.csv'), nrows=LIMIT)
# DF_HomeCredit_columns_description = pd.read_csv(root.joinpath('HomeCredit_columns_description').with_suffix('.csv'), nrows=LIMIT)
# DF_installments_payments = pd.read_csv(root.joinpath('installments_payments').with_suffix('.csv'), nrows=LIMIT)
# DF_application_train = pd.read_csv(root.joinpath('application_train').with_suffix('.csv'), nrows=LIMIT)
# DF_credit_card_balance = pd.read_csv(root.joinpath('credit_card_balance').with_suffix('.csv'), nrows=LIMIT)

app_train = pd.read_csv(root.joinpath('application_train').with_suffix('.csv'))

from sklearn.ensemble import RandomForestClassifier

# Make the random forest classifier
random_forest = RandomForestClassifier(n_estimators = 100, random_state = 50, verbose = 1, n_jobs = -1)

random_forest.fit(train, train_labels)
predictions = random_forest.predict_proba(test)[:, 1]


submit = app_test[['SK_ID_CURR']]
submit['TARGET'] = predictions
