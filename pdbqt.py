a=input('input file name:')
def extract_coordinates(pdbqt_file):
    coordinates = []
    
    with open(pdbqt_file, 'r') as file:
        for line in file:
            
            if line.startswith("HETATM") or line.startswith("ATOM"):
                # 提取原子类型和坐标
                atom_type = line[76:78].strip()  
                x = float(line[30:38].strip())  
                y = float(line[38:46].strip())  
                z = float(line[46:54].strip())  
                
                
                coordinates.append(f"{atom_type} {x:8.4f} {y:8.4f} {z:8.4f}")
    
    return coordinates



if __name__ == "__main__":
    input_file = a  
    output_file = "coordinates.txt"  

    
    coords = extract_coordinates(input_file)

    
    with open(output_file, 'w') as f:
        f.write("\n".join(coords))
    
    print(f"finished!")
