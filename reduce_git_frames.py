from PIL import Image, ImageSequence

def reduce_gif_frames(input_gif_path, output_gif_path, reduction_factor):
    with Image.open(input_gif_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        
        reduced_frames = frames[::reduction_factor]
        
        reduced_frames[0].save(
            output_gif_path,
            save_all=True,
            append_images=reduced_frames[1:],
            loop=0
        )

# Example usage
input_gif_path = 'assets/gif/segmentation_origin.gif'
output_gif_path = 'assets/gif/segmentation.gif'
reduction_factor = 10 # Adjust this to keep every nth frame

reduce_gif_frames(input_gif_path, output_gif_path, reduction_factor)
