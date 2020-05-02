import json
import urllib.request
 
def top_rated_movies(event, context):

    #Form the URL to use
    TmdbApiUrl = "https://api.themoviedb.org/3/movie/top_rated?api_key=your_tmdb_apikey&language=en-US&page=1&region=US"
    URLToUse = TmdbApiUrl
    
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
        movie_output = "Here are the top rated movies: " + movieString
        
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