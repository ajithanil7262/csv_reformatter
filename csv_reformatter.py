import pandas as pd
class CsvDataCleaner:
    def __init__(self, filename):
        self.filename = filename

    def data_reformat(self):
        try:
            df = pd.read_csv(self.filename)

            columns = ['Revenue', 'Profit', 'Cost', 'Expense', 'Income', 'Price', 'Salary', 'Investment']

            df[columns] = df[columns].replace('[\$,]', '', regex=True).replace('\s+', '0.0', regex=True)
            df[columns] = df[columns].apply(pd.to_numeric, errors='coerce').fillna(0.00)

            # Format numeric columns
            for col in columns:
                df[col] = df[col].apply(
                    lambda x: '{:.2f}'.format(x) if pd.notnull(x) and isinstance(x, (int, float)) else x
                )

            return df
        except Exception as e:
            print(f"Error while formatting: {e}")
            return None


def group_data(df):
    columns = ['Revenue', 'Profit', 'Cost', 'Expense', 'Income', 'Price', 'Salary', 'Investment']

    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')

    result = df.groupby(['Master', 'ID'], as_index=False).agg({
        'Revenue': 'sum',
        'Profit': 'sum',
        'Cost': 'sum',
        'Expense': 'sum',
        'Income': 'sum',
        'Price': 'sum',
        'Salary': 'sum',
        'Investment': 'sum',
    })

    return result


def main():
    print("Process started...")
    filename = 'sample.csv'
    formatter = CsvDataCleaner(filename)
    formatted_df = formatter.data_reformat()

    if formatted_df is not None:
        grouped_result = group_data(formatted_df)
        print(grouped_result)
        print("Process complete\n")
    else:
        print("Data formatting process failed to complete.")

if __name__ == "__main__":
    main()

