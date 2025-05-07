import random

job_titles = [
    # General Software Roles
    "Software Engineer",
    "Software Developer",
    "Software Architect",
    "Systems Engineer",
    "Solutions Architect",

    # Front-End Roles
    "Frontend Developer",
    "UI/UX Developer",
    "Web Developer",

    # Back-End Roles
    "Backend Developer",
    "API Developer",
    # "Database Engineer",

    # Full-Stack Roles
    "Full Stack Developer",
    "MEAN/MERN Stack Developer",

    # Mobile Development
    "Mobile App Developer",
    "Android Developer",
    "iOS Developer",
    "Cross-Platform Mobile Developer",

    # DevOps/Infrastructure Roles
    "DevOps Engineer",
    "Site Reliability Engineer (SRE)",
    "Infrastructure Engineer",
    # "Build and Release Engineer",

    # Cloud Computing Roles
    # "Cloud Engineer",
    "Cloud Architect",
    "AWS/Azure/Google Cloud Engineer",

    # Machine Learning & AI
    "Machine Learning Engineer",
    "AI Engineer",
    "Data Scientist",
    "NLP/Computer Vision Engineer",
    "Deep Learning Engineer",

    # Data Roles
    "Data Engineer",
    "Data Architect",
    "Data Analyst",
    "Database Administrator (DBA)",

    # Embedded Systems/IoT
    "Embedded Systems Engineer",
    "Firmware Developer",
    "IoT Developer",
    "Robotics Engineer",

    # Testing & QA
    "QA Engineer",
    "Automation Engineer",
    "Software Tester",

    # Game Development
    "Game Developer",
    # "Unity/Unreal Developer",
    # "Gameplay Programmer",

    # Security Roles
    "Cybersecurity Engineer",
    # "Security Analyst", 
    "Penetration Tester",
    # "Ethical Hacker",

    # Specialized Roles
    "Blockchain Developer",
    "AR/VR Developer",
    "Simulation Engineer",
    "Firmware Engineer",

    # Leadership & Management
    # "Engineering Manager",
    # "Technical Lead",
    # "Product Manager (Technical)",
    # "CTO (Chief Technology Officer)",

    # Other Titles
    "Research Engineer",
    "Technical Program Manager",
    "Software Consultant",
    "Technical Support Engineer",
    "Integration Specialist"
]

def getRandomJobTitle():
    return random.choice(job_titles)
