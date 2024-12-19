<!-- markdownlint-disable -->

<a href="../../project/MovieHotline.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `MovieHotline.py`
This is a movie information resource that asks users for a movie title then refines that input to accurately find information about that movie. The information displayed is choosen by the user through rudimentary menus.

## Installation Instructions

1. **Aquire the respoitory:**  You can use either Github download or this script to get the required files:

         git clone [https://github.com/Jon-Mcdonald093/-Movie-Hotline]
   

2. **Install required files:**

     Use the following code in terminal, with the correct path, to install:
         pip install -r requirements.txt

3. **Get API KEY and Load .env:**

     This program requires 2 api keys, both are free, provided you accept their various terms.

     **https://developer.themoviedb.org/reference/intro/getting-started**

     **https://api.watchmode.com/**

     Once you've aquired your keys edit the .env.example file to contain them with the TMDB key first then watchmode second, then rename the file to remove .example

4. **Creating .exe file:**

     Once you've made your .env file return to a terminal window in the path of the repository, in that window type:
   
         pyinstaller --onefile MovieHotline.py

     This will take a moment so give it time. Once the build is complete the .exe file will be located in a dist folder in the directory that contained the repository.

5. **Running the Program:**

     Run the MovieHotline.exe file, a command prompt window should appear.
     In this window will be prompted to enter a movie title, please spell correctly, though case doesn't matter.
     After you input a film title you'll be prompted to refine your search within the given list, this list can be expanded or shortened in the code.
     Once you've confirmed your selection you'll be presented some basic facts on the film, then 8 choices of further information
     From here you can loop around or exit to close the window.
     _YOU MUST KEEP THE .exe IN THE DIRECTORY OF THE .env FOR THE PROGRAM TO FUNCTION_


**Global Variables**
---------------
- **cpi_library** - Open variable to hold the cpi library 
- **second_key** - For Watchmode API key, I used .env files for security
---

<a href="../../project/MovieHotline.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```

Main function that runs the movie search engine.

This function proceeds through the following steps: 1. Asks for user input in the form of a movie title, or quit 2. Requests movie details that match the user input through API to The Movie DB(TMDB) 3. The results are sorted by the popularity metric provided by TMDB then printed for user selection 4. Basic information from the selected film is print, full Title, runtime, Director, writer, and top billed actors. 5. User is then prompted to choose one of the following options:
    -Full Cast and Crew
    -Trailer
    -Production infomation
    -Synopsis
    -Website
    -Tagline
    -Extra Facts

The main loop allows the user to choose further informtion, return to search, or exit.

See Also:  This program relies heavily on library tmdbv3api created by Anthony Bloomer  Further information on those functions can be found at:  https://github.com/AnthonyBloomer/tmdbv3api


---

<a href="../../project/MovieHotline.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `refine_search`

```python
refine_search(list)
```

Takes list of movies from user input query then refines it to aquire movie id



**Args:**

 - <b>`list`</b> (list):  Top 5 movies that conform to user input sorted by popularity



**Returns:**
 movie id or error if input error


---

<a href="../../project/MovieHotline.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `details`

```python
details(movie, id)
```

Takes movie then queries TMDB for basic information on movie that's formatted then printed



**Args:**
  tmdbv3api's movie instance
 - <b>`id`</b> (int):  movie id from TMDB



**Returns:**
 Prints various basic movie facts that would be found on a poster id of the movie


---

<a href="../../project/MovieHotline.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ask_further_info`

```python
ask_further_info(movie, n)
```

Presents user with list of options each item is a function to query DB for that information exit and return inputs allow user to navigate out or back



**Args:**

  - <b>`movie `</b>:  tmdbv3api's movie instance
  - <b>`n`</b> (int):  movie id

**Returns:**
 List of options for user to pick Allows user to exit




---

<a href="../../project/MovieHotline.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_synopsis`

```python
get_synopsis(movie, n)
```

Uses movie id to retrieve synopsis



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id

**Returns:**
 Prints movie synopsis


---

<a href="../../project/MovieHotline.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_full_cast_and_crew`

```python
get_full_cast_and_crew(movie, n)
```

Retrieves credits



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints formated credits line by line


---

<a href="../../project/MovieHotline.py#L260"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_trailer`

```python
get_trailer(movie, n)
```

Retrieves trailer link



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints usable link to video on Youtube.com


---

<a href="../../project/MovieHotline.py#L285"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_production_information`

```python
get_production_information(movie, n)
```

Gets production information, such as company, budget, revenue, calculates profit from given information.





**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints production information Also checks year movie is made then pings user for inflation calculation if older than 1990


---

<a href="../../project/MovieHotline.py#L325"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_extra_facts`

```python
get_extra_facts(movie, n)
```

Retrieves extra information for movie that didn't fit other categories





**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints original title, Alternative title, Genre, and Spoken language


---

<a href="../../project/MovieHotline.py#L356"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_website`

```python
get_website(movie, n)
```

Retrieves website link for movie



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints link to the movie's website


---

<a href="../../project/MovieHotline.py#L374"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_tagline`

```python
get_tagline(movie, n)
```

Retrieves tagline



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints tagline for movie


---

<a href="../../project/MovieHotline.py#L392"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_credits`

```python
get_credits(movie, id)
```

Retrieves credits then splits that into Director, up to 3 writers, and first 5 billed actors



**Args:**

 - <b>`movie `</b>:  tmdbv3api's movie instance
 - <b>`n`</b> (int):  movie id



**Returns:**
 Prints top 5 actors as Top Billed, Director, and up to 3 Writers


---

<a href="../../project/MovieHotline.py#L431"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_streaming`

```python
get_streaming(movie, id)
```

An api connection to the Watchmode db that can provide streaming information on the requested movie. The amount of streaming sources returned is determined by the film in question's availablity and default values.



**Args:**

  - <b>`movie`</b>:  tmdbv3api's movie instance -- unused in this function, but due to oversights must be included.
  - <b>`n`</b> (int):  movie id

**Returns:**
 Prints a list of movie streaming sites with appropriate information regarding cost, format, and if the film is to rent or own.

**Notes:**

> max_results limits the results to prevent spam, but can be changed item.get("region") Limits region to US to prevent showing useless results, but can be changed to any country code depending on use case.

>Streaming data powered by Watchmode.com


---

<a href="../../project/MovieHotline.py#L481"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_list`

```python
format_list(list)
```

Formats lists so they print correctly



**Args:**

 - <b>`list`</b> (list):  list of names



**Returns:**
 Formated list with proper spacing or fills list with "N/A" if empty


---

<a href="../../project/MovieHotline.py#L497"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `adjust_for_inflation`

```python
adjust_for_inflation(rev, year, budget)
```

Checks production year and if before 1990 asks user if they want to adjust monetary figures for inflation



**Args:**

 - <b>`rev`</b> (int):  revenue of movie
 - <b>`year`</b> (int):  year of movie as int
 - <b>`budget`</b> (int):  budget of movie



**Returns:**
 Depending on user input: if Y, outputs budget, rev, and profit adjusted for inflation by CPI library if N, or film after 1990, returns budget, rev, and profit as found in TMDB


---

<a href="../../project/MovieHotline.py#L528"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `initialize_cpi_library`

```python
initialize_cpi_library()
```

Initializes the cpi library only when inflation adjustment is request to prevent lag time at program start up.



**Args:**
  None

**Returns:**
  cpi object




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
