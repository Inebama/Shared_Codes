import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Here we create some random values to show whatever we need

x  = np.linspace(0,4*np.pi,100)
y1 = np.cos(x)
y2 = (np.sin(x)**5)/2
y3 = (y1+y2)

A,B = np.meshgrid(x, x)
Z   = (np.cos(A)+np.cos(B))/2.0

# Tutorial Gridspec

# Basic common

fig = plt.figure(1,figsize=(12,8))   # We set the enviroment figure of matplotlib where we gonna plot also here we set the "Fig size" (x,y) proportions respectively

# We call the function of gridspec which will generate the positions squares in the figure acording to what we define inside

# Example 2x2

#     |
#(0,0)|(0,1)
#     |
#-----|-----
#     |
#(1,0)|(1,1)
#     |

# Or 2x3
#     |     |
#(0,0)|(0,1)|(0,2)
#     |     |
#-----|-----|-----
#     |     |
#(1,0)|(1,1)|(1,2)
#     |     |


# The benefit of this function it's that allow us to assign this areas asymetrically with specific widths and heights

# by using the standard notation of lists
# Example: in the 2x3 example the AX=fig.add_subplot(gs[:,2]) will imply to for AX we will use area (2,0) and (2,1)

#__________________________________

# Here by some examples that you can take as a guide depending of what you want


#-------------------------
# Align plots in vertical (share x and y optional)
if True:
    gs = gridspec.GridSpec(3,1,                            # Number of axis y,x
                        height_ratios = [0.33,0.33,0.33],  # relatives ratios of heigh
                        width_ratios  = [1],               # relatives ratio of with
                        left  = 0.1,      # Space to the edge of left   from the nearest axis
                        right = 0.95,     # Space to the edge of right  from the nearest axis
                        bottom= 0.08,     # Space to the edge of bottom from the nearest axis
                        top   = 0.97,     # Space to the edge of top    from the nearest axis
                        wspace= 0.1,      # Space horizontal between each of the axis
                        hspace= 0.0)      # Space vertical   between each of the axis

    ax1  = fig.add_subplot(gs[0,0])
    ax2  = fig.add_subplot(gs[1,0],sharex=ax1,sharey=ax1)
    ax3  = fig.add_subplot(gs[2,0],sharex=ax1)

    # (here we can define if we want to share axes and with which one)
    #--
    # Ploting
    ax1.plot(x,y1,'r',lw=2,label='$F_1$=Cos(x)')
    ax1.legend(loc='upper right')

    ax2.plot(x,y2,'b',lw=2,label=r'$F_2$=$\frac{sin(x)^5}{3}$')
    ax2.legend(loc='upper right')

    ax3.plot(x,y3,'g',lw=2,label='$F_1$+$F_2$')
    ax3.legend(loc='upper right')

    # Erasing extra y labels
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)

    # Solutions for label of axis
    #ax2.set_ylabel('Amplitude',fontsize=14)
    #ax3.set_xlabel('Period to 4$\pi$',fontsize=14)
    fig.supxlabel('Period to 4$\pi$',fontsize=14)
    fig.supylabel('Amplitude',fontsize=14)
    plt.show()

    plt.show()

#-------------------------
# Align plots in Horizontal
if False:
    gs = gridspec.GridSpec(1,3,                            # Number of axis y,x
                        height_ratios = [1],               # relatives ratios of heigh
                        width_ratios  = [0.33,0.33,0.33],  # relatives ratio of with
                        left  = 0.1,      # Space to the edge of left   from the nearest axis
                        right = 0.95,     # Space to the edge of right  from the nearest axis
                        bottom= 0.08,     # Space to the edge of bottom from the nearest axis
                        top   = 0.97,     # Space to the edge of top    from the nearest axis
                        wspace= 0.0,      # Space horizontal between each of the axis
                        hspace= 0.0)      # Space vertical   between each of the axis

    ax1  = fig.add_subplot(gs[0,0])
    ax2  = fig.add_subplot(gs[0,1],sharex=ax1,sharey=ax1)
    ax3  = fig.add_subplot(gs[0,2],sharey=ax1)

    # (here we can define if we want to share axes and with which one)
    #--
    # Ploting
    ax1.plot(y1,x,'r',lw=2,label='$F_1$=Cos(x)')
    ax1.legend(loc='upper right')

    ax2.plot(y2,x,'b',lw=2,label=r'$F_2$=$\frac{sin(x)^5}{3}$')
    ax2.legend(loc='upper right')

    ax3.plot(y3,x,'g',lw=2,label='$F_1$+$F_2$')
    ax3.legend(loc='upper right')

    # Erasing extra y labels
    plt.setp(ax2.get_yticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)

    # Solutions for label of axis
    #ax1.set_ylabel('Amplitude',fontsize=14)
    #ax2.set_xlabel('Period to 4$\pi$',fontsize=14)
    fig.supylabel('Period to 4$\pi$',fontsize=14)
    fig.supxlabel('Amplitude',fontsize=14)
    plt.show()


