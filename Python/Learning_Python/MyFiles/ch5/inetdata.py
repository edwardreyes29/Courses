# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  webURL = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webURL.getcode()))  # returns 200

  data = webURL.read()
  print(data) # returns the HTML code


if __name__ == "__main__":
  main()
