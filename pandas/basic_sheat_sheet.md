Here’s a complete Pandas cheat sheet, covering essential functions and commands along with brief descriptions. This guide is structured to help you perform common data manipulation and analysis tasks in Python using Pandas.

---

### **1. Basics**

```python
import pandas as pd
```

- **pd.Series(data, index)**: Create a 1D array with optional index.
- **pd.DataFrame(data, index, columns)**: Create a 2D table (DataFrame) from a variety of sources like lists, dicts, Series, or another DataFrame.

### **2. Data Importing/Exporting**

- **pd.read_csv('file.csv')**: Read a CSV file into a DataFrame.
- **pd.read_excel('file.xlsx')**: Load an Excel file.
- **pd.read_json('file.json')**: Load a JSON file.
- **df.to_csv('file.csv')**: Export DataFrame to CSV.
- **df.to_excel('file.xlsx')**: Export DataFrame to Excel.
- **df.to_json('file.json')**: Export DataFrame to JSON.

### **3. Data Inspection**

- **df.head(n)**: View the first `n` rows.
- **df.tail(n)**: View the last `n` rows.
- **df.shape**: Get the dimensions of the DataFrame (rows, columns).
- **df.columns**: List of column names.
- **df.index**: List of row indices.
- **df.dtypes**: Data types of each column.
- **df.info()**: Summary of the DataFrame.
- **df.describe()**: Summary statistics for numeric columns.

### **4. Data Selection & Filtering**

- **df['column']** or **df.column**: Select a column.
- **df[['col1', 'col2']]**: Select multiple columns.
- **df.iloc[row, col]**: Select by row/column index.
- **df.loc[row, col]**: Select by labels.
- **df[df['column'] > value]**: Filter rows based on a condition.

### **5. Data Cleaning**

- **df.dropna()**: Remove rows with missing values.
- **df.fillna(value)**: Replace missing values.
- **df.isna()**: Check for missing values.
- **df.drop_duplicates()**: Remove duplicate rows.
- **df.replace(to_replace, value)**: Replace specific values.

### **6. Data Transformation**

- **df.rename(columns={'old_name': 'new_name'})**: Rename columns.
- **df.astype(dtype)**: Change the data type of columns.
- **df.apply(func)**: Apply a function to each column.
- **df.applymap(func)**: Apply a function element-wise.
- **df['column'].map(dict)**: Map values of a column.

### **7. Aggregation and Grouping**

- **df.groupby('column')**: Group data by column(s).
- **df.groupby('column').mean()**: Mean of each group.
- **df.groupby('column').agg(['mean', 'sum'])**: Aggregate with multiple functions.
- **df.pivot_table(values, index, columns, aggfunc)**: Create pivot tables.

### **8. Merging & Joining**

- **pd.concat([df1, df2])**: Concatenate DataFrames vertically or horizontally.
- **df.merge(other_df, on='column', how='inner')**: Merge DataFrames.
  - **how**: 'left', 'right', 'outer', or 'inner'.

### **9. Sorting**

- **df.sort_values(by='column')**: Sort by column values.
- **df.sort_index()**: Sort by index.
- **df.nlargest(n, 'column')**: Get `n` largest values.
- **df.nsmallest(n, 'column')**: Get `n` smallest values.

### **10. Data Analysis**

- **df['column'].value_counts()**: Count unique values in a column.
- **df.corr()**: Correlation between columns.
- **df.cov()**: Covariance between columns.

### **11. Time Series**

- **pd.to_datetime(df['date_column'])**: Convert to datetime.
- **df['column'].dt.year**: Extract year.
- **df['column'].dt.month**: Extract month.
- **df.resample('M').mean()**: Resample by month and calculate the mean.

### **12. Plotting with Pandas**

- **df.plot()**: Line plot of all columns.
- **df.plot(kind='bar')**: Bar plot.
- **df.plot(kind='hist')**: Histogram.
- **df.plot(kind='box')**: Box plot.
- **df.plot(kind='scatter', x='col1', y='col2')**: Scatter plot.

