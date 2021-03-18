"""
Tools to interact with the roblox catalogue search api (avatar).

The design of this is based off of KILR's roblox api wrapper.

Data is returned in a dict in the form of {"NAME" : id}
This obviously is not very convenient in itself, however you can simply loop through the dict to retrieve and store results in a better way (shown at the end of this file)

Search parameters:
[] = Optional, <> = Required
[Category], <Keyword to search for>

To indicate that you do not want to input a category, simply set its value to None when using the function, do not leave it unassigned.
For docs on what these parameters are, refer to: https://developer.roblox.com/en-us/articles/Catalog-API

CATEGORY VALUES:
Featured (=0), 
All (=1),
Collectibles (=2),
Clothing (=3),
BodyParts (=4), 
Gear (=5),
Accessories (=11), 
AvatarAnimations (=12),
CommunityCreations (=13).

Examples:
c.search_catalogue(queryName="Duck", queryCategory=None)
c.search_catalogue(queryName="Korblox", queryCategory=2)
"""

import requests
import json

# Simple Util class for GET requests
class Utils:
  def __init__(self):
    pass
    
  def req_get(url):
      req = requests.get(url)
      return json.loads(req.text)

# Create the catalogue search class
class CatalogueSearch:
  def __init__(self, queryName : str, queryCategory=None):
    self.queryCategory = queryCategory # The category, by default this is none

    self.queryName = queryName # The name or keyword that we will be searching for

  def update(self):
    if self.queryCategory is None:
      url = f"https://catalog.roblox.com/v1/search/items/details?Keyword={self.queryName}&Limit=10"
    else:
      url = f"https://catalog.roblox.com/v1/search/items/details?Category={self.queryCategory}&Keyword={self.queryName}&Limit=10"

    r = Utils.req_get(url) 

    if "data" not in r.keys():
      err_code = r["errors"][0]["code"]
      err_msg = r["errors"][0]["userFacingMessage"]
      error_str = f"ROBLOX API ERROR: Error code {err_code} | {err_msg}"

      print(error_str)
      return

    if len(r["data"]) == 0:
      print("ROBLOX API ERROR: No results found for your inputted parameters")
      return

    items = {} # Create a dict called items

    for item in r["data"]:
      """
      This dict displays the found items in a {'NAME':ID} format, alone this itself is obviously not that great, but with a simple for loop this can easily be worked around
      """
      ID = item["id"] 
      name = item["name"]

      items[name] = ID 
    
    return items # Return the dict


class Client:
  def __init__(self):
    pass
      
  def search_catalogue(self, queryCategory : int, queryName : str):

        """
        Simple error handling
        """

        queryCategory_IsStr = isinstance(queryCategory, str)

        queryName_IsInt = isinstance(queryName, int)

        if queryCategory_IsStr:
          raise TypeError(f"Query Category ({queryCategory}) must be an integer")
        
        if queryName_IsInt:
          raise TypeError(f"Query name ({queryName}) must be a string")

        # Create the class and set its attributes
        searchCatalogue = CatalogueSearch(queryCategory=queryCategory, queryName=queryName)

        # Actually return our dict here
        return searchCatalogue.update()


# Actually testing the functionality
c = Client()

results = c.search_catalogue(queryName="cheese", queryCategory=0) # Search for an item called "cheese" in the item category of 0 / featured

for name, id in results.items():
    print(f"{name} | {id}")
