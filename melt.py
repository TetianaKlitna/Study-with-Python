# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars = ['year'],
value_vars= ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], var_name = ['month'], value_name = 'unempl_rate')

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x = 'date', y = 'unempl_rate')
plt.show()


# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars = ['metric'], var_name = 'date', value_name = 'close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query(' metric == "close" ')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = dji.merge(bond_perc_close, on='date', suffixes = ('_dow', '_bond') )

# Plot only the close_dow and close_bond columns
dow_bond.plot(y = ['close_dow', 'close_bond'], x='date', rot=90)
plt.show()