### **13. Saving DataFrames**

- **df.to_csv('file.csv', index=False)**: Save as CSV without index.
- **df.to_excel('file.xlsx', sheet_name='Sheet1')**: Save as Excel.
- **df.to_json('file.json')**: Save as JSON.

---

This cheat sheet should cover most of your daily data manipulation tasks in Pandas! Let me know if you need more details on specific functions or operations.



Yes, there are a few additional Pandas functions and operations that weren’t covered in the basic cheat sheet, especially for advanced data handling, reshaping, and statistical analysis. Here’s a cheat sheet to cover these more advanced functionalities.

---

### **14. Advanced Indexing and Selection**

- **df.set_index('column', inplace=True)**: Set a column as the index.
- **df.reset_index()**: Reset the index, moving the index back to a column.
- **df.at[row, 'column']**: Fast access to a scalar value.
- **df.iat[row, col]**: Fast access to a scalar value by position.
- **df.xs(key, level, axis=0)**: Cross-section for rows/columns with multi-level indexing.

### **15. Handling MultiIndex DataFrames**

- **pd.MultiIndex.from_arrays(arrays)**: Create a MultiIndex from arrays.
- **df.stack()**: Pivot columns to rows, creating a stacked DataFrame.
- **df.unstack()**: Pivot rows to columns (inverse of `stack()`).
- **df.swaplevel(i, j)**: Swap levels in a MultiIndex.
- **df.sort_index(level=0)**: Sort DataFrame by a specified index level.

### **16. Reshaping Data**

- **df.melt(id_vars, value_vars)**: Unpivot DataFrame from wide to long format.
- **df.pivot(index, columns, values)**: Pivot long-format data back to wide format.
- **df.pivot_table(values, index, columns, aggfunc)**: Create a pivot table.
- **df.T**: Transpose the DataFrame.

### **17. Window Functions**

- **df.rolling(window)**: Rolling window calculations, e.g., `df.rolling(3).mean()`.
- **df.expanding()**: Expanding window calculations, e.g., `df.expanding().sum()`.
- **df.ewm(alpha)**: Exponential moving window calculations.

### **18. Text Data Operations**

- **df['column'].str.contains('pattern')**: Check if string contains a pattern.
- **df['column'].str.replace('old', 'new')**: Replace text in strings.
- **df['column'].str.extract('regex')**: Extract matching strings using regex.
- **df['column'].str.split('delimiter')**: Split strings by a delimiter.
- **df['column'].str.strip()**: Remove whitespace from strings.

### **19. Statistical and Mathematical Operations**

- **df.mean()**, **df.sum()**, **df.std()**, **df.var()**: Basic statistics.
- **df.min()**, **df.max()**: Minimum and maximum values.
- **df.quantile(q)**: Quantiles of data.
- **df.cumsum()**: Cumulative sum.
- **df.cumprod()**: Cumulative product.
- **df.diff()**: Difference between each row/column.
- **df.rank()**: Rank of values within columns.

### **20. Advanced Grouping with Transformations**

- **df.groupby('column').transform(func)**: Apply function to groups and broadcast the result to the original DataFrame.
- **df.groupby('column').filter(func)**: Filter groups that satisfy a function.
- **df.groupby('column').apply(func)**: Apply a function to each group independently.

### **21. Working with Categories**

- **df['column'] = df['column'].astype('category')**: Convert a column to a categorical type.
- **df['column'].cat.categories**: View categories of a categorical column.
- **df['column'].cat.rename_categories(new_categories)**: Rename categories.
- **df['column'].cat.add_categories(['new'])**: Add new categories.
- **df['column'].cat.remove_unused_categories()**: Remove unused categories.

### **22. Sparse Data**

- **pd.SparseDtype()**: Specify a sparse data type.
- **df.astype(pd.SparseDtype())**: Convert a DataFrame to sparse format.

