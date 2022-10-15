# Datasets

This section contains the datasets used in this project.

| Dataset                                            | Description                                             | Source                                                                                                                   |
| -------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [threecubes_20070419.csv](threecubes_20070419.csv) | List of solutions of x^3 + y^3 + z^3 = n for n < 1000   | [Andreas-Stephan Elsenhans and Joerg Jahnel](https://www.uni-math.gwdg.de/jahnel/Arbeiten/Liste/threecubes_20070419.txt) |
| [313.csv](313.csv)                                 | Exhaustive list of solutions to (3,1,3) below 1,000,000 | [Jaroslaw Wroblewski](https://www.math.uni.wroc.pl/~jwr/eslp/tables.htm)                                                 |

# Script for retrieving Equal Sums of Powers (3,1,3) data

The following script downloads the data:

```python
temp_folder = "C:/Temp/"

file_list = ["https://www.math.uni.wroc.pl/~jwr/eslp/313.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-1.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-2.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-3.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-4.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-5.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-6.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-7.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-8.zip",
    "https://www.math.uni.wroc.pl/~jwr/eslp/313-9.zip"]

for file_name in file_list:
    r = requests.get(file_name)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(temp_folder)
```

The following script merges the downloaded data:

```python
temp_folder = "C:/Temp/"

file_list = ["313-100K.TXT",
    "313-1.txt",
    "313-2.txt",
    "313-3.txt",
    "313-4.txt",
    "313-5.txt",
    "313-6.txt",
    "313-7.txt",
    "313-8.txt",
    "313-9.txt"]

data = ""
for file_name in file_list :
   with open(temp_folder + file_name, "r") as file_handle :
      temp_data = file_handle.read()
      data = data + temp_data 

with open (temp_folder + "313.csv", "a") as file_handle : 
  file_handle.write(data)
```

# The final dataset for Equal Sums of Powers (3,1,3)

The final dataset for Equal Sums of Powers (3,1,3) is available at Kaggle: [Equal Sums of Powers (3,1,3)](https://www.kaggle.com/datasets/eldarsultanow/equal-sums-of-powers-313).
