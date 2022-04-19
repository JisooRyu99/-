'''
The length_of_time field in the UFO dataset is a text field that has the number of minutes within the string. Here, you'll extract that number from that text field using regular expressions.
'''

def return_minutes(time_string):

    # Use \d+ to grab digits
    pattern = re.compile(r"\d+")
    
    # Use match on the pattern and column
    num = re.match(pattern, time_string)
    if num is not None:
        return int(num.group(0))
        
# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)

# Take a look at the head of both of the columns
print(ufo[['length_of_time', 'minutes']].head())


<script.py> output:
        length_of_time  minutes
    2  about 5 minutes      NaN
    4       10 minutes     10.0
    7        2 minutes      2.0
    8        2 minutes      2.0
    9        5 minutes      5.0
