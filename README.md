# Homework for BEW1.1
Gotta find out how to do the API good.

## QUESTION 1
```bash
Describe the data contained in the API response. What can we discern about the weather in the specified city?
```
It's itemized with each entry correlating to what one would consider its standard analogue, with the notable exception of temperature. Temperature appears to be in Kelvin.

```bash
How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)
```
Temperature is found under the 'stations' category, within it's 'main' dictionary and under the 'temp' value. Temperature appears to be listen in Kelvin.
