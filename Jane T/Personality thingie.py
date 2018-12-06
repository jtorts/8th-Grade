import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

sport = pg.prompt("What sport do you like to play?")
if sport == "Field hockey":
    wb.open("https://www.google.com/search?q=field+hockey&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjO5Lf2z6HeAhVtmuAKHYeTDGAQ_AUIDigB&biw=924&bih=639#imgrc=FCpGZY2CS5KVXM:")
    t.sleep(3)
    pg.alert("That is a lot of running!")
    points += 5
elif sport == "tennis":
    wb.open ("https://www.youtube.com/watch?v=2wAkfLneYEY")
    t.sleep(3)
    pg.alert("Tennis is fun")
    points += 3
elif sport == "Water polo":
    wb.open ("https://www.google.com/search?q=water+polo&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj2gpaMpLPeAhXSmeAKHQYuA40Q_AUIDygC&biw=681&bih=647#imgrc=nf-bFmIT1RGw6M:")
    t.sleep(3)
    pg.alert("Swimming is great exercise!")
    points +=3
elif sport == "Lacrosse":
    wb.open("https://www.google.com/search?q=lacrosse&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj8obKjpLPeAhVPT98KHbqADRAQ_AUIDigB&biw=681&bih=647#imgrc=iFaNmTmaK9oWjM:")
    t.sleep(3)
    pg.alert("Lacrosse is so fun to watch!")
    points -= 1
elif sport == "Soccer":
    t.sleep(3)
    pg.alert("The World Cup is so cool!")
    points -= 1
elif sport == "Chess":
    wb.open("https://www.google.com/search?q=someone+playing+chess&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjKrJ_apLPeAhWEdt8KHSWvC6MQ_AUIDigB&biw=681&bih=647#imgrc=O1CW1YA_wybvnM:")
    t.sleep(3)
    pg.alert ("Chess isn't a sport!")
    points -= 18
else:
    pg.alert("you enjoy playing " + sport)
          
show = pg.prompt("What show do you like to watch?")
if show == "The Office":
    wb.open("https://www.youtube.com/watch?v=-9HORvD2IHc")
    t.sleep(3)
    pg.alert ("Bears. Beets. Battlestar Galactica.")
    points += 8
elif show == "Riverdale":
    wb.open("https://www.google.com/search?q=riverdale&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwix3uGwpbPeAhWBc98KHRrIB0cQ_AUIDygC&biw=681&bih=647#imgrc=g2a2GR1w1MP9zM:")
    t.sleep(3)
    pg.alert("That is a bad show.")
    points -= 3
elif show == "Gossip girl":
    wb.open("https://www.google.com/search?q=gossip+girl&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiBj9vIpbPeAhWJTt8KHfvvDPoQ_AUIDygC&biw=681&bih=647")
    t.sleep(3)
    pg.alert("That show is so interesting!")
    points += 3
elif show == "Cupcake Wars":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=681&bih=647&tbm=isch&sa=1&ei=uP7aW8SyBq6Jggfp34bwDw&q=cupcakes&oq=cupcakes&gs_l=img.3..0j0i67j0l4j0i67j0l3.47634.49447..49584...0.0..0.64.451.8......0....1..gws-wiz-img.t7bpHurS-q4#imgrc=p4LLDQlWokvGkM:")
    t.sleep(3)
    pg.alert("Cupcakes are delicious!")
    points -= 1
elif show == "Friends":
    wb.open("https://www.google.com/search?q=friends&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwix4aD_pbPeAhXlmeAKHVKgAY8Q_AUIDygC&biw=681&bih=647#imgrc=mFNg1ac3_9uhaM:")
    t.sleep(3)
    pg.alert("They are so funny!")
    points += 1

else:
    pg.alert("You enjoy watching " + show)


food = pg.prompt("What is your favorite food?")
if food == "Pasta":
    wb.open("https://www.youtube.com/watch?v=NHiqsrYkcuk")
    t.sleep(3)
    pg.alert ("Pasta is super good.")
    points += 7
elif  food == "Fish":
    wb.open("https://www.youtube.com/watch?v=cC9r0jHF-Fw")
    t.sleep(3)
    pg.alert("Fish is gross.")
    points -=19 
elif food == "Pizza":
    wb.open("https://www.google.com/search?q=pizza&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi0keXTprPeAhWCTd8KHf5DA4UQ_AUIDygC&biw=681&bih=647")
    t.sleep(3)
    pg.alert("There's a great pizza place in Greenwich.")
    points += 5         
elif food == "apple":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&tbm=isch&q=apple&chips=q:apple,g_1:red:6q6ORDK0ROQ%3D&usg=AI4_-kTH3WuydNxwI95A7juqz51FEDwEtw&sa=X&ved=0ahUKEwi4r5jlprPeAhUMVd8KHavkBmAQ4lYILSgD&biw=681&bih=647&dpr=1#imgrc=ONmY3cE3dCIUEM:")
    t.sleep(3)
    pg.alert("That's so healthy!")
    points += 1