#--------------------------
# Imshow with color bar and Plots
if False:
    gs = gridspec.GridSpec(2,4,                                    # Number of axis y,x
                        height_ratios = [0.5,0.5],              # relatives ratios of heigh
                        width_ratios  = [0.35,0.05,0.65,0.05], # relatives ratio of with
                        left  = 0.1,      # Space to the edge of left   from the nearest axis
                        right = 0.95,     # Space to the edge of right  from the nearest axis
                        bottom= 0.08,     # Space to the edge of bottom from the nearest axis
                        top   = 0.97,     # Space to the edge of top    from the nearest axis
                        wspace= 0.1,      # Space horizontal between each of the axis
                        hspace= 0.2)      # Space vertical   between each of the axis

    ax1  = fig.add_subplot(gs[0,0])
    ax2  = fig.add_subplot(gs[1,0])
    ax3  = fig.add_subplot(gs[:,2])
    cbax = fig.add_subplot(gs[:,3])

    # (here we left the column [:,1] empty to better separation between plots)
    #--
    # Ploting

    ax1.plot(x,y1)
    ax2.plot(y1,x)

    #--
    diff=x[2]-x[1] # just to have the pixels in the imshow centered

    IM=ax3.imshow(Z,              # 3D-data
                  vmin=0,vmax=1,  # Limits of colorbar values
                  aspect='auto',  # Scaling the rate (number of pixel in Y)/(Number of pixels in X)
                  origin='lower', # From which Corner the plot it's generated
                  extent=(x.min()-diff, # min value in x axis
                          x.max()+diff, # max value in x axis
                          x.min()-diff, # min value in y axis
                          x.max()+diff),# max value in y axis
                  cmap='nipy_spectral') # colormap
    #--
    plt.colorbar(IM,cax=cbax) # Generate the colorbar and indicate which axe have to use


    plt.tight_layout() # Giving to matplotlib the chanse to reescale some values to make it more symetric
    plt.show()


