## v1.0.1-beta

Breaking changes:

-   Headers for post requests are not longer in postData but are also in the query (same as GET queries)
-   JSON post data is now sent using a JSON base64 encoded string
-   The Post and Header special tokens changed to `$$headers[]` and `$$post`

Fixes:

-   Fixed problem in GET queries headers not being applied correctly

Features:

-   Being able to change the spceial tokens prefix and header split token as well
-   Being able to pass in a real JSON which now retains the type as well so numbers and other JSON accepted types now work ex: `{"test": 4}` before `4` would have been considered a string
