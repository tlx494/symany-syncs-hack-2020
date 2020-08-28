# symany-syncs-hack-2020
Team Symany for Syncs Hack 2020

# Api Summary
 API Endpoint @ /document
 e.g. http://127.0.0.1:8080/document

## Get Request 
Hasn't really been implemented, just returns "lol hi"

## Post Request
Body will look like this:
{
    "title" : "Huge news as universe ending threat approaches planet Earth!!!"
    "link" : "www.link.com" # only accepts valid links
}

Title is mandatory, Link is optional. Parsed title will be run through the model charlie made. Parsed link does nothing currently.