import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Event listeners
screen.listen()
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect car_manager collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("Squish")
            scoreboard.game_over()
            game_is_on = False
        
        if player.xcor() > car.xcor() + 10 and car.distance(player) < 25:
            print("Squish")
            scoreboard.game_over()
            game_is_on = False

    # Detect finish line collision
    if player.ycor() >= 290:
        print("Player reached finish line")
        # Increase score
        scoreboard.increase_score()
        # TODO Increase car_manager move speed by MOVE_INCREMENT
        car_manager.increase_car_speed()
        # TODO Delete all car_managers
        
        # Return player to starting position
        player.refresh_player()
        
        
screen.exitonclick()