### **23. Working with Duplicates**

- **df.duplicated()**: Boolean Series indicating duplicate rows.
- **df.drop_duplicates()**: Remove duplicate rows.
- **df.drop_duplicates(subset=['col1', 'col2'], keep='first')**: Drop duplicates by specific columns.

### **24. DataFrame Memory Optimization**

- **df.memory_usage(deep=True)**: Get the memory usage of the DataFrame.
- **df.astype(dtype)**: Change column data types to reduce memory usage (e.g., using `float32` instead of `float64`).
- **pd.to_numeric(df['column'], downcast='float')**: Downcast numeric types for smaller memory footprint.

### **25. DataFrame Operations**

- **df.add(other, fill_value=0)**: Add DataFrames with a fill value.
- **df.sub(other, fill_value=0)**: Subtract DataFrames.
- **df.mul(other, fill_value=1)**: Multiply DataFrames.
- **df.div(other, fill_value=1)**: Divide DataFrames.

### **26. Datetime Operations**

- **pd.to_datetime(df['column'])**: Convert a column to datetime.
- **df['column'].dt.date**: Get the date component.
- **df['column'].dt.time**: Get the time component.
- **df['column'].dt.dayofweek**: Day of the week (Monday=0).
- **df['column'].dt.week**: Week number of the year.
- **df['column'].dt.to_period('M')**: Convert to a period (e.g., 'M' for monthly).

### **27. Custom Functions with Apply and Map**

- **df.apply(lambda x: x**2)**: Apply a function across each column.
- **df.applymap(lambda x: x+1)**: Apply a function element-wise.
- **df['column'].map(lambda x: x*2)**: Map a function to a column.

### **28. MultiIndex Grouping and Aggregation**

- **df.groupby(['col1', 'col2']).size()**: Group by multiple columns.
- **df.groupby(['col1', 'col2']).agg({'col3': 'mean', 'col4': 'sum'})**: Apply different aggregations to different columns.

### **29. Working with JSON-like Data in Pandas**

- **df['column'].apply(pd.Series)**: Expand JSON/dict columns into separate columns.
- **pd.json_normalize(json_data)**: Normalize JSON data into a flat table.

### **30. Miscellaneous Functions**

- **df.sample(n)**: Randomly sample `n` rows from the DataFrame.
- **pd.get_dummies(df, columns=['col1'])**: Convert categorical variables into dummy/indicator variables.
- **df.crosstab(index, columns)**: Compute cross-tabulation of two or more factors.

---

This expanded cheat sheet covers advanced functionalities in Pandas, enhancing your ability to handle complex data manipulation tasks. Let me know if you need examples for any specific function!



This is now a highly comprehensive Pandas cheat sheet, but a few more specialized functions and advanced data manipulation techniques are still available in Pandas. Here’s a final cheat sheet that includes:

1. **Sparse Data Operations**
2. **Advanced Plotting with Pandas**
3. **Advanced Data Manipulation & Reshaping**
4. **Multi-level DataFrame Aggregation and Window Functions**
5. **Experimental and Special Functions**

These will cover the niche and specialized functionalities in Pandas, which can be useful in specific cases.

---

### **31. Sparse Data Operations**

Sparse data structures are useful for working with large datasets where many values are zero or missing, saving memory.

- **pd.SparseDataFrame(data)**: Create a sparse DataFrame.
- **pd.SparseArray(data)**: Create a sparse array.
- **df.sparse.from_spmatrix(matrix)**: Convert a sparse matrix to a Pandas DataFrame.
- **df.sparse.density**: Calculate the density of non-zero values.
- **df.to_sparse()**: Convert a DataFrame to a sparse DataFrame (for older versions of Pandas).

### **32. Advanced Plotting with Pandas**

Pandas has some integration with `matplotlib` for quick plotting but can also work with other libraries for specialized plots.

