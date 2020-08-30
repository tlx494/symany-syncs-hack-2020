# symany-syncs-hack-2020
Team Symany for Syncs Hack 2020

## Post Request

This API is published to Google Cloud and sits at https://symanyapi.gq

### POST: /check-post

Accepts a json body with title of post and link to it. e.g.:
```
{
    "title" : "Huge news as universe ending threat approaches planet Earth!!!"
    "link" : "https://www.link.com" # only accepts valid links
}
```

The parsed link will be run through the machine learning algorithm, and the domain through our blacklist-checker. 

See a full description at: 
https://devpost.com/software/symany