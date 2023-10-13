# Happy Cinema

## Description
Happy Cinema is a Movie Recommendation Application. You can either search for a current movie using the search feature, or manually enter qualities of your desired movie. The application will then recommend the most similar movie that you can currently watch in theatres or at home. The project uses web scraping for the search feature which can return any movie that has existed. It also uses web scraping to create the recommended movie database however that is limited to movies at home and in theatres. The recommendation compares the similarity of both genre and description using Natural Language Processing and gives a similarity score weighted on both features. 

## Usage
Too use this application you can clone the repository. Within this repository you must run the 'gui.py' file and it will start the application.

## Example
There are two ways to use the application. One is with the search function. You would accept the search prompt and enter a movie. The movie must be the **exact** name, for example if you wanted Lord of the Rings you would have to enter 'The Lord of the Rings: The Fellowship of the Ring'. If the movie doesn't appear it's likely you must add the year since there are multiple movies with that name. If all else fails you can check rotten tomatoes and use the name they reference. If the movie is found the application will load and then return the movie reccomendation. The other function is to input your desired movie manually. For example a description would be 'I want a long twisted movie with a female lead' and genre 'Horror and Thriller'. 
