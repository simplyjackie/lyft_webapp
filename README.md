# lyft_webapp 

- Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
- Return a JSON object with the key “return_string” and a string containing every third letter from the original string

POST request in form:
   
   ```curl -d '{"string_to_cut": string}' localhost:8080```

Returns:
   
   ```{"return_string": return_string}```
    
   where return_string is every third letter from the original string_to_cut

Usage:
   
   ```./server.py [<port>]```
   
Sample:
   
   ```curl -d '{"string_to_cut": "iamyourlyftdriver"}' localhost:8080/```
   
   Returns: 
   
   ```{"return_string": "muydv"}```
