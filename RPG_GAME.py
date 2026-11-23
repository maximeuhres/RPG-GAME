import pygame
import sys
import time
import random
import csv
pygame.init()
#pygame.font.init()
running = True

#screen config
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((50, 100, 50))
pygame.display.flip()
pygame.display.set_caption("RPG Game")
clock = pygame.time.Clock()
clock.tick(60)

#font load
black_clover_font=pygame.font.Font(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\font/BlackCloverFont.otf",32)

#image load
player=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/player_frames.png").convert_alpha()
player_original=pygame.transform.scale(player, (256, 64))
grass=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/grass_background.png").convert_alpha()
grass_original=pygame.transform.scale(grass,(800, 600))
pause_menu_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/pause_menu.png").convert_alpha()
pause_menu_image=pygame.transform.scale(pause_menu_image, (380, 256))
sword=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/sword1.png").convert_alpha()
sword=pygame.transform.scale(sword, (32, 32))
sword_frames=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/sword_frames.png").convert_alpha()
sword_frames=pygame.transform.scale(sword_frames, (288, 64))
inventory_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/inventory.png").convert_alpha()
inventory_image=pygame.transform.scale(inventory_image, (576, 230))
black_square=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/black_square.png").convert_alpha()
black_square=pygame.transform.scale(black_square, (32, 32))
red_square=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture/red_square.png").convert_alpha()
red_square=pygame.transform.scale(red_square, (26, 26))
#basic weapon image load
basic_axe_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_axe.png").convert_alpha()
basic_axe_image=pygame.transform.scale(basic_axe_image, (64, 64))
basic_sword_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_sword.png").convert_alpha()
basic_sword_image=pygame.transform.scale(basic_sword_image, (64, 64))
basic_warhammer_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_warhammer.png").convert_alpha()
basic_warhammer_image=pygame.transform.scale(basic_warhammer_image, (64, 64))
basic_dagger_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_dagger.png").convert_alpha()
basic_dagger_image=pygame.transform.scale(basic_dagger_image, (64, 64))
basic_bow_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_bow.png").convert_alpha()
basic_bow_image=pygame.transform.scale(basic_bow_image, (64, 64))
basic_staff_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_staff.png").convert_alpha()
basic_staff_image=pygame.transform.scale(basic_staff_image, (64, 64))
basic_spellbook_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_spellbook.png").convert_alpha()
basic_spellbook_image=pygame.transform.scale(basic_spellbook_image, (64, 64))
basic_shield_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\weapon_texture\basic_weapon_texture/basic_shield.png").convert_alpha()
basic_shield_image=pygame.transform.scale(basic_shield_image, (64, 64))
#potion image load
potion_speed_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\potion_texture/speed_potion.png").convert_alpha()
potion_speed_image=pygame.transform.scale(potion_speed_image, (64, 64))
potion_fire_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\potion_texture/fire_potion.png").convert_alpha()
potion_fire_image=pygame.transform.scale(potion_fire_image, (64, 64))
potion_healing_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\potion_texture/healing_potion.png").convert_alpha()
potion_healing_image=pygame.transform.scale(potion_healing_image, (64, 64))
#monster image load
blue_slime_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\enemy_texture\slime_texture/blue_slime.png").convert_alpha()
blue_slime_image=pygame.transform.scale(blue_slime_image, (128, 128))
caramel_slime_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\enemy_texture\slime_texture/caramel_slime.png").convert_alpha()
caramel_slime_image=pygame.transform.scale(caramel_slime_image, (128, 128))
acid_slime_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\enemy_texture\slime_texture/acid_slime.png").convert_alpha()
acid_slime_image=pygame.transform.scale(acid_slime_image, (128, 128))
acid_big_slime_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\enemy_texture\slime_texture/acid_big_slime.png").convert_alpha()
acid_big_slime_image=pygame.transform.scale(acid_big_slime_image, (192, 192))
acid_big_slime_key_image=pygame.image.load(r"C:\Users\uhres\Documents\Python_project\RPG_ressources\texture\enemy_texture\slime_texture/acid_big_slime_key.png").convert_alpha()
acid_big_slime_key_image=pygame.transform.scale(acid_big_slime_key_image, (192, 192))

#setup background
screen.blit(grass_original,(0,0))
pygame.display.flip()
actual_time_ig=0

#settings stats
str_stat=0
int_stat=0
vit_stat=0
dex_stat=0

#starter stats
basic_hp=10
vit_percentage=100
character_HP=0
basic_speed=1
speed_percentage=100
character_speed=0
basic_strenght=1
strenght_percentage=100
character_strenght=0
basic_int=1
int_percentage=100
character_int=0

#IG modifier
hp_bonus=0
speed_bonus=0
strenght_bonus=0
int_bonus=0

#player item/money
player_money=100
money_cost=0
money_gain=0

#player inventory
stuff_inventory_bonus=0
basic_weapon_inv=1
basic_armour_inv=1
basic_consumable_inv=1
inventory_weapon_item=[]
inventory_armour_item=[]
inventory_consumable_item=[]
inv_weapon_max_slot=0
inv_armour_max_slot=0
inv_consumable_max_slot=0
inventory_temp_variable_1=0
inventory_active=[True,False]
inventory_position_on_screen_x=(SCREEN_WIDTH-576)/2
inventory_position_on_screen_y=(SCREEN_HEIGHT-216)/2
inventory_weapon_position=[(inventory_position_on_screen_x+22,inventory_position_on_screen_y+10),(inventory_position_on_screen_x+106,inventory_position_on_screen_y+10),(inventory_position_on_screen_x+22,inventory_position_on_screen_y+85),(inventory_position_on_screen_x+106,inventory_position_on_screen_y+85),(inventory_position_on_screen_x+22,inventory_position_on_screen_y+160),(inventory_position_on_screen_x+106,inventory_position_on_screen_y+160)]
inventory_consumable_position=[(inventory_position_on_screen_x+412,inventory_position_on_screen_y+10),(inventory_position_on_screen_x+490,inventory_position_on_screen_y+10),(inventory_position_on_screen_x+406,inventory_position_on_screen_y+85),(inventory_position_on_screen_x+490,inventory_position_on_screen_y+85),(inventory_position_on_screen_x+406,inventory_position_on_screen_y+160),(inventory_position_on_screen_x+490,inventory_position_on_screen_y+160)]

#pickup variable setting
weapon=''
armour=''
food=''

#weapon stats
'''basic set'''
basic_axe_stats=[5,0.7,0.1,0.5,0]
basic_sword_stats=[3,1,0.3,0.2,0]
basic_warhammer_stats=[6,0.5,0,0.6,0]
basic_dagger_stats=[2,1.2,0.6,-0.2,0]
basic_bow_stats=[3,0.3,0.6,0,0]
basic_staff_stats=[4,0.8,0,0.2,0]
basic_spellbook_stats=[2,1,0,-0.1,0]
basic_shield_stats=[0,0,0,0.6,3]
'''tavern set'''

#monster stats
'''slime set'''
blue_slime_stats=[1,1,20,0]
caramel_slime_stats=[2,0.5,25,0]
acid_slime_stats=[2,0.7,20,0]
acid_big_slime_stats=[3,0.5,40,0]
acid_big_slime_key_stats=[3,0.5,40,0]
slime_stats=[blue_slime_stats,caramel_slime_stats,acid_slime_stats,acid_big_slime_stats,acid_big_slime_key_stats]



#weapons list
basic_collection=['basic_axe','basic_sword','basic_warhammer','basic_dagger','basic_bow','basic_staff','basic_spellbook','basic_shield']
basic_collection_image=[basic_axe_image,basic_sword_image,basic_warhammer_image,basic_dagger_image,basic_bow_image,basic_staff_image,basic_spellbook_image,basic_shield_image]
#tavern_collection=[big_meat_clever,spatula_sword,mash_hammer,chief_knife,'???',mop_staff,recipe_spellbook,top_barrel_shield]

#consumable list
potion_list=['speed_potion','fire_potion','healing_potion']
potion_list_image=[potion_speed_image,potion_fire_image,potion_healing_image]

#armour list


#monster list
slime_type=['blue_slime','caramel_slime','acid_slime','acid_big_slime','acid_big_slime_key']
slime_type_image=[blue_slime_image,caramel_slime_image,acid_slime_image,acid_big_slime_image,acid_big_slime_key_image]
bat_type=[]
skeleton_type=[]
monster_type=[slime_type,bat_type,skeleton_type]


#consumable settings
'''speed potion settings'''
speed_potion_used=False
cooldown_speed_potion_usable=True
cooldown_speed_potion=0
speed_potion_stock=0
'''fire potion settings'''
fire_potion_used=False
cooldown_fire_potion_usable=True
cooldown_fire_potion=0
fire_potion_stock=0
'''healing potion settings'''
healing_potion_used=False
cooldown_healing_potion_usable=True
cooldown_healing_potion=0
healing_potion_stock=0

#player position
player_pos_x=400
player_pos_y=300
player_move_1 = pygame.Rect(0, 0, 64, 64)
player_move_2 = pygame.Rect(64, 0, 64, 64)
player_move_3 = pygame.Rect(128, 0, 64, 64)
player_move_4 = pygame.Rect(192, 0, 64, 64)
player_move=[player_move_1,player_move_2,player_move_3,player_move_4]
player_move_count=-1
player_background_save = grass_original.subsurface((player_pos_x, player_pos_y, 64, 64)).copy()
disable_player_movement=False

#monster position(for all monster)
monster_number_on_screen=0
monster_position_on_screen=[]
monster_type_on_screen=[]

#sword position
sword_move_1 = pygame.Rect(0, 0, 64, 64)
sword_move_2 = pygame.Rect(100, 0, 80, 64)
sword_move_3 = pygame.Rect(192, 0, 64, 64)
sword_move=[sword_move_1,sword_move_2,sword_move_3]
sword_move_count=0
sword_attack_background_save = grass_original.subsurface((player_pos_x+30, player_pos_y+30, 32, 32)).copy()

#pose menu setting
pause_menu_temp_variable_1=0
pause_menu_active=[True,False]
resume_click_zone=pygame.Rect(0,0,100,100)

#utilisation des stats pour set les valeurs de base du personnage
def calc_character_hp ():
    global character_HP, vit_stat, vit_percentage, basic_hp, hp_bonus
    character_HP=((vit_stat+vit_percentage)/100)*basic_hp+hp_bonus
def calc_character_spd ():
    global character_speed, dex_stat, speed_percentage, basic_speed, speed_bonus
    character_speed=((dex_stat+speed_percentage)/100)*basic_speed+speed_bonus
def calc_character_str ():
    global character_strenght, str_stat, strenght_percentage, basic_strenght, strenght_bonus
    character_strenght=((str_stat+strenght_percentage)/100)*basic_strenght+strenght_bonus
def calc_character_int ():
    global character_int, int_stat, int_percentage, basic_int, int_bonus
    character_int=((int_stat+int_percentage)/100)*basic_int+int_bonus
calc_character_hp()
calc_character_spd()
calc_character_str()
calc_character_int()

#money system
def player_money():
    global player_money,money_cost,money_gain
    player_money=player_money+money_gain-money_cost
    money_cost=0
    money_gain=0
    return player_money

#drop function
weapon_zone_on_screen=pygame.Rect(0,0,0,0)
def basic_weapon_drop(basic_collection):
    global weapon_zone_on_screen, weapon_drop, basic_weapon_drop_background_save,weapon_zone_on_screen1,weapon_zone_on_screen2
    weapon_drop_number=random.randint(0,len(basic_collection)-1)
    weapon_drop=basic_collection[weapon_drop_number]
    weapon_zone_on_screen1=random.randint(100,700)
    weapon_zone_on_screen2=random.randint(100,500)
    basic_weapon_drop_background_save=grass_original.subsurface((weapon_zone_on_screen1,weapon_zone_on_screen2, 64, 64)).copy()
    screen.blit(basic_collection_image[weapon_drop_number],(weapon_zone_on_screen1,weapon_zone_on_screen2))
    pygame.display.flip()
    weapon_zone_on_screen=pygame.Rect(weapon_zone_on_screen1,weapon_zone_on_screen2,64,64)
consumable_zone_on_screen=pygame.Rect(0,0,0,0)
def potion_list_drop(potion_list):
    global consumable_zone_on_screen, consumable_drop, potion_list_drop_background_save,consumable_zone_on_screen1,consumable_zone_on_screen2
    consumable_drop_number=random.randint(0,len(potion_list)-1)
    consumable_drop=potion_list[consumable_drop_number]
    print(consumable_drop)
    consumable_zone_on_screen1=random.randint(100,700)
    consumable_zone_on_screen2=random.randint(100,500)
    potion_list_drop_background_save=grass_original.subsurface((consumable_zone_on_screen1,consumable_zone_on_screen2, 64, 64)).copy()
    screen.blit(potion_list_image[consumable_drop_number],(consumable_zone_on_screen1,consumable_zone_on_screen2))
    pygame.display.flip()
    consumable_zone_on_screen=pygame.Rect(consumable_zone_on_screen1,consumable_zone_on_screen2,64,64)
def armour_drop (armour):
    pass

#spawn an entity
def spawn_entity(monster_type, slime_type, slime_type_image):
    global monster_number_on_screen, monster_position_on_screen, monster_type_on_screen
    answer=str(input("voulez vous faire spawn le mob au hasard?\n")).strip().upper()
    entity_drop_number=random.randint(0,len(slime_type)-1)
    entity_drop=slime_type[entity_drop_number]
    if answer == 'YES':
        entity_spawn_zone_on_screen1=random.randint(300,(500))
        entity_spawn_zone_on_screen2=random.randint(200,400)
    elif answer == 'NO':
        entity_spawn_zone_on_screen1=int(input("saisissez la coordonnée x:\n"))
        entity_spawn_zone_on_screen2=int(input("saisissez la coordonnée y:\n"))
    else:
        return
    screen.blit(slime_type_image[entity_drop_number],(entity_spawn_zone_on_screen1,entity_spawn_zone_on_screen2))
    monster_number_on_screen+=1
    monster_position_on_screen.append((entity_spawn_zone_on_screen1,entity_spawn_zone_on_screen2))
    monster_type_on_screen.append(slime_type[entity_drop_number])
    pygame.display.flip()

def get_weapon_stats(weapon):
    pass

#inventory system
def inventory_max_slot_weapon(stuff_inventory_bonus):
    global inv_weapon_max_slot
    inv_weapon_max_slot=basic_weapon_inv+stuff_inventory_bonus
def inventory_max_slot_armour(stuff_inventory_bonus):
    global inv_armour_max_slot
    inv_armour_max_slot=basic_armour_inv+stuff_inventory_bonus
def inventory_max_slot_consumable(stuff_inventory_bonus):
    global inv_consumable_max_slot
    inv_consumable_max_slot=basic_consumable_inv+stuff_inventory_bonus

inventory_max_slot_weapon(stuff_inventory_bonus)
inventory_max_slot_consumable(stuff_inventory_bonus)
inventory_max_slot_armour(stuff_inventory_bonus)

#pickup system
def weapon_pick_up(weapon):
    global inventory_weapon_item,inv_weapon_max_slot,weapon_zone_on_screen
    if inv_weapon_max_slot >=1:
        inventory_weapon_item.append(weapon)
        inv_weapon_max_slot-=1
        weapon_zone_on_screen=pygame.Rect(0,0,0,0)
        screen.blit(basic_weapon_drop_background_save,(weapon_zone_on_screen1,weapon_zone_on_screen2))
        pygame.display.flip()
    else:
        print('not enought space in inventory for: \n', weapon)
def armour_pick_up(armour):
    '''global inventory_armour_item,inv_armour_max_slot,armour_zone_on_screen
    if inv_armour_max_slot >=1:
        inventory_armour_item.append(armour)
        inv_armour_max_slot-=1
        armour_zone_on_screen=pygame.Rect(0,0,0,0)
        screen.blit(basic_armour_drop_background_save,(armour_zone_on_screen1,armour_zone_on_screen2))
        pygame.display.flip()
    else:
        print('not enought space in inventory for: \n', armour)'''
def consumable_pick_up(consumable):
    global inventory_consumable_item,inv_consumable_max_slot,consumable_zone_on_screen
    if inv_consumable_max_slot >=1:
        inventory_consumable_item.append(consumable)
        inv_consumable_max_slot-=1
        consumable_zone_on_screen=pygame.Rect(0,0,0,0)
        screen.blit(potion_list_drop_background_save,(consumable_zone_on_screen1,consumable_zone_on_screen2))
        pygame.display.flip()
    else:
        print('not enought space in inventory for: \n', consumable)


def sword_attack(disable_player_movement,sword_move_count):
    global sword_move
    disable_player_movement=True
    for i in range (len(sword_move)):
        if sword_move_count <2:
            sword_attack_background_save = grass_original.subsurface((player_pos_x+23, player_pos_y, 80, 64)).copy()
            screen.blit(sword_attack_background_save, (player_pos_x+23, player_pos_y))
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            screen.blit(sword_frames.subsurface(sword_move[sword_move_count]),(player_pos_x+23, player_pos_y))
        elif sword_move_count==2:
            sword_attack_background_save = grass_original.subsurface((player_pos_x+23, player_pos_y, 80, 64)).copy()
            screen.blit(sword_attack_background_save, (player_pos_x+23, player_pos_y))
            sword_attack_background_save = grass_original.subsurface((player_pos_x+23, player_pos_y+30, 80, 64)).copy()
            screen.blit(sword_attack_background_save, (player_pos_x+23, player_pos_y+30))
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            screen.blit(sword_frames.subsurface(sword_move[sword_move_count]),(player_pos_x+23, player_pos_y+30))
        sword_move_count+=1
        pygame.display.flip()
        time.sleep(0.1)
    sword_attack_background_save = grass_original.subsurface((player_pos_x+23, player_pos_y, 80, 64)).copy()
    screen.blit(sword_attack_background_save, (player_pos_x+23, player_pos_y))
    sword_attack_background_save = grass_original.subsurface((player_pos_x+23, player_pos_y+30, 80, 64)).copy()
    screen.blit(sword_attack_background_save, (player_pos_x+23, player_pos_y+30))
    screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
    screen.blit(sword_frames.subsurface(sword_move[0]),(player_pos_x+23, player_pos_y))
    pygame.display.flip()
    disable_player_movement=False
    sword_move_count=0

#function for showing the health bar and making it work
health_bar_background_save = grass_original.subsurface(0, 0, 0, 0).copy()
def hp_value (pv_impact_value):
    global health_bar_length, actual_character_hp, health_bar_background_save
    screen.blit(health_bar_background_save, (10, 100))
    health_bar_length=int(character_HP)
    actual_character_hp=character_HP+pv_impact_value
    actual_character_hp=int(actual_character_hp)
    health_bar_background_save = grass_original.subsurface(10, 100, 32+10*health_bar_length, 32).copy()
    screen.blit(health_bar_background_save, (10, 100))
    if actual_character_hp>health_bar_length:
        health_bar_length=actual_character_hp
    a=10
    for i in range (health_bar_length):
        a+=10
        screen.blit(black_square, (a, 100))
    a=13
    for i in range (actual_character_hp):
        a+=10
        screen.blit(red_square, (a,103))
    pygame.display.flip()

def enemy_movements_to_player(actual_monster):
    #check la direction du joueur, faire avancer le monstre dans cette direction, re-set la position du monstre dans la liste pour ne pas la perdre
    actual_monster_near_player=False

#function for moving enemy
entity_moov_timer=5
def enemy_movements_random():
    global monster_type, slime_type, bat_type, skeleton_type, monster_number_on_screen, monster_position_on_screen, monster_type_on_screen
    for i in range (monster_number_on_screen):
        actual_monster=monster_type_on_screen[i]
        #test si la position du monstre est suffisement proche du joueur, ou si joueur détecté et faire test une fonction qui détecte le joueur à chaque mouvements
        if actual_monster_near_player == True:
            enemy_movements_to_player(actual_monster)
            pass
        actual_monster_position=monster_position_on_screen[i-1]
        monster_image_surface=slime_type_image[i].get_size()
        monster_background_save = grass_original.subsurface(((actual_monster_position), (monster_image_surface))).copy()
        movement_x=random.randint(-10,10)*slime_stats[slime_type.index(actual_monster)][1]
        movement_y=random.randint(-10,10)*slime_stats[slime_type.index(actual_monster)][1]
        monster_new_position=actual_monster_position[0]+movement_x,actual_monster_position[1]+movement_y
        monster_position_on_screen[i-1]=(monster_new_position)
        screen.blit(monster_background_save,(monster_new_position))
        screen.blit(slime_type_image[i],(monster_new_position))
        pygame.display.flip()

#function for closing interface
def resume_fonction ():
    global disable_player_movement, pause_menu_temp_variable_1
    screen.blit(pause_menu_background_save, (0, 0))
    pygame.display.flip()
    pause_menu_temp_variable_1=0
    disable_player_movement=False
def resume_inventory_fonction ():
    global disable_player_movement, inventory_temp_variable_1
    screen.blit(inventory_background_save, (inventory_position_on_screen_x, inventory_position_on_screen_y))
    pygame.display.flip()
    inventory_temp_variable_1=0
    disable_player_movement=False

ancient_time=round(time.perf_counter())
while running:
    #where we get the actual time of the game
    actual_time=round(time.perf_counter())
    #function for a clock, print the actual time every second
    '''if actual_time>=ancient_time:
        print(actual_time)
        ancient_time=actual_time+1'''
    for event in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if disable_player_movement==False:
            player_background_save = grass_original.subsurface((player_pos_x, player_pos_y, 64, 66)).copy()
            screen.blit(player_background_save, (player_pos_x, player_pos_y))
            player_pos_x+=character_speed
            player_move_count+=1
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            pygame.display.flip()
            if player_move_count == 3:
                player_move_count=-1
        time.sleep(0.1)
    if keys[pygame.K_q]:
        if disable_player_movement==False:
            player_background_save = grass_original.subsurface((player_pos_x, player_pos_y, 64, 66)).copy()
            screen.blit(player_background_save, (player_pos_x, player_pos_y))
            player_pos_x-=character_speed
            player_move_count+=1
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            pygame.display.flip()
            if player_move_count == 3:
                player_move_count=-1
        time.sleep(0.1)
    if keys[pygame.K_s]:
        if disable_player_movement==False:
            player_background_save = grass_original.subsurface((player_pos_x, player_pos_y, 64, 64)).copy()
            screen.blit(player_background_save, (player_pos_x, player_pos_y))
            player_pos_y+=character_speed
            player_move_count+=1
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            pygame.display.flip()
            if player_move_count == 3:
                player_move_count=-1
        time.sleep(0.1)
    if keys[pygame.K_z]:
        if disable_player_movement==False:
            player_background_save = grass_original.subsurface((player_pos_x, player_pos_y, 64, 68)).copy()
            screen.blit(player_background_save, (player_pos_x, player_pos_y))
            player_pos_y-=character_speed
            player_move_count+=1
            screen.blit(player_original.subsurface(player_move[player_move_count]),(player_pos_x, player_pos_y))
            pygame.display.flip()
            if player_move_count == 3:
                player_move_count=-1
        time.sleep(0.1)
    if keys[pygame.K_a]:
        if disable_player_movement==False:
            sword_attack(disable_player_movement,sword_move_count)
        time.sleep(0.1)
    if keys[pygame.K_f]:
        drop_answer=str(input("choisissez le truc à drop"))
        if drop_answer=='consumable':
            potion_list_drop(potion_list)
        if drop_answer=='weapon':
            basic_weapon_drop(basic_collection)
        time.sleep(1)
    if keys[pygame.K_g]:
        spawn_entity(monster_type, slime_type, slime_type_image)
        time.sleep(1)
    #lines calling mooving entity
    if entity_moov_timer<=actual_time:
        enemy_movements_random()
        entity_moov_timer+=5
    if keys[pygame.K_p]:
        pv_impact_value=1
        hp_value(pv_impact_value)
        time.sleep(1)
    if keys[pygame.K_o]:
        pv_impact_value=-1
        hp_value(pv_impact_value)
        time.sleep(1)
    if keys[pygame.K_w]:
        #check if there are speed potion in inventory, could be anywhere as long as it is call somewhere, maybe when pick up potion
        speed_potion_stock=0
        for potion_number in range (len(inventory_consumable_item)):
            if inventory_consumable_item[potion_number]=='speed_potion':
                speed_potion_stock+=1
        if cooldown_speed_potion_usable == True:
            if speed_potion_used ==False:
                if speed_potion_stock>=1:
                    speed_potion_stock-=1
                    speed_bonus+=5
                    calc_character_spd()
                    cooldown_speed_potion=actual_time+10
                    speed_potion_duration=actual_time+5
                    cooldown_speed_potion_usable=False
                    speed_potion_used=True
        time.sleep(0.2)
    if speed_potion_used==True:
        if speed_potion_duration<=actual_time:
            speed_bonus-=5
            calc_character_spd()
            speed_potion_used=False
    if cooldown_speed_potion<=actual_time:
        cooldown_speed_potion_usable=True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pause_menu_temp_variable_1==1:
            if resume_click_zone.collidepoint(event.pos):
                resume_fonction()
        if weapon_zone_on_screen.collidepoint(event.pos):
            weapon_pick_up(weapon_drop)
            time.sleep(0.4)
        if consumable_zone_on_screen.collidepoint(event.pos):
            consumable_pick_up(consumable_drop)
            time.sleep(0.4)
    if keys[pygame.K_e]:
        if inventory_active[inventory_temp_variable_1] == True:
            disable_player_movement=True
            inventory_background_save = grass_original.subsurface(inventory_position_on_screen_x, inventory_position_on_screen_y, 576, 230).copy()
            screen.blit(inventory_image, (inventory_position_on_screen_x, inventory_position_on_screen_y))
            if len(inventory_weapon_item)>0:
                for i in range(len(inventory_weapon_item)):
                    a=basic_collection.index(inventory_weapon_item[i])
                    inventory_weapon_temp_var_weapon_item=basic_collection_image[a]
                    inventory_weapon_temp_var_weapon_position=inventory_weapon_position[i]
                    screen.blit(inventory_weapon_temp_var_weapon_item, inventory_weapon_temp_var_weapon_position)
            if len(inventory_consumable_item)>0:
                for i in range(len(inventory_consumable_item)):
                    a=potion_list.index(inventory_consumable_item[i])
                    inventory_consumable_temp_var_consumable_item=potion_list_image[a]
                    inventory_consumable_temp_var_consumable_position=inventory_consumable_position[i]
                    screen.blit(inventory_consumable_temp_var_consumable_item, inventory_consumable_temp_var_consumable_position)
            pygame.display.flip()
            inventory_temp_variable_1=1
        elif inventory_active[inventory_temp_variable_1]==False:
            resume_inventory_fonction()
        time.sleep(0.5)
    if keys[pygame.K_ESCAPE]:
        if pause_menu_active[pause_menu_temp_variable_1] == True:
            disable_player_movement=True
            pause_menu_background_save = grass_original.subsurface((0, 0, 380, 256)).copy()
            screen.blit(pause_menu_image, (0, 0))
            pygame.display.flip()
            pause_menu_temp_variable_1=1
        elif pause_menu_active[pause_menu_temp_variable_1]==False:
            resume_fonction()
        time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()