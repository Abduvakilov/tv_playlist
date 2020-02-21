import urllib.request, json, codecs


# itv
data = {}
with urllib.request.urlopen("http://itv.uz/api2/channels/list") as url:
    data = json.loads(url.read().decode())

channels = data['data']['channels']

m3u = '#EXTM3U\n'

for channel in channels:
  if channel['is_free'] == "false":
    continue
  poster_url = channel["poster_url"]
  title = channel['title']
  # poster_path = 'covers/' + title + poster_url[-4:]
    
  # urllib.request.urlretrieve(f'http://itv.uz/{poster_url}', poster_path)

  channel_data = {}
  with urllib.request.urlopen(f"http://itv.uz/api2/channels/showchannel?id={channel['id']}") as url:
    channel_data = json.loads(url.read().decode())
  
  m3u += f'#EXTINF:-1 tvg-logo="http://itv.uz{poster_url}", {title}\n'
  m3u += channel_data['data']['channel']['source_url'] + '\n'

# mediabox
data = {}

with urllib.request.urlopen("https://api.new.mediabox.uz/v2/tv/channels") as url:
  data = json.loads(url.read().decode())

channels = data['data']

for channel in channels:
  poster_url = channel['image']
  title = channel['title']

  m3u += f'#EXTINF:-1 tvg-logo="{poster_url}", {title}\n'
  m3u += channel['tv_link'] + '\n'

file = codecs.open("tv.m3u", "w", "utf-8")
file.write(m3u)
file.close()
