# PasswordExtractor

This tool is used to extract passwords matching a certain policy from a password dump.

usage: PasswordExtractor.py [-h] -i INPUT [-o OUTPUT] [-l LENGTH] [-a] [-A]
                            [-n] [-s]

Password extractor matching a particular policy.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Password input file (newline separated)
  -o OUTPUT, --output OUTPUT
                        Output file containing matching passwords
  -l LENGTH, --length LENGTH
                        Minimum password length
  -a                    Password contains lowercase character
  -A                    Password contains uppercase character
  -n                    Password contains number
  -s                    Password contains special character
