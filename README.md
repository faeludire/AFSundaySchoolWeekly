# AFSundaySchoolWeekly

This project scrapes the latest Sunday school lesson details from apostolicfaithweca.org and tweets updates everyday.

## To run an instance of this app, you need:

#### Twitter API Key
- Create `credentials.py` in `AFSundaySchoolWeekly/`
- `credentials.py` holds your own Twitter API Keys


```
credentials.py
consumer_key = "YOUR-CONSUMER-KEY-HERE"
consumer_secret = "YOUR-CONSUMER-SECRET-HERE"
access_token = "YOUR-TOKEN-HERE"
access_token_secret = "YOUR-TOKEN-SECRET-HERE"
```

#### Clone the Repo
- The code is hosted at https://github.com/faeludire/AFSundaySchoolWeekly.git
- Check out the latest development version:
    ```
    $ git clone https://github.com/faeludire/AFSundaySchoolWeekly.git
    $ cd AFSundaySchoolWeekly/
    ```

- To install libraries, run:

    ```
    $ pip install -r requirements.txt
    ```
    
- To start the app run:

    ```
    $python3 weekly_sunday_school.py
    ```