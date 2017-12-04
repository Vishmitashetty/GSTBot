import aiml
import os

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles='/home/vishmitashetty/Documents/hackathon/aiml-en-us-foundation-alice/std-startup.xml',
                 commands="load aiml b")

'''if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = '/home/vishmitashetty/Documents/hackathon/aiml-en-us-foundation-alice/std-startup.xml', commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")'''

# kernel now ready for use
while True:
    #print kernel.respond(raw_input("Enter your message >> "))
    x = kernel.respond(raw_input(">> "))
    #print "here is your response"
    print x
