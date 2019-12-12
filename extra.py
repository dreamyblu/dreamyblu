"""
THIS IS EXTRA.PY ! This python file has the necessary goods to help out bobaBot. I used some of the code from A3 to help guide my bot to completion. I added a new function called "is_exclamtion" to look for possible use of the "!" symbol. When executed in the bobaBot, the bot itself is aware of it and tells the user to 'lower their voice' because robots have feelings too!

"""
# we shall import strings and random to help us out!
import string
import random

# this function checks to see if the user has input a '?'
def is_question(input_string):
    output = '?' in input_string
    return output

# this function checks to see if the user has input a '!"
def is_exclamation(input_string):
    output = '!' in input_string
    return output

# Once we know if an input is a question, we are going to get
# rid of all punctuation.
def remove_punctuation(input_string):
    out_string = ""
    for c in input_string:
        if c not in string.punctuation:
            out_string += c
    return out_string

def remove_punctuation(val):
    return ''.join([x for x in val if x not in string.punctuation])

# a more general function to prepare the text inputs for processing.
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

# a function that will help us select an output for the chatbot,
# based on the input it got.
def selector(input_list, check_list, return_list):
    output = None
    for i in range(len(input_list)):
        if input_list[i] in check_list:
            output = random.choice(return_list)
    return output

# this function ends the chat if you input 'quit'
def end_chat(input_list):
    return 'quit' in input_list

# this shows what you must input to get a certain greeting output
GREETINGS_IN = ['hello', 'hi', 'hey']
GREETINGS_OUT = ["hiya! it's boba bot - let's chat! type 'option'!"]

#this shows up when greeted with something that bobaBot does not understand
UNKNOWN = ["that's a little off-topic, let's spill the tea again. :)",
           "huh? sorry i don't understand. :( back to boba talk"]

# this appears when bobaBot sees a user-input question. bobaBot does not want
# to answer random questions.
QUESTION = ("hm. i'm too shy to answer 👉🏽👈🏽 let's just talk about tea again")

# this appears when bobaBot sees a user-input exclmation. bobaBot does not
# want to hear loud things. it does not like that.
EXCLAMATION = ("aaaaa ! is there anyway you could lower your voice? 🥺")

# this appears when you are greeted with two options. the user can either
# order or discuss boba toppings!
OPTIONS_IN = ['option']
OPTIONS_OUT = ['what would you like to do? order or discuss?']

# this appears when the user is ready to order! it starts off with asking
# whether the user wants green or black tea. 
ORDER1_IN = ['order']
ORDER1_OUT = ['great! what kind of tea would you like? green or black?']

# this appears when the user picks a tea. it then continues with toppings.
TEA_IN = ['black', 'green', 'black tea', 'green tea']
TEA_OUT = ['sounds great! would you like any toppings?']

# this appears when the user picks a topping. it then asks if that is all.
TOPPINGS_IN = ['boba', 'egg pudding', 'lychee jelly', 'coffee jelly']
TOPPINGS_OUT = ['good choice! i will add that to the order! is that all?',
               'ooh that sounds good! is that all?' ]

# this appears when the user is finished and the bot tells them to 'quit'
FINISH_IN = ['yes', 'done']
FINISH_OUT = ["okay! now 'quit' to get your order! :)"]

# this appears when the user is not finished and would like to order more.
INCOMPLETE_IN = ['no']
INCOMPLETE_OUT = ["okay! if you would like to order again, just 'order'!"]

#this appears when the user wants to know more about the toppings. user
# MUST input the acronyms of the toppings. 
DISCUSS_IN = ['discuss']
DISCUSS_OUT = ["""you have questions about the toppings?
    just type in their designated ACRONYMS we have: boba (bb),
    egg pudding (ep), lychee jelly (lj), and coffee jelly (cj)!"""]

# this appears when the user wants to know more about boba
BB_DISCUSS_IN = ['bb']
BB_DISCUSS_OUT = ["""boba is a chewy tapioca ball that
    is used as a topping in tea drinks! it can come
    in different forms such as mini boba and also
    fruit juice filled 'popping boba'! what other
    toppings interest you? or are you ready to
    'order'?"""]

# this appears when the user wants to know more about egg pudding
EP_DISCUSS_IN = ['ep']
EP_DISCUSS_OUT = ["""egg pudding is a jello-like snack that
    is used as a topping in tea drinks! it has a nice
    texture and usually tastes like caramel. what other
    toppings interest you? or are you ready to
    'order' ? """]

# this appears when the user wants to know more about lychee jelly
LJ_DISCUSS_IN = ['lj']
LJ_DISCUSS_OUT = ["""lychee jelly is a jello-like item that
    is used as a topping in tea drinks! it has a crunchy
    texture and tastes similar to the tropical fruit
    it is named after. what other toppings interest you?
    or are you ready to 'order' ? """]

# this appears when the user wants to know more about coffee jelly
CJ_DISCUSS_IN = ['cj']
CJ_DISCUSS_OUT = ["""coffee jelly is a jello-like item that
    is used as a topping in tea drinks! it has a crunchy
    texture and tastes similar to the drink it is named after.
    what other toppings interest you? or are you ready to
    'order' ? """]

# this is our main function, tea_time! it is the BACKBONE of
# bobaBot. 
def tea_time():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)
        
        # Check if the input is an exclamation
        exclamation = is_exclamation(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'enjoy your drink! goodbye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            # Check if the input looks like you're picking a topping
            outs.append(selector(msg, TOPPINGS_IN, TOPPINGS_OUT))
            
            # Check if the input looks like you're asking to order or discuss what
            # toppings are if so
            outs.append(selector(msg, OPTIONS_IN, OPTIONS_OUT))
            
            # Check if the input looks like you're asking to order
            outs.append(selector(msg, ORDER1_IN, ORDER1_OUT))
            
            # Check if the input looks like you're picking a tea
            outs.append(selector(msg, TEA_IN, TEA_OUT))
            
            # Check if the input looks like you're done with your order
            outs.append(selector(msg, FINISH_IN, FINISH_OUT))
            
            # Check if the input looks like you're not done with your order
            outs.append(selector(msg, INCOMPLETE_IN, INCOMPLETE_OUT))
            
            # Check if the input looks like you're asking to what toppings are if so
            outs.append(selector(msg, DISCUSS_IN, DISCUSS_OUT))
            
            # Check if the input looks like you're asking what boba is
            outs.append(selector(msg, BB_DISCUSS_IN, BB_DISCUSS_OUT))
            
            # Check if the input looks like you're asking what egg pudding is
            outs.append(selector(msg, EP_DISCUSS_IN, EP_DISCUSS_OUT))
            
            # Check if the input looks like you're asking what lychee jelly is
            outs.append(selector(msg, LJ_DISCUSS_IN, LJ_DISCUSS_OUT))
            
            # Check if the input looks like you're asking what coffee jelly is 
            outs.append(selector(msg, CJ_DISCUSS_IN, CJ_DISCUSS_OUT))
            
            # We could have selected multiple outputs from the topic search above
            # (if multiple return possible outputs)
            # We also might have appended None in some cases, meaning we don't have a reply
            # To deal with this, we are going to randomly select an output from the set of
            # outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg
        # related to it being a question
        if not out_msg and question:
            out_msg = QUESTION
        
        # if we don't have an output yet, but the input was an exclamation, return msg
        # related to it being an exclamation
        if not out_msg and exclamation:
            out_msg = EXCLAMATION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)