CURERNT GOAL: MO MORE HARDCODED STRINGS!

LOLlipopWrapper is a fairly heavyweight wrapper for the public League of Legends API.
    * easy-to-use request mechanism
    * learning/tutorial-type error handling: incorrect calls will be explained, etc. 

Libraries/modules currently used in LOLlipopWrapper:
    * requests (http://docs.python-requests.org/en/master/)
    * requests-cache (https://pypi.python.org/pypi/requests-cache)
    * json (https://docs.python.org/3/library/json.html)
    * time

Current descriptions of files:
    api_key.txt
        * plaintext file that holds the API key
        * (https://developer.riotgames.com/docs/api-keys)
    get_api_key.py
        * funtion that retrieves API key from file.
        * IMPORTANT: change variable apiKeyFilePath to whatever the
        path of the api_key.txt file is
    form_urls.py
        * holds constant strings for IDs like region and platform
        * contains suffix-generation for different API requests
        * current contains commented-out function names for all possible API requests
        * contains URL-generation given different suffixes
    form_urls_test.py
        * contains methods to make API request and test it out
        * handles errors/exceptions from HTTP request
        * handles error of invalid API request
        * all errors/exceptions currently return strings
    initialize_database.py
        * contains function to initialize champion database with allChampsSuffix method
        * database = dictionary of championId to empty list
        * contains function to tet out requestsCache
    test_values.py: 
        *contains variables for testing (e.g. some summoner names and summoner matches, teams, regions, etc)

Organizational notes:
    requestMaker class: will make the actual HTTP request to the API
        * one instance of requestMaker per program: static
        * requestMaker will have one request-cache?
        * will have a text file kind of thing to hold static info / database json info?
            * will this text-file thing update itself each time the requestMaker class is used?
                * date stored to record when the text file was last checked?
                * static data versions -- look into this
    ambiguous function parameters: functions that can accept one argument or a list
        * will accept lists only, as per the pythonic way of explicit over implicit
        * if only one item is being passed, rather than a list, then the item must be put in a list and passed that way
    leaguesBySummonerSuffix: doesnt work, results in error... get teamIDs from getTeam API call


DONE:
    * fill in optional values for API requests that have them

TODO/other notes:
    * RESTRUCTURE REQUESTS TO REDUCE HARDCODING -- in progress
    * implement requestMaker and requests-cache for entire thing
    * implement requests-q
    * default region setup? 
    * figure out how to handle errors gracefully
    * parse/interpret status messages for incorrect API calls?
    * individual testing/print output messages for each API request?
    * create API request class? probably not necessary
    * level of depth for objects (summoner, runes, masteries, champions, etc)
    * list checking (length) for maximum number of objects that can be passed
    * patchable: versions in API call should be able to be updated with ease
    * tournament provider api requests
    * move APIkey filepath and rate limiting constants to their own file


structure notes
    * four kinds of requests: api/lol, championmastery, observer-mode, tournament/public
    * api/lol requests can be regional or static: static data requests are in a diff. format
    * by default, all requests have one param in the params section: the apiKey. construct default?
    * idea: one request former/builder that builds individual requests?
    * different caches for different kinds of requests

basic api (non champ mastery, non observer-mode, non tournament)
    * suffix format is in the form of /api/lol/ + static (if static) + region + version + request category + further modifiers
    * REQUESTS_Q with cache, spaces out requests
    * "refreshable" objects: objects saved (e.g. player, player's masteries) and to refresh, make a refresh call and request will be added to stack