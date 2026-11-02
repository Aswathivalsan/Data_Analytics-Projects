feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
# Add More Feedback

n = int(input("How many more feedback do you want to add? "))
for i in range(n):
    print("\n Enter feedback Details")

    name = input("Enter Name: ")
    feedback =input("Enter Written feedback: ")

    while True:
        rating = int(input("Enter Rating (1-5): "))

        if rating >= 1 and rating <= 5:
            break
        else:
            print("Invalid rating! please enter a rating between 1 and 5.")

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

    print("\nFeedback added successfully!")
    print(feedback_data)

    for i in range(len(feedback_data['Feedback'])):

        text = feedback_data['Feedback'][i]
        
        text = text.replace(".","")
        text = text.lower()
        text = text.replace(",","")
        text = text.replace("!","")
        text = text.replace("?","")
        text = " ".join(text.split())

        feedback_data['Feedback'][i] = text
    print("\nCleaned Feedbacks: ")
    print(feedback_data['Feedback'])

'''word count '''
def count_word_in_feedbacks(word):
    count = 0
    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count = count +1

    return count

print("\nWord Count Insights")
print("Feedbacks Containing Good: ",count_word_in_feedbacks("good"))
print("Feedbacks containing poor: ", count_word_in_feedbacks("poor"))
print("Feedbacks containing excellent: ", count_word_in_feedbacks("excellent"))
print("\n Final Cleaned Feedback Data : ")
print(feedback_data)

total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])
average_rating = total_rating / total_feedbacks
print("\nAverage Rating:", round(average_rating, 2))


longest_feedback = ""
longest_name = ""
max_words = 0

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback
        longest_name = feedback_data['Name'][i]

print("\nLongest Feedback")

print("Name:", longest_name)
print("Feedback:", longest_feedback)
print("Word Count:", max_words)



unique_words = []

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        if word not in unique_words:
            unique_words.append(word)

print("\nUnique Words:")

print(unique_words)


sorted_feedbacks = sorted(
    zip(
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[2],
    reverse=True
)

print("\nFeedbacks Sorted by Rating:")

for name, feedback, rating in sorted_feedbacks:

    print("Name:", name,
          "| Feedback:", feedback,
          "| Rating:", rating)

                                                             

    
