import re

class FeatureExtract(object):
    def  __init__(self):
        self.evidence = None
        self.statusKarma = None
	self.statusAccAge = None
	self.statusPrevAct = None

    def findEvidence(self,request_text_edit_aware):
	'''Find reddit post with image/proof
	   On roap, users often post thier photo/video 
           as an evidence of thier condition/existence
	   this module uses regex library (re) to parse
	   url from imgur and youtube
           As well as url with jpg and png file 		
	   1 - evidence is found
           0 - evidence is not found
        '''

	regex = re.compile(r"([Hh]ttp(\S)+((imgur)|(youtube))(\w|\W)+)|([Hh]ttp(\S)+((jpe?g)|(png)))")
	match = re.search(regex,request_text_edit_aware)	
	if match: 	
            self.evidence = 1
	else :
	    self.evidence = 0

    def evalStatus(self,requester_upvotes_minus_downvotes_at_request, \
	requester_account_age_in_days_at_request, requester_number_of_comments_in_raop_at_request,\
	requester_number_of_posts_on_raop_at_request):
	'''evaluate the status of the requester
	   statusKarma = overall karma point at request time
	   statusAccAge = account age at request time
	   statisPrevAct 1-->previously active on raop, else 0
	'''
	self.statusKarma = requester_upvotes_minus_downvotes_at_request
	self.statusAccAge = requester_account_age_in_days_at_request
	self.statusPrevAct = 1 if requester_number_of_comments_in_raop_at_request + \
	requester_number_of_posts_on_raop_at_request > 0 else 0
