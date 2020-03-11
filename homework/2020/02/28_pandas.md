1、导入pandas库


```python
import pandas as pd
```

2、导入数据集airlines


```python
airlines_csv = 'https://raw.githubusercontent.com/zhoujinhai/pandasData/master/airlines.csv'
```

3、将数据集存入一个名为airlines的数据框内


```python
airlines = pd.read_csv(airlines_csv, sep=',')
```

4、查看后面5行行内容


```python
print(airlines.tail())
```

                           airline  avail_seat_km_per_week  incidents_85_99  \
    51       United / Continental*              7139291291               19   
    52  US Airways / America West*              2455687887               16   
    53            Vietnam Airlines               625084918                7   
    54             Virgin Atlantic              1005248585                1   
    55             Xiamen Airlines               430462962                9   
    
        fatal_accidents_85_99  fatalities_85_99  incidents_00_14  \
    51                      8               319               14   
    52                      7               224               11   
    53                      3               171                1   
    54                      0                 0                0   
    55                      1                82                2   
    
        fatal_accidents_00_14  fatalities_00_14  
    51                      2               109  
    52                      2                23  
    53                      0                 0  
    54                      0                 0  
    55                      0                 0  
    

5、观察数据集的信息


```python
print(airlines.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 56 entries, 0 to 55
    Data columns (total 8 columns):
     #   Column                  Non-Null Count  Dtype 
    ---  ------                  --------------  ----- 
     0   airline                 56 non-null     object
     1   avail_seat_km_per_week  56 non-null     int64 
     2   incidents_85_99         56 non-null     int64 
     3   fatal_accidents_85_99   56 non-null     int64 
     4   fatalities_85_99        56 non-null     int64 
     5   incidents_00_14         56 non-null     int64 
     6   fatal_accidents_00_14   56 non-null     int64 
     7   fatalities_00_14        56 non-null     int64 
    dtypes: int64(7), object(1)
    memory usage: 3.6+ KB
    None
    

6、打印数据集大小


```python
print(airlines.shape)
```

    (56, 8)
    

7、打印出全部的列名称


```python
print(airlines.columns)
```

    Index(['airline', 'avail_seat_km_per_week', 'incidents_85_99',
           'fatal_accidents_85_99', 'fatalities_85_99', 'incidents_00_14',
           'fatal_accidents_00_14', 'fatalities_00_14'],
          dtype='object')
    
