from cafef_scraping import FinanceStat 

# export data to .csv file, only use once to download data
data = FinanceStat('pnj')
# data.export_findata(form='xlsx', report_format='traditional')