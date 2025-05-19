
# Web Scraping Using Python (BeautifulSoup)





## Prerequisites
1. Python 3.6+
2. install BeautifulSoup **```pip install beautifulsoup4```**
3. install Requests **```pip install requests```**
4. install Pandas **```pip install pandas```**



## Process of Web Scraping
1. Importing the required libraries
2. Specifying the URL containing the dataset and passing it to **`requests.get()`** to get the HTML content of the page.
3. Using BeautifulSoup to parse the HTML content
4. Extracting the required information from the data
5. Saving the pandas dataframe as a CSV file called **`Amazon Data.csv`**


## Project Specifications
1. It contains a python file **`scraper.py`** which contains the rough codes to be used in the final notebook file.
2. It contains a jupyter notebook file **`Amazon Web Scraper.ipynb`** which contains the final codes to be used in the project.
    * function to Extract Product Title
    * function to Extract Product Price
    * function to Extract Product Rating
    * function to Extract Number of User Reviews
    * function to Extract Product Availability
3. It contains a csv file **`Amazon Data.csv`** which contains the final data extracted from the website.
