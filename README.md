# Use-computational-methods-to-roughly-estimate-the-size-of-small-molecule-compounds

During docking(https://github.com/LIJIAWEI040301/Blind-Docking-for-Target-Fishing-based-on-Autodock), the setting of the `overlap` parameter is critical:
- **Set too small**: Some high-scoring docking poses may be ignored because they fall into gaps.
- **Set too large**: This significantly increases computational cost.

To quantitatively determine the size of small molecules and assist in selecting the appropriate `overlap` parameter, we provide a simple method.

## Methodology

We use the following tools and steps to calculate the size of small molecules:
1. Extract the coordinates of the small molecule from PDB or PDBQT files.
2. Input the coordinates into an online tool for calculation.
3. Use the calculation results to select a reasonable `overlap` parameter.

For more details, refer to: [Molecular Size Calculation](https://jerkwin.github.io/2016/06/24/%E5%88%86%E5%AD%90%E5%B0%BA%E5%AF%B8%E5%A4%A7%E5%B0%8F%E7%9A%84%E8%AE%A1%E7%AE%97/#opennewwindow).

## Usage Steps

### 1. Extract Small Molecule Coordinates

We provide scripts to extract coordinates from PDB or PDBQT files.

Run the following commands:
```bash
python pdb.py
# or
python pdbqt.py
```

Then, follow the prompt to input the file name of the small molecule:
```bash
Enter the name of the file: [your_file_name]
```

The script will automatically extract the coordinates of the small molecule.

### 2. Calculate Molecular Size

Input the extracted coordinates into the following online tool: [Molecular Size Calculation Tool](https://jerkwin.github.io/2016/06/24/%E5%88%86%E5%AD%90%E5%B0%BA%E5%AF%B8%E5%A4%A7%E5%B0%8F%E7%9A%84%E8%AE%A1%E7%AE%97/#opennewwindow).

The tool will output the size information of the small molecule.

### 3. Set the `overlap` Parameter

Adjust the `overlap` parameter based on the calculation results and specific requirements:

## References

- [Molecular Size Calculation](https://jerkwin.github.io/2016/06/24/%E5%88%86%E5%AD%90%E5%B0%BA%E5%AF%B8%E5%A4%A7%E5%B0%8F%E7%9A%84%E8%AE%A1%E7%AE%97/#opennewwindow)

---

