import pygame
from random import randint, uniform as randfloat
from time import time
import pickle

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set the width and height of the canvas
width = 800
height = 600

# Create the canvas
canvas = pygame.display.set_mode((width, height),pygame.NOFRAME)

#Font
Font = pygame.font.SysFont("Arial", 36)
TitleFont = pygame.font.SysFont("Arial", 72)
ButtonFont = pygame.font.SysFont("Arial", 48)
shopUIFont = pygame.font.SysFont("Arial", 56)
marketFishNameFont = pygame.font.SysFont("Arial", 48)
marketFishPropertiesFont = pygame.font.SysFont("Arial", 36)

#Colors
DarkBrown = (170,121,89)

#Player Animation Properties
PlayerFrame = 0
PlayerLook = 0
Right = 12
Left = 8
Up = 4
Down = 0
playerImages = []
for i in range(16):
    playerImages.append(pygame.transform.scale(pygame.image.load("Pictures/Player/ (" + str(i+1) + ").png"),(64,64)))

#Player Properties
playerX = 64
playerXX = 0
playerY = 64
playerYX = 0
lastCords = [0,0]
canPlay = True
canTravel = False
travelTime = time()
canFish = False
isFishing = False
moneyBalance = 0
currentFishingRod = "Hands"
currentBait = "None"
initLoad = True



#Fish Properties
commonFish = {'Goldfish':[0.1,5,0.05,2], 'Bluegill':[0.1,4.5,0.1,4], 'Perch':[0.1,6,0.2,5], 'Catfish':[1,220,0.2,0.5], 'Trout':[0.5,44,0.2,0.5], 'Carp':[0.1,88,0.1,0.5]} # max price = ~25
defaultCommonChance = 0
commonChance = defaultCommonChance
uncommonFish = {'Clownfish':[0.02,0.5,25,100], 'Tilapia':[1,10,2,5], 'Pufferfish':[1,30,1,4], 'Bass':[0.5,20,3,7.5], 'Snapper':[2,50,1,2], 'Mackerel':[0.5,7,8,15]} # max price = ~50
defaultUncommonChance = 70
uncommonChance = defaultUncommonChance  
rareFish = {'Lionfish':[0.5,2.6,50,100],'Angelfish':[0.1,4,10,60],'Mandarinfish':[0.03,0.2,500,1250],'Sturgeon':[10,1500,0.01,0.2],'Cobia':[5,135,1,2],'WolfFish':[1,88,2,4]} # max price = ~250
defaultRareChance = 85
rareChance = defaultRareChance
epicFish = {'Electric Eel': [2, 44, 5, 10], 'Giant Grouper': [10, 880, 0.3, 0.6], 'Golden Dorado': [5, 70, 1, 5], 'Tarpon': [10, 280, 1, 2], 'Arapaima': [22, 485, 0.5, 1.1], 'Opah (Moonfish)': [30, 600, 0.5, 1]} # max price = ~500
defaultEpicChance = 96
epicChance = defaultEpicChance
legendaryFish = {'Coelacanth': [40, 198, 1, 5], 'Arapaima Gigas': [22, 485, 1, 2], 'Atlantic Bluefin Tuna': [200, 1500, 0.5, 1], 'White Sturgeon': [50, 1799, 0.3, 0.75], 'Goliath Tigerfish': [20, 154, 3, 8], 'Alligator Gar': [10, 350, 1, 5]} # max price = ~1000
defaultLegendaryChance = 99.5
legendaryChance = defaultLegendaryChance
mythicalFish = {'Kraken Fish': [1000, 50000,0.1,0.2],'Leviathan': [10000, 200000,0.01,0.05],"Mermaid's Kiss": [200, 5000,1,2],'Dragonfish': [0.1, 1000,5,10],'Sea Serpent': [500, 100000,0.05,0.1],'Jormungandr': [50000, 500000,0.005,0.01]} # max price = ~10000
defaultMythicalChance = 99.9
mythicalChance = defaultMythicalChance
fishInventory = []

# Equitments Properties

fishingRods = {'Basic Bamboo Rod':[100,[10,5,1,0.5,0]],'Sturdy Wooden Rod':[500,[20,10,4,2.5,0.9]],'Fiberglass Rod':[2500,[30,15,9,5,2.9]],'Carbon Fiber Rod':[10000,[40,25,15,7.5,5]],'Professional Titanium Rod':[100000,[60,40,30,15,10]]}
fishingBaits = {'Worms':[100,[5,2.5,0.5,0.25,0]],'Bread Crumbs':[500,[10,5,2,1,0.5]],'Minnow':[2500,[15,7.5,4,2,1]],'Artificial Lure':[10000,[20,10,8,4,2.5]],'Magic Fish':[100000,[30,15,12,6,4]]}

#UI Properties
UIImages = []
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/background.png"),(512,512)))
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/X.png"),(32,32)))
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/arrowL.png"),(32,54)))
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/arrowR.png"),(32,54)))
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/fishUI.png"),(96,96)))
UIImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/buttonUp.png"),(140,86)))
UIImages.append(pygame.image.load("Pictures/UI/ProperitesUI.png"))
fishGridImages = []
fishGridImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/Fish/FishGrid.png"),(128,128)))
fishGridImages.append(pygame.transform.scale(pygame.image.load("Pictures/UI/Fish/NoFishGrid.png"),(128,128)))



#Map Images
grassBackgroundImages = []
for i in range(77):
    grassBackgroundImages.append(pygame.transform.scale(pygame.image.load("Pictures/Grass/tile (" + str(i+1) + ").png"),(64,64)))
grassBackgroundImages.append(pygame.transform.scale(pygame.image.load("Pictures/Grass/tile (78).png"),(128,32)))
for i in range(77):
    grassBackgroundImages.append(pygame.transform.scale(pygame.image.load("Pictures/Path/tile (" + str(i+1) + ").png"),(64,64)))
for i in range(35):
    grassBackgroundImages.append(pygame.transform.scale(pygame.image.load("Pictures/House/ (" + str(i+1) + ").png"),(64,64)))
for i in range(9):
    grassBackgroundImages.append(pygame.transform.scale(pygame.image.load("Pictures/House/House/ (" + str(i+1) + ").png"),(64,64)))
#[0] = to left corner, [1] = middle top, [2] = right corner,
#[11] = left mile,     [12] = middle,    [13] = right mile, 
#[22] = left bottom,   [23] = middle bottom, [24] = right bottom
#[77] = Water bacground 128x32
#-1 Tiles are no image, only collider
#Path Tiles are offset by 78
#House Interior Tiles are offset by 154
#House Tiles are offset by 190

#fishMap[x][y]'s value = image
fishMap = [[[],[11,89],[90],[13,91],[],[],[],[],[],[],[],[],[]],
        [[0 ],[28,89],[90],[27,91],[1 ],[2 ],[],[],[],[],[],[],[]],
        [[11],[12,89],[90],[12,91],[12],[13],[],[],[],[],[],[],[]],
        [[11],[12,89],[90],[12,91],[12],[13],[],[],[],[],[],[],[]],
        [[22],[17,89],[90],[55,91],[12],[13],[],[],[],[],[],[],[]],
        [[],[11,89],[90],[12,91],[12],[13],[],[],[],[],[],[],[]],
        [[1,79],[28,106],[90],[12,91],[12],[13],[],[],[],[],[],[],[]],
        [[90],[90],[90],[12,91],[12],[13],[],[],[],[],[],[],[]],
        [[23,101],[23,101],[23,101],[23,102],[23],[24],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[],[],[]]]

toolMap = [[[],[],[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[  ],[0 ],[1 ],[1 ],[1 ],[1 ],[1 ],[2 ],[],[],[]],
        [[],[],[0 ],[28],[12],[12],[12],[12,159],[12,160,-1],[27,161],[2 ],[],[]],
        [[],[],[11],[12,159],[-1,12,160],[12,161],[12],[12,173],[174],[12,175],[13],[],[]],
        [[],[],[11],[12,176,173],[174],[12,175],[-1,12],[12,176,187],[170,158,188],[12,178,189],[13],[],[]],
        [[],[],[11],[12,176,187],[170,158,188],[12,178,189],[12],[12,89],[90],[12,91],[13],[],[]],
        [[],[],[22],[17,89],[90],[12,105],[12,79],[12,106],[90],[12,105],[27,79],[1,79],[1,79]],
        [[],[],[],[22,100],[17,95],[90],[90],[90],[90],[90],[90],[90],[90]],
        [[],[],[],[],[22,100],[23,101],[23,101],[23,101],[23,101],[23,101],[23,101],[23,101],[23,101]],
        [[],[],[],[],[],[],[],[],[],[],[],[],[]]]

sellMap = [[[],[],[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[0 ],[1 ],[-1, 1],[1 ],[2 ],[],[]],
        [[],[],[],[],[],[],[11],[-1,12,190],[12,191],[-1,12,192],[13],[],[]],
        [[],[],[],[],[],[],[11],[-1,12,193],[12,194],[-1,12,195],[13],[],[]],
        [[],[],[],[],[],[],[11],[-1,12,196],[12,197],[-1,12,198],[13],[],[]],
        [[],[00,78],[1,79],[1,79],[1,79],[1,79],[28,79],[12,79],[12,108],[12,80],[13],[],[]],
        [[],[11,89],[90],[90],[90],[90],[90],[90],[90],[16,91],[24],[],[]],
        [[],[11,89],[90],[16,94],[23,101],[23,101],[23,101],[23,101],[23,101],[24,102],[],[],[]],
        [[],[11,89],[90],[13,91],[],[],[],[],[],[],[],[],[]]] 

#map properties
currentMap = fishMap
showStats = False

#Map Properties
cornerIndex = [0,1,2,11,13,22,23,24]
colliderIndex = [-1,161,162,163,168,175,176,177]
OverlapTiles = [159,160,161,166,167,168,173,174,175,180,181,182,187,188,189,190,191,192,193,194,195,196,198]
fastTravelCordsFishMap = {(2,0):[sellMap,[2,8,2]],(0,7):[toolMap,[11,7,1]]}
fastTravelCordsSellMap = {(2,8):[fishMap,[2,0,0]]}
fastTravelCordsToolMap = {(11,7):[fishMap,[0,7,0]]}
fastTravelDict = {0:fastTravelCordsFishMap, 2:fastTravelCordsSellMap, 1:fastTravelCordsToolMap}
fastTravelCords = fastTravelCordsFishMap

#/////////////Functions/////////////
#Render game
def renderGame() -> None:
    # draw the background 
    for i in range(0, 800, 128):
        for j in range(0, 600, 32):
            canvas.blit(grassBackgroundImages[77], (i, j))
            
    # draw the map
    yVal = 0
    for grassY in currentMap:
        xVal = 0
        for grassX in grassY:
            if grassX != []:
                for i in grassX:
                    if i not in OverlapTiles:
                        if i >= 0:
                            canvas.blit(grassBackgroundImages[i], (xVal*64, yVal*64))
            xVal += 1
        yVal += 1
    
    # draw the player
    canvas.blit(playerimage, (playerX, playerY))

    yVal = 0
    for grassY in currentMap:
        xVal = 0
        for grassX in grassY:
            if grassX != []:
                for i in grassX:
                    if i in OverlapTiles:
                        if i >= 0:
                            canvas.blit(grassBackgroundImages[i], (xVal*64, yVal*64))
            xVal += 1
        yVal += 1

    # draw fast travel prompt
    if canTravel:
        fontX = 0
        fontY = 0
        fontRender = Font.render("Press T to Fast Travel", 1, (255,255,255))
        if playerX-fontRender.get_width()/2 < 10:
            fontX = 10
        elif playerX+fontRender.get_width()/2 > 790:
            fontX = 790-fontRender.get_width()
        else:
            fontX = playerX-fontRender.get_width()/2
        if playerY-fontRender.get_height() < 10:
            fontY = 10
        elif playerY+fontRender.get_height() > 590:
            fontY = 590-fontRender.get_height()
        else:
            fontY = playerY-fontRender.get_height()
        canvas.blit(fontRender,(fontX, fontY))
        

    # draw fishing prompt
    if canFish and not canTravel:
        fontX = 0
        fontY = 0
        fontRender = Font.render("Press F to Fish", 1, (255,255,255))
        if playerX-fontRender.get_width()/2 < 10:
            fontX = 10
        else:
            fontX = playerX-fontRender.get_width()/2
        if playerY-fontRender.get_height() < 10:
            fontY = 10
        else:
            fontY = playerY-fontRender.get_height()
        canvas.blit(fontRender,(fontX, fontY))

    # draw the stats
    if showStats:
        canvas.blit(UIImages[6], (500, 0))
        fontRender = Font.render("Money: $" + str(round(moneyBalance,2)), 1, (DarkBrown))
        canvas.blit(fontRender, (500+UIImages[6].get_width()/2-fontRender.get_width()/2, 15))
        fontRender = Font.render("Fishing Rod: ", 1, (DarkBrown))
        canvas.blit(fontRender, (500+UIImages[6].get_width()/2-fontRender.get_width()/2, 65))
        fontRender = Font.render(currentFishingRod, 1, (DarkBrown))
        canvas.blit(fontRender, (500+UIImages[6].get_width()/2-fontRender.get_width()/2, 100))
        fontRender = Font.render("Bait: " + currentBait, 1, (DarkBrown))
        canvas.blit(fontRender, (500+UIImages[6].get_width()/2-fontRender.get_width()/2, 150))
        fontRender = Font.render("Fish Caught: " + str(len(fishInventory)), 1, (DarkBrown))
        canvas.blit(fontRender, (500+UIImages[6].get_width()/2-fontRender.get_width()/2, 200))

    pygame.display.update()

#Render UI popup
def renderUI() -> None:
    canvas.blit(UIImages[0], (400-UIImages[0].get_width()/2, 300-UIImages[0].get_height()/2))

#fishing minigames
def Fishing() -> None:
    minigames[0]()
    temp = minigames[0]
    minigames.pop(0)
    minigames.append(temp)

def fishingGame1() -> None:
    fishLocation = [randint(0, 2), randint(0, 2)]
    isFishing = True
    startTime = time()

    
    while isFishing:
        # remaining time
        timeRemain = startTime + 5 - time()

        #Render Game
        renderUI()
        #Render instruction
        fontRender = Font.render("Find the Fish", 1, (255,255,255))
        canvas.blit(fontRender, (400-fontRender.get_width()/2, 110))
        for i in range(3):
            for j in range(3):
                gridX = 400-192+i*128
                gridY = 350-192+j*128
                if fishLocation == [i,j]:
                    canvas.blit(fishGridImages[0], (gridX,gridY))
                else:
                    canvas.blit(fishGridImages[1], (gridX,gridY))
                pygame.draw.rect(canvas, (255,255,255), (gridX,gridY, 128, 128), 2)
    
        # draw the time remaining
        timeText = Font.render("Time Remaining: " + str(round(timeRemain)), 1, (255,255,255))
        canvas.blit(timeText, (400-timeText.get_width()/2, 75))
        pygame.display.update()

        #checks if time is up
        if timeRemain < 0:
            isFishing = False
            break

        #Checks if player clicked on the fish
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX > 400-192 and mouseX < 400+192 and mouseY > 350-192 and mouseY < 350+192:
                    gridX = (mouseX - (400-192))//128
                    gridY = (mouseY - (300-192))//128
                    if fishLocation == [gridX,gridY]:
                        isFishing = False
                        getFish((startTime + 5 - time())/5)
                        break
        clock.tick(60)
        
def fishingGame2() -> None:
    isFishing = True
    startTime = time()
    charachters = []
    for i in range(5):
        charachters.append(randint(97, 122))

    
    while isFishing:
        # remaining time
        timeRemain = startTime + 10 - time()

        #Render Game
        renderUI()
        #Render instruction
        fontRender = Font.render("Type the following", 1, (255,255,255))
        canvas.blit(fontRender, (400-fontRender.get_width()/2, 150))
        #Render the first index character
        fontRender = Font.render(chr(charachters[0]-32), 1, (255,255,255))
        canvas.blit(fontRender, (400-fontRender.get_width()/2, 300-fontRender.get_height()/2))
    
        # draw the time remaining
        timeText = Font.render("Time Remaining: " + str(round(timeRemain)), 1, (255,255,255))
        canvas.blit(timeText, (400-timeText.get_width()/2, 75))
        pygame.display.update()

        #checks if time is up
        if timeRemain < 0:
            isFishing = False
            break

        #Checks if player typed corectly
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == charachters[0]:
                    charachters.pop(0)
                    if len(charachters) == 0:
                        isFishing = False
                        getFish((startTime + 10 - time())/10)
                        break

        clock.tick(60)

def fishingGame3() -> None:
    isFishing = True
    startTime = time()
    amountClicked = 0
    
    while isFishing:
        # remaining time
        timeRemain = startTime + 10 - time()


        #Render Game
        renderUI()
        #Render minigame
        fontRender = Font.render("Click!!!", 1, (255,255,255))
        canvas.blit(fontRender, (400-fontRender.get_width()/2, 150))
        scoreText = Font.render("Score: " + str(amountClicked), 1, (255,255,255))
        canvas.blit(scoreText, (400-scoreText.get_width()/2, 300-scoreText.get_height()/2))
        #Add score
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                amountClicked += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    amountClicked += 1
        
        # draw the time remaining
        timeText = Font.render("Time Remaining: " + str(round(timeRemain)), 1, (255,255,255))
        canvas.blit(timeText, (400-timeText.get_width()/2, 75))
        pygame.display.update()

        #checks if time is up
        if timeRemain < 0:
            isFishing = False
            break

        pygame.display.update()
        clock.tick(60)
    getFish(amountClicked/100)

#luck and fish
def getFish(luck: float) -> None:
    chance = randfloat(0, 100)
    if chance > mythicalChance:
        fish = mythicalFish
    elif chance > legendaryChance:
        fish = legendaryFish
    elif chance > epicChance:
        fish = epicFish
    elif chance > rareChance:
        fish = rareFish
    elif chance > uncommonChance:
        fish = uncommonFish
    else:
        fish = commonFish

    fishName = list(fish.keys())[randint(0, len(fish)-1)]
    fishProperties = fish.get(fishName)
    fishWeight = round(randfloat(fishProperties[0], fishProperties[1]) * luck, 2)
    fishPrice = round(randfloat(fishProperties[2], fishProperties[3]) * fishWeight,2)

    print("You got:" + fishName, "Weight: " + str(fishWeight), "Price: $" + str(fishPrice))

    for i in range(len(fishInventory)):
        if fishInventory[i][0] == fishName:
            fishInventory[i][1] += fishWeight
            fishInventory[i][2] += fishPrice
            fishInventory[i][3] += 1
            return
        

    fishInventory.append([fishName, fishWeight, fishPrice, 1])

#check if player is on a fishing spot
def checkFishing() -> bool:
    if fishMap[int(playerY/64)+playerYX][int(playerX/64)+playerXX] != []:
        if fishMap[int(playerY/64)+playerYX][int(playerX/64)+playerXX][0] in cornerIndex:
            return True
    return False

#check if player is on a fast travel spot
def checkFastTravel() -> bool:
    if (int(playerX/64),int(playerY/64)) in fastTravelCords.keys() and time()-travelTime > 1:
        return True
    return False

#fast travel
def fastTravel(fastTravelCords) -> tuple:
    mapChange = fastTravelCords.get((int(playerX/64),int(playerY/64)))
    return mapChange[0], mapChange[1][0]*64, mapChange[1][1]*64, fastTravelDict.get(mapChange[1][2]), time()

#market and shop system
def shopUI(marketNum: int, balance: float) -> list[int,str,str]:
    inShop = True
    renderArrows = False
    sellButton = False
    buyButton = False
    shopPage = 0
    shopPageMax = 1

    returnList = [0,"",""]

    #shopUI properties
    #fish market
    if marketNum == 0:
        shopPageMax = len(fishInventory)-1
        if shopPageMax > -1:
            sellButton = True
        if shopPageMax > 0:
            renderArrows = True
            
    #fishing rod shop
    elif marketNum == 1:
        shopPageMax = 4
        renderArrows = True
        buyButton = True
    #bait shop
    elif marketNum == 2:
        shopPageMax = 4
        renderArrows = True
        buyButton = True
    #fallback, should never happen
    else:
        inShop = False

    # Shop UI render
    while inShop:
        #render UI
        renderUI()
        # Exit button render
        canvas.blit(UIImages[1], (170,70))
        # Render Arrows
        if renderArrows:
            if shopPage > 0:
                canvas.blit(UIImages[2], (170, 300-27))
            if shopPage < shopPageMax:
                canvas.blit(UIImages[3], (600, 300-27))
 
        #fish market
        if marketNum == 0:
            #Title
            title = shopUIFont.render("Fish Market", 1, (DarkBrown))
            canvas.blit(title, (350-title.get_width()/2, 100))
            #Render Fish
            canvas.blit(UIImages[4], (500,85))
            if shopPageMax >= 0:
                #Fish Name
                fishName = marketFishNameFont.render(fishInventory[shopPage][0], 1, (DarkBrown))
                canvas.blit(fishName, (400-fishName.get_width()/2, 248-fishName.get_height()/2))
                #Fish Properties
                fishWeight = marketFishPropertiesFont.render("Weight: " + str(fishInventory[shopPage][1]), 1, (DarkBrown))
                canvas.blit(fishWeight, (400-fishWeight.get_width()/2, 300-fishWeight.get_height()/2))

                fishPrice = marketFishPropertiesFont.render("Price: " + str(fishInventory[shopPage][2]), 1, (DarkBrown))
                canvas.blit(fishPrice, (400-fishPrice.get_width()/2, 350-fishPrice.get_height()/2))

                #sell button
                sellText = marketFishPropertiesFont.render("Sell", 1, (DarkBrown))
                canvas.blit(UIImages[5], (400-UIImages[5].get_width()/2, 425-UIImages[5].get_height()/2))
                canvas.blit(sellText, (400-sellText.get_width()/2, 423-sellText.get_height()/2))

                

        #fishing rod shop
        elif marketNum == 1:
            #Title
            title = shopUIFont.render("Fishing Rod Market", 1, (DarkBrown))
            canvas.blit(title, (400-title.get_width()/2, 100))

            #Render Fishing Rods
            #Fishing Rod Name
            fishingRodName = list(fishingRods.keys())[shopPage]
            fishingRodRenderer = marketFishNameFont.render(fishingRodName, 1, (DarkBrown))
            canvas.blit(fishingRodRenderer, (400-fishingRodRenderer.get_width()/2, 200-fishingRodRenderer.get_height()/2))

            #Fishing Rod Properties
            fishingRodProperties = fishingRods.get(fishingRodName)
            fishingRodPrice = marketFishPropertiesFont.render("Price: $" + str(fishingRodProperties[0]), 1, (DarkBrown))
            canvas.blit(fishingRodPrice, (400-fishingRodPrice.get_width()/2, 250-fishingRodPrice.get_height()/2))
            listOfChanges = ["Uncommon: +%", "Rare: +%", "Epic: +%", "Legendary: +%", "Mythical: +%"]
            for i in range(5):
                change = marketFishPropertiesFont.render(listOfChanges[i] + str(fishingRodProperties[1][i]), 1, (DarkBrown))
                canvas.blit(change, (400-change.get_width()/2, 280+i*36-change.get_height()/2))

        #bait shop
        elif marketNum == 2:
            #Title
            title = shopUIFont.render("Bait Market", 1, (DarkBrown))
            canvas.blit(title, (400-title.get_width()/2, 100))

            #Render Baits
            #Bait Name
            baitName = list(fishingBaits.keys())[shopPage]
            baitRenderer = marketFishNameFont.render(baitName, 1, (DarkBrown))
            canvas.blit(baitRenderer, (400-baitRenderer.get_width()/2, 200-baitRenderer.get_height()/2))

            #Bait Properties
            baitProperties = fishingBaits.get(baitName)
            baitPrice = marketFishPropertiesFont.render("Price: $" + str(baitProperties[0]), 1, (DarkBrown))
            canvas.blit(baitPrice, (400-baitPrice.get_width()/2, 250-baitPrice.get_height()/2))
            listOfChanges = ["Uncommon: +%", "Rare: +%", "Epic: +%", "Legendary: +%", "Mythical: +%"]
            for i in range(5):
                change = marketFishPropertiesFont.render(listOfChanges[i] + str(baitProperties[1][i]), 1, (DarkBrown))
                canvas.blit(change, (400-change.get_width()/2, 280+i*36-change.get_height()/2))

            #Buy Button
            buyText = marketFishPropertiesFont.render("Buy", 1, (DarkBrown))
            canvas.blit(UIImages[5], (170, 450))
            canvas.blit(buyText, (170+UIImages[5].get_width()/2-buyText.get_width()/2, 445+UIImages[5].get_height()/2-buyText.get_height()/2))

        if buyButton:
            #Buy Button
            buyText = marketFishPropertiesFont.render("Buy", 1, (DarkBrown))
            canvas.blit(UIImages[5], (170, 450))
            canvas.blit(buyText, (170+UIImages[5].get_width()/2-buyText.get_width()/2, 445+UIImages[5].get_height()/2-buyText.get_height()/2))

            #Balance
            balanceText = marketFishPropertiesFont.render("Balance: $" + str(balance), 1, (DarkBrown))
            canvas.blit(balanceText, (320, 490-balanceText.get_height()/2))

        #check if player clicked on any button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                #exit button
                if mouseX > 170 and mouseX < 170+UIImages[1].get_width() and mouseY > 70 and mouseY < 70+UIImages[1].get_height():
                    inShop = False
                #Arrows
                if renderArrows:
                    if shopPage > 0:
                        if mouseX > 170 and mouseX < 170+UIImages[2].get_width() and mouseY > 300-27 and mouseY < 300-27+UIImages[2].get_height():
                            shopPage -= 1
                    if shopPage < shopPageMax:
                        if mouseX > 600 and mouseX < 600+UIImages[3].get_width() and mouseY > 300-27 and mouseY < 300-27+UIImages[3].get_height():
                            shopPage += 1
                #Sell Button
                if sellButton:
                    if mouseX > 400-UIImages[5].get_width()/2 and mouseX < 400-UIImages[5].get_width()/2+UIImages[5].get_width() and mouseY > 425-UIImages[5].get_height()/2 and mouseY < 425-UIImages[5].get_height()/2+UIImages[5].get_height():
                        returnList[0] += round(fishInventory[shopPage][2],2)
                        fishInventory.pop(shopPage)
                        shopPageMax -= 1
                        if shopPageMax == -1:
                            sellButton = False
                #Buy Button
                if buyButton:
                    if marketNum == 1:
                        if mouseX > 170 and mouseX < 170+UIImages[5].get_width() and mouseY > 450 and mouseY < 450+UIImages[5].get_height():
                            if balance >= fishingRods.get(list(fishingRods.keys())[shopPage])[0]:
                                balance -= fishingRods.get(list(fishingRods.keys())[shopPage])[0]
                                returnList[0] -= fishingRods.get(list(fishingRods.keys())[shopPage])[0]
                                returnList[1] = list(fishingRods.keys())[shopPage]
                    elif marketNum == 2:
                        if mouseX > 170 and mouseX < 170+UIImages[5].get_width() and mouseY > 450 and mouseY < 450+UIImages[5].get_height():
                            if balance >= fishingBaits.get(list(fishingBaits.keys())[shopPage])[0]:
                                balance -= fishingBaits.get(list(fishingBaits.keys())[shopPage])[0]
                                returnList[0] -= fishingBaits.get(list(fishingBaits.keys())[shopPage])[0]
                                returnList[2] = list(fishingBaits.keys())[shopPage]
        
        pygame.display.update()
        clock.tick(60)
    return returnList

#Minigames properties
minigames = [fishingGame1, fishingGame2, fishingGame3]

# Main game loop
inPlay = True
isMainMenu = True
while inPlay:
    if isMainMenu:
        # draw the background 
        for i in range(0, 800, 128):
            for j in range(0, 600, 32):
                canvas.blit(grassBackgroundImages[77], (i, j))

        #Render Title
        title = TitleFont.render("Fishing Game", 1, (DarkBrown))
        pygame.draw.rect(canvas, (232,207,166), (400-title.get_width()/2-10, 75-10, title.get_width()+20, title.get_height()+20))
        canvas.blit(title, (400-title.get_width()/2, 75))

        #Render Player
        canvas.blit(pygame.transform.scale(playerImages[0],(256,256)), (400-128, 300-128))

        #Render play Button
        playButton = ButtonFont.render("Play", 1, (DarkBrown))
        canvas.blit(UIImages[5], (300-playButton.get_width()/2-10, 500-UIImages[5].get_height()/2-10))
        canvas.blit(playButton, (300-playButton.get_width()/2+20, 500-UIImages[5].get_height()/2))

        #Render Exit Button
        exitButton = ButtonFont.render("Exit", 1, (DarkBrown))
        canvas.blit(UIImages[5], (450-exitButton.get_width()/2-10, 500-UIImages[5].get_height()/2-10))
        canvas.blit(exitButton, (450-exitButton.get_width()/2+20, 500-UIImages[5].get_height()/2))

        #check if player clicked on the buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                #play button
                if mouseX > 300-playButton.get_width()/2-10 and mouseX < 300-playButton.get_width()/2-10+UIImages[5].get_width() and mouseY > 500-UIImages[5].get_height()/2-10 and mouseY < 500-UIImages[5].get_height()/2-10+UIImages[5].get_height():
                    isMainMenu = False
                    if initLoad:
                        with open("save", "rb") as file:
                            loadedData = pickle.load(file)
                            moneyBalance = loadedData[0]
                            currentFishingRod = loadedData[1]
                            currentBait = loadedData[2]
                            fishInventory = loadedData[3]
                            if str(currentFishingRod).lower() != "hands":
                                propetiesChange = fishingRods.get(currentFishingRod)[1]
                                uncommonChance = defaultUncommonChance - propetiesChange[0]
                                rareChance = defaultRareChance - propetiesChange[1]
                                epicChance = defaultEpicChance - propetiesChange[2]
                                legendaryChance = defaultLegendaryChance - propetiesChange[3]
                                mythicalChance = defaultMythicalChance - propetiesChange[4]
                            if currentBait != "none":
                                propetiesChange = fishingBaits.get(currentBait)[1]
                                uncommonChance = defaultUncommonChance - propetiesChange[0]
                                rareChance = defaultRareChance - propetiesChange[1]
                                epicChance = defaultEpicChance - propetiesChange[2]
                                legendaryChance = defaultLegendaryChance - propetiesChange[3]
                                mythicalChance = defaultMythicalChance - propetiesChange[4]
                            file.close()
                            initLoad = False
                #exit button
                if mouseX > 450-exitButton.get_width()/2-10 and mouseX < 450-exitButton.get_width()/2-10+UIImages[5].get_width() and mouseY > 500-UIImages[5].get_height()/2-10 and mouseY < 500-UIImages[5].get_height()/2-10+UIImages[5].get_height():
                    inPlay = False
                    



                    

        pygame.display.update()
        clock.tick(60)
    else:
        # check if player is in between grid
        if playerX/64 % 1 != 0 and playerX/64 < 11:
            playerXX = 1
        else:
            playerXX = 0

        if playerY/64 % 1 != 0 and playerY/64 < 9:
            playerYX = 1
        else:
            playerYX = 0

        # check if player can fish or fast travel    
        if currentMap == fishMap:
            canFish = checkFishing()
        else:
            canFish = False
        canTravel = checkFastTravel()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isMainMenu = True
        
        # check if player is in a shop or market
        if currentMap == sellMap:
            showStats = False
            if [int(playerX/64), int(playerY/64)] == [8,3] and lastCords != [8,3]:
                process = shopUI(0,0)
                moneyBalance += process[0]
        elif currentMap == toolMap:
            showStats = False
            if [int(playerX/64), int(playerY/64)] == [8,3] and lastCords != [8,3]:
                process = shopUI(1,moneyBalance)
                moneyBalance += process[0]
                if process[1] != "":
                    currentFishingRod = process[1]
                    propetiesChange = fishingRods.get(currentFishingRod)[1]
                    uncommonChance = defaultUncommonChance - propetiesChange[0]
                    rareChance = defaultRareChance - propetiesChange[1]
                    epicChance = defaultEpicChance - propetiesChange[2]
                    legendaryChance = defaultLegendaryChance - propetiesChange[3]
                    mythicalChance = defaultMythicalChance - propetiesChange[4]
            elif [int(playerX/64), int(playerY/64)] == [4,4] and lastCords != [4,4]:
                process = shopUI(2,moneyBalance)
                moneyBalance += process[0] 
                if process[2] != "":
                    currentBait = process[2]
                    propetiesChange = fishingBaits.get(currentBait)[1]
                    uncommonChance = defaultUncommonChance - propetiesChange[0]
                    rareChance = defaultRareChance - propetiesChange[1]
                    epicChance = defaultEpicChance - propetiesChange[2]
                    legendaryChance = defaultLegendaryChance - propetiesChange[3]
                    mythicalChance = defaultMythicalChance - propetiesChange[4]
        else:
            showStats = True

        lastCords = [int(playerX/64), int(playerY/64)]

        #player actions
        if keys[pygame.K_f] and canFish:
            canPlay = False
            Fishing()
            canPlay = True
        if keys[pygame.K_t] and canTravel:
            currentMap, playerX, playerY, fastTravelCords, travelTime = fastTravel(fastTravelCords)
                

        # move and set starting index for the direction, and update picture number
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and canPlay:
            PlayerLook = Down
            PlayerFrame = (PlayerFrame + 1) %4 + Down
            checkMove = False
            if playerY < 500:
                checkMove = True
            if currentMap[int(playerY/64)+1][int(playerX/64)] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+1][int(playerX/64)]:
                    if i in colliderIndex:
                        checkMove = False

            if currentMap[int(playerY/64)+1+playerYX][int(playerX/64)] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+1+playerYX][int(playerX/64)]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+1][int(playerX/64)+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+1][int(playerX/64)+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+1+playerYX][int(playerX/64)+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+1+playerYX][int(playerX/64)+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if checkMove:
                playerY += 32
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and canPlay:
            PlayerLook = Up
            PlayerFrame = (PlayerFrame + 1) %4 + Up
            checkMove = False
            if playerY > 0:
                checkMove = True
            if currentMap[int(playerY/64)-1][int(playerX/64)] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)-1][int(playerX/64)]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)-1+playerYX][int(playerX/64)] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)-1+playerYX][int(playerX/64)]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)-1][int(playerX/64)+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)-1][int(playerX/64)+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)-1+playerYX][int(playerX/64)+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)-1+playerYX][int(playerX/64)+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if checkMove:
                playerY -= 32
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and canPlay:
            PlayerLook = Left
            PlayerFrame = (PlayerFrame + 1) %4 + Left
            checkMove = False
            if playerX > 0:
                checkMove = True
            if currentMap[int(playerY/64)][int(playerX/64)-1] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)][int(playerX/64)-1]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+playerYX][int(playerX/64)-1] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+playerYX][int(playerX/64)-1]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)][int(playerX/64)-1+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)][int(playerX/64)-1+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+playerYX][int(playerX/64)-1+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+playerYX][int(playerX/64)-1+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if checkMove:
                playerX -= 32
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and canPlay:
            PlayerLook = Right
            PlayerFrame = (PlayerFrame + 1) %4 + Right
            checkMove = False
            if playerX < 736:
                checkMove = True
            if currentMap[int(playerY/64)][int(playerX/64)+1] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)][int(playerX/64)+1]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+playerYX][int(playerX/64)+1] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+playerYX][int(playerX/64)+1]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)][int(playerX/64)+1+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)][int(playerX/64)+1+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if currentMap[int(playerY/64)+playerYX][int(playerX/64)+1+playerXX] == []:
                checkMove = False
            else:
                for i in currentMap[int(playerY/64)+playerYX][int(playerX/64)+1+playerXX]:
                    if i in colliderIndex:
                        checkMove = False
            if checkMove:
                playerX += 32
        else:
            PlayerFrame = PlayerLook
        
        
        #cycle through player images
        playerimage = playerImages[PlayerFrame]
        renderGame()

        clock.tick(8)
        pygame.event.clear()


# Quit Pygame
pygame.quit()

# Save the game
if not initLoad:
    with open("save", "wb") as file:
        pickle.dump([moneyBalance, currentFishingRod, currentBait, fishInventory], file)
        file.close()