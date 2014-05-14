#!/usr/bin/env python

import random

def main():
    buzz1 = random.choice(["Social media", "E-reference", "Outreach programs", "Badges", 
                           "QR codes", "Emerging technologies", "Discovery tools", "Mobile applications",
                           "Platinum open access", "MOOCs", "Responsive design", "Patron-driven acquisitions", 
                           'Graphic novels', 'Makerspaces', 'GIS', 'Best practices', 'Crowdsourcing',
                           "Big data", 'Hackathons', "Zombie walks", "Augmented reality", 'Gamification', 
                           'Altmetrics', "Rethinking", "Flipped classrooms", "Zines", "New media", "Mashups", "Web 3.0", 
                           "Engaging users", "Flashmobs", "Community engagement"])
    buzz2 = random.choice(["for", 'for', 'with', 'with', 'without', 'to assist', "to create", 'to enable', 'to extend',
                           'to empower', 'in', 'and', 'and', 'for', 'to assist', 'to create', 'to enable', 'to extend', 
                           'in', 'and', 'to reinvent', 'to reinvent'])
    buzz3 = random.choice(['non-traditional students.', 'embedded librarians.', 'underserved populations.', 
                           'information literacy.', 'digital natives.', 'born-digital content.', 
                           'iPads.', 'just-in-time instruction.', 'data curation.', 'communcating value.', 
                           'digital humanities.', 'digital learning objects.', 'non-traditional learners.',
                           'copyright compliance.', 'fair use.', 'makerspaces.', 'the semantic web.', 
                           'outcomes assessment.', 'ebook readers.', 'net neutrality.', 'interoperability.',
                           'next-generation reference service.', 'intellectual freedom.', '3D printers.',
                           'the cloud.', 'scholarly communications.', 'tweens.', 'gigabit networks.', 
                           "digital preservation.", "web 3.0.", "one-shot instruction sessions.",
                           "job seekers.", "unemployed librarians.", "community engagement.",
                           "defending challenged materials."])
    
    if buzz3 == "communcating value." or buzz3 == "defending challenged materials.":
        buzz2 = random.choice(['for', 'and'])  
        
    if buzz1 == "Rethinking":
        buzz2 = ""

    
    print """
    <html>
    <head>
      <Title>Library Buzz</Title>
      <link rel="stylesheet" type="text/css" href = "./buzz.css">
      <meta name="description" content="Why not let a computer decide your next library project?">
    <head>
    <body>
	  <div id = "container">
        <div class = "content" id = "intro">Your new library initiative is:</div>
        <div class = "content" id = "buzz">%s %s %s</div>  
        <div class="content" id="outro"><a href="javascript:history.go(0)">Refresh the page to get another</a></div>
	  </div>
	<div id = "footer">
	    This random library buzzword generator was created by <a href="http://www.zachsharrow.info/">Zachary Sharrow</a> for fun and practice.
	</div>
    </body>
    </html> """ % (buzz1, buzz2, buzz3)
    
try: 
    print"Content-Type: text/html\n\n"
    main()

except:
    print"Content-Type: text/html\n\n"
    print """
    <html>
      <Title>Random Library Buzzword Generator</Title>
    <body>
        <div id = "error">Uh oh.  Something broke.  It's probably your fault.</div>
    </body>
    </html> """
    