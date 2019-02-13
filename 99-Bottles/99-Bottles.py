def play_song(num_bottles):
    for num in range(num_bottles, 0, -1):
        if num > 1:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down, pass it around, {num -1} bottles of beer on the wall.")
        else:
            print(f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down, pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")

play_song(99)