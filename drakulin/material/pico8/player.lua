istep=0

function player_draw()
    --draw the player's sprite at
	--p.x,p.y but since map tiles
	--are 12 pixels wide and tall,
	--we have to multiply the
	--coordinates by TILE. (example:
	--map tile 2,3 would be drawn
	--at pixel coordinates 24,36) +2 each to center each draw
	spr(p.sprite,margin + p.x*tile+2, margin +p.y*tile+2)
end



--player functions

function make_player()
	p={}  --create empty table
	
	p.x=0 --position on 10x10 map
	p.y=0
	


	p.sprite=009 --sprite
end

function draw_placed_arrows()

	for i = 1, 10 do
        for j = 1, 10 do
			if map[i][j] == 34 then
				spr(34,margin + (i-1)*tile+2, margin +(j-1)*tile+2)
			end
        end
    end
end


function change_mode()
	if (btnp(🅾️)) then
		--change mode
		if (mode == 1) then 
			mode = 0
		else
			mode = 1
		end
		--initialize objects
		vampire_start()
	end
end

function check_finish()
end

function place_object()
	if (btnp(❎)) then
		if can_place_object() then
			if arrows[1] != nil then
				--add arrow to inventory
				if map[p.x+1][p.y+1] != 16 then
					add(arrows, map[p.x+1][p.y+1])
				end
				map[p.x+1][p.y+1] = arrows[1]
				deli(arrows, 1)
			else
				--add arrow to inventory if there is no arrow on inventory
				if map[p.x+1][p.y+1] != 16 then
					add(arrows, map[p.x+1][p.y+1])
					map[p.x+1][p.y+1] = 16
				end
			end
		end
	end
end

function can_place_object()
	if (map[p.x+1][p.y+1] > 31 and map[p.x+1][p.y+1] < 40) or map[p.x+1][p.y+1] == 16 then
		return true
	else
		return false
	end
end

function move_player()

	--make two variables and store
	--where the player is now.
	--we'll change these to track
	--where the player is trying
	--to go
	local new_x,new_y=p.x,p.y

	--change new_x and new_y
	--depending on which buttons
	--they press
	if (btnp(⬅️)) new_x-=1
	if (btnp(➡️)) new_x+=1
	if (btnp(⬆️)) new_y-=1
	if (btnp(⬇️)) new_y+=1

	--if the new player position
	--is at all different from the 
	--player's current position...
	if (new_x!=p.x or new_y!=p.y) then
	 
        --...and the new position is
        --not blocked...

        
        --...set the player's
        --position to the new
        --coordinates
        p.x=new_x
        p.y=new_y 
        

     end
 	
end

function draw_instructions()
	rectfill(4,64,116,116,0)
	if istep == 0 then
		--first instructions
		print("WELCOME TO drakulin",6,66,7)
		print("YOU NEED TO GUIDE drakulin",6,72,7)
		print("TO HIS COFFIN BEFORE",6,78,7)
		print("IT IS TOO LATE",6,84,7)

		print("PRESS ❎ TO CONTINUE",20,100,7)

	elseif istep == 1 then
		--second instructions
		print("PLACE THE FIRST ARROW",6,66,7)
		print("WITH ❎",6,72,7)
		print("PRESS 🅾️ TO ALLOW drakulin",6,84,7)
		print("TO WALK",6,90,7)

		print("PRESS ❎ TO CONTINUE",20,100,7)
	end

end

function change_instructions()
	if (btnp(❎)) then
		istep+=1
	end
	if(istep == 2) mode = 0
end