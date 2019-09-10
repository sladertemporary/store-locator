# Store Locator
## Overview

This application displays a directory of stores loaded from a JSON file. The application allows searching of these stores within a given radius.

Built using Flask.

*Post interview assignment

## Installation

To install and run the application, while in the top level directory (not the `store-finder` package), run the following commands in your terminal:

**Note:** the `flask init-db` command may take up to two minutes to initialise and populate the database.
```
$> pip install -r requirements.txt

$> export FLASK_APP=StoreLocator

$> flask init-db

Initialized the database.

$> flask run
```


If this was done successfully, you should see a similar message appear:
```
 * Serving Flask app "store-finder" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 164-171-902
```

The site should now be locally accessible through your browser at http://127.0.0.1:5000/.

## Testing

To test the application is working correctly and the database has been initialised properly, run the following command:
```
$> pytest
```

## Questions
> Tell us what test you completed (backend or full-stack)

Backend
> Tell us what you'd have changed if you'd have had more time?

I would have added: validation to the inputted data with appropriate error responses, caching views and database results for optimization, more tests,  automatic updates to the database triggered when changes to the stores directory file are made and potentially a visual map on the frontend.
> What bits did you find the toughest? What bit are you most proud of? In both cases, why?

I found that the toughest part was figuring out the logic behind determining the distance between two coordinates when checking stores located within a certain radius. Aside from that, I am most proud of adding additional front end functionality for usage of the store search function and links to each store location on Google maps.
> What's one thing we could do to improve this test?

Potentially add more stores to the `stores.json` file for testing optimisation, however, on the whole I think it's a very reasonable test with a few interesting challenges :).

