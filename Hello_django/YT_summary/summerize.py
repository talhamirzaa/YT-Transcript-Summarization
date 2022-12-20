#imprt stmnts for add step...
import urllib.request
import json
import urllib
from transformers import pipeline
#step 1
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

#step 2

#jeff bezos 
#https://www.youtube.com/watch?v=EctzLTFrktc
#vid_id = 'EctzLTFrktc'

#Germany
#"https://www.youtube.com/watch?v=A4OmtyaBHFE"
vid_id = 'A4OmtyaBHFE'

data =  yta.get_transcript(vid_id)



#additional step

  
params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % vid_id}
url = "https://www.youtube.com/oembed"
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string

with urllib.request.urlopen(url) as response:
    response_text = response.read()
    vid_title = json.loads(response_text.decode())
    file_title = vid_title['title']
    file_title = re.sub('[|/\:?*"<>]', '-', file_title)
    print(file_title)

#step 3
transcript=''
for value in data:
    for key,val in value.items():
        if key == 'text':
            transcript +=' '+val


l= transcript.splitlines()
final_tra = " ".join(l) 

#print(final_tra) #to print output in console
print(len(final_tra))

#step 4 (to get output in txt file)
file = open(file_title+".txt",'w')
file.write(final_tra)
file.close()


# Step 5: *Summarziation Part*

summarizer = pipeline('summarization')
summary_text = summarizer(final_tra)[0]['summary_text']
print("Summary: \n")
print(summary_text)
#print(summarized_text)