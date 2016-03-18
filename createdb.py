# creates db for SDV-Summary
import config

database_structure_dict = {'md5':'TEXT',
'url':'TEXT',
'isMale':'TEXT',
'pantsColor0':'BIGINT',
'pantsColor1':'BIGINT',
'pantsColor2':'BIGINT',
'pantsColor3':'BIGINT',
'combatLevel':'BIGINT',
'maxHealth':'BIGINT',
'hair':'BIGINT',
'favoriteThing':'TEXT',
'maxItems':'BIGINT',
'skin':'BIGINT',
'friendshipsWilly':'BIGINT',
'friendshipsClint':'BIGINT',
'friendshipsJodi':'BIGINT',
'friendshipsHarvey':'BIGINT',
'friendshipsLeah':'BIGINT',
'friendshipsWizard':'BIGINT',
'friendshipsJas':'BIGINT',
'friendshipsAbigail':'BIGINT',
'friendshipsMaru':'BIGINT',
'friendshipsElliott':'BIGINT',
'friendshipsCaroline':'BIGINT',
'friendshipsPam':'BIGINT',
'friendshipsDwarf':'BIGINT',
'friendshipsShane':'BIGINT',
'friendshipsDemetrius':'BIGINT',
'friendshipsAlex':'BIGINT',
'friendshipsGus':'BIGINT',
'friendshipsVincent':'BIGINT',
'friendshipsSebastian':'BIGINT',
'friendshipsRobin':'BIGINT',
'friendshipsSam':'BIGINT',
'friendshipsLewis':'BIGINT',
'friendshipsMarnie':'BIGINT',
'friendshipsPenny':'BIGINT',
'friendshipsHaley':'BIGINT',
'friendshipsPierre':'BIGINT',
'friendshipsEvelyn':'BIGINT',
'friendshipsLinus':'BIGINT',
'friendshipsGeorge':'BIGINT',
'friendshipsEmily':'BIGINT',
'friendshipsKent':'BIGINT',
'friendshipsKrobus':'BIGINT',
'friendshipsSandy':'BIGINT',
# 'friendshipsBouncer':'BIGINT',
# 'friendshipsGil':'BIGINT',
# 'friendshipsGovernor':'BIGINT',
# 'friendshipsGrandpa':'BIGINT',
# 'friendshipsGunther':'BIGINT',
# 'friendshipsMarlon':'BIGINT',
# 'friendshipsMorris':'BIGINT',
# 'friendshipsMr_Qi':'BIGINT',
'farmingLevel':'BIGINT',
'statsRocksCrushed':'BIGINT',
'statsDaysPlayed':'BIGINT',
'statsStepsTaken':'BIGINT',
'statsSpecificMonstersKilledFly':'BIGINT',
'statsSpecificMonstersKilledGhost':'BIGINT',
'statsSpecificMonstersKilledBat':'BIGINT',
'statsSpecificMonstersKilledSkeleton':'BIGINT',
'statsSpecificMonstersKilledGrub':'BIGINT',
'statsSpecificMonstersKilledDust_Spirit':'BIGINT',
'statsSpecificMonstersKilledStone_Golem':'BIGINT',
'statsSpecificMonstersKilledFrost_Bat':'BIGINT',
'statsSpecificMonstersKilledDuggy':'BIGINT',
'statsSpecificMonstersKilledRock_Crab':'BIGINT',
'statsSpecificMonstersKilledBig_Slime':'BIGINT',
'statsSpecificMonstersKilledSludge':'BIGINT',
'statsSpecificMonstersKilledFrost_Jelly':'BIGINT',
'statsSpecificMonstersKilledBug':'BIGINT',
'statsSpecificMonstersKilledGreen_Slime':'BIGINT',
'statsSpecificMonstersKilledLava_Crab':'BIGINT',
'statsSpecificMonstersKilledLava_Bat':'BIGINT',
'statsSpecificMonstersKilledMetal_Head':'BIGINT',
'statsSpecificMonstersKilledShadow_Brute':'BIGINT',
'statsSpecificMonstersKilledShadow_Shaman':'BIGINT',
'statsSpecificMonstersKilledMummy':'BIGINT',
'statsSpecificMonstersKilledSerpent':'BIGINT',
'statsSpecificMonstersKilledArmored_Bug':'BIGINT',
'statsSpecificMonstersKilledVoid_Spirit':'BIGINT',
'statsSpecificMonstersKilledSquid_Kid':'BIGINT',
'statsSpecificMonstersKilledPurple_Slime':'BIGINT',
'statsSpecificMonstersKilledRed_Slime':'BIGINT',
'statsSpecificMonstersKilledTransparent_Slime':'BIGINT',
'statsSlimesKilled':'BIGINT',
'statsPreservesMade':'BIGINT',
'statsGeodesCracked':'BIGINT',
'statsSeedsSown':'BIGINT',
'statsNotesFound':'BIGINT',
'statsMonstersKilled':'BIGINT',
'statsStumpsChopped':'BIGINT',
'statsCropsShipped':'BIGINT',
'statsCowMilkProduced':'BIGINT',
'statsFishCaught':'BIGINT',
'statsPiecesOfTrashRecycled':'BIGINT',
'statsTrufflesFound':'BIGINT',
'statsIridiumFound':'BIGINT',
'statsTimesFished':'BIGINT',
'statsStarLevelCropsShipped':'BIGINT',
'statsCopperFound':'BIGINT',
'statsBarsSmelted':'BIGINT',
'statsBouldersCracked':'BIGINT',
'statsCoinsFound':'BIGINT',
'statsCaveCarrotsFound':'BIGINT',
'statsStoneGathered':'BIGINT',
'statsQuestsCompleted':'BIGINT',
'statsGoatMilkProduced':'BIGINT',
'statsCoalFound':'BIGINT',
'statsIronFound':'BIGINT',
'statsCheeseMade':'BIGINT',
'statsItemsCooked':'BIGINT',
'statsWeedsEliminated':'BIGINT',
'statsTimesUnconscious':'BIGINT',
'statsChickenEggsLayed':'BIGINT',
'statsSheepWoolProduced':'BIGINT',
'statsDiamondsFound':'BIGINT',
'statsRabbitWoolProduced':'BIGINT',
'statsAverageBedtime':'BIGINT',
'statsBeveragesMade':'BIGINT',
'statsOtherPreciousGemsFound':'BIGINT',
'statsDuckEggsLayed':'BIGINT',
'statsItemsCrafted':'BIGINT',
'statsGiftsGiven':'BIGINT',
'statsSticksChopped':'BIGINT',
'statsPrismaticShardsFound':'BIGINT',
'statsDirtHoed':'BIGINT',
'statsGoldFound':'BIGINT',
'statsMysticStonesCrushed':'BIGINT',
'statsItemsShipped':'BIGINT',
'statsGoatCheeseMade':'BIGINT',
'shirt':'BIGINT',
'uniqueIDForThisGame':'BIGINT',
'miningLevel':'BIGINT',
'facialHair':'BIGINT',
'money':'BIGINT',
'newEyeColor0':'BIGINT',
'newEyeColor1':'BIGINT',
'newEyeColor2':'BIGINT',
'newEyeColor3':'BIGINT',
'maxStamina':'BIGINT',
'farmName':'TEXT',
'foragingLevel':'BIGINT',
'fishingLevel':'BIGINT',
'deepestMineLevel':'BIGINT',
'accessory':'BIGINT',
'catPerson':'TEXT',
'totalMoneyEarned':'BIGINT',
'millisecondsPlayed':'BIGINT',
'hairstyleColor0':'BIGINT',
'hairstyleColor1':'BIGINT',
'hairstyleColor2':'BIGINT',
'hairstyleColor3':'BIGINT',
'name':'TEXT',
'professions0':'TEXT',
'professions1':'TEXT',
'professions2':'TEXT',
'professions3':'TEXT',
'professions4':'TEXT',
'professions5':'TEXT',
'professions6':'TEXT',
'professions7':'TEXT',
'professions8':'TEXT',
'professions9':'TEXT',
'farm_info':'TEXT',
'farm_url':'TEXT',
'avatar_url':'TEXT',
'added_time':'FLOAT',
'ip':'TEXT',
'del_token':'BIGINT',
'views':'BIGINT',
'date':'TEXT',
'savefileLocation':'TEXT',
'petName':'TEXT',
'portrait_info':'JSON',
'portrait_url': 'TEXT'}

