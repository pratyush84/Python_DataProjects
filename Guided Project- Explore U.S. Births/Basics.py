
# coding: utf-8

# In[1]:

f = open("US_births_1994-2003_CDC_NCHS.csv","r")
data = f.read()


# In[2]:

split_data = data.split("\n")
print(split_data[:10])


# In[3]:

def read_csv(filename):
    f = open(filename,"r")
    data = f.read()
    string_list = data.split("\n")[1:]
    final_list = []
    
    for item in string_list:
        int_fields = []
        string_fields = item.split(",")
        for item in string_fields:
            int_fields.append(int(item))
        final_list.append(int_fields)
    return(final_list)


# In[4]:

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[5]:

print(cdc_list[:10])


# In[6]:

def month_births(birth_list):
    births_per_month = {}
    for item in birth_list:
        month = item[1]
        births = item[4]
        
        if(month in births_per_month):
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    
    return(births_per_month)


# In[7]:

cdc_month_births = month_births(cdc_list)


# In[8]:

cdc_month_births


# In[13]:

def dow_births(list_births):
    births_per_dow = {}
    for item in list_births:
        dow = item[3]
        births = item[4]
        
        if(dow in births_per_dow):
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
        
    return(births_per_dow)


# In[15]:

cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[20]:

def calc_counts(data, column):
    births_per_col = {}
    
    for item in data:
        births = item[4]
        col_val = item[column]
        
        if(col_val in births_per_col):
            births_per_col[col_val] = births_per_col[col_val] + births
        else:
            births_per_col[col_val] = births
        
    return(births_per_col)


# In[21]:

cdc_year_births = calc_counts(cdc_list,0)
cdc_year_births


# In[23]:

cdc_month_births = calc_counts(cdc_list,1)
cdc_month_births


# In[24]:

cdc_dom_births = calc_counts(cdc_list,2)
cdc_dom_births


# In[25]:

cdc_dow_births = calc_counts(cdc_list,3)
cdc_dow_births


# In[31]:

def min_max(dictionary):
    max_value = dictionary[max(dictionary)]
    min_value = dictionary[min(dictionary)]
    return(min_value, max_value)


# In[32]:

min_max(cdc_dow_births)


# In[43]:

def birth_trends(start_year, end_year, col_idx, col_val=1):
    yearly_stats = {}
    #cdc_year_births = calc_counts(cdc_list,0)
    
    for i in range(start_year, end_year+1):
        year_list = [item for item in cdc_list if (item[0] == i)]
        cdc_col_idx = calc_counts(year_list,col_idx)
        if (col_idx):
            value = cdc_col_idx[col_val]
        else:
            value = cdc_col_idx[i]
        yearly_stats[i] = value
    
    year = start_year
    year_val = yearly_stats[start_year]
    diff_list=[]
    for i in range(year+1, end_year+1):
        val_curr = yearly_stats[year]
        val_next = yearly_stats[i]
        
        diff = val_next - val_curr
        diff_list.append(diff)
        year = i
    
    return(diff_list)


# In[44]:

birth_trends(1994,2003,3,6)


# In[45]:

birth_trends(1994,2003,0)


# In[3]:

ssa_list = read_csv("US_births_2000-2014_SSA.csv")


# In[51]:

ssa_list[:10]


# In[2]:

overlap_years = [2000,2001,2002,2003]
final_ssa_list = [item for item in ssa_list if (item[0] not in overlap_years)]
final_list = cdc_list + final_ssa_list


# In[ ]:



