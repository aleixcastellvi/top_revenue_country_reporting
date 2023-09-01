# Luigi Task to obtain global revenue statistics

This application uses the Luigi framework to generate monthly CSV files containing a ranking of the top ten countries that have generated the highest revenue in a sales dataset. The **CalculateMonthlyStatistics** class in Luigi plays a pivotal role in this process.

The CalculateMonthlyStatistics class is responsible for determining whether the output file corresponding to the requested month and year already exists in the destination directory. If the file has not been generated yet, the class initiates the process to obtain the ranking of the top ten countries with the highest revenue for that specific period. However, if the file already exists in the directory, the Luigi class does not run again to prevent duplicate generation of results.

To initiate the Luigi class and generate statistics, specifying the month and year of interest is required. This customization allows users to obtain statistics for any desired period.

While this solution is effective for use in a local environment, it could be further improved to make the most of Luigi's capabilities. One proposed enhancement could be to enable the Luigi class to automatically determine the latest available dataset and check whether it has been processed previously. If it has not been processed, the class would initiate the necessary tasks to generate the final CSV file. This enhancement could be combined with an automated mechanism that runs the Luigi class automatically on the first day of each month when a new monthly dataset is loaded for analysis.

This improvement would further automate the process, eliminating the need for manual specification of the month and year, and ensuring that statistics are generated periodically for new monthly data.

---
*Data source:* [Click here](https://www.kaggle.com/datasets/annakhew/sample-country-sales-dataset?resource=download)

## Previous steps

Before generating the statistics, an application is launched that takes a CSV file containing sales data, performs the necessary date and year conversion and processing, and then organizes the data into a directory structure based on years and months. Each resulting CSV file contains order data for a specific month of a specific year.

The description accurately reflects the purpose and operation of the process_dataset_by_year_by_month function. This function prepares the data before monthly statistics can be calculated, which is a common practice in data analysis.

Therefore, we transition from having a single CSV file with multiple sales records to having sales files organized as shown below:

```
orders/
├── 2015/
│   ├── January_15.csv
│   ├── February_15.csv
│   ├── March_15.csv
│   ...
│   └── December_15.csv
├── 2016/
│   ├── January_15.csv
│   ├── February_15.csv
│   ├── March_15.csv
│   ...
│   └── December_15.csv
└── ...

```


## Step by step installation and program execution process

#### Prerequisites

- python
- pip


#### Create a virtualenv for the project

```
conda create -n app-env python=3.10
conda activate app-env

# alternative to conda
virtualenv app-env python=3.10

# activation on linux
source app-env/bin/activate
# activation on windows
app-env\Scripts\activate

```

Install luigi and the requirements with pip:

```
pip install luigi

pip install -r requirements.txt

```


#### Execute previous application

This application generates the initial directory of csv files.

```
$ python build_files_directory.py
```


#### Execute luigi Task

Specify the year and month you want to analyze. In the following example call, we generate the ranking of the top ten countries for the month of May 2017 based on sales data.

```
$ python statistics_report.py CalculateMonthlyStatistics --year 2017 --month May --local-scheduler
```


#### Delete generated files and directories

**This is optional**. If you wish to delete the files and directories generated during the process, you can run the following command. This will not cause any issues if you decide to restart the entire process described above.

```
$ python delete_items.py
```
