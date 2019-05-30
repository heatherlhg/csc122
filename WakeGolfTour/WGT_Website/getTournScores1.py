import requests, bs4
# loop for each golfer
for i in range(1,31):
    # get golfer tournament scores webpage
    resp = requests.get('http://localhost:8000/golfer/'+str(i))
    
     # if successful,
    if resp.status_code == 200:
        
        # create a beautiful soup object with the response text
        golfer = bs4.BeautifulSoup(resp.text, "html.parser")
        
        # first 'h2' element is the golfer name
        golfer_name = golfer.find('h2').text.strip() 
        print("Golfer: " + golfer_name + '\n')
        
        # the scores are in a list of 'td' elements 
        td_list = golfer.select ('td')
        
        # 1st element then every other element is the tournament name
        # second element then every other element is the score 
        # so loop using a step of 2
        for i in range(0,len(td_list), 2):
            tourn_name = td_list[i].getText().strip() 
            tourn_score = td_list[i+1].getText().strip()
            # longest name is 21 chars so use for justification # note when display is 'piped'
            # it will lose the justification
            row = tourn_name.ljust(21) + " " + tourn_score 
            print (row)
            
        print ('===========================\n')