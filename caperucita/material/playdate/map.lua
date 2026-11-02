--initialize the  map
map = {}
function map_start(dimension)

    for i = 1, dimension  do
        map[i] = {}

        for j = 1, dimension do
            map[i][j] = 0 -- Fill the values here
        end
    end

end

function map_fill()
    map[1][1] = 1 --caperucita
    map[1][4] = 2 --house
    map[1][4] = 3 --tree
end

function map_draw_bottom()
    
    tree = gfx.image.new( "resources/tree.png" )
    gfx.clear( gfx.kColorWhite ) 
    

    for i=1,4 do
      for j=1,4 do
        print( map[i][j] )
      end
    end


x=0
y=0
  x = x + 1 
  if ( x > 400 ) then x = -80 end
  
  y = y + 1
  if ( y > 240 ) then y = -85 end
  
  tree:draw( x, y )


  print( "Example ~ Drawing a basic image to the screen ~ RWSS" )
   
end