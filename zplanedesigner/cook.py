import numpy as np
import matplotlib.pyplot as plt

def get_frequency_response(zeros, poles, resolution = 100):
    angles = np.linspace(0, np.pi, resolution)
    
    zeros_distances = np.ones((1,resolution))
    poles_distances = np.ones((1,resolution))
    
    for i, this_zeros in enumerate(zeros):
        zeros_distances = zeros_distances * np.array([np.sqrt((np.cos(this_val)-this_zeros[0])**2 + (np.sin(this_val)-this_zeros[1])**2) for this_val in angles])
            
    for i, this_pole in enumerate(poles):
        poles_distances = poles_distances * np.array([np.sqrt((np.cos(this_val)-this_pole[0])**2 + (np.sin(this_val)-this_pole[1])**2) for this_val in angles])
            
    distances = zeros_distances / poles_distances
            
    return angles, np.reshape(distances, (100,))

def plot_freq_response(angles, distances, f_s = 44.1):
    fig, ax = plt.subplots(figsize = (8,3))
    ax.set_title('Frequency Response')
    ax.plot(np.linspace(0,f_s/2,len(angles)), distances)

    # x_ticks = ax.set_xticks([np.pi/4, np.pi/2, np.pi], ['pi/4','pi/2','pi'])
    x_ticks = ax.set_xticks(np.linspace(0,22,12), [f'{f:.2f} kHz' for f in np.linspace(0,22,12)], rotation = 45)
    
    ax.grid()

    ax.set_ylim([-36,24])

    y_vals = np.linspace(-36,24,6)

    y_ticks = ax.set_yticks(y_vals, [f'{val:.1f}dB' for val in y_vals])
    plt.tight_layout()

    fig.savefig('./zplanedesigner/static/freq_resp.png')
    
def polar_to_cartesian(phasors):
    
    return [[mag*np.cos(angle), mag*np.sin(angle)] for (mag, angle) in phasors]

def generate_z_plane(zeros, poles, resolution = 50):
    
    fig, ax = plt.subplots(figsize=(5,5))
    
    angles = np.linspace(0,2*np.pi, resolution)
    
    x = np.cos(angles)
    y = np.sin(angles)
    
    ax.plot(x, y)
    ax.axis('equal')
    
    for pole in poles:
        ax.scatter(pole[0], pole[1], c='b', marker='x')
        
    for zero in zeros:
        ax.scatter(zero[0], zero[1], c='g', marker='o')

    save_path = './static/z_plane.png'

    fig.savefig('./zplanedesigner/static/z_plane.png')

    return save_path

def generate_freq_resp(zeros, poles):
    angles, distances = get_frequency_response(zeros, poles)

    plot_freq_response(angles, 20*np.log10(distances))


