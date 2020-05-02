import json
import urllib.request
import random
 
def suggest_movie(event, context):
    slots = event['currentIntent']['slots']
    
    genre = slots['Genre']
    certification = slots['Certification']
    runtime = slots['Runtime']
    
    genreUrl = '&with_genres=' + genre
    certificationUrl = '&certification.lte=' + certification
    runtimeUrl = '&with_runtime.lte=' + runtime
    
    #Form the URL to use
    TmdbApiUrl = "https://api.themoviedb.org/3/discover/movie?api_key=your_tmdb_apikey&language=en-US&region=gb&sort_by=popularity.desc&certification_country=uk&include_adult=false&include_video=false"
    
    URLToUse = TmdbApiUrl + genreUrl + certificationUrl + runtimeUrl
    
    try:
        #Call the API
        APIResponse = urllib.request.urlopen(URLToUse).read()
        
        #Get the JSON structure
        MovieJSON = json.loads(APIResponse)
        
        movieList = []
        for movie in MovieJSON['results']:
            movieTitle = movie['title'] 
            movieList.append(movieTitle)

        movieSuggestion = random.choice(movieList)
        
        #Form the string to use
        movie_output = "Based on your input here is a movie suggestion: " + movieSuggestion
        
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