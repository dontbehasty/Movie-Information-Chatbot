import json
import urllib.request
 
def similar_movies(event, context):

    slots = event['currentIntent']['slots']
    MovieName = slots['MovieName']
    
    #Get Movie ID
    #Form the URL to use
    MovieToGet = TurnToURL(MovieName)
    TmdbApiUrl = "https://api.themoviedb.org/3/search/movie?api_key=your_tmdb_apikey&language=en-US&page=1&include_adult=false&query="
    URLToUse = TmdbApiUrl + MovieToGet
    print(URLToUse)
    
    try:
        #Call the API
        APIResponse = urllib.request.urlopen(URLToUse).read()
        print(APIResponse)
        
        #Get the JSON structure
        MovieJSON = json.loads(APIResponse)
        print(MovieJSON)
        
        for movie in MovieJSON['results']:
            movieTitle = movie['title']
            if movieTitle.lower() == MovieName.lower():
                movieID = movie['id'] 
                print(movieID)
                break
            
        #Use Movie ID to get similar movies
        #Form the URL to use
        TmdbApiUrl = "https://api.themoviedb.org/3/movie/"
        UrlEnding = "/similar?api_key=a56eb6f732de03767af24be8812ef6c6&language=en-US&page=1"
        StringID = str(movieID)
        URLToUse = TmdbApiUrl + StringID + UrlEnding
        print(URLToUse)
    
        try:
            #Call the API
            APIResponse = urllib.request.urlopen(URLToUse).read()
            print(APIResponse)
        
            #Get the JSON structure
            MovieJSON = json.loads(APIResponse)
            print(MovieJSON)
        
            similarList = []
            for similar in MovieJSON['results']:
                title = similar['title']
                similarList.append(title)

            similarString = ', '.join(similarList)
            print(similarString)
        
            #Form the string to use
            movie_output = "Here are some movies that are similar: " + similarString
        except:
            movie_output = "I encountered an error getting information. Please try again!"
    except:
        movie_output = "I encountered an error getting information. Please try again."
    
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