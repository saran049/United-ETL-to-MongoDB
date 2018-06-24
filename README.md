# United-ETL-to-MongoDB

Summary of the project:
United Super Markets data that consist of 5 flat files and one of which is scraped data.

The aim was to examine the data, conduct the cleansing process and transform the data to make them ready to load to the NoSQL database, namely to Mongo DB. Item list file is updated with the new “UPC” detail by comparing the existing item list with the extracted item list details from FTP server. The scrapped data contains the prices of the competitors which can be used by the United Super Markets to compare their prices with them and change accordingly.

Resources:
The resources of this ETL process are 5 flat files; namely Item List, Sales Details, Customer List, Item Attributes, and Store Location. These files were provided by United Super Markets via a cloud link. To process the data, Python (a programming language) and Mongo DB (Cross-platform document-oriented NoSQL database) are used as software. 
