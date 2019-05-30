import requests, bs4

# to loop through the golfers' webpages
for i in range (1,31):
    resp=requests.get('http://localhost:8000/golfer/'+str(i))
    
    # to scrape and parse the html text
    golfer=bs4.BeautifulSoup(resp.text,"html.parser")
    golfer_name=golfer.find('h2').text
    golfer.select('td')
    
    print("Golfer: " + golfer_name + "\n")
    
    # to create a list of each of the golfer's tournaments and scores, including HTML tags
    td_list = golfer.select('td')
    
    # to get header row
    tourn_title = td_list[0].getText()
    tourn_title = tourn_title.strip()
    score_title = td_list[1].getText()
    score_title = score_title.strip()
    title = tourn_title.ljust(21) + " " + score_title 
    print(title)
   
    #to get dashed seperator row
    t_dash_line = "----------"
    s_dash_line = "-----------"
    dash_line = t_dash_line.ljust(21) + " " + s_dash_line
    print(dash_line)
    
    # to loop through the list of tournaments and scores
    for index in range(2,len(td_list), 2):
        # to get just the text, not the tags & eliminate leading and trailing whitespace
        tourn_name = td_list[index].getText()
        tourn_name = tourn_name.strip()
        score = td_list[index+1].getText()
        score = score.strip()
        
        tourn_score = tourn_name.ljust(21) + " " + score
        print(tourn_score)
    
    print("\n")
    