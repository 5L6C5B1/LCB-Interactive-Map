CHARACTER_DATA = {
    # receptionist
    'Cortana': {
        'name': 'Cortana',
        'directions': ['left'],
        'look_around': True,
        'dialog': {
            'start': {
                'text': 'Welcome to LCB! I\'m Cortana, how can I help you?',
                'options': [
                    {'text': 'What courses do you offer?', 'next': 'courses'},
                    {'text': 'Do you do evening classes?', 'next': 'study_mode'},
                    {'text': 'How much are the tuition fees?', 'next': 'fees'},
                    {'text': 'Is there a dormitory?', 'next': 'dorm'},
                    {'text': 'I\'m just looking around.', 'next': 'end'}
                ]
            },
            'courses': {
                'text': [
                    'We offer Business, Computing, Culinary, and Law courses.',
                    'The courses we provide are awarded by University of Essex, Kensington College, City & Guilds, and Pearson BTEC.'
                ],
                'options': [
                    {'text': 'Tell me more?', 'next': 'courses_detail'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what would you like to know?',
                'options': [
                    {'text': 'What courses do you offer?', 'next': 'courses_detail'},
                    {'text': 'Do you do evening classes?', 'next': 'study_mode'},
                    {'text': 'How much are the tuition fees?', 'next': 'fees'},
                    {'text': 'Is there a dormitory?', 'next': 'dorm'},
                    {'text': 'Nevermind.', 'next': 'end'},
                ]
            },
            'courses_detail': {
                'text': 'You may see the courses we offer by pressing TAB or X, or find more information on our website!',
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'study_mode': {
                'text': [
                    'Yes! We offer both full-time and evening classes for those who work part-time.',
                    'However, not all courses offer evening classes.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'fees': {
                'text': [
                    'Our fees vary upon the course you\'re interested in.'
                ],
                'options': [
                    {'text': 'Where do I make payments for deposits/fees?', 'next': 'payment'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'payment': {
                'text': [
                    'Our finance department is located here at the rooftop level. It is open every day until 4:30 PM.',
                    'However, if you are unable to make it before that time, the office will be open at night on Tuesdays, Thursdays, and Fridays.',
                    'Feel free to inquire the receptionist there when you visit our college in person.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'dorm': {
                'text': [
                    'We do have a dormitory on Jalan Laksamana Abdul Razak, next to the traffic light. It\'s a 5-minute walk from here.',
                    'It has 24-hour security, a car park, common laundry room, gym, and Wifi which connects up to 3 devices per student.',
                    'We also provide housekeeping, air-conditioning, beds, study tables, wardrobes and black-out curtains.',
                    'For more details, you can check our website under Campus Life, then Accomodation.'
                ],
                'options': [
                    {'text': 'How much is the rent?', 'next': 'dorm_rent'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'dorm_rent': {
                'text': [
                    'All rooms have a different rate depending on area size, ensuite bathrooms, and balconies.',
                    'Our lowest rate is $240/month while our highest is $450/month.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'end': {
                'text': 'Alright, have a great day!',
                'options': None # none = dialog end
            }
        }
    },
    # rooftop eceptionist
    'Cortana_r': {
        'name': 'Cortana',
        'directions': ['left'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Welcome to LCB! I\'m Cortana, how can I help you?',
                'options': [
                    {'text': 'What courses do you offer?', 'next': 'courses'},
                    {'text': 'Do you do evening classes?', 'next': 'study_mode'},
                    {'text': 'How much are the tuition fees?', 'next': 'fees'},
                    {'text': 'Is there a dormitory?', 'next': 'dorm'},
                    {'text': 'I\'m just looking around.', 'next': 'end'}
                ]
            },
            'courses': {
                'text': [
                    'We offer Business, Computing, Culinary, and Law courses.',
                    'The courses we provide are awarded by University of Essex, Kensington College, City & Guilds, and Pearson BTEC.'
                ],
                'options': [
                    {'text': 'Tell me more?', 'next': 'courses_detail'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what would you like to know?',
                'options': [
                    {'text': 'What courses do you offer?', 'next': 'courses_detail'},
                    {'text': 'Do you do evening classes?', 'next': 'study_mode'},
                    {'text': 'How much are the tuition fees?', 'next': 'fees'},
                    {'text': 'Is there a dormitory?', 'next': 'dorm'},
                    {'text': 'Nevermind.', 'next': 'end'},
                ]
            },
            'courses_detail': {
                'text': 'You may see the courses we offer by pressing TAB or X, or find more information on our website!',
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'study_mode': {
                'text': [
                    'Yes! We offer both full-time and evening classes for those who work part-time.',
                    'However, not all courses offer evening classes.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'fees': {
                'text': [
                    'Our fees vary upon the course you\'re interested in.'
                ],
                'options': [
                    {'text': 'Where do I make payments for deposits/fees?', 'next': 'payment'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'payment': {
                'text': [
                    'Our finance department is located here at the rooftop level. It is open every day until 4:30 PM.',
                    'However, if you are unable to make it before that time, the office will be open at night on Tuesdays, Thursdays, and Fridays.',
                    'Feel free to inquire the receptionist there when you visit our college in person.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'dorm': {
                'text': [
                    'We do have a dormitory on Jalan Laksamana Abdul Razak, next to the traffic light. It\'s a 5-minute walk from here.',
                    'It has 24-hour security, a car park, common laundry room, gym, and Wifi which connects up to 3 devices per student.',
                    'We also provide housekeeping, air-conditioning, beds, study tables, wardrobes and black-out curtains.',
                    'For more details, you can check our website under Campus Life, then Accomodation.'
                ],
                'options': [
                    {'text': 'How much is the rent?', 'next': 'dorm_rent'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'dorm_rent': {
                'text': [
                    'All rooms have a different rate depending on area size, ensuite bathrooms, and balconies.',
                    'Our lowest rate is $240/month while our highest is $450/month.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'end': {
                'text': 'Alright, have a great day!',
                'options': None # none = dialog end
            }
        }
    },
    # librarian
    'Cortana_lib': {
        'name': 'Cortana',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Welcome to the library! Remember to keep your voice down.',
                'options': [
                    {'text': 'What are those books on the tables?', 'next': 'booksale'},
                    {'text': 'What are the individual rooms for?', 'next': 'individual'},
                    {'text': 'Where are the tutorial rooms?', 'next': 'tutorial'},
                    {'text': 'May I use the Computer Lab?', 'next': 'lab5'},
                    {'text': 'I\'m just looking around.', 'next': 'end'}
                ]
            },
            'booksale': {
                'text': [
                    'We\'re selling some used books for a good price.',
                    'They might come in handy for your studies.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what would you like to know?',
                'options': [
                    {'text': 'What are those books on the tables?', 'next': 'booksale'},
                    {'text': 'What are the individual rooms for?', 'next': 'individual'},
                    {'text': 'Where are the tutorial rooms?', 'next': 'tutorial'},
                    {'text': 'May I use the Computer/Mac Lab?', 'next': 'lab5'},
                    {'text': 'Nevermind.', 'next': 'end'}
                ]
            },
            'individual': {
                'text': [
                    'The individual rooms are for those who want to study privately on their own.',
                    'You may use them for up to one hour, but you are allowed to extend it by asking the librarian.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'tutorial': {
                'text': [
                    'The tutorial rooms are just across from here.',
                    'You may use those rooms for group studies, but there are also some classes who require that room.',
                    'Be sure to ask the librarian if you plan on using them.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'lab5': {
                'text': [
                    'As long as you\'re a Computing degree student, of course.',
                    'Otherwise, you may only use the ones around here.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'end': {
                'text': 'Alright, see you soon.',
                'options': None # none = dialog end
            }
        }
    },

    # guide
    'Atticus': {
        'name': 'Atticus',
        'directions': ['down', 'left', 'right'],
        'look_around': True,
        'dialog': {
            'start': {
                'text': 'Welcome to LCB, do you need any assistance?',
                'options': [
                    {'text': 'What are the rooms on this level?', 'next': 'rooms'},
                    {'text': 'Who are you?', 'next': 'who'},
                    {'text': 'No, thank you.', 'next': 'end'}
                ]
            },
            'rooms': {
                'text': [
                    'To my left, there\'s Computer Lab 4 and the escalator going down to Level 2.',
                    'On my right is a hallway leading to Lecture Halls 1 and 2, along with Lecture Rooms 1, 2, and 3.',
                    'In between Lecture Room 2 and 3, you can access our Surau if you\'d like to pray.',
                    'There are more rooms down the path across from us.'
                ],
                'options': [
                    {'text': 'Thank you.', 'next': 'end'}
                ]
            },
            'who': {
                'text': [
                    'My name is Atticus, I\'m part of the student council.',
                    'I\'m here to guide, so if you happen to be lost or unsure just talk to me.',
                    'Or if you just want to talk, I don\'t mind.'
                ],
                'options': [
                    {'text': 'Thank you.', 'next': 'end'},
                    {'text': 'Student council?', 'next': 'sc'},
                ]
            },
            'sc':{
                'text': [
                    'Yup. Student council. We host and manage events, as well as volunteer for other events if we\'re needed.',
                    'You can talk to our student council president, Najib, up at the rooftop level if you have more questions.'
                ],
                'options': [
                    {'text': 'I see, thank you.', 'next': 'end'}
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # annexe level 2
    'Atticus_a2': {
        'name': 'Atticus',
        'directions': ['left'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Hey, it\'s you. Welcome to the Annexe building.',
                'options': [
                    {'text': 'What rooms are around here?', 'next': 'rooms'},
                    {'text': 'You too.', 'next': None}
                ]
            },
            'rooms': {
                'text': [
                    'Lecture Halls 10, 11, and 12. There\'s also the Auditorium right across from us.',
                    'The stairs lead to either Level 1 or 3, and the elevator is just to my right by the lounge.'
                ],
                'options': [
                    {'text': 'Thanks bro.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # annexe level 3
    'Atticus_a3': {
        'name': 'Atticus',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Hey, bro.',
                'options': [
                    {'text': 'Just one room?', 'next': 'rooms'},
                    {'text': 'Hey, bro.', 'next': None}
                ]
            },
            'rooms': {
                'text': [
                    'Yup. Just the event hall, otherwise named "The Roof".',
                    'Fun fact, the student council hosts their Hari Raya event here.',
                    'Occasionally, there would be local businesses selling here during special events hosted by our BTEC business students.'
                ],
                'options': [
                    {'text': 'Good to know.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # annexe elevator
    'Atticus_e': {
        'name': 'Atticus',
        'directions': ['right'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'The elevator only goes up and in a loop. Sorry for the inconvenience.',
                    'The order goes from Level G to 1 to 2 to 3, then back to G.',
                    'The developer has declared full fault for this and will improve in the near future.'
                ],
                'options': None
            }
        }
    },
    #main level 3 south
    'Atticus_m3south': {
        'name': 'Atticus',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Hello again.',
                'options': [
                    {'text': 'Hello.', 'next': None},
                    {'text': 'What are the rooms in this area?', 'next': 'rooms'},
                    {'text': 'How did you get here so quick?', 'next': 'teleport'}
                ]
            },
            'rooms': {
                'text': [
                    'Lecture Halls 3 and 8 are to my right, then there\'s Computer Lab 3 to my left next to the QA officer\'s office.',
                    'Further down the hall across from us, you can find Lecture Hall 9 and the bridge to the Annexe building.'
                ],
                'options': [
                    {'text': 'Thanks.', 'next': 'end'},
                ]
            },
            'teleport': {
                'text': [
                    'Just trying to be efficient, haha.',
                    'Is there anything you need?'
                ],
                'options': [
                    {'text': 'About the rooms...', 'next': 'rooms'},
                    {'text': 'Not at the moment.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # main level 2 south
    'Atticus_m2': {
        'name': 'Atticus',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Hello again.',
                'options': [
                    {'text': 'Hi.', 'next': None},
                    {'text': 'What are the rooms in this area?', 'next': 'rooms'}
                ]
            },
            'rooms': {
                'text': [
                    'On my right is the library and beside it are some lockers you can rent out.',
                    'Going up the hall leads to Lecture Halls 4, 5, and 6, Lecture Room 4, and the cafeteria.',
                    'There\'s also Tutorial Room 1 and some offices. Our Counselling Unit office is next to the incubation centre.'
                    'It looks like a train, you can\'t miss it.'
                ],
                'options': [
                    {'text': 'Thanks.', 'next': 'end'},
                    {'text': 'Incuvation?', 'next': 'incuvation'},
                ]
            },
            'incuvation': {
                'text': [
                    'The incuvation centre is where you can propose business ideas to LCB. They\'ll mentor you to make sure you\'re on the right track too.',
                    'Two foundation students proposed to rebrand the Kiosk in the library and turned it into a stationery shop.',
                    'Isn\'t that inspiring?'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Seems so. Thanks for the info.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what\'s your question?',
                'options': [
                    {'text': 'What are the rooms on this level?', 'next': 'rooms'},
                    {'text': 'Nevermind.', 'next': 'end'}
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # main level 2 cafeteria
    'Atticus_cafe': {
        'name': 'Atticus',
        'directions': ['down'],
        'look_around': True,
        'dialog': {
            'start': {
                'text': [
                    'Hey, welcome to the cafeteria!',
                    'Some of the students are here, maybe you can interact with them to know about their course.'
                ],
                'options': [
                    {'text': 'I see, thanks.', 'next': 'end'},
                    {'text': 'What are the rooms in this area?', 'next': 'rooms'},
                    {'text': 'I was actually going back up.', 'next': 'mistake'}
                ]
            },
            'rooms': {
                'text': [
                    'You\'ve passed the library and the locker room beside it.',
                    'Going up the hall leads to Lecture Halls 4, 5, and 6, as well as Lecture Room 4.',
                    'We also have some offices here and a meeting room. Then there\'s our guidance counsellor\'s office next to the incubation centre.',
                    'It looks like a train, you can\'t miss it.'
                ],
                'options': [
                    {'text': 'Thanks.', 'next': 'end'},
                    {'text': 'Incubation?', 'next': 'incuvation'},
                ]
            },
            'incuvation': {
                'text': [
                    'The incubation centre is where you can propose business ideas to LCB.',
                    'Two foundation students proposed to rebrand the Kiosk in the library and turned it into a stationery shop.',
                    'Isn\'t that inspiring?'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Seems so. Thanks for the info.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what\'s your question?',
                'options': [
                    {'text': 'What are the rooms on this level?', 'next': 'rooms'},
                    {'text': 'Nevermind.', 'next': 'end'}
                ]
            },
            'mistake':{
                'text': '...My bad, haha.',
                'options': None # none = dialog end
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    # rooftop
    'Atticus_r': {
        'name': 'Atticus',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'Rooftop level!',
                    'Good to see you again.'
                ],
                'options': [
                    {'text': 'Nice to see you, too.', 'next': None},
                    {'text': 'What are the rooms in this area?', 'next': 'rooms'}
                ]
            },
            'rooms': {
                'text': [
                    'There\'s Computer Lab 2, the Student Council meeting room, and the Mockup Cabin down the hall.',
                    'The Computing, Registrar, and Finance offices are here too.',
                    'The stairs beside the Registrar leads to the Upper Rooftop where Computer Lab 1 and Lecture Hall 7 are.'
                ],
                'options': [
                    {'text': 'Thanks.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },
    #upper rooftop
    'Atticus_ur': {
        'name': 'Atticus',
        'directions': ['left'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'Upper rooftop level!'
                ],
                'options': [
                    {'text': 'Yes!', 'next': None},
                    {'text': 'What are the rooms in this area?', 'next': 'rooms'}
                ]
            },
            'rooms': {
                'text': [
                    'To my left is Lecture Hall 7, then to my right is Computer Lab 1.'
                ],
                'options': [
                    {'text': 'Thanks.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem, I\'ll be around.',
                'options': None # none = dialog end
            }
        }
    },

    # computing
    'Nico': {
        'name': 'Nico',
        'directions': ['down'],
        'radius': 0,
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Oh hey, could you help me with something?',
                'options': [
                    {'text': 'What\'s up?', 'next': 'minigame'},
                    {'text': 'I\'m busy at the moment.', 'next': 'reject'}
                ]
            },
            'minigame': {
                'text': [
                    'I\'m finishing up some game projects for my Computer Science degree.',
                    'Would you like to test them out for my report? The controls use SPACE and the arrow buttons.'
                ],
                'options': [
                    {'text': 'Sure! (Play Space Invaders)', 'next': 'launch_si'},
                    {'text': 'Sure! (Play Breakout)', 'next': 'launch_b'},
                    {'text': 'Maybe another time.', 'next': 'reject'},
                ]
            },
            'minigame_win': {
                'text': 'Woah, you\'re good! Thanks for testing it out.',
                'options': [
                    {'text': 'No problem!', 'next': 'end'},
                ]
            },
            'minigame_lose':{
                'text': [
                    'Seems like you lost... Don\'t worry, you can try again next time.',
                    'But hey, at least the game works.',
                    'Thanks for playing!'
                ],
                'options': [
                    {'text': 'See you.', 'next': 'end'},
                ]
            },
            'reject': {
                'text': 'I see, no worries.',
                'options': None # none = dialog end
            },
            'end':{
                'text': 'Thanks again.',
                'options': None # none = dialog end
            }
        }
    },

    # student council
    'Najib': {
        'name': 'Najib',
        'directions': ['left'],
        'look_around': True,
        'dialog': {
            'start': {
                'text': 'Hey, I\'m Najib! Are you interested in joining the student council?',
                'options': [
                    {'text': 'What\'s that?', 'next': 'sc'},
                    {'text': 'No, just passing through.', 'next': 'end'}
                ]
            },
            'sc': {
                'text': [
                    'We\'re a group of elected and volunteer students. We organise and host events in the college and contribute to the community welfare.',
                    'It\'s also a platform where you can develop and enhance your leadership skills.' 
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'department': {
                'text': [
                    'We have 5 departments consisting of Logistics, Media & Communications, Secretariat, Sports, and Treasury.',
                    'Our Sports department is also responsible for overseeing all CCA clubs.',
                ],
                'options': [
                    {'text': 'What CCA\'s do you have?', 'next': 'cca'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'cca': {
                'text': [
                    'It varies every year, actually.',
                    'Although, Badminton, Futsal, Dodgeball, and Performing Arts have stuck around for some time now.',
                    'Despite it being dissolved before, E-Sports made a comeback recently.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'why_join': {
                'text': [
                    'You can gain work-related experience, as well as develop soft skills and find many other opportunities.',
                    'You also get to mingle with people within the LCB community and network with those outside of it!'
                ],
                'options': [
                    {'text': 'How do I join?', 'next': 'how_join'},
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'how_join': {
                'text': [
                    'Look for our recruitment poster or come here to our meeting room to acquire a recruitment form.',
                    'Afterwards, you would have to attend an interview and if you have potential to make the cut, you will be under supervision for 3 months.',
                    'Just to see how you are, of course.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'contact': {
                'text': [
                    'You can send us an email at council@laksamanacollege.edu.bn or through Instagram @lcbstudentcouncil.',
                    'For anything sports-related, please email sports.sc@laksamanacollege.edu.bn.'
                ],
                'options': [
                    {'text': 'I want to ask something else.', 'next': 'questions'},
                    {'text': 'Thank you.', 'next': 'end'},
                ]
            },
            'questions':{
                'text': 'Sure, what do you want to know?',
                'options': [
                    {'text': 'What do you guys do again?', 'next': 'sc'},
                    {'text': 'What are your departments?', 'next': 'department'},
                    {'text': 'Why should I join?', 'next': 'why_join'},
                    {'text': 'How do I contact you for events?', 'next': 'contact'},
                    {'text': 'Nevermind.', 'next': 'end'},
                ]
            },
            'end': {
                'text': 'Okay, no problem!',
                'options': None # none = dialog end
            }
        }
    },

    # hospitality & tourism
    'Chell': {
        'name': 'Chell',
        'directions': ['down'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'I don\'t think I can hangout for some time, just got assigned for work attachments at Empire Hotel.',
                    'I\'ll treat you guys next time. After all, I earned good profit from my business last semester.'
                ],
                'options': None
            }
        }
    },

    # law
    'Alcina': {
        'name': 'Alcina',
        'directions': ['left'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'Got a Law Society workshop this week too.'
                ],
                'options': [
                    {'text': 'Law Society?', 'next': 'law_society'},
                    {'text': '...', 'next': None}
                ]
            },
            'law_society': {
                'text': [
                    'Hm?',
                    'Oh, it\'s just a community for law students to gain practical experience and network with professionals.'
                ],
                'options': [
                    {'text': 'Cool.', 'next': 'end'},
                    {'text': '...', 'next': None}
                ]
            },
            'end': {
                'text': [
                    'Maybe you can join sometime if you\'re interested in law.'
                ],
                'options': None
            }
        }
    },

    # business
    'Enise': {
        'name': 'Enise',
        'directions': ['up'],
        'look_around': False,
        'dialog': {
            'start': {
                'text': [
                    'It\'s alright, I gotta plan and manage an event by next month.',
                    'Also that marketing campaign assignment...'
                ],
                'options': None
            }
        }
    },

    # culinary
    'Amjad': {
        'name': 'Amjad',
        'directions': ['down'],
        'radius': 0,
        'look_around': False,
        'dialog': {
            'start': {
                'text': 'Welcome to the Chef! Do you have a reservation?',
                'options': [
                    {'text': 'No, I\'m just looking around.', 'next': 'end'},
                    {'text': 'What\'s with the costume?', 'next': 'answer'}
                ]
            },
            'answer': {
                'text': [
                    'We\'re having a themed dinner tonight with dishes made by our culinary students.',
                    'Tonight we\'re focused on superhero-inspired dishes.'
                ],
                'options': [
                    {'text': 'Oh, how much?', 'next': 'price'},
                    {'text': 'I see, thank you.', 'next': 'end'},
                ]
            },
            'price': {
                'text': [
                    'It\'s $15 for a 3-course meal consisting of an appetiser, main course, and dessert with a special beverage.',
                    'Otherwise, it\'s $10 for just the meal with water provided.'
                ],
                'options': [
                    {'text': 'I see, thank you.', 'next': 'end'},
                ]
            },
            'end':{
                'text': 'No problem!',
                'options': None # none = dialog end
            }
        }
    }
}


UNIVERSITY_PARTNERS = {
    'University of Essex': {
        'icon': 'uoelogo',
        'banner': 'uoebanner',
        'description': 'The University of Essex is a vibrant institution renowned for its research-driven approach and diverse academic offerings. It fosters an inclusive environment that emphasizes innovation, social justice, and personal development for students.',
        'programs': 'We provide undergraduate level programmes in LLB Law, BA (Hons) & BSc (Hons) ranging from Accounting and Finance, Marketing, Business Management, International Tourism Management, and Computer Science from one of UK\'s top universities.'
    },
    'Kensington College': {
        'icon': 'kcblogo', 
        'banner': 'kcbbanner',
        'description': 'Kensington College of Business is a leading provider of business and management education in London, offering a range of accredited programs. It focuses on providing practical skills and academic knowledge to help students excel in their professional careers in a global business environment.',
        'programs': 'We provide foundation courses & BA Common Year 1 awarded by the Kensington College of London, as well as some specialised courses designed specifically for international students.'
    },
    'City & Guilds': {
        'icon': 'cnglogo',
        'banner': 'cngbanner',
        'description': 'City & Guilds is a UK-based global leader in vocational education and training, offering qualifications in a wide range of industries. It focuses on developing practical skills and providing certifications that help individuals advance in their careers and contribute to workforce development.',
        'programs': 'We provide Level 2 & 3 in Culinary Arts, including Patisserie and Food & Beverage Service. Come visit to check out and meet with the chefs.'
    },
    'Pearson BTEC': {
        'icon': 'bteclogo',
        'banner': 'btecbanner',
        'description': 'Pearson BTEC offers qualifications that are designed to help students gain practical skills and knowledge in specific industries, preparing them for both higher education and the workforce. BTEC qualifications are widely recognised and valued by employers, providing flexible pathways to career advancement.',
        'programs': 'Choose from our wide range of courses throughout 3 different fields of expertise: Business, Computing, and Hospitality Management. Make your BTEC qualification an exceptional one!'
    }
}

COURSE_DATA = {
    # UNIVERSITY OF ESSEX
    'BA (Hons) Accounting & Finance': {
        'partner': 'University of Essex',
        'field': 'business',
        'duration': '2 Years',
        'icon': 'accounting',
        'description': 'The BA (Hons) Accounting & Finance program provides comprehensive knowledge of financial principles, accounting practices, and business management. Students develop analytical skills essential for careers in finance, accounting, and business administration.',
        'modules': {
            'Year 2': [
                '- Business Law',
                '- Management Accounting',
                '- Human Resources Management',
                '- Contemporary Issues in Management',
                '- Financial Accounting',
                '- Auditing I'
            ],
            'Year 3': [
                '- Strategic Management',
                '- Performance Management',
                '- Financial Management',
                '- Financial Reporting',
                '- Taxation',
                '- Auditing II'
            ]
        },
        'entry_requirements': {
            '': [
                '- BA COMMON YEAR 1',
                '- BTEC LEVEL 5 HND IN BUSINESS / EQUIVALENT'
            ]
        }
    },
    'BA (Hons) Business Management': {
        'partner': 'University of Essex',
        'field': 'busman',
        'duration': '2 Years', 
        'icon': 'busman',
        'description': 'The BA (Hons) Business Management program develops leadership skills and strategic thinking capabilities. Students learn to analyze business environments, manage teams, and make informed decisions in complex organizational settings.',
        'modules': {
            'Year 2': [
                '- Business Law',
                '- Management Accounting',
                '- Human Resources Management',
                '- Contemporary Issues in Management',
                '- Market Research',
                '- Marketing Planning & Control'
            ],
            'Year 3': [
                '- Strategic Management',
                '- International Marketing',
                '- E-Marketing',
                '- Marketing Communications',
                '- Project Management',
                '- Financial Management'
            ]
        },
        'entry_requirements': {
            '': [
                '- BA COMMON YEAR 1',
                '- BTEC LEVEL 5 HND IN BUSINESS / EQUIVALENT'
            ]
        }
    },
    'BA (Hons) Marketing': {
        'partner': 'University of Essex',
        'field': 'business',
        'duration': '2 Years',
        'icon': 'marketing', 
        'description': 'The BA (Hons) Marketing program focuses on consumer behavior, brand management, and digital marketing strategies. Students develop creative and analytical skills to excel in the dynamic marketing industry.',
        'modules': {
            'Year 2': [
                '- Business Law',
                '- Management Accounting',
                '- Human Resources Management',
                '- Market Research',
                '- Marketing Planning & Control',
                '- Delivering Customer Value'
            ],
            'Year 3': [
                '- Strategic Management',
                '- International Marketing',
                '- E-Marketing',
                '- Marketing Communications',
                '- Project Management',
                '- Financial Management'
            ]
        },
        'entry_requirements': {
            '': [
                '- BA COMMON YEAR 1',
                '- BTEC LEVEL 5 HND IN BUSINESS / EQUIVALENT'
            ]
        }
    },
    'BA (Hons) International Tourism Management': {
        'partner': 'University of Essex',
        'field': 'tourism',
        'duration': '3 Years',
        'icon': 'plane',
        'description': 'The BA (Hons) International Tourism Management program prepares students for careers in the global tourism industry. Students learn about sustainable tourism, hospitality management, and cultural awareness.',
        'modules': {
            'Year 1': [
                '- Marketing Principles',
                '- Understanding International Tourism',
                '- Event Tourism',
                '- Managing Service Experiences',
                '- Developing Professional Practice'
            ],
            'Year 2': [
                '- Marketing Management',
                '- Research in Context',
                '- Weddings, Sports, and Cultural Events',
                '- Tourism Planning and Management',
                '- Tourism in Global Society'
            ],
            'Year 3': [
                '- Strategic Management',
                '- Leadership and Change Management',
                '- Management Research Project',
                '- International Tourism Development',
                '- Tourism Futures'
            ]
        },
        'entry_requirements': {
            'Year 1': [
                '- MIN. 112 UCAS POINTS (GCE A\'LEVEL)',
                '- IB - 26 POINTS',
                '- HNTEC Certificate',
                '- BTEC LEVEL 3 DIPLOMA IN HOSPITALITY (OVERALL MERIT)',
                '- BTEC LEVEL 3 DIPLOMA IN TRAVEL & TOURISM'
                ],
            'Year 2': '- BTEC LEVEL 5 HND IN HOSPITALITY MANAGEMENT / EQUIVALENT'
        }
    },
    'BSc (Hons) Computer Science': {
        'partner': 'University of Essex',
        'field': 'computer',
        'duration': '3 Years',
        'icon': 'compsci',
        'description': 'The Computer Science program provides students with a theoretical and practical understanding of how computers work, how software is developed, how computers communicate, and how data is processed and stored.',
        'modules': {
            'Year 1': [
                '- Introduction to Databases',
                '- Computer Organisation & Operating Systems',
                '- Network Fundamentals',
                '- Software Engineering Principles',
                '- Web Development',
                '- Professional Skills for Computing',
                '- Mathematics for Computing',
                '- Introduction to Programming'
            ],
            'Year 2': [
                '- Data Structures & Algorithms',
                '- Advanced Databases & Warehousing',
                '- Cybersecurity',
                '- Further Networking',
                '- Mobile Application Programming',
                '- Team Project'
            ],
            'Year 3': [
                '- Capstone Project',
                '- System Analysis & Design',
                '- Network Security',
                '- AI & Machine Learning',
                '- Computer Games Development'
            ]
        },
        'entry_requirements': {
            'Year 1': [
                '- MIN. 112 UCAS POINTS (GCE A\'LEVEL)',
                '- IB - 26 POINTS',
                '- HNTEC CERTIFICATE',
                '- BTEC LEVEL 3 DIPLOMA IN IT (OVERALL MERIT-MERIT)',
                '- FOUNDATION IN IT / EQUIVALENT'
                ],
            'Year 2': '- BTEC LEVEL 5 HND IN COMPUTING / EQUIVALENT'
        }
    },
    'LLB Law': {
        'partner': 'University of Essex',
        'field': 'law',
        'duration': '3 Years',
        'icon': 'law',
        'description': 'The LLB Law program provides a comprehensive foundation in legal principles and practices. Students develop critical thinking skills and legal reasoning abilities essential for careers in law and related fields.',
        'modules': {
            'Year 1': [
                '- Contract Law',
                '- Land Law',
                '- Foundations of Public Law',
                '- Criminal Law',
                '- Career Management and Personal Development Skills I'
            ],
            'Year 2': [
                '- Tort Law',
                '- Law of the European Union',
                '- Career Management and Personal Development Skills II',
                '- Equity and Trusts',
                '- Company Law',
                '- Legal Research Skills'
            ]
        },
        'entry_requirements': {
            '': [  # Multiple requirements without year grouping
            '- 3 BBB GCE / IGCSE A\'LEVEL IN ENGLISH MEDIUM SUBJECTS',
            '- IB - 30 POINTS',
            '- KCB FOUNDATION IN LAW (MIN. 60% AVERAGE)'
            ]
        },
        'whats_next': {
            '': '→ Final year (Year 3) at University of Essex, UK'
        }
    },
    'Master of Business Management':{
        'partner': 'University of Essex',
        'field': 'business',
        'duration': '1-2 Years',
        'icon': 'busman',
        'description': 'This programme equips you with a solid understanding of key business functions, organisational structures, and the external forces that shape them. You’ll strengthen your financial analysis skills, enabling you to make data-driven decisions and tackle complex challenges confidently.',
        'modules': {
            'N/A': [
                '- N/A'
            ]
        },
        'entry_requirements': {
            '': '- MIN. 2:2 DEGREE / INTERNATIONAL EQUIVALENT IN ANY DISCIPLINE'
        }
    },

    # KENSINGTON COLLEGE OF BUSINESS
    'University Foundation Course':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '1 Year',
        'icon': 'business',
        'description': 'The University Foundation Course, designed by Kensington College of Business and endorsed by 17 universities, is an accredited A-Level alternative accepted for entry into various degree programs.',
        'modules': {
            '': [
                '- Study Skills',
                '- Quantitative Skills',
                '- English for Academic Purposes',
                '- Introduction to Computing',
                '- Introduction to Accounting',
                '- Introduction to Business Management',
                '- Introduction to Economics',
                '- Introduction to Law'
            ]
        },
        'entry_requirements': {
            '': [
                '- 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS',
                '- BDTVEC PRE-NATIONAL DIPLOMA'
            ]
        },
        'whats_next': {
            '': [
                '→ BA Common Year 1'
            ]
        }
    },
    'Foundation in Information Technology':{
        'partner': 'Kensington College',
        'field': 'computer',
        'duration': '1 Year',
        'icon': 'compsci',
        'description': 'The Foundation in Information Technology is an accredited program that prepares students for Computing degrees worldwide by enhancing subject knowledge, English proficiency, and academic skills, with progression options in areas like AI, Big Data, and Robotics.',
        'modules': {
            '': [
                '- Study Skills',
                '- Quantitative Skills',
                '- English for Academic Purposes',
                '- Mathematics for Computing',
                '- Introduction to Programming',
                '- Introduction to Databases'
            ]
        },
        'entry_requirements': {
            '': [
                '- 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS',
                '- BDTVEC PRE-NATIONAL DIPLOMA'
            ]
        },
        'whats_next': {
            '': [
                '→ BSc (Hons) Computer Science'
            ]
        }
    },
    'Foundation in Law':{
        'partner': 'Kensington College',
        'field': 'law',
        'duration': '1 Year',
        'icon': 'law',
        'description': 'The accredited Foundation in Law program, designed by Kensington College of Business and accepted by multiple universities as an A-Level alternative, prepares students with essential legal knowledge and academic skills for progression to an LLB Law degree.',
        'modules': {
            '': [
                '- Study Skills',
                '- Quantitative Skills',
                '- English for Academic Purposes',
                '- Introduction to the English Legal System & Method',
                '- Introduction to Criminal Law',
                '- Introduction to Contract Law'
            ]
        },
        'entry_requirements': {
            '': [
                '- 5 GCE/IGCSE O\'LEVEL CREDITS IN 4 ENGLISH MEDIUM SUBJECTS AND 1 ENGLISH LANGUAGE'
            ]
        },
        'whats_next': {
            '': [
                '→ LLB Law',
            ]
        }
    },
    'BA Common Year 1':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '1 Year',
        'icon': 'business',
        'description': 'The KCB BA Common Year One offers direct entry to the second year of many degrees, allowing students to explore various subjects and identify their interests for a successful and fulfilling career path.',
        'modules': {
            '': [
                '- Business Accounting',
                '- Business Skills',
                '- IT Fundamentals I',
                '- Marketing',
                '- Quantitative Methods',
                '- Business Economics',
                '- Introduction to Research Skills',
                '- IT Fundamentals II',
                '- Management Accounting',
                '- Business Management'
            ]
        },
        'entry_requirements': {
            '': [
                '- 2 A\'LEVEL IN ENGLISH MEDIUM SUBJECTS',
                '- IB - 24 POINTS',
                '- HNTEC CERTIFICATE',
                '- BTEC LEVEL 3 DIPLOMA (OVERALL MERIT)',
                '- UNIVERSITY FOUNDATION COURSE / EQUIVALENT'
            ]
        },
        'whats_next': {
            'Year 2 of': [
                '→ BA (Hons) Marketing',
                '→ BA (Hons) Accounting and Finance',
                '→ BA (Hons) Business Management',
                '→ BA (Hons) International Tourism Management, with the pre-requisite module'
            ]
        }
    },
    'Certificate in Business Management':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '6 Months',
        'icon': 'busman',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
        'modules': {
            '': [
                '- Introduction to Economics',
                '- Introduction to Accounting',
                '- Business Communication Skills',
                '- Introduction to Business Administration'
            ]
        },
        'entry_requirements': {
            '': '- MIN. 2 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS'
        },
        'whats_next': {
            '': [
                '→ KCB Diploma in Business Management'
            ]
        }
    },
    'Diploma in Business Management':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '6 Months',
        'icon': 'busman',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
        'modules': {
            '': [
                '- Business Accounting',
                '- Business Communication',
                '- Business Management',
                '- Business Economics'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 2 GCE A\'LEVELS',
                '- IB - 24 POINTS',
                '- MATURE STUDENTS WITH MIN. 2 YEARS OF WORK EXPERIENCE'
            ]
        },
        'whats_next': {
            '': [
                '→ KCB Advanced Diploma in Business Management'
            ]
        }
    },
    'Advanced Diploma in Business Management':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '6 Months',
        'icon': 'busman',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
        'modules': {
            '': [
                '- Business Law',
                '- Marketing',
                '- Quantitative Studies',
                '- Management Accounting'
            ]
        },
        'entry_requirements': {
            '': '- DIPLOMA IN BUSINESS MANAGEMENT'
        },
        'whats_next': {
            '': [
                '→ KCB Higher Diploma in Business Management'
            ]
        }
    },
    'Higher Diploma in Business Management':{
        'partner': 'Kensington College',
        'field': 'business',
        'duration': '6 Months',
        'icon': 'busman',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
        'modules': {
            '': [
                '- Information Management',
                '- Management of Operations',
                '- Marketing Communication',
                '- Human Resource Management'
            ]
        },
        'entry_requirements': {
            '': '- ADVANCED DIPLOMA IN BUSINESS MANAGEMENT'
        },
        'whats_next': {
            '': [
                '→ Degree in Business with our University Partners in the UK (1 Year)',
                '→ Degree in Business at LCB, Brunei awarded by University of Essex, UK (2 Years)'
            ]
        }
    },
    'Higher Diploma in Airline Hospitality Business':{
        'partner': 'Kensington College',
        'field': 'tourism',
        'duration': '2 Years',
        'icon': 'plane',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'The KCB Airline Hospitality Business programme, taught in English, prepares students with essential language, communication, and subject-specific skills to progress from high school to degree-level study in Airline Hospitality at UK universities.',
        'modules': {
            '': [
                '- English for Academic Purposes',
                '- Communication Skills',
                '- Presentation Skills',
                '- Airline Customer Service',
                '- In-flight Service',
                '- Airport Ground Service',
                '- Interview Skills and Personal & Professional Development',
                '- Introduction to Human Resource Management',
                '- Airline Leadership',
                '- Hospitality & Tourism Management',
                '- Hospitality & Tourism Marketing',
                '- Sustainable Development in Hospitality',
                '- Airline Management',
                '- Contemporary Issues in Hospitality Management',
                '- Hospitality Supervision and Training Skills',
                '- International Destination Management',
                '- Leadership, Innovation, & Technology for Tourism, Hospitality, & Events',
                '- Senior Customer Service'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVELS / EQUIVALENT*',
                '- IB - 24 POINTS',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN BUSINESS',
                '- UNIVERSITY FOUNDATION COURSE'
            ]
        },
        'whats_next': {
            'Year 2 of': [
                '→ BA (Hons) International Tourism Management @ LCB',
                '→ BA (Hons) Business Management @ LCB',
                '→ BA (Hons) Marketing @ LCB',
                '→ BA (Hons) Hospitality Management @ University of Essex, UK',
                '→ BA (Hons) Events Management @ University of Essex, UK',
                '→ BA (Hons) Aviation and Airport Management Semester 2 @ University College Birmingham (UCB) accredited by the University of Warwick, UK'
            ],
            'Year 3 of': [
                '→ BA (Hons) International Hospitality, Tourism, and Wellness Management @ Coventry University, UK',
                '→ BA (Hons) International Hospitality & Tourism Management @ University College Birmingham (UCB) accredited by the University of Warwick, UK',
                '→ BA (Hons) International Hospitality Management Semester 2 @ Swiss Hotel Management School (SHMS) awarded by SHMS and University of Derby, UK',
                '→ BA (Hons) International Hospitality and Events Management Semester 2 @ Swiss Hotel Management School (SHMS) awarded by SHMS and University of Derby, UK'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.',
                'Admission is ultimately based on the high school grades, English language qualifications, and interview submitted by the applicant.'
            ]
        }
    },
    'Higher Diploma in Sports and Leisure Managment':{
        'partner': 'Kensington College',
        'field': 'tourism',
        'duration': '2 Years',
        'icon': 'sports',
        'warning': '! ONLY FOR INTERNATIONAL STUDENTS !',
        'description': 'The Higher Diploma in Sports and Leisure at Kensington College of Business Brunei prepares students for global careers through internships and training in essential sports skills, aiming to meet the needs of international sports and leisure organisations.',
        'modules': {
            '': [
                '- English for Academic Purposes',
                '- Communication Skills',
                '- Presentation Skills',
                '- Introduction to Accoutning',
                '- Sports Development',
                '- Customer Service in Golf and Leisure',
                '- Sports and Leisure Event Organisation',
                '- Management of Golf Course',
                '- Sports and Leisure Facilities Operations',
                '- Managing and Developing the Business Sports and Leisure',
                '- Marketing Strategy and Sales in Sports and Leisure',
                '- Hospitality and Tourism Marketing',
                '- Contemporary Issues in Hospitality Management',
                '- Introduction to Human Resource Management',
                '- Hospitality Supervision and Training Skills',
                '- Leadership, Innovation, & Technology for Tourism, Hospitality, & Events',
                '- Senior Customer Service'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL / EQUIVALENT*',
                '- IB - 24 POINTS',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN BUSINESS',
                '- UNIVERSITY FOUNDATION COURSE'
            ]
        },
        'whats_next': {
            'Year 2 of': [
                '→ BA (Hons) International Tourism Management @ LCB',
                '→ BA (Hons) Business Management @ LCB',
                '→ BA (Hons) Marketing @ LCB',
            ],
            'Year 3 of': [
                '→ BA (Hons) Sports Management @ University College Birmingham (UCB) accredited by the University of Warwick, UK',
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.',
                'Admission is ultimately based on the high school grades, English language qualifications, and interview submitted by the applicant.'
            ]
        }
    },
    
    # CITY & GUILDS
    'Level 2 Diploma in Food Preparation & Culinary Arts':{
        'partner': 'City & Guilds',
        'field': 'culinary',
        'duration': '1 Year',
        'icon': 'culinary',
        'description': 'The Level 2 Diploma in Food Preparation & Culinary Arts equips candidates with transferable and job-specific skills to kickstart or advance their careers in hospitality through practical and knowledge-based assessments.',
        'modules': {
            '': [
                '- Understand the Hospitality Industry',
                '- Understand the Business Success',
                '- Provide Guest Service',
                '- Awareness of Sustainability in the Hospitality Industry',
                '- Professional Workplace Standards',
                '- Understand Own Role in Self Development',
                '- Food Safety',
                '- Meet Guest Requirements Through Menu Planning',
                '- Mise en Place',
                '- Cooking Methods, Techniques, and Commodities: Boiling, Poaching, and Steaming',
                '- Cooking Methods, Techniques, and Commodities: Stewing and Braising',
                '- Cooking Methods, Techniques, and Commodities: Baking, Roasting, and Grilling',
                '- Cooking Methods, Techniques, and Commodities: Deep and Shallow Frying',
                '- Understand Food Commodities'
            ]
        },
        'entry_requirements': {
            '': [
                '- 16 YEARS OLD AND ABOVE',
                '- PRE-ENTRY INTERVIEW REQUIRED UPON REGISTRATION'
            ]
        },
        'whats_next': {
            '': [
                '→ City & Guilds Level 3 Advanced Diploma in Culinary Arts & Supervision',
                '→ BA (Hons) in Culinary Arts awarded by Culinary Arts Academy Switzerland and University of Derby, UK (in Switzerland)'
            ]
        }
    },
    'Level 2 Diploma in Culinary Arts - Patisserie':{
        'partner': 'City & Guilds',
        'field': 'culinary',
        'duration': '1 Year',
        'icon': 'patisserie',
        'description': 'The Level 2 Diploma in Food Preparation & Culinary Arts - Patisserie prepares candidates for a career in hospitality by teaching food safety, workplace safety, and the preparation of various patisserie products, while developing both transferable and job-specific skills.',
        'modules': {
            '': [
                '- Understand the Hospitality Industry',
                '- Understand the Business Success',
                '- Provide Guest Service',
                '- Awareness of Sustainability in the Hospitality Industry',
                '- Professional Workplace Standards',
                '- Understand Own Role in Self Development',
                '- Food Safety',
                '- Meet Guest Requirements Through Menu Planning',
                '- Mise en Place',
                '- Prepare, Cook, and Finish Cakes, Biscuits, and Sponge Products Using Standardised Recipes',
                '- Prepare, Cook, and Finish Dough Products Using Standardised Recipes',
                '- Prepare, Cook, and Finish Hot Desserts Using Standardised Recipes',
                '- Prepare, Cook, and Finish Cold Desserts Using Standardised Recipes',
                '- Prepare, Cook, and Finish Simple Chocolate Products Using Standardised Recipes'
            ]
        },
        'entry_requirements': {
            '': [
                '- 16 YEARS OLD AND ABOVE',
                '- PRE-ENTRY INTERVIEW REQUIRED UPON REGISTRATION'
            ]
        },
        'whats_next': {
            '': [
                '→ City & Guilds Level 3 Advanced Diploma in Culinary Arts',
                '→ Bachelor of International Business in Pastry & Chocolate Arts awarded by Culinary Arts Academy Switzerland'
                '→ BA (Hons) in Culinary Arts awarded by Culinary Arts Academy Switzerland and University of Derby, UK (in Switzerland)'
            ]
        }
    },
    'Level 2 Diploma in Food and Beverage Services':{
        'partner': 'City & Guilds',
        'field': 'culinary',
        'duration': '1 Year',
        'icon': 'fnb',
        'description': 'The Level 2 Diploma in Food & Beverage equips candidates with transferable and role-specific skills for both front-of-house and kitchen roles in hospitality, preparing them for senior positions while aligning with the Global Hospitality Certification developed with Worldchefs and global employers.',
        'modules': {
            '': [
                '- Beverage Preparation',
                '- Beverage Product Knowledge',
                '- Business Success',
                '- Food and Beverage Service',
                '- Food Safety',
                '- Guest Service',
                '- Hospitality Principles',
                '- Menu Knowledge',
                '- Professional Development',
                '- Sustainability Awareness'
            ]
        },
        'entry_requirements': {
            '': [
                '- 16 YEARS OLD AND ABOVE',
                '- PRE-ENTRY INTERVIEW REQUIRED UPON REGISTRATION'
            ]
        }
    },
    'Level 3 Advanced Diploma in Culinary Arts & Supervision':{
        'partner': 'City & Guilds',
        'field': 'culinary',
        'duration': '1.5 Years',
        'icon': 'culinary',
        'description': 'The Level 3 Advanced Diploma in Culinary Arts & Supervision is designed for experienced chefs to enhance their supervisory skills, knowledge of kitchen operations, and broader understanding of the hospitality industry.',
        'modules': {
            '': [
                '- Developing Opportunities for Progression in the Culinary Industry',
                '- Supervise and Monitor Own Section',
                '- Contribute to Business Success',
                '- Contribute to the Guest Experience',
                '- Sustainability in Professional Kitchens',
                '- Monitoring and Supervision of Food Safety',
                '- Produce and Present Advanced Starters Using Standardised Recipes',
                '- Produce and Present Advanced Main Course Dishes Using Standardised Recipes',
                '- Produce and Present Advanced Desserts and Dough Using Standardised Recipes'
            ]
        },
        'entry_requirements': {
            '': [
                '- 17 YEARS OLD AND ABOVE; and',
                '- COMPLETED LEVEL 2 DIPLOMA IN FOOD PREPARATION AND CULINARY ARTS or FOOD PREPARATION & CULINARY ARTS - PATISSERIE / EQUIVALENT',
                '- PRE-ENTRY INTERVIEW REQUIRED UPON REGISTRATION'
            ]
        },
        'whats_next': {
            '': [
                '→ BA (Hons) in Culinary Arts awarded by Culinary Arts Academy Switzerland and University of Derby, UK (in Switzerland)'
            ]
        }
    },

    # PEARSON BTEC
    'Level 2 Certificate in Business':{
        'partner': 'Pearson BTEC',
        'field': 'business',
        'duration': '1 Year',
        'icon': 'business',
        'description': 'The course spans two semesters with six modules—three per semester—focusing on fundamental business concepts and soft skills, assessed through both practical and written methods.',
        'modules': {
            '': [
                '- Business Purposes',
                '- Business Organisations',
                '- Financial Forecasting for Business',
                '- The Marketing Plan',
                '- People in Organisations',
                '- Business Online',
                '- Communication in Business Contexts'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 4 GCE O\'LEVEL PASSES IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 EXTENDED CERTIFICATE',
                '- BDTVEC SKILL CERTIFICATE 2'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC Level 3 Diploma in Business',
                '→ BTEC Level 3 Diploma in Information Technology',
                '→ BTEC Level 3 Diploma in Hospitality',
                '→ BTEC Level 3 Diploma in Travel & Tourism'
            ]
        }
    },
    'Level 3 Diploma in Business':{
        'partner': 'Pearson BTEC',
        'field': 'business',
        'duration': '1.5 Years',
        'icon': 'business',
        'description': 'The BTEC National Diploma in Business is an internationally recognised, vocational qualification that prepares students for undergraduate study and equips them with practical skills in marketing, management, and finance.',
        'modules': {
            '': [
                '- Exploring Business',
                '- Research and Plan a Marketing Campaign',
                '- Business Finance',
                '- Managing an Event',
                '- Business Decision Making',
                '- Principles of Management',
                '- International Business',
                '- Market Research',
                '- Cost and Management Accounting'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 CERTIFICATE',
                '- BDTVEC PRE-NATIONAL DIPLOMA',
                '- NTEC DIPLOMA / EQUIVALENT'
            ]
        },
        'whats_next': {
            '': [
                '→ BA Common Year 1',
                '→ BTEC HND in Accounting/Marketing'
            ]
        }
    },
    'Level 5 HND in Business (Accounting)':{
        'partner': 'Pearson BTEC',
        'field': 'business',
        'duration': '2 Years',
        'icon': 'accounting',
        'description': 'The two-year BTEC Higher National Diploma in Business combines academic theory with practical application, offering pathways in accounting or marketing in the second year, and can serve as a standalone qualification or lead to direct entry into the second year of a university degree.',
        'modules': {
            'Level 4': [
                '- Business & the Business Environment',
                '- Marketing Essentials',
                '- Human Resource Management',
                '- Management and Operations',
                '- Management Accounting',
                '- Managing a Successful Business Project',
                '- Business Law',
                '- Financial Accounting'
            ],
            'Level 5 (!Core Units | *Specialist Units)': [
                '! Research Project',
                '! Organisational Behaviour',
                '- Taxation',
                '- Business Strategy',
                '* Financial Reporting',
                '* Advanced Accounting Management',
                '* Financial Management'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL + 4 GCE O\'LEVEL CREDITS*',
                '- BDTVEC NATIONAL DIPLOMA',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN BUSINESS',
                '- UNIVERSITY FOUNDATION COURSE'
            ]
        },
        'whats_next': {
            '': [
                '→ BA (Hons) Business Management',
                '→ BA (Hons) Marketing',
                '→ BA (Hons) Accounting & Finance'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.'
            ]
        }
    },
    'Level 5 HND in Business (Marketing)':{
        'partner': 'Pearson BTEC',
        'field': 'business',
        'duration': '2 Years',
        'icon': 'marketing',
        'description': 'The two-year BTEC Higher National Diploma in Business combines academic theory with practical application, offering pathways in accounting or marketing in the second year, and can serve as a standalone qualification or lead to direct entry into the second year of a university degree.',
        'modules': {
            'Level 4': [
                '- Business & the Business Environment',
                '- Marketing Essentials',
                '- Human Resource Management',
                '- Management and Operations',
                '- Management Accounting',
                '- Managing a Successful Business Project',
                '- Business Law',
                '- Financial Accounting'
            ],
            'Level 5 (!Core Units | *Specialist Units)': [
                '! Research Project',
                '! Organisational Behaviour',
                '- International Marketing',
                '- Business Strategy',
                '* Marketing Insights & Analytics',
                '* Integrated Marketing Communications',
                '* Digital Marketing'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL + 4 GCE O\'LEVEL CREDITS*',
                '- BDTVEC NATIONAL DIPLOMA',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN BUSINESS',
                '- UNIVERSITY FOUNDATION COURSE'
            ]
        },
        'whats_next': {
            '': [
                '→ BA (Hons) Business Management',
                '→ BA (Hons) Marketing',
                '→ BA (Hons) Accounting & Finance'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.'
            ]
        }
    },
    'Level 2 Diploma in Information Technology':{
        'partner': 'Pearson BTEC',
        'field': 'computer',
        'duration': '1 Year',
        'icon': 'it',
        'description': 'The Pearson BTEC International Level 2 in Information Technology offers a broad introduction to areas like programming, digital design, and networking, while also developing transferable skills for further education or employment.',
        'modules': {
            '': [
                '- Using IT to Support Information and Communication in Organisations',
                '- Data and Spreadsheet Modelling',
                '- Introduction to Computer Networking',
                '- Introduction to Programming',
                '- Introduction to Website Development',
                '- Introduction to App Development',
                '- Introduction to Games Design',
                '- Introduction to Database Systems'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 4 GCE O\'LEVEL PASSES IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 EXTENDED CERTIFICATE',
                '- BDTVEC SKILL CERTIFICATE 2'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC Level 3 Diploma in Information Technology',
                '→ BTEC Level 3 Diploma in Travel and Tourism',
                '→ BTEC Level 3 Diploma in Hospitality',
                '→ BTEC Level 3 Diploma in Business'
            ]
        }
    },
    'Level 3 Diploma in Information Technology':{
        'partner': 'Pearson BTEC',
        'field': 'computer',
        'duration': '1.5 Years',
        'icon': 'it',
        'description': 'The Level 3 BTEC Diploma in IT is an internationally recognised qualification that combines practical and theoretical learning, preparing students for IT careers through industry-relevant modules and workplace-based assignments.',
        'modules': {
            '': [
                '- Information Technology Systems',
                '- Data Modelling',
                '- Website Development',
                '- Big Data and Business Analytics',
                '- IT Technical Support and Management',
                '- Software Testing',
                '- Customising and Integrating Applications',
                '- Cloud Storage and Collaboration Tools',
                '- The Internet of Things',
                '- Enterprise in IT',
                '- Business Process Modelling Tools'
            ]
        },
        'entry_requirements': {
            '': [
                '- 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 CERTIFICATE',
                '- BDTVEC PRE-NATIONAL DIPLOMA',
                '- NCC DIPLOMA LEVEL 3',
                '- NTEC DIPLOMA / EQUIVALENT'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC HND in Computing (Application Development & Testing or Software Engineering)',
                '→ BSc (Hons) Computer Science'
            ]
        }
    },
    'Level 5 HND in Computing (App Development & Testing)':{
        'partner': 'Pearson BTEC',
        'field': 'computer',
        'duration': '2 Years',
        'icon': 'appdev',
        'description': 'The BTEC Higher National qualification in Computing provides Level 4 and 5 technical education, equipping students with broad, up-to-date knowledge in areas like software engineering and application development, and preparing them for IT careers or further study.',
        'modules': {
            '': [
                '- Programming',
                '- Networking',
                '- Professional Practice',
                '- Database Design & Development',
                '- Security',
                '- Planning a Computing Project',
                '- Software Development Lifecycles',
                '- Computing Research Project',
                '- Business Process Support',
                '- Maths for Computing',
                '- E-Commerce & Strategy',
                '- Operating Systems'
            ],
            '*Specialist Units': [
                '* Application Program Interfaces',
                '* Application Development',
                '* Risk Analysis & Systems Testing'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL + 4 GCE O\'LEVEL CREDITS*',
                '- BDTVEC NATIONAL DIPLOMA',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN INFORMATION TECHNOLOGY',
                '- FOUNDATION IN INFORMATION TECHNOLOGY'
            ]
        },
        'whats_next': {
            '': [
                '→ BSc (Hons) Computer Science'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.'
            ]
        }
    },
    'Level 5 HND in Computing (Software Engineering)':{
        'partner': 'Pearson BTEC',
        'field': 'computer',
        'duration': '2 Years',
        'icon': 'softeng',
        'description': 'The BTEC Higher National qualification in Computing provides Level 4 and 5 technical education, equipping students with broad, up-to-date knowledge in areas like software engineering and application development, and preparing them for IT careers or further study.',
        'modules': {
            '': [
                '- Programming',
                '- Networking',
                '- Professional Practice',
                '- Database Design & Development',
                '- Security',
                '- Planning a Computing Project',
                '- Software Development Lifecycles',
                '- Computing Research Project',
                '- Business Process Support',
                '- Maths for Computing',
                '- E-Commerce & Strategy',
                '- Operating Systems'
            ],
            '*Specialist Units': [
                '* Discrete Maths',
                '* Data Structures & Algorithms',
                '* Applied Programming & Design Principle'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL + 4 GCE O\'LEVEL CREDITS*',
                '- BDTVEC NATIONAL DIPLOMA',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN INFORMATION TECHNOLOGY',
                '- FOUNDATION IN INFORMATION TECHNOLOGY'
            ]
        },
        'whats_next': {
            '': [
                '→ BSc (Hons) Computer Science'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.'
            ]
        }
    },
    'Level 2 Certificate in Travel & Tourism':{
        'partner': 'Pearson BTEC',
        'field': 'tourism',
        'duration': '1 Year',
        'icon': 'plane',
        'description': 'The Pearson BTEC International Level 2 in Travel and Tourism prepares learners for careers in the industry through units in customer service, travel planning, tour guiding, and hospitality, while also developing transferable skills for further education or employment.',
        'modules': {
            '': [
                '- The Travel and Toruism Industry',
                '- Customer Service in Travel and Tourism Organisations',
                '- Travel Planning',
                '- Exploring Marketing in Travel and Tourism',
                '- Development of the Travel and Tourism Industry',
                '- Your Country as a Tourist Destination',
                '- Working as a Tour Guide',
                '- Hospitality in the Travel and Tourism Industry'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 4 GCE O\'LEVEL PASSES IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 EXTENDED CERTIFICATE',
                '- BDTVEC SKILL CERTIFICATE 2'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC Level 3 Diploma in Travel & Tourism',
                '→ BTEC Level 3 Diploma in Hospitality',
                '→ BTEC Level 3 Diploma in Business',
                '→ BTEC Level 3 Diploma in Information Technology'
            ]
        }
    },
    'Level 3 Diploma in Travel & Tourism':{
        'partner': 'Pearson BTEC',
        'field': 'tourism',
        'duration': '1.5 Years',
        'icon': 'plane',
        'description': 'The Pearson BTEC International Level 3 in Travel and Tourism prepares learners for higher education or entry-level roles in the sector, with industry-informed content designed to support progression within leisure, travel, and tourism careers.',
        'modules': {
            '': [
                '- The Travel and Tourism Industry',
                '- Worldwide Travel and Tourism Destination',
                '- Marketing Travel and Tourism to Domestic and International Customers',
                '- Customer Service in Travel & Tourism',
                '- Travel and Tourism Enterprises',
                '- Specialist Tourism',
                '- Sustainable Tourism',
                '- Events, Conferences, and Exhibitions for the Travel and Tourism Industry',
                '- Recruitment and Selection in Travel and Tourism'
            ]
        },
        'entry_requirements': {
            '': [
                '- MIN. 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 EXTENDED CERTIFICATE',
                '- BDTVEC SKILL CERTIFICATE 2'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC HND in Hospitality Management',
                '→ BA (Hons) International Tourism Management'
            ]
        }
    },
    'Level 3 Diploma in Hospitality':{
        'partner': 'Pearson BTEC',
        'field': 'tourism',
        'duration': '1.5 Years',
        'icon': 'hospitality',
        'description': 'The BTEC Level 3 Diploma in Hospitality is a vocational qualification that equips students with practical skills and theoretical knowledge for entry into the hospitality industry or progression to higher education.',
        'modules': {
            '': [
                '- The Hospitality Industry',
                '- Customer Service Provision in Hospitality',
                '- Contemporary Global Cuisine',
                '- Marketing for Hospitality',
                '- Environment and Sustainability in the Hospitality Industry',
                '- Events in Hospitality',
                '- Recruitment and Selection in Hospitality',
                '- Supervise Food and Beverage Service',
                '- The Principles of Leadership and Supervision',
                '- Hospitality Business Enterprise',
                '- Cost Control for Hospitality Supervisors',
                '- Accomodation Operations'
            ]
        },
        'entry_requirements': {
            '': [
                '- 4 GCE O\'LEVEL CREDITS IN ENGLISH MEDIUM SUBJECTS or 2 MALAY AND 2 ENGLISH MEDIUM SUBJECTS',
                '- BTEC LEVEL 2 CERTIFICATE',
                '- BDTVEC PRE-NATIONAL DIPLOMA',
                '- NTEC DIPLOMA / EQUIVALENT'
            ]
        },
        'whats_next': {
            '': [
                '→ BTEC HND in Hospitality Management',
                '→ BA (Hons) International Tourism Management'
            ]
        }
    },
    'Level HND in Hospitality Management':{
        'partner': 'Pearson BTEC',
        'field': 'tourism',
        'duration': '2 Years',
        'icon': 'hospitality',
        'description': 'The two-year Higher National Diploma in Hospitality focuses on management aspects of the industry—such as hotels, restaurants, and events—adapting core business concepts like marketing, management, and finance for a hospitality context, and is suitable for both experienced and new students.',
        'modules': {
            'Level 4': [
                '- The Contemporary Hospitality Industry',
                '- Managing the Customer Experience',
                '- Professional Identity and Practice',
                '- The Hospitality Business Toolkit',
                '- Leadership and Management for Service Industries',
                '- Managing Food and Beverage Operations',
                '- Managing Accomodation Services',
                '- Hospitality Marketing Essentials'
            ],
            'Level 5': [
                '- Research Project',
                '- Hospitality Consumer Behaviours and Insight',
                '- Menu Development, Planning, and Design',
                '- Revenue Management',
                '- Organisational Behaviour',
                '- Managing and Planning an Event'
            ]
        },
        'entry_requirements': {
            '': [
                '- 1 GCE A\'LEVEL + 4 GCE O\'LEVEL CREDITS*',
                '- HNTEC CERTIFICATE / EQUIVALENT',
                '- BTEC LEVEL 3 DIPLOMA IN HOSPITALITY',
                '- UNIVERSITY FOUNDATION COURSE'
            ]
        },
        'whats_next': {
            '': [
                '→ BSc (Hons) International Tourism Management'
            ]
        },
        'notes': {
            '': [
                '* GCE O\'Level in English or IELTS score of 5.5 can also be considered with this qualification.'
            ]
        }
    }
}