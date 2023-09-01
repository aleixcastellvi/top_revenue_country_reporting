import pandas as pd
import os
import luigi


class CalculateMonthlyStatistics(luigi.Task):

    year = luigi.IntParameter()
    month = luigi.Parameter()

    def output(self):
        output_path = f'statistics/top_revenue_country_{self.month}_{str(self.year)[2:]}.csv'
        return luigi.LocalTarget(output_path)

    def run(self):
        month = self.month.lower().title()
        year = str(self.year)[2:]

        processed_folder = os.path.exists('statistics')

        if not processed_folder:
            os.makedirs('statistics', exist_ok=True)

        df = pd.read_csv(f'orders/{self.year}/{month}_{year}.csv')

        revenue_by_country = df.groupby('Country')['Total Revenue'].sum().reset_index()

        revenue_by_country = revenue_by_country.sort_values(by='Total Revenue', ascending=False)

        revenue_by_country['Total Revenue'] = (revenue_by_country['Total Revenue'] / 1000000).apply(lambda x: '{:.2f} M'.format(x))

        top_revenue_by_country = revenue_by_country.head(10)

        top_revenue_by_country.to_csv(f'statistics/top_revenue_country_{month}_{year}.csv', index=False)


if __name__ == "__main__":
    luigi.run()