- **df.plot.hexbin(x='col1', y='col2', gridsize=25)**: Hexbin plot for data density.
- **df.plot.kde()**: Kernel Density Estimate plot.
- **df.plot.pie(y='column')**: Pie plot.
- **df.plot.area()**: Area plot.
- **df.plot(kind='density')**: Density plot for continuous distributions.
- **pd.plotting.scatter_matrix(df)**: Scatterplot matrix.
- **pd.plotting.parallel_coordinates(df, 'class_column')**: Parallel coordinates plot.
- **pd.plotting.andrews_curves(df, 'class_column')**: Andrews curves for multivariate data.

### **33. Advanced Data Manipulation & Reshaping**

This section covers complex reshaping tasks, especially useful for handling nested or hierarchical data.

- **df.explode('column')**: Expand lists/arrays in a column into separate rows.
- **df.pivot(index, columns, values)**: Create a DataFrame from a pivot table.
- **pd.wide_to_long(df, stubnames, i, j)**: Reshape from wide to long format based on stub names.
- **df.melt(id_vars, var_name, value_name)**: Unpivot DataFrame to longer format.
- **df.crosstab(index, columns)**: Cross-tabulation of two factors, often used for contingency tables.
- **pd.get_dummies(df, prefix, columns)**: Create dummy variables for categorical columns.

### **34. Multi-level DataFrame Aggregation**

Working with multi-level indices and hierarchical data, these functions are critical for summarizing data within subgroups.

- **df.groupby(level=[0,1]).sum()**: Group by multiple index levels.
- **df.groupby(['col1', 'col2']).agg({'col3': 'mean', 'col4': ['min', 'max']})**: Apply multiple aggregations to multiple columns.
- **df.pivot_table(values='data', index='row_index', columns='col_index', aggfunc='sum')**: Pivot table with multi-level indexes.
- **df.groupby(['col1', 'col2']).pipe(custom_func)**: Use custom functions with grouped data using `.pipe()`.

### **35. Advanced Window Functions**

Window functions perform operations within a sliding or expanding window over data.

- **df.rolling(window=3, min_periods=1).apply(func)**: Apply a custom function to a rolling window.
- **df.expanding(min_periods=1).mean()**: Expanding window with cumulative mean.
- **df.rolling(window=3).corr(df['other_column'])**: Rolling correlation with another column.
- **df.rolling(window=3, on='date_column').sum()**: Rolling calculations based on a date column.

### **36. Experimental and Special Functions**

Pandas periodically introduces experimental functions for advanced data analysis.

- **pd.eval('expression')**: Evaluate an expression (e.g., `'df.a + df.b'`) for efficient computation.
- **pd.query('expression')**: Query a DataFrame using a string expression (e.g., `'column > 3'`).
- **df.eval('new_col = col1 + col2')**: Inline calculation within DataFrame.
- **df.style.applymap(color_func)**: Style DataFrame by applying functions for color/formatting.
- **pd.api.types.is_numeric_dtype(df['column'])**: Check if a column is numeric.

### **37. Data Integrity and Validation**

Check and enforce data integrity to catch errors in datasets.

- **pd.isna(df['column'])**: Check for null values.
- **pd.notna(df['column'])**: Check for non-null values.
- **pd.api.types.is_string_dtype(df['column'])**: Check if column is of string type.
- **df.dropna(thresh=2)**: Drop rows where fewer than two elements are non-NA.
- **pd.Series(df['column']).dropna()**: Drop NA values in a series.

### **38. Data Security and Permissions**

Pandas provides minimal but essential support for securely loading data.

- **pd.read_csv('file.csv', storage_options={'key': 'my_key'})**: Load from a secure storage with credentials.
- **pd.read_sql(query, con, schema='schema')**: Load data from a SQL database.

---

These are some of the more advanced and niche functions in Pandas, which are useful in specialized cases or when handling large and complex datasets. Let me know if you'd like more in-depth examples or a focus on any specific area!
