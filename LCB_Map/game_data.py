CHARACTER_DATA = {
    'Cortana': {
        'directions': ['down'],
        'radius': 0,
        'look_around': False,
        'dialog': {
            'default': ['Welcome to LCB!']
        },
        'defeated': False
    },

    'Atticus': {

    },

    'Dylan': {

    },

    'Munaf': {
        'directions': ['down'],
        'radius': 0,
        'look_around': False,
        'dialog': {
            'default': ['Welcome to LCB!']
        },
        'defeated': False
    },

    'Chell': {

    },

    'Alcina': {

    },

    'Enise': {

    },

    'Jay': {

    }
}

# Course data structure to replace monster data
# course_data.py
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
                '- BTEC LEVEL 3 DIPLOMA IN HOSPITALITY (OVERALL MERIT-MERIT)',
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
                '- Mathematics for Computing'
                '- Introduction to Programming'
            ],
            'Year 2': [
                '- Data Structures & Algorithms',
                '- Advanced Databases & Warehousing',
                '- Cybersecurity',
                '- Further Networking',
                '- Mobile App Programming',
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
                '- Foundations of Public Law'
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
        'description': '',
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
                '- 4 GCE O\'LEVEL IN ENGLISH MEDIUM SUBJECTS',
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
        'description': '',
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
                '- 4 GCE O\'LEVEL IN ENGLISH MEDIUM SUBJECTS',
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
        'description': '',
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
                '- 5 GCE/IGCSE O\'LEVEL IN 4 ENGLISH MEDIUM SUBJECTS + 1 ENGLISH LANGUAGE'
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
        'description': '',
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
                '- BTEC LEVEL 3 DIPLOMA (OVERALL MERIT-MERIT)',
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
                '- MIN. 2 GCE A\'LEVEL CREDITS',
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
                '→ Degree in Business with our University Partners in the UK (1 Year); OR',
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
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
        'modules': {
            '': [
                '- English for Academic Purposes',
                '- Communication Skills',
                '- Presentation Skills',
                '- Airline Customer Service',
                '- In-flight Service',
                '- Airport Ground Service',
                '- Interview Skills & Personal and Professional Development',
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
                '- 1 GCE A\'LEVEL CREDITS / EQUIVALENT*',
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
        'description': 'KCB Professional Pathway (2 Years) -- The programme allows holders of the KCB Higher Diploma to gain direct entry into the final year of a BA in Business Studies, saving time and cost while equipping students with practical knowledge for entrepreneurship or roles in established businesses.',
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
                '- 1 GCE A\'LEVEL CREDITS / EQUIVALENT*',
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
    'Level 2 Diploma in Culinary Arts':{
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
                '→ City & Guilds Level 3 Advanced Diploma in Culinary Arts',
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
        'description': '',
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
        'description': '',
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
        'description': '',
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
        'description': '',
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
        'description': '',
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
        'description': '',
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
    'Level 5 HND in Computing (Application Development & Testing)':{
        'partner': 'Pearson BTEC',
        'field': 'computer',
        'duration': '2 Years',
        'icon': 'appdev',
        'description': '',
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
        'description': '',
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
}