import re
# pattern = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-])\.([a-z\.]{2,6})$')

pattern_email = re.compile(r""" 
            ^([a-z0-9_\.-]+)              # local Part 
            @                             # single @ sign 
            ([0-9a-z\.-]+)                # Domain name 
            \.                            # single Dot . 
            ([a-z]{2,6})$                 # Top level Domain   
             """,re.VERBOSE | re.IGNORECASE) # re.X | re.I

match = pattern_email.search("thomas123@yahoo.com")
print(match.group()) # thomas123@yahoo.com
print(match.groups())  # ('thomas123', 'yahoo', 'com')