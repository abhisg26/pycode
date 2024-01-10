## AVOID Using: "import *" At ALL Costs In Python
#order 1 requests module libraries get overshadowed by my_module libraries and then ends up in AttributeError
# from requests import *
# from my_module import *

#order 2
from my_module import *
from requests import *

from pprint import pprint

def main():
    url: str = 'https://www.python-guide.com'
    response: Response = get(url)
    print(response.status_code)

if __name__=="__main__":
    main()
    pprint(globals())
