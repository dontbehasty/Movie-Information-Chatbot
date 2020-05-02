import json
import urllib.request
 
def popular_movies_year(event, context):
    
    slots = event['currentIntent']['slots']
    MovieYear = slots['Year']
    
    if(str(MovieYear) == "None"):
        movie_output = "I encountered an error getting information. Please enter a valid year."
    else:
    
        #Form the URL to use
        TmdbApiUrl = "https://api.themoviedb.org/3/discover/movie?api_key=your_tmdb_apikey&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_original_language=en&primary_release_year="
        URLToUse = TmdbApiUrl + MovieYear
        
        try:
            #Call the API
            APIResponse = urllib.request.urlopen(URLToUse).read()
            
            #Get the JSON structure
            MovieJSON = json.loads(APIResponse)
            
            movieList = []
            for movie in MovieJSON['results']:
                movieTitle = movie['title'] 
                movieList.append(movieTitle)
    
            movieString = ', '.join(movieList)
            
            #Form the string to use
            movie_output = "Here are the top movies from " + MovieYear + ": " + movieString
            
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