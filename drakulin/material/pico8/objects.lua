--ARROWS
-- 32 UP GREEN
-- 33 DOWN GREEN
-- 34 LEFT GREEN
-- 45 RIGHT GREEN


arrows = {}
v={}
v.x=0 --position
v.y=0 --position
v.d=0 --direction
-- 0 UP
-- 1 DOWN
-- 2 LEFT
-- 3 RIGHT

function vampire_start()
	v.x= 8*tile+2
	v.y= 8*tile+2
	v.d=0
	v.s=000
end

function vampire_draw()
    --vampire
	-- where it is
	
    spr(v.s,v.x,v.y)
end

function move_vampire()

	local new_x,new_y=v.x,v.y

	--change new_x and new_y
	--depending on which direction is facing
	if (v.d == 0) new_y-=1
	if (v.d == 1) new_y+=1
	if (v.d == 2) new_x-=1
	if (v.d == 3) new_x+=1

	--if the new player position
	--is at all different from the 
	--player's current position...
	if (new_x!=v.x or new_y!=v.y) then
	 
        --...and the new position is
        --not blocked...

        if(can_move(new_x, new_y)) then
			--...set the player's
			--position to the new
			--coordinates
			v.x=new_x
			v.y=new_y 
		end

     end
end

function inventory_start()
	add(arrows, 34, 1)
end

function inventory_draw()
	for i in all(arrows) do
		spr(i,10*tile,0 +2)

	end

	if (mode == 0 or mode==1)  then
		print("1/10: to the left ",2,122,7)
	end

	--print("map:"..p.x..","..p.y,2,122,7)
	--print("screen:"..(p.x*8)..","..(p.y*8),60,122,7)
	
end

--collision functions

--this function checks an x,y
--map coordinate to see if it 
--can be walked on or not

function can_move(x,y)

	--if we go out of the tiles
	if(x < 0) or (y < 0) or (x > 120) or (y > 120) then
		return false
	end

	-- what element is in the map at x,y?
	-- if it is an arrow, we wait until we are on it
	-- 
	element_at = get_element_in_map_at(x,y)
	if(element_at == 34) then
		-- wait until we are in the perfect position
		perfect_x = (x\tile)*tile +2
		perfect_y = (y\tile)*tile +2
		if(x==perfect_x) and (y== perfect_y) then
			v.s=002
			v.d=2
		end
	end
	if(element_at == 8) then
		mode = 9
	end


	return true

end

function get_element_in_map_at(x,y)
	posx = x\tile
	posy = y\tile
	return map[posx+1][posy+1]
end