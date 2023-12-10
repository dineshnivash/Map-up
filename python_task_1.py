import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # pivot the dataframe to create the desired matrix
    df=df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    # Replace diagonal values with 0
    df.values[[i for i in range(df.shape[0])], [i for i in range(df.shape[0])]] = 0

    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Add new categorical column 'car_type' based on 'car' column values
    df['car_type'] = None
    for i, row in df.iterrows():
        if row['car'] <= 15:
            df.at[i, 'car_type'] = 'low'
        elif row['car'] > 15 and row['car'] <= 25:
            df.at[i, 'car_type'] = 'medium'
        else:
            df.at[i, 'car_type'] = 'high'
    
    # Calculate the count of occurrences for each car_type category
    car_type_counts = df['car_type'].value_counts().sort_values()
    
    # Return the sorted dictionary
    return dict(car_type_counts)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
     # Calculate the mean of bus column
    mean_bus = df['bus'].mean()
    
    # Filter the indices where bus value is greater than twice the mean
    filtered = df[df['bus'] > 2 * mean_bus].index.tolist()
    
    # Sort the filtered indices and return as a list
    return sorted(filtered)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Group the DataFrame by route and calculate the mean of truck column
    grouped = df.groupby('route')['truck'].mean()
    
    # Filter the routes with average truck value greater than 7
    filtered = grouped[grouped > 7]
    
    # Sort the filtered routes and return as a list
    return sorted(filtered.index.tolist())


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Multiply values based on custom conditions
    matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    # Round the modified values to 1 decimal place
    matrix = matrix.round(1)
    
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
