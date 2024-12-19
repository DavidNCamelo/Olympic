# Olympic Games Dataset | Medal and Event Data Extraction

If you've been searching for a complete dataset of historical Modern Olympic Games but found limited results, this repository is your solution. Using basic web scraping techniques, this project gathers detailed data on Olympic events, medals, and athletes, directly from the official website (https://olympics.com/en/olympic-games)

The repository contains scripts and tools to extract and update data for each Olympic session, making it a valuable resource for researchers, data analysts, and sports enthusiasts. Whether you're analyzing historical trends or visualizing medal counts, you'll find the data you need here.

## Class scripts

The files with no spaces in their titles are the class scripts used to retrieve data. These scripts are as follows:

These worked for events prior to Paris 2024:
* [Country_and_Medal_Lists](Country_and_Medals_Lists.py)
* [ExtractingMedalists](ExtractingMedalist.py)
* [Overview](Overviews.py) *(Note: This script was used to extract an overview for the Olympic Games Paris 2024, and generated null values for some important fields. For this case the values were inserted manually, searched over this page https://olympics.com/en/paris-2024/the-games/olympic-paralympic-games/olympic-games)*

The following script was used to extract data starting from the Olympic Games Paris 2024. If this website structure remains the same for future events, it should be possible to use this script to scrape them as well. The main difference is that the URLs for retrieving prize lists and athlete medalists are embedded within the link structure:
* [ExtractDataSinceParis](ExtractDataSinceParis.py)

Also this last class script contains both medal tables; **Country medals and Athletes Medal**

Once the desired extraction conditions were tested, each class and function was applied across the other files in this repository. Note that ['Extract URL by Ceremony'](Extract%20URL%20by%20Ceremony.py) is only used to retrieve the main link for each event and save it in the [past_olympics.csv](past_olympics.csv) file, which stores the necessary conditions to iterate scraping for each event.

## Extract Scripts

The files with spaces in their titles are the scripts where the previously mentioned classes are applied to generate the final .csv files. Note that there is one .ipynb file, which was specifically used for extracting prize lists. Additionally, this folder includes a script designed to extract and combine results from two events where it wasn’t possible to use the main Olympic page to retrieve the data.


| Script Name                           | Description                                               | Output File                                  |
|---------------------------------------|-----------------------------------------------------------|----------------------------------------------|
| Extracting Medalist.py                | Retrieves data on medalists from previous Olympics.       | Olympic medalists.csv                        |
| Extract Overviews.py                  | Retrieves data for Overview Sessions                      | Olympic Overview.csv                         |
| Extracting.ipynb                      | Extract detailed data of prizes and countries.            | Olympic Prizes.csv and Olympic Countries.csv |
| Extracting Prizes SinceParis.py       | Extracts detailed data starting from Paris 2024.          | Olympic Prizes.csv (added rows)              |
| Extracting Medalists SinceParis.py    | Extracts detailed data starting from Paris 2024.          | Olympic Medalists.csv (added rows)           |

### Sample Visualization

The visual project is located in my portfolio site: https://project.novypro.com/IYwptn
![Presentation](<Olympic Games History.png>)

### Periodic Updates
This dataset is updated after every Olympic session (both Summer and Winter) to ensure accuracy and relevance.  tracking data from the official site.

## Tags and Keywords
* Olympic Games Dataset
* Historical Medal Data
* Sports Data Analysis
* Web Scraping for Sports
* Modern Olympic Games Data