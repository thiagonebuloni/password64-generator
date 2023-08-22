# Password64 Generator

## This script is for study purposes only. It is not applicable to real-world scenarios and does not have any security reliability

Generates a base64 string with special characters based on a given string, with password generation purposes.
Input a selected word relative to a service to which you want to generate a random password.
You'll receive a base64 encoded string with special characters.
The same input, the same output.

Example for a video service like Youtube.com:
```
Input: python3 password64-generator -e videos

Output: dmlkZ-W9z
```
```
Input: python3 password64-generator -d dmlkZ-W9z

Output: videos
```