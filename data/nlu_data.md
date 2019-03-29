<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:lookup_by_faultcode
- Faultcode

## intent:21-00TASK_801
- [Smoke](fault) or [Fumes](fault) in the [Passenger Cabin](location) or [Flight Compartment](location), Reported During Flight, Smoke Stops With [Isolation Valve](part) Closed, [Right Pack](part) Switch Off - Fault Isolation
- [Smoke](fault) or [fumes](fault) flow into the [passenger cabin](location) or the [flight compartment](location) through the [air distribution system](part) during flight.
- This problem is usually caused by [contamination](cause) of the [air byoil](fluid), [glycol](fluid), [fuel](fluid), or [hydraulic fluid](fluid).
- In flight, [contamination](cause) can be caused by [leakage](cause) of these fluids in one of the [engines](part).
- [Smoke](fault) or [fumes](fault) can also be caused by [oil](fluid), [glycol](fluid), [hydraulic fluid](fluid), fuel fumes or exhaust fumes being ingested into the [inlet](part) of one of the engines.
- From the [inlet](part),the [contaminant](fault) can go into the [pneumatic](part) and/or the [air conditioning system](part) and vaporize at higher temperatures.
- [Fumes](fault) can also be caused by the use of petroleum jelly during maintenance of the [pneumatic ducts](part) or [air distribution ducts](part).
- Make sure the fault report shows the [smoke](fault) or [fumes](fault) were stopped with the [isolation valve](part) closed, the [right pack](part) switch off, and the two [recirculation fans](part) off.
- This means that the [No. 1 engine](part), the pneumatic air supply from the [No. 1 engine](part), the [left pack](part), and the related [airdistribution ducts](part) were not the source of the smoke or fumes.
- The Fault Isolation procedure below tells you how to find the cause of smoke in the [No. 2 engine](part), the pneumatic air supply from the [No. 2 engine](part), the [right pack](part), the [recirculation system](part), and the [related air distribution ducts](part).
- Do not do this procedure with the passengers or the crew on the airplane since it can cause [smoke](fault) or [fumes](fault) in the [passenger cabin](location).
- [Contamination](fault) in the [Engine No. 2 pneumatic system](part)
- [Hydraulic fluid](fluid) [leakage](fault)
- [Contamination](fault) in the [air distribution system](part)
- [Overheating](fault) of [recirculation fan](part)

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- I am [Charlie](name)
- I am [Ben](name)
- Call me [Susan](name)
- [Lucy](name)
- [Peter](name)
- [Mark](name)
- [Joseph](name)
- [Tan](name)
- [Pete](name)
- [Elon](name)
- [Penny](name)
- name is [Andrew](name)
- I [Lora](name)
- [Stan](name) is my name
- [Susan](name) is the name
- [Ross](name) is my first name
- [Bing](name) is my last name
- Few call me as [Angelina](name)
- Some call me [Julia](name)
- Everyone calls me [Laura](name)
- I am [Ganesh](name)
- My name is [Mike](name)
- just call me [Monika](name)
- Few call [Dan](name)
- You can always call me [Suraj](name)
- Some will call me [Andrew](name)
- My name is [Ajay](name)
- I call [Ding](name)
- I'm [Partia](name)
- Please call me [Leo](name)
- name is [Pari](name)
- name [Sanjay](name)


## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke
