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

    'Danya': {

    },

    'Valentyn': {
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

    'Amjad': {

    }
}

# Course data structure to replace monster data
UNIVERSITY_PARTNERS = {
    'University of Essex': {
        'icon': 'essex',
        'description': 'The University of Essex is a vibrant institution renowned for its research-driven approach and diverse academic offerings. It fosters an inclusive environment that emphasizes innovation, social justice, and personal development for students.',
        'programs': 'We provide undergraduate level programmes in LLB Law, BA (Hons) & BSc (Hons) ranging from Accounting and Finance, Marketing, Business Management, International Tourism Management, and Computer Science from one of UK\'s top universities.'
    },
    'Kensington College': {
        'icon': 'kensington',
        'description': 'A prestigious college offering specialized programs in business and professional development.',
        'programs': 'Focused programs in Business Management, Professional Development, and Industry-Specific Training.'
    },
    'City & Guilds': {
        'icon': 'city_guilds',
        'description': 'Leading vocational education provider with industry-recognized qualifications.',
        'programs': 'Professional certifications and vocational training across multiple industries.'
    },
    'Pearson BTEC': {
        'icon': 'pearson',
        'description': 'Practical, work-related qualifications designed to give learners the skills they need.',
        'programs': 'BTEC qualifications in various subjects including Business, Computing, and Engineering.'
    }
}

COURSE_DATA = {
    'BA (Hons) Accounting & Finance': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'accounting',
        'element': 'business',
        'description': 'The Accounting & Finance program provides comprehensive understanding of financial principles, management accounting, and corporate finance.',
        'modules': {
            'Year 1': [
                'Introduction to Financial Accounting',
                'Mathematics for Finance',
                'Business Economics',
                'Management Principles',
                'Statistics for Business'
            ],
            'Year 2': [
                'Management Accounting',
                'Corporate Finance',
                'Financial Analysis',
                'Business Law',
                'International Finance'
            ],
            'Year 3': [
                'Advanced Financial Reporting',
                'Investment Analysis',
                'Risk Management',
                'Strategic Management',
                'Dissertation Project'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Additional': 'HNTEC CERTIFICATE'
        },
        'career_prospects': [
            'Financial Analyst',
            'Management Accountant',
            'Investment Banker',
            'Corporate Finance Specialist',
            'Financial Controller'
        ]
    },
    'BA (Hons) Business Management': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'business',
        'element': 'business',
        'description': 'Comprehensive business program covering all aspects of modern management and entrepreneurship.',
        'modules': {
            'Year 1': [
                'Fundamentals of Management',
                'Marketing Principles',
                'Business Economics',
                'Organizational Behavior',
                'Financial Management'
            ],
            'Year 2': [
                'Strategic Management',
                'Operations Management',
                'Human Resource Management',
                'Digital Business',
                'Project Management'
            ],
            'Year 3': [
                'International Business',
                'Innovation Management',
                'Business Ethics',
                'Consultancy Project',
                'Dissertation'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Additional': 'HNTEC CERTIFICATE'
        },
        'career_prospects': [
            'Business Manager',
            'Management Consultant',
            'Project Manager',
            'Entrepreneur',
            'Operations Manager'
        ]
    },
    'BA (Hons) Marketing': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'marketing',
        'element': 'business',
        'description': 'Dynamic marketing program focusing on digital marketing, consumer behavior, and brand management.',
        'modules': {
            'Year 1': [
                'Marketing Fundamentals',
                'Consumer Behavior',
                'Market Research',
                'Business Communication',
                'Digital Literacy'
            ],
            'Year 2': [
                'Digital Marketing',
                'Brand Management',
                'Marketing Analytics',
                'International Marketing',
                'Creative Marketing'
            ],
            'Year 3': [
                'Strategic Marketing',
                'Marketing Campaign Management',
                'Social Media Marketing',
                'Marketing Dissertation',
                'Industry Placement'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Additional': 'HNTEC CERTIFICATE'
        },
        'career_prospects': [
            'Marketing Manager',
            'Digital Marketing Specialist',
            'Brand Manager',
            'Marketing Analyst',
            'Social Media Manager'
        ]
    },
    'BA (Hons) International Tourism Management': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'tourism',
        'element': 'business',
        'description': 'Specialized program in tourism industry management with global perspective.',
        'modules': {
            'Year 1': [
                'Introduction to Tourism',
                'Tourism Geography',
                'Hospitality Management',
                'Cultural Studies',
                'Business Principles'
            ],
            'Year 2': [
                'Sustainable Tourism',
                'Tourism Marketing',
                'Event Management',
                'Tourism Economics',
                'Language Studies'
            ],
            'Year 3': [
                'Tourism Policy',
                'Destination Management',
                'Tourism Technology',
                'Industry Project',
                'International Placement'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Additional': 'HNTEC CERTIFICATE'
        },
        'career_prospects': [
            'Tourism Manager',
            'Travel Consultant',
            'Event Coordinator',
            'Destination Marketing Manager',
            'Hotel Manager'
        ]
    },
    'BSc (Hons) Computer Science': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'computer',
        'element': 'technology',
        'description': 'The Computer Science program provides students with a theoretical and practical understanding of how computers work, how software is developed, how computers communicate, and how data is processed and stored.',
        'modules': {
            'Year 1': [
                'Introduction to Databases',
                'Computer Organization & Operating Systems',
                'Networks Fundamentals',
                'Web Development',
                'Professional Skills for Computing',
                'Introduction to Programming'
            ],
            'Year 2': [
                'Data Structures & Algorithms',
                'Big Data',
                'Cybersecurity',
                'Further Networking',
                'Software Engineering',
                'Team Project'
            ],
            'Year 3': [
                'Capstone Project',
                'System Analysis',
                'Advanced Programming',
                'AI & Machine Learning',
                'Computer Games Development'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Foundation': 'HNTEC CERTIFICATE',
            'Additional': 'BTEC LVL 3 DIPLOMA IN IT (OVERALL MERIT-MERIT)',
            'Equivalent': 'FOUNDATION IN IT / EQUIVALENT',
            'Year 2': 'BTEC LVL 5 HND IN COMPUTING / EQUIVALENT'
        },
        'career_prospects': [
            'Software Developer',
            'Data Scientist',
            'Cybersecurity Specialist',
            'Systems Analyst',
            'Web Developer',
            'AI/ML Engineer'
        ]
    },
    'LLB Law': {
        'university': 'University of Essex',
        'duration': '3 Years',
        'icon': 'law',
        'element': 'legal',
        'description': 'Comprehensive law degree covering fundamental legal principles and contemporary legal issues.',
        'modules': {
            'Year 1': [
                'Contract Law',
                'Criminal Law',
                'Constitutional Law',
                'Legal Skills',
                'Tort Law'
            ],
            'Year 2': [
                'Property Law',
                'Family Law',
                'Commercial Law',
                'Human Rights Law',
                'Legal Research'
            ],
            'Year 3': [
                'International Law',
                'Corporate Law',
                'Legal Practice',
                'Dissertation',
                'Advocacy Skills'
            ]
        },
        'entry_requirements': {
            'Year 1': 'MIN 112 UCAS PTS (GCE A LVL)',
            'Alternative': 'IB - 26 PTS',
            'Additional': 'HNTEC CERTIFICATE'
        },
        'career_prospects': [
            'Solicitor',
            'Barrister',
            'Legal Advisor',
            'Corporate Lawyer',
            'Legal Consultant'
        ]
    }
}