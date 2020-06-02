import json
import pprint
import random
from numpy import log
from collections import Counter

pp = pprint.PrettyPrinter(indent=4)

"""
with open("snips_benchmark_data.json", "rb") as fp:
    data = json.load(fp)


intents = list(
    map(
        lambda d: list(
            map(
                lambda di: {di["name"]: list(map(lambda diq: diq["text"], di["queries"]))},
                d["intents"]
            )
        ),
        data["domains"]
    )
)

pp.pprint([item for sublist in intents for item in sublist])
"""

mock_intents = {
    'ShareCurrentLocation': [ "Share my location with Hillary's sister",
                                    'Send my current location to my father',
                                    'Share my current location with Jim',
                                    'Send my location to my husband',
                                    'Send my location',
                                    'Always share my location with Lori',
                                    'Share my location with my boyfriend until '
                                    'I get home',
                                    'Send my current location to Anna',
                                    'Share my location with Steve for 3 days',
                                    'Share my location to mum until I get to '
                                    'school',
                                    'Share my location with my office manager '
                                    'until noon',
                                    'Share my location with my Uber driver',
                                    'Share my location with Robert for the '
                                    'next 10 min',
                                    'Share my location with Jo until 8pm',
                                    'Share my current location',
                                    'Send my current location to the friends '
                                    "I'm meeting with"],
    'ComparePlaces': ["What's the best hotel between Soho Grand and "
                             'Paramount Hotel?',
                             "What's the cheapest between the two restaurants "
                             'the closest to my hotel?',
                             "What's the closest between Jo's and Lori's "
                             'place?',
                             "Is my Airbnb closer than John's hotel?",
                             'Is The View more expensive than Masa?',
                             "What's the best between Le Bain and Marquee?",
                             'Is Vertigo Sky Lounge more expensive than the '
                             'bar I usually go to in New York?',
                             "I'd like to know whether Galli is more expensive "
                             "than Rao's",
                             'Is my favorite bar better than the Donut Pub?',
                             'Is Waldorf Astoria more luxurious than the Four '
                             'Seasons?',
                             "What's the cheapest place between my favorite "
                             'bar and Employees Only?',
                             'Is my hotel in NYC for this week better than the '
                             'hotel I stayed in when I was in Chicago?',
                             'Is Soho Grand better than Paramount?',
                             "What's the cheapest place between Galli and The "
                             'Smile?',
                             'Is Three Dots and a Dash cheaper than Lost Lake?',
                             'What is the closest theatre between Belasco '
                             'Theatre and Majestic Theatre?',
                             'What is the most expensive restaurant between '
                             "Per Se and Rao's?",
                             'Which restaurant is the cheapest, Shake Shack or '
                             'Five Guys ?',
                             'What is the cheapest restaurant between '
                             "Balthazar and Lombardi's?"],
    'GetPlaceDetails': ["Show me photos of the bar I'm going to for "
                               "Rand's birthday",
                               'Does the View has reserved parking?',
                               'How much is it to go to the top of Empire '
                               'State Building?',
                               "Give me the phone number of the place I'm "
                               'going to today',
                               "When is Rao's the most crowded?",
                               "What's the phone number of the Dead Rabbit?",
                               'Is there a parking at my hotel?',
                               'How crowded is Per Se right now?',
                               'What time does Pouring Ribbons open tonight?',
                               'How crowded is the bar near my place?',
                               "Is there wifi at the coffee place where I'm "
                               'meeting with John?',
                               "What's the address of the place where I was "
                               'yesterday night?',
                               'Is the Swan Oyster Depot cash-only?',
                               'Is there a wifi at The Smile?',
                               'Can I pay by credit card at Boom Boom Room?',
                               "What's the phone number of my hotel in Chicago "
                               'next month?',
                               'Is Pates Et Traditions cash only?',
                               'Are there good tips to know when going to the '
                               'Modern?',
                               "What's the price range for a dinner at Galli?",
                               'How far is Frying Pan from the Highline '
                               'Ballroom?',
                               'Who is playing tonight at the Madison Square '
                               'Garden?',
                               "What's planned at Slim's tonight?",
                               'Show me photos of Mondrian Soho',
                               'What time does Employees Only close?',
                               "I want to see photos of the place we're going "
                               'to tonight',
                               "What's happening this week at Smalls Jazz "
                               'Club?',
                               "Is there a children's menu at The Standard "
                               'Grill?',
                               "Show me the Butcher's Daughter's menu",
                               'Give me the address of the biggest Wallmart in '
                               'Boston area',
                               "Where's Irving Plaza located?",
                               'How expensive is the best French restaurant '
                               'near work?',
                               'How far is the NoMad Bar?',
                               'How much does it cost to go to Disneyland?',
                               'How far am I from the Guggenheim museum?',
                               'Is there wifi at my Airbnb in London next week '
                               'end?',
                               'Are there activities for children at Hard Rock '
                               'Cafe?',
                               "Does the Butcher's Daughter serve vegetarian "
                               'food only?',
                               'Can I park at Gershwin Theatre?',
                               'Give me the address of State Grill and bar',
                               'Show me the menu of the restaurant I booked '
                               'for tonight',
                               "What are the opening hours of Please Don't "
                               'Tell?',
                               "What's Lori's home address?",
                               'Where can I get tickets for a concert at Blue '
                               'Note?',
                               'Are there some tips to know when going to '
                               'Battery Park?',
                               'How much is a dinner at La Chine?',
                               "Give me Steve's address in Manhattan",
                               'Does Cafe Gitane have wifi?',
                               "What's today's menu at The Water Club?",
                               'When is it the quietest at Good Luck bar?',
                               'Is there valet parking at Kang Ho Dong '
                               'Baekjeong?'],
    'SearchPlace': ['Show me the cheapest cocktail bar near the hotel '
                           'my sister stays in',
                           'Find me a restaurant similar to the one I went to '
                           'yesterday evening',
                           'Show me the closest restaurants with all you can '
                           'eat buffets',
                           'Find me a 3 stars restaurant in Los Angeles',
                           'I want to eat some fried chicken. Any suggestions?',
                           "What's the closest pizza restaurant around here?",
                           'Show me the top 5 French restaurants in Manhattan',
                           'Where can I eat the best burger in Soho?',
                           'Show me veggie restaurants nearby',
                           'Find me a salad bar I can go to for my lunch '
                           'meeting',
                           "What's the best irish pub in hell's kitchen?",
                           "Find a store near Sia's place where I can buy "
                           'champagne',
                           'Is there a place similar to Per Se in '
                           'Williamsburg?',
                           'Find the top 3 family attractions in Hollywood not '
                           "far from Angie's place",
                           'Find the best restaurants near my airbnb that '
                           'serve brunch all day',
                           'Find me a romantic restaurant that serves good '
                           "expensive wine near my girlfriend's work",
                           'Show me the best museums to visit near my London '
                           'Airbnb',
                           'Find me a brunch spot in Lower Manhattan',
                           'Find me a coffee place similar to Starbucks that '
                           'has gluten free food',
                           'Find me the cheapest seafood restaurant near the '
                           'Golden Bridge',
                           'Find me a place that sells burritos in South '
                           'Harlem',
                           'What are the fanciest clubs in New York?',
                           'Where is the nearest Starbucks?',
                           'Find me a good expensive japanese restaurant near '
                           'work',
                           'Find a good fried chicken restaurant that is not a '
                           'fast food',
                           'Find me the closest theatre for tonight',
                           'Show me the parks with swings and pony rides '
                           "around my aunt's place",
                           'Find me the finest sushi restaurant in the area of '
                           'my next meeting'],
    'BookRestaurant': ['Find me a table for four for dinner tonight',
                              "Book a table for today's lunch at Eggy's Diner "
                              'for 3 people',
                              'Book a table at a restaurant near Times Square '
                              'for 2 people tomorrow night',
                              'Book a table for friday 8pm for 2 people at '
                              "Katz's Delicatessen",
                              "Book a table at Joan's on Third for my family "
                              'reunion on Saturday',
                              "I'd like a table in a peaceful restaurant "
                              'around Times Square',
                              'Book a table at Seven Hills for 6 people with a '
                              'nice view',
                              "Book a table for 6 people at Mr Donahue's for "
                              "tomorrow's lunch",
                              'Book a restaurant for 6 near my morning meeting '
                              'tomorrow at 1pm',
                              'I want reservations to grab brunch for 5 in '
                              'hells kitchen tomorrow',
                              'Book a table for Sophie and me at the Red '
                              'Lobster tonight',
                              'Book a table for 3 people at a restaurant that '
                              'serve tapas and wine for tonight',
                              'Book a table near my London hotel next '
                              'Wednesday evening',
                              'Book me a table for 8:45pm at a restaurant with '
                              'wifi near my Airbnb',
                              'Figure out if I can get a reservation at Ma '
                              'Peche after the concert',
                              'Book a table for four people at Tapestry for '
                              '9pm tonight',
                              'Get me a spot at Ippudo for lunch',
                              'Book a table at the best chinese restaurant in '
                              "town for today's lunch",
                              'Book a restaurant for brunch next Sunday',
                              'Book me a table for 2 people at the sushi place '
                              'next to the show tomorrow night',
                              "Make a reservation for 4 people for today's "
                              'lunch at Daniel',
                              'Book a table for four people at Mondrian Soho '
                              'for 8pm',
                              'Get me a table at Din Tai Fung for the 4th of '
                              'December at 12:30',
                              'Get me a table at a restaurant nearby that is '
                              'not too crowded for tomorrow evening',
                              'Find me an outdoor table at Five leaves for 3',
                              "Get me a table at Delmonico's next monday at "
                              '8pm',
                              'We are a party of 4 people and we want to book '
                              'a table at Seven Hills for sunset',
                              'I need reservations at Quince at 9:30',
                              "Make a reservation at Delmonico's on Saturday "
                              '8pm for 10 people',
                              'Book a table at an italian restaurant nearby '
                              'for dinner with 5 people',
                              'Book a table at the nearest sushi restaurant '
                              'for 2 for 1pm',
                              "Book me a table for 4 at Delmonico's around 8pm "
                              'this friday',
                              'Is there a table for boozy brunch at around 11 '
                              'nearby?',
                              'Need a table for lunch to eat steak near penn '
                              'station',
                              "Get me a table at a restaurant near Emily's "
                              'place for tomorrow 9pm',
                              "Book a table for 5 people at the restaurant I'm "
                              'used to going to every week',
                              'Make a reservation for breakfast at Batter & '
                              'Berries tomorrow',
                              'Get me a place near chelsea with good brunch '
                              'cocktails tomorrow at 10',
                              'Book a table for two people at a restaurant '
                              'near work',
                              'Table for a group of 12 near west village '
                              'tomorrow? go!',
                              'I want a reservation for 5 at Alinea',
                              "Make a reservation for 4 people for today's "
                              'lunch at a Starbucks nearby',
                              'Get me a table at a good deli near Mission '
                              'Dolores Park for lunch',
                              "Please book a table at Delmonico's this evening "
                              'for 3 at 8pm',
                              'I need a reservation for five people at Galli '
                              'for friday night',
                              'Can you make a reservation at a lebanese '
                              'restaurant nearby, for lunch, party of 5?',
                              "See if there's a table outside for noon at that "
                              'fried chicken restaurant I like',
                              'Book a table at Chops Lobster Bar for 5 people '
                              'at 7:30pm',
                              'I want to find a reservation at an old red '
                              'sauce joint at 6',
                              'Book a table for 3 people at the restaurant I '
                              'went to last week',
                              'Make a reservation for 3 at the finest '
                              'restaurant in the area where I was yesterday '
                              'afternoon',
                              'I want a table in a good japanese restaurant '
                              'near Trump tower',
                              'Table for two at Nobu New York tonight',
                              'Book a table at The Standard Grill for four '
                              'people for the day after tomorrow at 8:30pm',
                              'Book for 4 people at Per Se for Tuesday evening',
                              'I want a table for friday 8pm for 2 people at '
                              "Katz's Delicatessen",
                              'Need a table for 6',
                              'I want a reservation to get drinks after class '
                              'tomorrow for 10',
                              'Book a table at an American restaurant for '
                              'Thanksgiving',
                              'Book a table at Galli for 6 people tonight',
                              'Book for 4 at Nobu for tomorrow evening',
                              'Book a table for four people at La Chine for '
                              'the 11th at 8pm',
                              'Book a table at Saddle Peak Lodge for my diner '
                              'with friends tonight',
                              'Can I have a table at the Russian Tea Room for '
                              '4pm?',
                              'Book a table for 8 at Tavern on the Green for 8 '
                              'pm',
                              'Need a table for 12 in 3 hours',
                              'Book a table for me and my girlfriend in a '
                              "romantic restaurant for Valentine's day",
                              'Need a reservation for brunch for 5 in '
                              'williamsburg near the bridge',
                              'Book me and my sister a spot at the milk bar '
                              'place near the hotel she stays at in midtown',
                              "Book me a table for 4 at Delmonico's"],
    'RequestRide': ["Get a taxi to Emmit's Irish Pub",
                           'Get me a ride to the airport',
                           'Order a taxi for tomorrow 8am',
                           'Get a cab at my place right now',
                           'Order a taxi',
                           "I need a taxi for 6 to go to Audrey and Sam's "
                           'wedding',
                           'Book an Uber to my next meeting',
                           'I need a taxi to catch my flight tomorrow morning',
                           'Book a cab',
                           "Book a taxi to go to Sebastian's",
                           'Find a taxi',
                           'I need a cab to go to work',
                           'I need a taxi in 5 minutes at 36 5th avenue',
                           'Book an Uber to home',
                           'Can you find me a ride at this hour?',
                           'Order a cab for 6 people',
                           'I need an Uber right now',
                           'Book me a ride at my current location',
                           "Order a cab at my mother's place to go to the LA "
                           'stadium',
                           'Get an Uber to go to my dinner tonight',
                           'Book a Lyft car to go to 33 greene street',
                           'I want a taxi right now',
                           'Is there any Uber around?',
                           'Get a taxi to the nearest japanese restaurant',
                           'Order a cab at Shake Shack to go to the Empire '
                           'State Building',
                           "Get a Lyft car at Scott's place"],
    'GetDirections': ['How do I go to Montauk avoiding tolls?',
                             'Directions to Disneyworld avoiding traffic',
                             'Show me the way to go to 33 Greene Street',
                             "Give me directions to my parents' place avoiding "
                             'toll roads',
                             'Show me directions to my next meeting avoiding '
                             'traffic',
                             'Quickest directions to go pick up my son at '
                             'soccer practice',
                             'Show me directions to my yoga retreat avoiding '
                             'the highway',
                             'Bicycling directions to Millenium park',
                             'Directions to La Guardia airport using Waze',
                             'Cycling directions to Chelsea Market',
                             'Cycling directions to my surf lesson at 10am',
                             'Show me the fastest itinerary to my Airbnb on a '
                             'Friday night',
                             'Driving directions to Tavern on the Green',
                             'Transit directions to Barcelona Wine Bar',
                             'Navigate to Palo Alto avoiding traffic',
                             'Directions to JFK airport at 7am',
                             'How do I go back home?',
                             'Walking directions to my Christmas party with '
                             'Citymapper',
                             "Get me directions to John's place if I leave at "
                             '6pm',
                             'Walking directions from home to my Halloween '
                             'party stopping by a wine store',
                             'Directions to Tulsa with road 66',
                             'Show me the way to go to work',
                             'Give me transit directions from Grand Central to '
                             'Brooklyn bridge',
                             'Navigate me to Empire State Building using the '
                             'shortest way',
                             'Show me walking directions to MOMA',
                             'Get me directions to Las Vegas avoiding toll '
                             'roads',
                             'Show me directions to Jersey City avoiding the '
                             'highway',
                             'Show me the directions from the LA County Museum '
                             'to Santa Monica',
                             'Directions to my beach house avoiding tolls',
                             'Show me directions to my hotel',
                             'Show me the fastest itinerary to go to '
                             'Williamsburg',
                             'Fastest way to go to my next meeting',
                             "Directions to Joe's pub",
                             'I want to go to Boston with the quickest '
                             'itinerary',
                             "Show me the way to Rand's birthday party by "
                             'car'],
    'ShareETA': ['Share my ETA with Mary Jane',
                        "Send my ETA to the guy I'm meeting with",
                        'Share my time of arrival with my Airbnb host',
                        'Share my arrival time with Juan Carlos',
                        'Share my ETA with Jo',
                        'Share my estimated time of arrival with Lily',
                        'Send my time of arrival to Nina',
                        "Tell my friends what time I'll get there",
                        'Share with Franz my ETA',
                        'Send a message to John to tell him when I get there',
                        'Send my ETA to my girlfriend',
                        "Tell Valery how long it's gonna take to join her",
                        'Share my ETA with the guy who just called me',
                        'Share my ETA',
                        'Share my ETA with my data scientist',
                        'Share my estimated time of arrival with my mother',
                        'Send a message to Michael with my ETA',
                        'Share my ETA with the Snips team',
                        "Send my ETA to the girl I'm supposed to have dinner "
                        'with',
                        'Send a message to Montgomery with my arrival time',
                        'Send my ETA to the guests of my apartment',
                        'Send a message to my boss with my ETA'],
    'GetTrafficInformation': ['Should I expect traffic from here to '
                                     'Kennedy international airport?',
                                     'Any traffic problems to go to my dinner?',
                                     'Any accidents from my Airbnb to Golden '
                                     'Gate Bridge?',
                                     'Is there traffic from work to gym?',
                                     'Is there traffic on my way to the gym?',
                                     "How's traffic to go to my hotel?",
                                     "How's the road on the 11th avenue?",
                                     'I want to know if there is traffic to go '
                                     'to my upcoming meeting',
                                     'Is there traffic jam on 6th avenue?',
                                     'Any accidents to expect to go to my '
                                     "cousin's place?",
                                     "How's the traffic from here to Jo's "
                                     'place?',
                                     'Is there traffic on 8th avenue and west '
                                     '14th street?',
                                     'Shoud I expect traffic between broadway '
                                     'and prince street?',
                                     'Is there traffic on the US 50 portion '
                                     "I'm going to take to go to my client "
                                     'meeting?',
                                     'Are there any accidents from home to '
                                     'work?',
                                     'Should I expect any traffic to go meet '
                                     'my friends tonight?',
                                     'Is there traffic jam from here to '
                                     'Brooklyn bridge?',
                                     "How's the traffic from here to Central "
                                     'Park?',
                                     'Is the road to work congested?',
                                     'Is there any traffic on US 20?'],
    'GetWeather': ['Show me the forecast for New Orleans',
                          'Will it be cloudy at my facebook event?',
                          "What's the weather like at my parents'?",
                          'Is the weather good for a walk today?',
                          'Is it cold outside? ',
                          'Is it going to rain tomorrow?',
                          "What's the weather like at Jo's place right now?",
                          'Can I walk to my next meeting?',
                          'Show me the weather forecast for my upcoming trip '
                          'to Los Angeles',
                          'Will it rain in the next 30 minutes?',
                          "What's the weather like in Paris, New York and "
                          'Chicago?',
                          "What's the weather forecast for the rest of the "
                          'week?',
                          "What's the weather like from New York to Boston?",
                          'How windy will it be tomorrow?',
                          'Should I have an umbrella with me tomorrow?',
                          "What will the weather be like at Jo's place this "
                          'afternoon?',
                          'Can I go hiking this afternoon?',
                          'What is the temperature tomorrow morning?',
                          'Is it cold outside?',
                          'Should I take an umbrella to walk to my dinner?',
                          "What will the weather be like from Home to Jo's "
                          'place?',
                          "What's the weather like in 3 days?",
                          'What will the weather be like from 8am to 2pm in '
                          'Central Park?',
                          'What will the weather be like tomorrow morning?',
                          'Can I take my bike to go to work today?',
                          'What will the weather be like in London next week?',
                          'Is it windy today?',
                          "What's the weather like at work?",
                          'Is it going to be sunny next week?',
                          'I want the weather in Paris',
                          'It is a beautiful day for a walk?',
                          "What's it like outside?",
                          'What will the weather be like when I land in Paris?',
                          'Is it raining right now?',
                          'What will the weather be like at my Airbnb this '
                          'week end?',
                          'Whats the weather like in Bordeaux?',
                          "What's the weather like near my upcoming event?",
                          'Will it rain tomorrow near my all day event?',
                          "I need the weather at Jo's place around 8 pm",
                          'What will the weather be like when I get out of my '
                          'afternoon meeting?',
                          'Show me the forecast for my upcoming weekend',
                          'Should I take a rain coat today?']
}

with open("mock_data.json", "rb") as fp:
    mock_data = json.load(fp)


def wrap_data(md):
    i = random.choice(list(mock_intents.keys()))
    t = random.choice(mock_intents[i])
    ad = {
        "sample": {
            "text": t,
            "intent": i
        },
        "metadata": md
    }
    return ad


data = list(map(lambda md: wrap_data(md), mock_data))


with open("augmented_data.json", "w") as fp:
    json.dump(data, fp, indent=4, ensure_ascii=False)


def balance(seq):
    # 0 for a unbalanced data set
    # 1 for a balanced data set
    n = len(seq)
    classes = [(clas,float(count)) for clas,count in Counter(seq).items()]
    k = len(classes)

    H = -sum([ (count/n) * log((count/n)) for clas,count in classes]) #shannon entropy
    pp.pprint(n)
    pp.pprint(k)
    pp.pprint(classes)
    return H/log(k)

pp.pprint(
    balance(
        list(map(lambda d: d["metadata"]["gender"], data))
    )
)

pp.pprint(
    balance(
        list(map(lambda d: d["metadata"]["Race"], data))
    )
)
pp.pprint(
    balance(
        list(map(lambda d: d["metadata"]["id"], data))
    )
)