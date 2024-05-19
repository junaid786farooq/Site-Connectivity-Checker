# Site Connectivity Checker

This program checks the connectivity of a given URL by attempting to open it and printing the response code if successful.

## Features

- Verifies the connectivity of any given URL.
- Ensures the URL starts with `http://` or `https://`.
- Handles exceptions and provides error messages if the connection attempt fails.

## How to Use

1. **Run the Program:**
   - Execute the script in a Python environment.

2. **Enter the URL:**
   - When prompted, enter the URL of the site you want to check.
   - The program ensures that the URL starts with `http://` or `https://`.

3. **View Results:**
   - The program attempts to open the URL.
   - If successful, it prints a success message along with the response code.
   - If unsuccessful, it prints an error message.

## Example

```
This is a site connectivity checker program
Enter the URL of the site you want to check: example.com
Checking Connectivity....
Connected to https://example.com successfully
The response code was: 200
```

## Requirements

- Python 3.x
- `requests` library (Install using `pip install requests`)

## Libraries Used

- `requests`: A simple, yet elegant HTTP library for Python, used to handle HTTP requests easily.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