#--------------------------
# More complex figure with relation between values and zoom out of figure
if False:
    gs = gridspec.GridSpec(6,4,                                         # Number of axis y,x
                        height_ratios = [0.35,0.33,0.33,0.33,0.1,0.05], # relatives ratios of heigh
                        width_ratios  = [0.35,0.2,1,0.35],              # relatives ratio of with
                        left  = 0.1,      # Space to the edge of left   from the nearest axis
                        right = 0.95,     # Space to the edge of right  from the nearest axis
                        bottom= 0.08,     # Space to the edge of bottom from the nearest axis
                        top   = 0.97,     # Space to the edge of top    from the nearest axis
                        wspace= 0.,    # Space horizontal between each of the axis
                        hspace= 0.)    # Space vertical   between each of the axis

    ax1  = fig.add_subplot(gs[0,2])
    ax2  = fig.add_subplot(gs[1:4,3])
    ax3  = fig.add_subplot(gs[1:4,2],sharex=ax1,sharey=ax2)
    ax4  = fig.add_subplot(gs[1,0])
    ax5  = fig.add_subplot(gs[3,0],projection='3d')
    cbax = fig.add_subplot(gs[5,2])

    # (here we left the row [4,:] empty to better separation between plots)
    #--
    # Ploting

    ax1.plot(x,y1,lw=2,color='k')
    ax1.axvline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5) # Just extra lines

    ax2.plot(y1,x,lw=2,color='k')
    ax2.axhline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5)

    #--
    diff=x[2]-x[1] # just to have the pixels in the imshow centered

    IM=ax3.imshow(Z,              # 3D-data
                  vmin=0,vmax=1,  # Limits of colorbar values
                  aspect='auto',  # Scaling the rate (number of pixel in Y)/(Number of pixels in X)
                  origin='lower', # From which Corner the plot it's generated
                  extent=(x.min()-diff, # min value in x axis
                          x.max()+diff, # max value in x axis
                          x.min()-diff, # min value in y axis
                          x.max()+diff),# max value in y axis
                  cmap='jet') # colormap

    ax3.axvline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5) # Just extra lines
    ax3.axhline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5)
    #--
    plt.colorbar(IM,cax=cbax,orientation='horizontal') # Generate the colorbar and indicate which axe have to use

    #---
    # Generating a zoomed area

    a,b,c,d=5,7,6,8 # arbitrary lmits
    l1,l2  =abs(x-a).argmin(),abs(x-b).argmin() # get index of nearest value to the limit
    l3,l4  =abs(x-c).argmin(),abs(x-d).argmin() # this is according of how we generated the data

    zoomed=Z[l3:l4,l1:l2] # zoomed data

    #---
    IM2=ax4.imshow(zoomed,            # 3D-data
                  vmin=0,vmax=1,  # Limits of colorbar values
                  aspect='auto',  # Scaling the rate (number of pixel in Y)/(Number of pixels in X)
                  origin='lower', # From which Corner the plot it's generated
                  extent=(a-diff, # min value in x axis
                          b+diff, # max value in x axis
                          c-diff, # min value in y axis
                          d+diff),# max value in y axis
                  cmap='tab20c')  # colormap


    #---
    # Second Colorbar
    cbax2 = ax4.inset_axes([1.05, 0, .1, 1]) # position and width relative to the ax4 (colorbar)
    plt.colorbar(IM2,cax=cbax2)
    cbax2.spines[:].set_color('violet')       # Color of the axes in the zoomed area
    cbax2.spines[:].set_linewidth(1.1)      # Linewith of axes in the zoomed plot
    cbax2.tick_params(axis='both', colors='violet',which='both',labelsize=7) # ticks (which='minor'/'major')
    #---

    # this generates the box (controls the with and color) and the conectors
    rectpatch, connects=ax3.indicate_inset_zoom(ax4,linewidth=5.5, edgecolor="fuchsia",alpha=0.9)

    ax4.spines[:].set_color('fuchsia') # Color of the axes in the zoomed area
    ax4.spines[:].set_linewidth(5.5)   # Linewith of axes in the zoomed plot



    # Select Corners to conect
    connects[0].set_visible(True)
    connects[1].set_visible(False)
    connects[2].set_visible(False)
    connects[3].set_visible(True)

    for line in connects: # Linewidth of the line conecting the zoomed area
        line.set_linewidth(5.5)

    #-----------

    ax5.plot_surface(A, B, Z, cmap='jet',linewidth=0, antialiased=False) # Surface plot
    ax5.view_init(azim=60,elev=45) # initial inclination view

    # Erasing extra y labels
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_yticklabels(), visible=False)

    # Options for labels
    ax3.set_xlabel('Period to 4$\pi$',fontsize=10)
    ax3.set_ylabel('Period to 4$\pi$',fontsize=10)

    ax2.set_xlabel('Amplitude',fontsize=10)

    ax1.set_ylabel('Amplitude',fontsize=10)

    cbax.set_xlabel('Amplitude')

    plt.tight_layout() # Giving to matplotlib the chanse to reescale some values to make it more symetric
    plt.show()