elif food == "vegatables":
    wb.open("https://www.google.com/search?q=vegetables&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiVyeHzprPeAhUEUt8KHcwKBkYQ_AUIDigB&biw=681&bih=647#imgrc=8Iu8nndFUI9q3M:")
    t.sleep(3)
    pg.alert("Brocoli!")
    points -= 4
elif food == "lemonade":
    wb.open("https://www.google.com/search?q=lemonade&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiCwtuCp7PeAhUFU98KHbz9AaUQ_AUIDigB&biw=681&bih=647#imgrc=7XZL9n64Jm__VM:")
    t.sleep(3)
    pg.alert("Lemonade is so good!")
    points += 7
else:
    pg.alert("You enjoy eating " + food)


color = pg.prompt("What is your favorite color?")
if color == "Green":
    wb.open("https://www.google.com/search?q=green&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwisjKqTp7PeAhVhQt8KHQgQDIEQ_AUIDigB&biw=681&bih=647")
    t.sleep(3)
    pg.alert("Green is a pretty color!")
    points -= 3
elif color == "blue":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=681&bih=647&tbm=isch&sa=1&ei=eQDbW4OTIoyd_QafiIngDw&q=blue+people&oq=blue+people&gs_l=img.3..0l10.5604.5604..5800...0.0..0.63.63.1......0....1..gws-wiz-img.4MhxKHjfKAs#imgrc=hyRApwWwlTRWBM:")
    t.sleep(3)
    pg.alert("The color of the ocean is so pretty!")
    points += 6
elif color == "Purple":
    wb.open("https://www.google.com/search?q=purple&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiI5Jqwp7PeAhVFmuAKHeorAzkQ_AUIDigB&biw=681&bih=647#imgrc=hLGloeJ6n3RdHM:")
    t.sleep(3)
    pg.alert("I love purple flowers!")
    points += 2
elif color == "Red":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=681&bih=647&tbm=isch&sa=1&ei=wgDbW9LsNevn_Qbts6O4Ag&q=red+&oq=red+&gs_l=img.3..0i67l6j0l2j0i67l2.9306.9736..9983...0.0..0.65.240.4......0....1..gws-wiz-img.ue_XtvwYKLM#imgrc=9sW5vanh738I5M:")
    t.sleep(3)
    pg.alert("Red is so fun!")
    points -= 1
elif color == "Yellow":
    wb.open("https://www.google.com/search?q=artsy+yellow+backgrounds&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjA6urWp7PeAhXhg-AKHUc7AZEQ_AUIDigB&biw=681&bih=647#imgrc=HS7wogTp4TcJUM:")
    t.sleep(3)
    pg.alert("Yellow is a happy color!")
    points += 1
elif color == "orange":
    wb.open("https://www.google.com/search?q=artsy+yellow+backgrounds&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjA6urWp7PeAhXhg-AKHUc7AZEQ_AUIDigB&biw=681&bih=647#imgrc=HS7wogTp4TcJUM:")
    t.sleep(3)
    pg.alert("Orange is so pretty!")
    points += 1
else:
    pg.alert("You love the color" + color)


school = pg.prompt("What is your favorite class?")
if school == "History":
    wb.open("https://www.google.com/search?q=george+washington&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiu1safqLPeAhVlkuAKHe9kBOEQ_AUIDigB&biw=681&bih=647#imgrc=g8HmnlbFoJ-SBM:")
    t.sleep(3)
    pg.alert("Learning about the past is so cool!")
    points += 4
elif school == "english":
    wb.open("https://www.youtube.com/watch?v=GIYIUdy-KwQ")
    t.sleep(3)
    pg.alert("Reading is so fun!")
    points += 5
elif school == "Math":
    wb.open("https://www.youtube.com/watch?v=-wkr_vf18cw")
    t.sleep(3)
    pg.alert("Adding and subtracting is hard!")
    points -= 6
elif school == "science":
    wb.open("https://www.google.com/search?q=science&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi71tv0qLPeAhUkhuAKHfK6D4sQ_AUIDygC&biw=681&bih=647#imgrc=dBHnHydUCLy95M:")
    t.sleep(3)
    pg.alert("There are so many cool landforms in the United States!")
    points -= 3         
elif school == "Spanish":
    wb.open("https://www.google.com/search?q=spanish&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj60IWJqbPeAhUMTN8KHe2nBc8Q_AUIDigB&biw=681&bih=647#imgrc=F15aNSWqmtTzFM:")
    t.sleep(3)
    pg.alert("Hola!Como estas?")
    points += 3
elif school == "French":
    wb.open("https://www.google.com/search?q=french&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj66I-YqbPeAhXkg-AKHZpJB3cQ_AUIDigB&biw=681&bih=647#imgrc=jqvz6NWbE1C6iM:")
    t.sleep(3)
    pg.alert ("Bonjour!")
    points -= 5
else:
    pg.alert("you enjoy " + school)

pg.alert("You scored " + str(points)+"!")
    
