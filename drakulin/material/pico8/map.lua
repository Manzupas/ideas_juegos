tile=12
margin=0
map={}
mode=0

--mode: 
-- 0 place items
-- 1 simulation
-- 2 instructions
-- 9 you win

--initialize the 10x10 map
function map_start()

    for i = 1, 10 do
        map[i] = {}

        for j = 1, 10 do
            map[i][j] = 16 -- Fill the values here
        end
    end

end

function map_fill()
    map[4][5] = 8 --coffin
    map[9][9] = 1 --vampire
    -- 16 is floor.
end

function draw_map()
    draw_floor()
    draw_map_objects()

end

function draw_map_objects()
    --coffin
    spr(008,3*tile+2,4*tile+2)


    --arrows
    --spr(034,0*tile,11*tile)
end

function draw_floor()
    
    
    --rectfill(0,0,150,150,7)
    --tile floor
    for i = 0, 9, 1
    do
        for j = 0, 9, 1
        do
            if(i % 2 == 1) then
                if(j % 2 == 1) then
                        rectfill(margin+j*tile,margin+i*tile,margin+j*tile+tile,margin+i*tile+tile,1)
                        
                        
                        --margin+i*tile,margin+j*tile+tile,margin+i*tile+tile
                    else
                        rectfill(margin+j*tile,margin+i*tile,margin+j*tile+tile,margin+i*tile+tile,13)
                end
            else
                if(j % 2 == 1) then
                        rectfill(margin+j*tile,margin+i*tile,margin+j*tile+tile,margin+i*tile+tile,13)
                    else
                        rectfill(margin+j*tile,margin+i*tile,margin+j*tile+tile,margin+i*tile+tile,1)
                end
            end
        end
    end
    --Something is wrong above
    -- this 2 rects fixes it
    rectfill(120,0,121,128,0)
    rectfill(0,120,128,121,0)
end