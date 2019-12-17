
from __future__ import division
#General
import math
import os
import random
import time
import nltk
import string
import re


import discord
import youtube
import chatbot

#Artificial Intelligence
import AI_sim
import AI_extract
import AI_lda


from collections import Counter, defaultdict
from math import log,isinf
import csv
import codecs
import re
import random
import json

#Commands
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
var_a = True

prefix = "?"
money_list = {}
nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
# picklehi
rec_memory = {
}
input_added = ["test"]
output_added = ["out"]
#For the chatbot, it will not work if the flag is True
onsimilar_i = []
onsimilar_o = []

  

  
def most_frequent(list_): 
    return max(set(list_), key = List.count) 
f= open("user_list.txt","w+")
users = f.readlines()
def write_user(user):
      global f
      if(user not in users):
        f.write(str(user))
        users.append(user)

#
#reddit commands
#

import praw 
r = praw.Reddit(client_id='g80RLglE24ywrg',
                     client_secret='8KV0haXRiYIzlYZbDQCX6PIDQRM',
                     user_agent='android:com.example.myredditapp:v1.2.3 (by /u/whadktya)')

def search_reddit(searchterm):
  urls = []
  subs = []
  for submission in r.subreddit('all').search(searchterm):
      urls.append(submission.url)
      subs.append(submission.subreddit)
      
  sub= random.randint(1,len(urls))  

  if "i.reddit" in urls[sub]:
    
    if(subs[sub].over18):
      return "No that's nsfw."
  else:
    return str(urls[sub])  
def get_comments(submission):
    submission.comments.replace_more(limit=0)
    top_ = []
    for top_level_comment in submission.comments:
      top_.append(top_level_comment.body)
    return top_[0]  

def ask_reddit(askterm):
  titles = []
  urls = []
  content = []
  flat_comments=[]
  for submission in r.subreddit('all').search(askterm):
      urls.append(str(submission.url))
      titles.append(str(submission.title))
      try:
        content.append(str(get_comments(submission)))
      except Exception as E:
        content.append(str(submission.url))
        print(E)  

  gmax = get_max_arg(askterm,titles)
  return content[gmax]

def extract_sub(message):
  split = message.split(" ")
  for x in range(len(split)):
    if("r/" in split[x]):
      sub = split[x].replace("r/","")
  return sub    

def get_random_post(subreddit):
    sub = r.subreddit(subreddit)
    posts = sub.hot(limit=100)
    random_post_number = random.randint(0,100)
    for i,post in enumerate(posts):
      if i==random_post_number:
          return post.url

