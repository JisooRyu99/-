'''
Taking another look at the dataset comprised of volunteer information from New York City, we want to know what types we'll be working with as we start to do more preprocessing.

Which data types are present in the volunteer dataset?

The dataset volunteer has been provided.
Use the .dtypes attribute to check the datatypes.
'''

volunteer.dtypes
'''opportunity_id          int64
content_id              int64
vol_requests            int64
event_time              int64
title                  object
hits                   object
summary                object
is_priority            object
category_id           float64
category_desc          object
amsl                  float64
amsl_unit             float64
org_title              object
org_content_id          int64
addresses_count         int64
locality               object
region                 object
postalcode            float64
primary_loc           float64
display_url            object
recurrence_type        object
hours                   int64
created_date           object
last_modified_date     object
start_date_date        object
end_date_date          object
status                 object
Latitude              float64
Longitude             float64
Community Board       float64
Community Council     float64
Census Tract          float64
BIN                   float64
BBL                   float64
NTA                   float64
dtype: object
'''
