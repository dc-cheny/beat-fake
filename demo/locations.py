class landmarks:
    """
    脸部特征的位置列表
    """
    def __init__(self):
        self.XIABA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 115, 116, 117, 118, 119, 120, 
                      121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
        self.L_BROW = [93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114]
        self.R_BROW = [71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92]
        self.L_EYE = [49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70]
        self.R_EYE = [27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48]
        self.NOSE = [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]
        self.U_LIP = [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 181, 182, 183, 184, 185, 186, 
                      187, 188, 189, 190, 191, 192, 193, 194]
        self.D_LIP = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 167, 168, 169, 170, 171, 172, 173, 174, 175, 
                      176, 177, 178, 179, 180]
    
    def get_polygons_index(self, part_name):
        """
        获取特征轮廓索引
        """
        
        if part_name == 'XIABA':
            return [x-1 for x in self.XIABA]
        elif part_name == 'L_BROW':
            return [x-1 for x in self.L_BROW]
        elif part_name == 'R_BROW':
            return [x-1 for x in self.R_BROW]
        elif part_name == 'L_EYE':
            return [x-1 for x in self.L_EYE]
        elif part_name == 'R_EYE':
            return [x-1 for x in self.R_EYE]
        elif part_name == 'NOSE':
            return [x-1 for x in self.NOSE]
        elif part_name == 'U_LIP':
            return [x-1 for x in self.U_LIP]
        elif part_name == 'D_LIP':
            return [x-1 for x in self.D_LIP]
        else:
            return None