def get_random_tps(subreddit):
  sub = r.subreddit(subreddit)
  posts = sub.hot(limit=100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(posts):
      if i==random_post_number:
          return [post.url,post.score,post.title]
def get_random_content(subreddit):
  sub = r.subreddit(subreddit)
  posts = sub.hot(limit=100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(posts):
      if i==random_post_number:
          return post.selftext

def get_random_joke():
  sub = r.subreddit("jokes")
  posts = sub.hot(limit=100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(posts):
      if i==random_post_number:
          return [post.title, post.selftext]
          

def get_random_title(subreddit):
  sub = r.subreddit(subreddit)
  posts = sub.new(limit=100)
  random_post_number = random.randint(0,100)
  for i,post in enumerate(posts):
      if i==random_post_number:
          return post.title          
greenflag_ai = False
def filter_resp(input_,input_list):
  filtered = []
  for x in range(len(input_list)):
    if(AI_sim.sim(input_,input_list[x]) > 0.5):
      filtered.append(input_list[x])
    else:
      pass
  filtered.remove(input_)
  return filtered      
def check_if_question(text):
  greenflag = False
  simdex = []
  for x in range(len(questions)):
    if(AI_sim.sim(text,questions[x-1])>0.75):
      greenflag = True
    else:
      simdex.append(AI_sim.sim(text,questions[x-1]))
  if(greenflag == True or sum(simdex)/len(simdex)>0.6):
    return True
     
i = 0
def add_input(input_,output):
  input_added.append(input_)
  output_added.append(output)
  with open("user_in.txt", 'a') as file:
    file.write("\n" + input_)
  with open("bot_out.txt", 'a') as file:
    file.write("\n" + output)


def a_sim(user_c,real_c):
 if AI_sim.sim(" ".join(user_c.list())," ".join(real_c.list())>0.7):
    return True
 else:
    return False  
 for x in range(len(commands)):
    if a_sim(message,commands[x]):
      predicted = commands[x]
    return commands[x]    

def get_response(input_):
  i = 0
  greenflag = False
  while(i<len(input_added)and greenflag is False):
    if(AI_sim.sim(input_,input_added[i])>0.5):
      return(output_added[i])
      greenflag = True
    else:
      i = i+1
     
def get_max(input_,input_list):
   i = 0
   simdex = []
   for x in range(len(input_list)):
     simdex.append(AI_sim.sim(input_,input_list[x-1]))
   max_out = input_list[np.argmax(simdex)]  
   return max_out

def get_max_arg(input_,input_list):
   i = 0
   simdex = []
   for x in range(len(input_list)):
     simdex.append(AI_sim.sim(input_,input_list[x-1]))
   max_out = np.argmax(simdex)
   return max_out   
def get_3maximum_indices(text,list_of_text):
  simdex = []
  for x in range(len(list_of_text)):
    simdex.append(AI_sim.sim(text,list_of_text[x]))
  wimdex = []  
  for x in range(len(3)):
    wimdex.append(np.argmax(simdex))
    del wimdex[np.argmax(simdex)]
  return wimdex  

def get_max(inp,input_):
  sims = []
  for x in range(len(input_)):
    sims.append(AI_sim.sim(inp,input_[x]))
  out = np.argmax(sims)
  out = input_[out]  
  return out

def get_max_c(inp,input_,output_):
  sims = []
  for x in range(len(input_)):
    sims.append(AI_sim.sim(inp,input_[x]))
  out = np.argmax(sims)
  out = output_[out]  
  return out


answers = ["C as it is the "]
disses=["Wait, were you born on a highway? That's where most accidents happen.","I could agree with you, but then we'd both be wrong"]

eightball = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def word_occurence(message_content):
  return message_content.split(" ").count(random.choice(message_content.split(" ")))

def print_discord(printable):
  return(printable)

green_flag = True

from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


def ai_check(x):
  if("?ai" in x):
    return True


def find_longest(words):
  try:
    words = words.split(" ")
  except:
    pass  
  w_len = []
  for w in words:
    w_len.append(len(list(w)))
  return words[np.argmax(w_len)]  




def combine(sentlist):
  combined_search = []
  for x in range(sentlist):
    combined_search.append(find_longest(sentlist))





def compare(a,b):
  lista = a.split(" ")
  listb = b.split(" ")
  return len(list(set(lista).intersection(listb)))

def compare_v2(a,b):
  l1 = a.split(" ")
  l2 = b.split(" ")
  l3 = [x for x in l1 if x not in l2]
  return " ".join(l3)


def command_check(m, x):
  for i in x:
    if m.lower().startswith(i):
      return True  

def a_sim(user_c,real_c):
  return AI_sim.sim(" ".join(list(user_c))," ".join(list(real_c)))
  
def get_max_a(inp,input_):
  sims = []
  for x in range(len(input_)):
    sims.append(a_sim(inp,input_[x]))
  out = np.argmax(sims)
  out = input_[out]  
  return out

commands = [
  "?reddit",
  "?showerthought",
  "?meme",
  "?copypasta",
  "?joke",
  "?ask",
  "?rsearch",
  "?recommend",
  "?cat",
  "?chat",
  "?teach",
  "?8ball",
  "?rolldice",
  "?say",
  "?credits",
  "?commands",
  "?whensaid",
  "?wastetime",
  "?rate",
  "?google",
  "?topics",
  "?youtube"
]

command_desc = [
  "Gets a random post from a certain subreddit",
  "Gets a showerthought from r/showerthoughts",
  "Gets a meme from r/dankmemes",
  "Gets a copypasta from r/copypastae",
  "Gets a joke from r/jokes",
  "Artificial Intelligence interface with Reddit to ask questions and get a _hopefully_ proper answer. Very slow, wouldn't recommend using",
  "Search Reddit for a certain term",
  "Recommend a reddit post or youtube video based upon the ongoing conversation using Artificial Intelligence and another weird algorithm",
  "Get a picture of a cat!",
  "Chat with the community taught chat module",
  "Teach the community taught chat module using `?teach <similar_input> | <output> (deletes all responses within one day)",
  "Literally shakes an 8ball doesn't use AI as much as it seems.",
  "Rolls a dice.",
  "Make the bot say stuff",
  "If you're interested in the bot's contributors, probably not though",
  "Displays this message",
  "If user says x the bot should say y:?whensaid x|y",
  "Waste someones time by making a spoiler filled message using ?wastetime <message>, they could of course just copy paste it but as I've noticed, people aren't that smart",
  "Literally rates you by finding the cosine similarity of your nickname with whadk#4346",
  "Experimental command, coming soon",
  "What were you just talking about? Find out! This is more of a testing command using the algorithm used for recommendations",
  "Does this thing work? No? Ok."

]
def autocorrect(command_s):
  try:
    command_l = command_s.split(" ")
  except:
    command_l = [command_s]
  for x in range(len(command_l)):
    if(command_l[x-1] in commands or "?" not in command_l[x-1]):
      pass
    else:
      command_s = command_s.replace(command_l[x-1],get_max_a(command_l[x-1],commands))
  return command_s      


def com(sentences):
  ret = []
  for sen in sentences:
    ret.append(find_longest(sen))
  return " ".join(ret)
    
  
potential_users = []
messages = []
@client.event
async def on_message(message):   
    print(message.content)
    print(message.author)
    print(message.channel)
    if(message.author not in potential_users):
      potential_users.append(message.author)
    if(message.content.startswith("?")):
      u_command = message.content
    else:
      if(message.channel not in rec_memory):
        rec_memory[message.channel] = [message.content]
      else:        
        rec_memory[message.channel].append(message.content)
    input_ = []
    output_ = []
    for x in range(len(messages)):
      input_.append(messages[x-1])
      output_.append(messages[x])

    if("what" in message.content or "why" in message.content or "is" in message.content or "how" in message.content):
      await message.channel.send(youtube.search_tube(message.content))
      
    if (message.content.startswith("?")):
      if("?chat" in message.content):
        messages.append(message.content.replace("?chat",""))
      else:  
        pass
    else:
      messages.append(message.content)      
    
    if message.content in onsimilar_i:
      await message.channel.send(onsimilar_o[onsimilar_i.index(message.content)])
    if message.content.startswith("?")  and any(x in message.content.split(" ") for x in commands) is not True:
      u_command = autocorrect(message.content)
      await message.channel.send("I think you meant `" + u_command+"`")
    else:
      u_command = message.content  
    if message.content.split(" ")[0] in commands:
      if(str(message.author) in users):
        pass
      else:
        write_user(message.author)  

    if message.author != client.user and "?say" == u_command.split(" ")[0]:  
      await message.channel.send( u_command[5:])    
      await client.delete_message(message)
      pass
  


    if message.author != client.user and u_command == ("?eightball") or u_command == ("?8ball") or ai_check(u_command) == True and AI_sim.sim("shake an eightball",u_command) > 0.5:  
      embed = discord.Embed(title="Ok, shaking an eightball",description="eightball result: "+random.choice(eightball)+"." ,color=int("00a2e8",16))
      var_a = False
      await message.channel.send(embed=embed)

    if message.author != client.user and "?wastetime"  in u_command: 
      text = u_command.replace("?wastetime ","")

      embed = discord.Embed(title="Look you can now waste someone's time with this:",description = "`||" + "||||".join(list(text)) + "||`",color=int("00a2e8",16))
      var_a = False
      await message.channel.send(embed=embed) 

    if message.author != client.user and u_command == ("?rate"):
      embed = discord.Embed(title="Here's my rating:",description="I rate you {}/10.".format(a_sim(str(message.author),"whadk#4346")*10) ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)    

    if message.author != client.user and "?tagrate" in u_command:
      to_rate = "yeet"
      embed = discord.Embed(title="Here's my rating:",description="I rate {0} {1}/10.".format(a_sim(str(message.author),"whadk#4346")*10) ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)    

    if message.author != client.user and u_command == ("?rolldice")or ai_check(u_command) == True and AI_sim.sim("roll a dice",u_command) > 0.5:
      embed = discord.Embed(title="Ok, rolling a dice:",description="Dice roll result: "+str(random.randint(1,6))+"." ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)

    if message.author != client.user and u_command == ("?recommend"):
      embed = discord.Embed(title="Here's my recommendation for this discussion",description="Result: "+search_reddit(AI_lda.find_topics(rec_memory[message.channel]))+"." ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)

    if message.author != client.user and u_command == ("?topics"):
      embed = discord.Embed(title="I picked out the following topics from the conversation",description="Result: "+AI_lda.find_topics(rec_memory[message.channel])+"." ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)


    if message.author != client.user and "?whensaid" in u_command:
      io = u_command.replace("?whensaid ","")
      i = io.split("|")[0]
      o = io.split("|")[1]
      onsimilar_i.append(i)
      onsimilar_o.append(o)
      embed = discord.Embed(title="Alright, thats *temporarily* been set so now you can have some fun.",description="When user says: "+i+" I say "+o+"." ,color=int("00a2e8",16))
      var_a = False      
      await message.channel.send(embed=embed)


    if message.author != client.user and u_command == ("?servercount") or ai_check(u_command) == True and AI_sim.sim("how many servers are you on",u_command) > 0.5:
      servers = list(client.guilds)
      description="Connected on " + str(len(servers)) + " servers. " 
      for x in range(len(servers)):
        print(' '+servers[x-1].name)
      var_a = False       
      await message.channel.send(description)

    if u_command == ("?commands"):
      embed = discord.Embed(title="Literally all {} commands:".format(len(commands)), colour=discord.Colour(0x4a90e2))
      embed.set_footer(text="Made by whadk with help from the whybot team", icon_url="https://avatars1.githubusercontent.com/u/38283382?s=460&v=4")
      for x in range(len(commands)):
        embed.add_field(name="`"+commands[x]+"`", value=command_desc[x], inline=True)
      await message.channel.send( embed = embed)

    if message.author != client.user and u_command == ("?coinflip")or ai_check(u_command) == True and AI_sim.sim("flip a coin",u_command) > 0.5:
      coinsides=["heads","tails"]  
      embed = discord.Embed(title="Coin flip",description="Result: " + random.choice(coinsides),color=int("00a2e8",16))
      var_a = False       
      await message.channel.send(embed=embed)
    
    if message.author != client.user and u_command == ("?credits"):
      embed= discord.Embed(title="Credits: `People who contributed to me` Thank you!" , description = "The whybot team: `Aditya Khanna, Keshan Kandeepan, Elmo Jebaharan, Surush Ghosh, Minojh Malawwa-Thanisegaran`",color=int("00a2e8",16))
      await message.channel.send(embed=embed)

    if message.author != client.user and u_command == ("?cat") or ai_check(u_command) == True and AI_sim.sim("show a picture of a cat",u_command)>0.5:
      var_a = False 
      await message.channel.send(get_random_post("cutecats"))
      pass

  
      
    if message.author != client.user and u_command == ("?rap_sw") :
      startWord = u_command[8:]
      init_get()
      process_text()
      rap = generate_text(150)  
      await message.channel.send("Alright, here it is: " + makeRap(startWord, rapprob_d)) 

    if message.author != client.user and u_command == ("?rap"):
      startWord = u_command[5:]
      init_get()
      process_text()
      rap = generate_text(150)  
      var_a = False       
      await message.channel.send("Alright, here it is: "+abc)# + makeRap(startWord, rapProbDict))
  
    if message.author != client.user and u_command == ("?dog")or ai_check(u_command) == True and AI_sim.sim("show a picture of a dog",u_command)>0.5:
      var_a = False       
      await message.channel.send(await message.channel.send(get_random_post("dogs")))

    if message.author != client.user and u_command == ("?meme"):
      tps = get_random_tps("dankmemes")
      embed= discord.Embed(title=tps[2],color=int("00a2e8",16))
      img =tps[0]
      embed.set_image(url=img)
      await message.channel.send(embed=embed)

    if message.author != client.user and  ai_check(u_command) == True and AI_sim.sim("show me a post from ",u_command)>0.3:
      if("r/" not in u_command):
        await message.channel.send("You need to specify a subreddit using r/<subreddit> if you want some posts from there.")
      else:
        await message.channel.send(get_random_post(extract_sub(u_command)))  


             
    if message.author != client.user and u_command == ("_code_"):
      embed= discord.Embed(title="_code_" , description = "```518413161813245963```",color=int("00a2e8",16))
      await message.channel.send(embed=embed)

  

    if message.author != client.user and len(u_command.split(" "))>300:      
      embed= discord.Embed(title="Spam message detected..." , description = "You repeated the word `"+str(word_occurence(u_command)) + "` times",color=int("00a2e8",16))
      await message.channel.send(embed=embed)


    if message.author != client.user and u_command == ("?kick"):
      try:
        player_name = u_command[5:].strip()
        msg = player_name[2:]
        msg = msg[:-1]
        await client.kick(message.server.get_member(msg))
        await message.channel.send( "`kicked` {}.".format(player_name))
      except AttributeError:
        await message.channel.send( "ERROR:`Something went wrong but I don't know what`")  
      except:
        await message.channel.send( "ERROR:`Could not kick `{}` because either you or I don't have the kick members role`".format(player_name))

    if message.author != client.user and u_command == ("?ban"):
     if message.author.server_permissions.ban_members:
      try:
        player_name = u_command[5:].strip()
        msg = player_name[2:]
        msg = msg[:-1]
        await client.ban(message.server.get_member(msg))
        await message.channel.send( "banned {}".format(player_name))
      except AttributeError:
        await message.channel.send( "ERROR:`Something went wrong but I don't know what`")  
      except:
        await message.channel.send( "ERROR:`Could not ban {} because either you or I don't have the ban members role`".format(player_name))
    if message.author != client.user and u_command == ("?teach"):
      io=u_command[6:].split("|")
      input_ = io[0]
      output = io[1]
      add_input(input_,output)  
      embed = discord.Embed(title="Added "+output+" as a response to "+input_,description="Thanks for teaching me!",color=int("00a2e8",16))
      await message.channel.send(embed=embed)    

    if message.author != client.user and u_command == ("?compatibility"):
      io=u_command[15:].split("|")
      
      person1 = " ".join(io[0])
      person2 = " ".join(io[1])
      await message.channel.send("{0} has a compatibility of {1}% with {2}".format(io[0],AI_sim.sim(person1,person2)*100,io[1]))  

    if message.author != client.user and u_command == ("?hack"):
      playername = u_command[5:]
      t1 = time.perf_counter()
      msg = await message.channel.send( "Hacking: {}".format(playername))
      t2 = time.perf_counter()
      await message.channel.edit(msg,"Email address: {}@gmail.com \n Password: ******** \n")
      t3 = time.perf_counter()
      await message.channel.edit(msg,"Test scores: \n Maths: {0}% \n Science: {1}% \n English: {2}%".format(random.randint(1,100),random.randint(1,100),random.randint(1,100)))
    if str(message.author) == "whadk#4346" and "?chremove" in u_command:
      try:
         messages.remove(u_command[12:])
         await message.channel.send("I removed the message")   

      except: 
         await message.channel.send("It's not in the list, so I can't really remove it. Sorry.") 
    if str(message.author) == "whadk#4346" and u_command.startswith("?chlist"):
      try:
         await message.channel.send("Here it is: ```" + ", ".join(messages)+ "```")   

      except Exception as e: 
         await message.channel.send("Whoops: `" + str(e) + "`")

    if str(message.author) == "whadk#4346" and "?chrestart" in u_command:
        message_len = len(messages)
        messages.clear()
        await message.channel.send("Cleared "+str(message_len)+" messages.")  

    if str(message.author) != "whadk#4346" and u_command.startswith("?chrestart") or u_command.startswith("?chlist") or u_command.startswith("?chremove") :
        await message.channel.send("This is a private command for use only by the bot owner. Request @whadk#4346 for removals.")        


    if message.author != client.user and "?reddit" in u_command:
      if(r.subreddit(u_command[8:]).over18 == True):
        await message.channel.send("That subreddit may contain NSFW content. This bot does not support NSFW content, use Dank Memer instead.")
      else:
                 
        try:
          tps = get_random_tps(u_command[8:])
          if("i.redd.it" in tps[0]):
            embed= discord.Embed(title=tps[2],color=int("00a2e8",16))
            img =tps[0]
            embed.set_image(url=img)
            await message.channel.send(embed=embed)
          else:
            await message.channel.send(get_random_title(u_command[8:]))                 
        except:
          await message.channel.send("Seems like there's something wrong with that subreddit. Might be that its banned, nsfw, nonexistent or there just aren't many posts.")          

    if message.author != client.user and "?showerthought" in u_command:
      try:
        await message.channel.send(get_random_title("showerthoughts"))   
      except:
         await message.channel.send("Somethings wrong with me, sorry.")   



    if message.author != client.user and "?copypasta" in u_command:
        print("rec_copy")
        try:
          print("rec copypasta")
          await message.channel.send(get_random_content("copypasta"))   
        except Exception as e:
          await message.channel.send("Somethings wrong with me, sorry.")
          print(e)         

    if message.author != client.user and "?youtube" in u_command:
        try:
          await message.channel.send(youtube.search_tube(u_command.replace("?youtube","")))   
        except Exception as e:
          await message.channel.send("Somethings wrong with me, sorry. This has been logged by the way so you aren't gonna go ignored.")
          print(e)         



  
    if message.author != client.user and "?joke" in u_command:
      joke = get_random_joke()
      try:
        await message.channel.send(joke[0])
        await message.channel.send("|| {} ||".format(joke[1]))   
      except Exception as e:
         await message.channel.send("Somethings wrong with me, sorry." + str(e))        
    if message.author != client.user and "?rsearch" in u_command:
        await message.channel.send(search_reddit(u_command[8:]))   


    if message.author != client.user and "?ask" in u_command:
      try:
        await message.channel.send(ask_reddit(u_command[4:]))   
      except Exception as e:
        await message.channel.send("Seems like there's something wrong with that ask query. Might be that its nsfw, vague or there just aren't many posts.")              
        print(e)        
    if (message.author != client.user and u_command.startswith("?chat")):
        print(message.author)
        try: 
          await chatbot.chat(u_command)
        except Exception as e:
          await message.channel.send(random.choice(messages)) 
          print(e)      

    if (message.author != client.user and u_command.startswith("?teach")):
        tot = u_command.replace("?teach","")
        totmin = tot.split("|")
        i = totmin[0]
        o = totmin[1]
        try: 
          input_.append(i)
          output_.append(o)
        except Exception as e:
          await message.channel.send(random.choice(messages)) 
          print(e)      



keep_alive()
token = "NTE4NDEzMTYxODEzMjQ1OTYz.XYU3EQ.GJfO5QIfxng7mWdc5l1IsvgibXQ"
client.run(token)


