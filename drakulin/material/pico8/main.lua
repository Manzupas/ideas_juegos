function _init()
    map_start()
    map_fill()
    inventory_start()
    make_player()
    vampire_start()
    mode = 2
end

function _update()
    
    if(mode != 9) then
        change_mode()
    end
    
    if(mode == 0) then
        place_object()
        move_player()
        --stablish the limits
        if p.x < 0 then
            p.x = 0
        end
        if p.y < 0 then
            p.y = 0
        end
        if p.x > 9 then
            p.x = 9
        end
        if p.y > 9 then
            p.y = 9
        end
    elseif (mode == 1) then
        move_vampire()

    elseif (mode == 2) then
        change_instructions()

    
    end

end

function _draw()
    if(mode == 9) then
        
        -- win message
        rectfill(4,64,116,116,0)
		print("drakulin HAS ARRIVED!",20,72,7)

		print("YOU WIN!",40,100,7)
    elseif (mode == 1 or mode == 0 or mode == 2) then
        cls()
        draw_map()
    
        if (mode == 0) player_draw()
    
        draw_placed_arrows()
        vampire_draw()
        
        --print where the player is
        --in both screen coordinates
        --and in map tile coordinates
        inventory_draw()
    
        if mode == 2 then
            draw_instructions()
        end
    end
end
