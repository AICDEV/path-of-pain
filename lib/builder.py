import random

class map():
    def __init__(self, size):
        self._col = int(size / 2)
        self._row = int(size / 2)
        self._start_position = []
        self._end_position = []
        self._generated_map = []

        self._build_map()
        self._generate_start_position()
        self._build_path()
        self._mark_end_position()


    def get_start_position(self):
        return self._start_position
    
    def get_end_postion(self):
        return self._end_position

    def get_map(self):
        return self._generated_map

    def _build_path(self):

        counter = 0

        while counter < 10:
            move = random.choice(["l","t","r","b"])

            if move == "l":
                self._paint_path([self._start_position[0]-1, self._start_position[1]])
                
            if move == "t":
                self._paint_path([self._start_position[0]+1, self._start_position[1]+1])
                
            if move == "r":
                self._paint_path([self._start_position[0], self._start_position[1]+1])
                
            if move == "b":
                self._paint_path([self._start_position[0]-1, self._start_position[1]-1])

            counter = counter + 1
    
    def _paint_path(self, pos):

        if (pos[0] or pos[1]) < 0 or (pos[0] or pos[1]) > (self._col / 2):
            return False
        
        self._generated_map[pos[0]][pos[1]][5] = 1
        self._start_position = [pos[0],pos[1]]
        return True

    def _mark_end_position(self):
        self._generated_map[self._end_position[0]][self._end_position[1]][8] = 1

    def _build_map(self):
        for r in range(0, self._row):
            map_line = []
            if r == 0:
                for c in range(0, self._col):
                    if c == 0:
                        map_line.append(self._get_top_left_corner())
                    elif c == self._col - 1:
                        map_line.append(self._get_top_right_corner())
                    else:
                        map_line.append(self._get_top_middle())

            elif r < self._row - 1:
                for c in range(0, self._col):
                    if c == 0:
                        map_line.append(self._get_mid_left())
                    elif c == self._col - 1:
                        map_line.append(self._get_mid_right())
                    else:
                        map_line.append(self._get_mid())
            else:
                for c in range(0, self._col):
                    if c == 0:
                        map_line.append(self._get_bottom_left_corner())
                    elif c == self._col - 1:
                        map_line.append(self._get_bottom_right_corner())
                    else:
                        map_line.append(self._get_bottom_middle())
            self._generated_map.append(map_line)

    def _get_top_left_corner(self):
        return [0,0,1,1,"tlc",0,0,0,0]

    def _get_top_middle(self):
        return [1,0,1,1,"tm",0,0,0,0]

    def _get_top_right_corner(self):
        return [1,0,0,1,"trc",0,0,0,0]

    def _get_mid_left(self):
        return [0,1,1,1,"ml",0,0,0,0]

    def _get_mid(self):
        return [1,1,1,1,"mm",0,0,0,0]

    def _get_mid_right(self):
        return [1,1,0,1,"mr",0,0,0,0]

    def _get_bottom_left_corner(self):
        return [0,1,1,0,"blc",0,0,0,0]

    def _get_bottom_middle(self):
        return [1,1,1,0,"bm",0,0,0,0]

    def _get_bottom_right_corner(self):
        return [1,1,0,1,"brc",0,0,0,0]

    def _generate_start_position(self):
        x = random.choice(range(0, int(self._col / 2)))
        y = random.choice(range(0, int(self._row / 2)))
        self._generated_map[y][x][7] = 1
        self._start_position = [y, x]
        self._end_position = [y,x]

