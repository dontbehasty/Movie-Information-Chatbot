import json
import urllib.request

def general_movie_info(event, context):
    
    slots = event['currentIntent']['slots']
    MovieName = slots['MovieName']
    MovieInfo = slots['MovieInfo']
    
    
    #Form the URL to use
    MovieToGet = TurnToURL(MovieName)
    OmdbApiUrl = "http://www.omdbapi.com/?apikey=your_omdb_apikey="
    FullURL = OmdbApiUrl + MovieToGet
    print(FullURL)
    
    try:
        #Call the API
        APIResponse = urllib.request.urlopen(FullURL).read()
        
        #Get the JSON structure
        MovieJSON = json.loads(APIResponse)
        
        #Form the string to use
        if MovieInfo == "All":
            movie_output = "You asked for the movie " + MovieJSON["Title"] + ".  " \
                        "It was release in " + MovieJSON["Year"] + ".  " \
                        "It was directed by " + MovieJSON["Director"] + ".  " \
                        "It starred " + MovieJSON["Actors"] + ".  " \
                        "It has a runtime of " + MovieJSON["Runtime"] + ".  " \
                        "It has an IMDB Rating of " + MovieJSON["imdbRating"] + ".  " \
                        "The plot is as follows: " + MovieJSON["Plot"] + ".  "
        elif MovieInfo == "Runtime":
            movie_output = "The runtime for " + MovieJSON["Title"] + " is " + MovieJSON["Runtime"] + "."
        elif MovieInfo == "ReleaseDate":
            movie_output = MovieJSON["Title"] + " was released on " + MovieJSON["Released"] + "."
        elif MovieInfo == "Plot":
            movie_output = "The plot is as follows: " + MovieJSON["Plot"] + "."
        elif MovieInfo == "imdbRating":
            movie_output = MovieJSON["Title"] + " has an IMDB Rating of " + MovieJSON["imdbRating"] + "."
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