'''
Created by David Camelo helped by ChatGPT 09/26/2024

Overview from Olympics URL's
Works for all past Olympic Games
However on Paris 2024 will be blak spaces
'''

#Import Required Libraries
import pandas as pd


class over_view_info:

    def __init__(self):
        self.name = ""
        self.image_url = ""
        self.overview_dataf = pd.DataFrame() # Initialize the Overview Dataframe

    # Extract the name from the h2 element
    def extract_name(self, soupb):
        name_element = soupb.find("h2")
        self.name = name_element.text

        return self.name
    
    # Extract the image URL from the sources
    def extract_image(self, soupb):
        image_element = soupb.find("source")
        if image_element:
            self.image_url = image_element.get("srcset").split(", ")[0]
        return self.image_url
    
    #Extract the overviwe details and include name and images
    def extract_overview(self, soupb):
        overview = soupb.find_all("div", {"class": "sc-6ba3678f-2"})

        overview_data = {}

        for ovr in overview:
            key = ovr.find("span").text
            # print(key)

            value = ovr.text.replace(key, "").strip()
            # print(value)
            overview_data[key] = value

        overview_data = pd.DataFrame([overview_data])

        overview_data["Event Name"] = self.name
        overview_data["Olympic Logo URL"] = self.image_url

        self.overview_dataf = pd.concat([self.overview_dataf, overview_data], ignore_index= True)
        
#End of the function