#--------------------------
# More complex figure with relation between values and zoom inside of figure
if False:
    gs = gridspec.GridSpec(2,4,                              # Number of axis y,x
                        height_ratios = [0.35,1],          # relatives ratios of heigh
                        width_ratios  = [0.35,1,0.1,0.05],   # relatives ratio of with
                        left  = 0.1,      # Space to the edge of left   from the nearest axis
                        right = 0.95,     # Space to the edge of right  from the nearest axis
                        bottom= 0.08,     # Space to the edge of bottom from the nearest axis
                        top   = 0.97,     # Space to the edge of top    from the nearest axis
                        wspace= 0.,    # Space horizontal between each of the axis
                        hspace= 0.)    # Space vertical   between each of the axis

    ax1  = fig.add_subplot(gs[0,1])
    ax2  = fig.add_subplot(gs[1,0])
    ax3  = fig.add_subplot(gs[1,1],sharex=ax1,sharey=ax2)
    cbax = fig.add_subplot(gs[1,3])

    # (here we left the column [:,2] empty to better separation between plots and colorbar)
    #--
    # Ploting Data

    ax1.plot(x,y1,lw=2,color='k')
    ax1.axvline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5) # Just extra lines

    ax2.plot(y1,x,lw=2,color='k')
    ax2.axhline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5)
    ax2.invert_xaxis()

    #--
    diff=x[2]-x[1] # just to have the pixels in the imshow centered

    IM=ax3.imshow(Z,                     # 3D-data
                  vmin=0,vmax=1,         # Limits of colorbar values
                  aspect='auto',         # Scaling the rate (number of pixel in Y)/(Number of pixels in X)
                  origin='lower',        # From which Corner the plot it's generated
                  extent=(x.min()-diff,    # min value in x axis
                          x.max()+diff,    # max value in x axis
                          x.min()-diff,    # min value in y axis
                          x.max()+diff),   # max value in y axis
                  cmap='gist_heat')            # colormap

    ax3.axvline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5) # Just extra lines
    ax3.axhline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5)
    #--
    plt.colorbar(IM,label='Amplitude',cax=cbax,orientation='vertical') # Generate the colorbar and indicate which axe have to use

    #---
    # Generating a zoomed area

    a,b,c,d=5,7,4,6.5 # arbitrary lmits (x1,x2,y1,y2)
    l1,l2  =abs(x-a).argmin(),abs(x-b).argmin() # get index of nearest value to the limit
    l3,l4  =abs(x-c).argmin(),abs(x-d).argmin() # this is according of how we generated the data

    zoomed=Z[l3:l4,l1:l2] # zoomed data
    #---

    # Inside plot zoom
    ax4   = ax3.inset_axes([0.68, .68, .32, .32]) # position and width relative to the ax3
    cbax2 = ax4.inset_axes([1.05, 0, .1, 1]) # position and width relative to the ax4 (colorbar)

    IM2=ax4.imshow(zoomed,            # 3D-data
                  vmin=0,vmax=1,  # Limits of colorbar values
                  aspect='auto',  # Scaling the rate (number of pixel in Y)/(Number of pixels in X)
                  origin='lower', # From which Corner the plot it's generated
                  extent=(a-diff, # min value in x axis
                          b+diff, # max value in x axis
                          c-diff, # min value in y axis
                          d+diff),# max value in y axis
                  cmap='tab20c') # colormap

    ax4.axvline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5) # Just extra lines
    ax4.axhline(np.pi*2,lw=2,ls='--',color='k',alpha=0.5)

    #---
    # Second Colorbar
    plt.colorbar(IM2,cax=cbax2)
    cbax2.spines[:].set_color('cyan')       # Color of the axes in the zoomed area
    cbax2.spines[:].set_linewidth(1.1)      # Linewith of axes in the zoomed plot
    cbax2.tick_params(axis='both', colors='cyan',which='both',labelsize=7) # ticks (which='minor'/'major')
    #---
    # this generates the box (controls the with and color) and the conectors
    rectpatch, connects=ax3.indicate_inset_zoom(ax4,linewidth=3.5, edgecolor="cyan",alpha=0.9)

    ax4.spines[:].set_color('cyan')       # Color of the axes in the zoomed area
    ax4.spines[:].set_linewidth(3.5)      # Linewith of axes in the zoomed plot
    ax4.tick_params(axis='both', colors='cyan',which='both',labelsize=12) # ticks (which='minor'/'major')
    #ax4.set_facecolor("black")


    # Select Corners to conect
    connects[0].set_visible(False)
    connects[1].set_visible(True)
    connects[2].set_visible(True)
    connects[3].set_visible(False)

    for line in connects: # Linewidth of the line conecting the zoomed area
        line.set_linewidth(5.5)

    # Erasing extra y labels
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax3.get_yticklabels(), visible=False)

    # Options for labels
    ax3.set_xlabel('Period to 4$\pi$',fontsize=10)

    ax2.set_ylabel('Period to 4$\pi$',fontsize=10)
    ax2.set_xlabel('Amplitude',fontsize=10)

    ax1.set_ylabel('Amplitude',fontsize=10)


    # Another options for the plot
    #-bg color of plot
    ax1.set_facecolor("silver")
    ax2.set_facecolor("silver")
    #-bg color of figure
    fig.set_facecolor('black')
    #-color of axis label
    ax1.yaxis.label.set_color('red')
    ax1.xaxis.label.set_color('red')
    ax2.yaxis.label.set_color('blue')
    ax2.xaxis.label.set_color('blue')
    ax3.yaxis.label.set_color('green')
    ax3.xaxis.label.set_color('green')
    cbax.yaxis.label.set_color('white')
    cbax.xaxis.label.set_color('white')
    #-color of axis edge
    ax1.spines[:].set_color('red') # you can set differentially with spines['bootom'], etc.
    ax2.spines[:].set_color('blue')
    ax3.spines[:].set_color('green')
    cbax.spines[:].set_color('white')
    #-color of axis number and ticks
    ax1.tick_params(axis='both', colors='red',which='both')
    ax2.tick_params(axis='both', colors='blue',which='both')
    ax3.tick_params(axis='both', colors='green',which='both')
    cbax.tick_params(axis='both', colors='white',which='both')



    plt.tight_layout() # Giving to matplotlib the chanse to reescale some values to make it more symetric
    plt.show()