if config.USE_SQLITE==True:
	database_structure_dict['id']='INTEGER PRIMARY KEY AUTOINCREMENT'
	sqlesc = '?'
	idcode='INTEGER PRIMARY KEY AUTOINCREMENT'
else:
	sqlesc = '%s'
	idcode='SERIAL PRIMARY KEY'
	database_structure_dict['id']='SERIAL PRIMARY KEY'

database_fields = ''
for key in sorted(database_structure_dict.keys()):
	database_fields+=key+','
database_fields = database_fields[:-1]

def connect_db():
	if config.USE_SQLITE == True:
		import sqlite3
		connection = sqlite3.connect(config.DB_SQLITE)
	else:
		import psycopg2
		connection = psycopg2.connect('dbname='+config.DB_NAME+' user='+config.DB_USER+' password='+config.DB_PASSWORD)
	return connection

def generate_db():
	database_structure = ''
	for key in sorted(database_structure_dict.keys()):
		database_structure += key + ' ' +database_structure_dict[key] + ',\n'
	database_structure = database_structure[:-2]

	errors_structure = 'id '+idcode+', ip TEXT, time BIGINT, notes TEXT'
	todo_structure = 'id '+idcode+', task TEXT, playerid TEXT'

	connection = connect_db()
	c = connection.cursor()
	c.execute('CREATE TABLE playerinfo('+database_structure+')')
	c.execute('CREATE TABLE errors('+errors_structure+')')
	c.execute('CREATE TABLE todo('+todo_structure+')')
	connection.commit()
	print('done')

def generate_blog():
	connection=connect_db()
	c = connection.cursor()
	statement = 'CREATE TABLE blog(id '+idcode+', time BIGINT, author TEXT, title TEXT, post TEXT, live BOOLEAN);'
	c.execute(statement)
	connection.commit()
	connection.close()
	print('done')

def delete_db():
	import getpass
	from werkzeug import check_password_hash
	connection = connect_db()
	c = connection.cursor()
	print('you must log in as admin to delete the database')
	username = input('username: ')
	password = getpass.getpass('password: ')
	c.execute('SELECT password FROM admin WHERE username='+sqlesc,(username,))
	passhash = c.fetchone()
	if check_password_hash(passhash[0],password) == True:
		a = input('just to double check, you REALLY want to delete everything? (y/n): ')
		if a=='y':
			c.execute('DROP TABLE playerinfo')
			c.execute('DROP TABLE errors')
			c.execute('DROP TABLE todo')
			c.execute('DROP TABLE blog')
			connection.commit()
			connection.close()
			print('all (except admin) deleted')
	else:
		print('incorrect credentials')

if __name__ == "__main__":
	a = input('Drop databases? (y/n): ')
	if a == 'y':
		delete_db()
	a = input('Generate databases? (y/n): ')
	if a == 'y':
		generate_db()
	a = input('Generate blog database? (y/n): ')
	if a == 'y':
		generate_blog()

