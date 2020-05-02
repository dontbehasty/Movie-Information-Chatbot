import json
import urllib.request

def specific_movie_info(event, context):
    
    slots = event['currentIntent']['slots']
    MovieName = slots['MovieName']
    MovieInfo = slots['MovieInfo']
    
    #Form the URL to use
    MovieToGet = TurnToURL(MovieName)
    OmdbApiUrl = "http://www.omdbapi.com/?apikey=your_omdb_apikey="
    FullURL = OmdbApiUrl + MovieToGet
    
    try:
        #Call the API
        APIResponse = urllib.request.urlopen(FullURL).read()
        
        #Get the JSON structure
        MovieJSON = json.loads(APIResponse)
        
        #Form the string to use
        if MovieInfo == "Runtime":
            movie_output = "The runtime for this movie is " + MovieJSON["Runtime"] + "."
        elif MovieInfo == "ReleaseYear":
            movie_output = "It was released in the year " + MovieJSON["Year"] + "."
        elif MovieInfo == "ReleaseDate":
            movie_output = "It was released on " + MovieJSON["Released"] + "."
        elif MovieInfo == "Genre":
            movie_output = "This movie meets the following genres: " + MovieJSON["Genre"] + "."
        elif MovieInfo == "Director":
            movie_output = "It was directed by " + MovieJSON["Director"] + "."
        elif MovieInfo == "Production":
            movie_output = "This movie was produced by " + MovieJSON["Production"] + "."
        elif MovieInfo == "Plot":
            movie_output = "The plot is as follows: " + MovieJSON["Plot"] + "."
        elif MovieInfo == "Actors":
            movie_output = "It starred: " + MovieJSON["Actors"] + "."
        elif MovieInfo == "imdbRating":
            movie_output = "It has an IMDB Rating of " + MovieJSON["imdbRating"] + "."
        elif MovieInfo == "AgeRating":
            movie_output = "It has an age rating of " + MovieJSON["Rated"] + "."
    except:
        movie_output = "I encountered an error getting information for that movie. " \
                        "Please try a different movie." 
    
    message = movie_output 
 
    return {"dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": message,
        }}}
        
#Format movie name for URL (put + signs between words)
def TurnToURL(InSlot):
  
  #Split the string into parts using the space character    
  SplitStr = InSlot.split()
  
  OutStr = ""   #Initialise to avoid a reference before assignment error
   
  #Take each component and add a + to the end   
  for SubStr in SplitStr:
    OutStr = OutStr + SubStr + "+"
      
  #Trim the final + off (as we don't need it)
  return OutStr[:-1]