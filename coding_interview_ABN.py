import pandas as pd

# Importing the datasets

ds1 = pd.read_csv (r'C:\Users\aditi\OneDrive\Desktop\Career\Mploy\ABN Amro\codc-interviews\dataset_one.csv')

ds2 = pd.read_csv (r'C:\Users\aditi\OneDrive\Desktop\Career\Mploy\ABN Amro\codc-interviews\dataset_two.csv')

# Subsetting main data to take clients only from NL and UK
df_uk_nl = ds1[ds1.country.isin(["Netherlands", "United Kingdom"])]

# Not removing any personal information from the dataset_one as First Name and 
# Last Name are important to uniquely identify a person and send the promotion email

# Removing credit card number from dataset_two

#Creating columns to keep variable to make it easy in future to keep/ remove other columns
columns_to_keep = ['id','btc_a','cc_t']
df_no_ccn = ds2[columns_to_keep]

# Creating a joined dataset
total = pd.merge(df_uk_nl, df_no_ccn, on='id', how="inner")

# Renaming the columns for better readability
total.columns=['Client_Identifier','First_Name', 'Last_Name', 'Email', 'Country', 'Bitcoin_address', 'Credit_Card_Type']

#################################################################################################################
#################### Now creating a user defined function that perfoms the above automatically ###################
##################################################################################################################

def email_promotion(file1_path, file2_path, countries):
    
    file1 = pd.read_csv (file1_path) # importing file1 from path argument
    file2 = pd.read_csv (file2_path) # importing file2 from path argument
    
    file1_countries = file1[file1.country.isin(countries)] # Filtering for required countries
    file2_no_ccn = file2[['id','btc_a','cc_t']] # Removing credit card number 
    
    # Joining the files
    merged = pd.merge(file1_countries, file2_no_ccn, on='id', how="inner")
    # Giving proper column names for readability
    merged.columns=['Client_Identifier','First_Name', 'Last_Name', 'Email', 'Country', 'Bitcoin_address', 'Credit_Card_Type']
    
    # Returning final dataset
    return merged


    
 # Calling the function to ensure it works   
 # Need to call function into variable in order to store return dataset 
sample = email_promotion('C:\\Users\\aditi\\OneDrive\\Desktop\\Career\\Mploy\\ABN Amro\\codc-interviews\\dataset_one.csv', 
                    'C:\\Users\\aditi\\OneDrive\\Desktop\\Career\\Mploy\\ABN Amro\\codc-interviews\\dataset_two.csv',
                    ['United States', 'France'])


#################################################################################################################
####################### Now creating a user defined generic function that renames columns  #######################
##################################################################################################################

def col_rename(data, col, val): # Need to provide data, original column names and new column names
    
    # This is incase multiple columns need to be renamed
    for i in range (0, len(val)) :
        data = data.rename( {col[i] : val[i]}, axis=1, copy=True, inplace=False)
        # Each column will be identified and replaced
        
    return data

# trying if it works
x = col_rename(ds1, [ 'id','country', 'first_name', 'last_name'], [ 'Identificatie','Land', 'Voornaam', 'Achternaam'])


#################################################################################################################
######################### Now creating a user defined Generic function for filtering data ########################
##################################################################################################################
#

def data_filter(data, column_name, values): # Need to provide data, list of columns and list of filter values
          
    for i in range (0, len(values)) :
        data = data[data[column_name[i]].isin(values[i])] # This is incase multiple columns need to be filtered
    return data

# Checking with one filter only
y = data_filter(ds1, ['country'], [['United States', 'France']])


# Checking with multiple filters
z = data_filter(ds1, ['country', 'first_name', 'last_name'], [['United States', 'France'], ['Aaron'],
                                                               ['Palle', 'Witham']])











