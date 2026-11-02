Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: D:/Akshay/Aswathi/data analytics/python/Survey Feedback Analyzer.py =
How many more feedback do you want to add? 1

 Enter feedback Details
Enter Name: asw
Enter Written feedback: good Service
Enter Rating (1-5): 4

Feedback added successfully!
{'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha', 'asw'], 'Feedback': ['   Very GOOD Service!!!', 'poor support,        not happy   ', 'GREAT experience! will come again.', 'okay     okay...', '   not    BAD', 'Excellent care, excellent staff!', 'good food and good ambience!', 'Poor response and poor handling of issue', 'Satisfied. But could be better.', 'Good support... quick service.', 'good Service'], 'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4, 4]}

Cleaned Feedbacks: 
['very good service', 'poor support not happy', 'great experience will come again', 'okay okay', 'not bad', 'excellent care excellent staff', 'good food and good ambience', 'poor response and poor handling of issue', 'satisfied but could be better', 'good support quick service', 'good service']

Word Count Insights
Feedbacks Containing Good:  4
Feedbacks containing poor:  2
Feedbacks containing excellent:  1

 Final Cleaned Feedback Data : 
{'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha', 'asw'], 'Feedback': ['very good service', 'poor support not happy', 'great experience will come again', 'okay okay', 'not bad', 'excellent care excellent staff', 'good food and good ambience', 'poor response and poor handling of issue', 'satisfied but could be better', 'good support quick service', 'good service'], 'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4, 4]}

Average Rating: 3.45

Longest Feedback
Name: Kiran
Feedback: poor response and poor handling of issue
Word Count: 7

Unique Words:
['very', 'good', 'service', 'poor', 'support', 'not', 'happy', 'great', 'experience', 'will', 'come', 'again', 'okay', 'bad', 'excellent', 'care', 'staff', 'food', 'and', 'ambience', 'response', 'handling', 'of', 'issue', 'satisfied', 'but', 'could', 'be', 'better', 'quick']

Feedbacks Sorted by Rating:
Name: Ravi | Feedback: very good service | Rating: 5
Name: Sam | Feedback: great experience will come again | Rating: 5
Name: Divya | Feedback: excellent care excellent staff | Rating: 5
Name: Arjun | Feedback: good food and good ambience | Rating: 4
Name: Nisha | Feedback: good support quick service | Rating: 4
Name: asw | Feedback: good service | Rating: 4
Name: Anu | Feedback: okay okay | Rating: 3
Name: Leela | Feedback: satisfied but could be better | Rating: 3
Name: Meera | Feedback: poor support not happy | Rating: 2
Name: Raj | Feedback: not bad | Rating: 2
Name: Kiran | Feedback: poor response and poor handling of issue | Rating: 1
