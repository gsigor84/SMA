import random


index=[]
n=0
for x in range(9):
    index.append(n)
    n=n+1

HASH=[
'#healthylife #healthcoach #fitnessjourney #healthynutrition #eatright #nutritioncoaching #nutrients #nutrtion #protein #nutritionist'
,'#salad #trick #fitnessfood #fitfood #fitfoodie #eatyourveggies #eatarainbow #fitmencook #nutrition #eatwell'
,'#mealprepdaily #hacklife #yummy #tipweekend #simplemillspartnerporridge #porridgepassion #foodblog #breakfast #foodieblog #healthyfood'
,'#plantbased #oats #soyamilk #healthyeating #plantprotein #veganprotein #veganbreakfast #proats #veganlife #healthybreakfast'
,'#foodstagram #veganfood #foodblogger #f52grams #veggielife #foodporn #nutritionist #oatmeal #porridgelover #foodie'
,'#peanutbutter #granolait #hannahharvestinghealth #glutenfree #choosingbalance #easyrecipes #healthybreakfastwedding #wovintogether #winniesbalancemiten'
,'#nutritionaltips #nutritionmyths #nutritionresearch #healthyeah #healthyeatingideas #healthyeat #healthyfoodideas #healthyideas #healthyfoodchoices #healthychoises'
,'#healthynutrition #healthyeatinghabits #nutritionmatters #nutritionaltherapy #nutritioncoaching #nutritions #nutritiongoals #nutritional #nutritiontips #healthyfoodchoice'
,'#healthyfoodlove #musclefood #fatlossjourney #macros #irishfitfam #deadlifting #healthylifestyle #gymmemes #nutritionfacts #fatlosstips'
,'#fatlosscoach #onlinecoach #personaltrainer #physiology #hypertrophy #weightlossideas #weightlossdiet #healthyme #flexibledieting #weightlossgoal'
,'#dietstartstomorrowDid #healthyfoodsharing #healthyfoodwithme #healthyfoodlifestyle #healthylifestylechange #healthytip #healthylive #healthylivingtips #healthylivingrevolution #healthychoicesmatter'
    ]
m=random.choice(index)
hashtag=HASH[m]
print(HASH[m])
