import time

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "What do you mean 3?"
	time.sleep(4)
	print "Well, I guess maybe just this one time..."
	print"""
LET'S RIDE!
                           ____          ____
                          / --.|        |.-- \
                         /,---||        ||---.\
                        //    ||        ||    \\
                       //     ||        ||     \\
                      // __   ||        ||   __ \\
                     //,'  `. ||        || ,'||`.\\
                    //( \`--|)||        ||( \'|  )\\
                   //  `.-_,' ||________|| `.-_,'  \\
                  //        | ||   _|   ||          \\
                 //         | || | .. | ||           \\
                //          | || | :: | ||            \\
               /    __     888|| |  _ | ||        __    \
              /   ,'|_'. _ 888|| |  | | ||  _   ,'-.`.   \
             /   ( ,-._ | |888|| | -| | || |_| (   |==)   \
            /     `O__,'|_|8@ || | [| | |@ |_|  `._|,'     \
           /            __..|--| | )| | |--|_|__            \           ,==.
          /      __,--''      |  |  | |  |      ``--.__      \         //[]\\
         /    ,::::'          |-=|  | |  |::::..       `-.    \       //||||\\
        /  ,-':::::       ..::|  | /| |  |::::::::        `-.  \     ||,'  `.||
       / ,'    ''       ::::::|  | \| |  |  ''::::     oo    `. \    |--------|
      /,'           ,'\ :::'''|] |  | |  |   ....    o8888o    `.\   |:::_[[[[]
     /'           ,'   )      |> |  | | [|  ::::::     88888  ..  \  |    |   ]
    /           ,'     |      |] |=_| | [|  '::::'oo     8   ::::  \-'    |---|
   .'     o   ,'    \_/       | :| \| |.[|      o8888o        ::;-'      ,'   |
  ,'     o88,'   `._/:\|      | :|  | |: |     88888888      ,-'  \  _,-'     |
  |     8888 ``--'|::::|      |_:|  | |:_|       8888     ,-'   \ ,-'   .::_,-'
 ,'    8888      ''--""      || || [| || ||            ,-'    _,-'   \ _::'
 |                           || |_,--._| ||         ,-'  \ ,-'     _,-'
 |                           |__(______)__|      ,-'   _,-' .::_,-'   |
|'                  88o     =====,,--..=====  .-'   ,-' \  _::'       `|
|                  888888o    ,-'\    /`-.     \ \-' . _,-'            |
`---._____        888888888 ,' / [HHHH[=====-   \ |_::'       _____.---'
  __|_____`=======._____   /   \ [HHHH[=====-    `'__.======='_____|__
 {I |  _______________ || /    /\/____\/\:.  \ || _______________  | I}
 [I |  :___]__[_______ ||(    /   _.._   \:.  )|| ______]___[___:  | I]
 {I_|____________o8o___|| \  /:  /\  /\   \: / ||__________________|_I}
    |_____,------'         \/:'  \ \/ /    \/:..   88`-------._____|
.---'   ::::::              `.   [||||]   ,'  '::..                `---.
|          '::..::        ,'  `-.      ,-'  `.  ':'                    |
|.        .:::''        ,' __    ``--''    __ `.     .::.             ,|
 |        '''         ,' ,'||`.    __    ,'||`. `.    '::::.          |
 |                  ,'  (||||||) ,'||`. (||||||) 88.    '::::.        |
 `.               ,'     `.||,' (||||||) `.||,' 88888.    ':'        ,'
  |             ,'      __       `.||,'       __  88  `.             |
  `.          ,'      ,'||`.       __       ,'||`.      `.          ,'
   `.       ,'       (||||||)    ,'||`.    (||||||)       `.       ,'
     \    ,'          `.||,'    (||||||)    `.||,'          `.    /
      `.  |                      `.||,'                      |  ,'
        `-|                                                  |-'
          `.   ,'.                                    .`.   ,'
            `-:,'o88o ,/                        \.     `.;-'
               `-888 //      /     ||ooo  \ oo88 \\ __,-'
                    `--..__ /'     ||888  `\ oo8;--'
                           ```-----''-----''''
"""

else:
	print "You stumble around and fall on a knife and die. Good job!"