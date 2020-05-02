import json
import urllib.request
 
def actor_movies(event, context):
    
    slots = event['currentIntent']['slots']
    MovieActor = slots['Actor']
    
    #Form the URL to use
    ActorToGet = TurnToURL(MovieActor)
    TmdbApiUrl = "https://api.themoviedb.org/3/search/person?api_key=your_tmdb_apikey&language=en-US&include_adult=false&query="
    URLToUse = TmdbApiUrl + ActorToGet
    
    try:
        #Call the API
        APIResponse = urllib.request.urlopen(URLToUse).read()
        print(APIResponse)
        
        #Get the JSON structure
        MovieJSON = json.loads(APIResponse)
        print(MovieJSON)
        
        movieList = []
        for kf in MovieJSON['results']:
            dept = kf['known_for_department']
            if dept == "Acting":
                for movie in kf['known_for']:
                    mediatype = movie['media_type']
                    if mediatype == "movie":
                        movieTitle = movie['title'] 
                        movieList.append(movieTitle)

        movieString = ', '.join(movieList)
        
        #Form the string to use
        movie_output = MovieActor + " is mainly known for the following movies: " + movieString
        
    except:
        movie_output = "I encountered an error getting information. Please try again"
    
    message = movie_output 
 
    return {"dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": message
        }}}
        
#Takes the information from the slot and turn it into the format for the URL which 
#puts % signs between words
def TurnToURL(InSlot):
  print(InSlot)    
  
  #Split the string into parts using the space character    
  SplitStr = InSlot.split()
  
  OutStr = ""   #Just initialise to avoid a reference before assignment error
   
  #Take each component and add a + to the end   
  for SubStr in SplitStr:
    OutStr = OutStr + SubStr + "%20"
      
  #Just trim the final + off as we don't need it
  return OutStr[:-3]       