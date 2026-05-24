import sys
import argparse
import os
import matplotlib.pyplot as plt

# Ensure the polyforms source directory is in the path
script_dir = os.path.dirname(os.path.abspath(__file__))
polyforms_src = os.path.join(script_dir, 'polyforms', 'src')
sys.path.insert(0, polyforms_src)

from polyforms.draw_scene import DrawScene, Align
from polyforms.polyiamond import Polyiamond

def draw_from_construction(construction_str, output_filename="construction_output.png"):
    parts = [p.strip() for p in construction_str.split('|')]
    if len(parts) != 5:
        print("Error: Construction string must have exactly 5 parts separated by '|'")
        return
        
    u, v, w, x, y = parts
    
    # We use a larger spacing (e.g., 50 units) to prevent overlap between k=1, 2, 3
    scene = DrawScene(Align.BASELINE)
    added = 0
    
    current_x_offset = 0
    for k in range(1, 4):
        s = u + v*k + w + x*k + y
        sides = list(zip(range(len(s), 0, -1), list(s)))
        try:
            p = Polyiamond(sides)
            # Add to scene with calculated offset
            scene.add_polyiamond(f'k={k}', p, (current_x_offset, 0))
            
            # Calculate width to determine next offset
            min_x, max_x, min_y, max_y = p.get_rect_box()
            current_x_offset += (max_x - min_x) + 5
            added += 1
        except Exception as e:
            print(f"Error at k={k}: {e}")
            
    if added == 0:
        print("No valid polyiamonds were created.")
        return
        
    scene.pack()
    fig = scene.fig
    fig.suptitle(construction_str, fontsize=12, y=1.05)
    # Adjust size based on how many were added
    fig.set_size_inches(4 * added, 4)
    fig.savefig(output_filename, bbox_inches='tight')
    plt.close(fig)
    print(f"Successfully generated {output_filename} with {added} polyiamonds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw first 3 polyiamonds from a construction string using Matplotlib.")
    parser.add_argument("construction", type=str, nargs="?", 
                        default="ABF | BFDF | DEDCD | CDCB | C",
                        help="Construction string (e.g. 'ABF | BFDF | DEDCD | CDCB | C')")
    parser.add_argument("-o", "--output", type=str, default="construction_output.png",
                        help="Output image filename")
                        
    args = parser.parse_args()
    draw_from_construction(args.construction, args.output)
