import 'CoreLibs/graphics.lua'
import 'map.lua'

gfx = playdate.graphics


function gameSetUp() 
    playdate.display.setRefreshRate( 15 )


    map_start(4)
    map_fill()
    map_draw_bottom()
end

  
gameSetUp()

function playdate.update()

end
