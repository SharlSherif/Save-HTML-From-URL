import urllib.request, urllib.error, urllib.parse

urls = open("./urls.txt").read().split("\n")
print(f"{len(urls)} URLs Found..")
for url in urls:
    response = urllib.request.urlopen(url)
    webContent = response.read()
    print(f"[RECIEVED] {url}")

    f = open(f'./content/{url.replace("https://", "").replace("http://","")}.txt', 'wb')
    f.write(webContent)
    f.close()

print("[COMPLETED]")